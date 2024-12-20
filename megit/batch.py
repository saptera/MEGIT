# MEGIT batch process (video based) functions

import copy
import json
import h5py as h5
import numpy as np
from shapely.geometry import Point, Polygon
from .fio import hml_read, cjsh_read
from .data import (get_lbl_det, conv_hm2js_blob, conv_hm2js_max, arr_raw_jsl, get_proc_rng, pad_nan, sel_mtp,
                   flt_spl_frm, lin2p, poly_lin_poschk, poly_area_poschk, get_frm_gap, crs_det_frm)
from .utils import prog_print

"""Function list:
    avgint_roi(roi_js, im_hdf, im_ext='png', disp=(True, 4)): Compute average intensity of ROIs.
    det_avgint(roi_int, th=5, disp=(True, 4)): Detect crossings based on average intensity of ROIs.
    grp_conv_hm2js(hml_hdf, conv_meth='blob', smth=False, disp=(True, 4), **kwargs): Convert HeatMap to JSON labels.
    det_prdpos(roi_js, lbl_cj, tst=True, th=0, disp=(True, 4)): Detect crossings based on model prediction positions.
    comb_det(avg_grd, avg_cns, prd_det, prd_rer, frm_lst, th=6): Combining detection results.
"""


def avgint_roi(roi_js, im_hdf, disp=(True, 4)):
    """ Compute average intensity of ROIs.

    Args:
        roi_js (str): ROI definition JSON file (*.roi)
        im_hdf (str): Frame image HDF5 file (*.frm)
        disp (tuple[bool, int]): Process print control, flag and indention (default: (True, 4))

    Returns:
        dict[str, list[int]]: Mean intensity of ROIs, keys = {'gap', 'top', 'btm'}
    """
    disp_prt = disp[0]
    disp_ind = 0 if disp[1] < 0 else disp[1]

    # Read image file list
    disp_prt and print("%sAcquiring input frame files" % (' ' * disp_ind))
    im_fp = h5.File(im_hdf, 'r')
    im_lst = sorted(list(im_fp.keys()), key=int)
    height, width = im_fp[im_lst[0]][()].shape

    # Read ROI JSON file
    disp_prt and print("%sComputing ROI features" % (' ' * disp_ind))
    with open(roi_js, 'r') as f:
        roi = json.load(f)
    # Convert ROI data to polygon
    roi = {int(frm): {rgn: Polygon([roi[frm][rgn]['tl'], roi[frm][rgn]['tr'], roi[frm][rgn]['br'], roi[frm][rgn]['bl']])
           if roi[frm][rgn] is not None else None for rgn in roi[frm]} for frm in roi}
    # Get all pixel indices within the ROI polygon
    pts = [Point(i, j) for i in range(width) for j in range(height)]
    idx = {frm: {rgn: np.asarray([(p.x, p.y) for p in pts if roi[frm][rgn].contains(p)], dtype=int).T
           if roi[frm][rgn] is not None else None for rgn in roi[frm]} for frm in roi}

    rc = [0, 0]  # INIT VAR
    rt = [0, 0]  # INIT VAR
    rb = [0, 0]  # INIT VAR
    gap_avg = np.zeros(len(idx), dtype=np.float32)  # INIT VAR
    top_avg = np.zeros(len(idx), dtype=np.float32)  # INIT VAR
    btm_avg = np.zeros(len(idx), dtype=np.float32)  # INIT VAR
    # Compute average intensity of images
    for i, frm in enumerate(idx):
        if idx[frm]['C'] is not None: rc = idx[frm]['C']
        if idx[frm]['T'] is not None: rt = idx[frm]['T']
        if idx[frm]['B'] is not None: rb = idx[frm]['B']
        img = im_fp[im_lst[i]][()]
        gap_avg[i] = np.mean(img[rc[1], rc[0]])
        top_avg[i] = np.mean(img[rt[1], rt[0]])
        btm_avg[i] = np.mean(img[rb[1], rb[0]])
        disp_prt and prog_print(i, len(idx), "%sComputing average intensity:" % (' ' * disp_ind))
    # Covert to binary lists
    disp_prt and print("%sConverting data" % (' ' * disp_ind))
    gap_avg = gap_avg.tolist()
    top_avg = top_avg.tolist()
    btm_avg = btm_avg.tolist()

    # Close file and return
    im_fp.close()
    return {'gap': gap_avg, 'top': top_avg, 'btm': btm_avg}


def det_avgint(roi_int, th_grd=5, th_cns=10, disp=(True, 4)):
    """ Detect crossings based on average intensity of ROIs.

    Args:
        roi_int (dict[str, list[int]]): Mean intensity of ROIs, keys = {'gap', 'top', 'btm'}
        th_grd (int or float or tuple[int or float, int or float, int or float]): No-false-negative limits (default: 5)
        th_cns (int or float or tuple[int or float, int or float, int or float]): No-false-positive limits (default: 10)
        disp (tuple[bool, int]): Process print control, flag and indention (default: (True, 4))

    Returns:
        tuple[dict[str, list[int]], dict[str, list[int]]]: Detection with mean intensity of ROIs
            - grd (dict[str, list[int]]): Greedy threshold detection results, keys = {'gap', 'top', 'btm'}
            - cns (dict[str, list[int]]): Conservative threshold detection, keys = {'gap', 'top', 'btm'}
    """
    # Check greedy threshold input
    if type(th_grd) == int or type(th_grd) == float:
        grd_ths = {'gap': th_grd, 'top': th_grd, 'btm': th_grd}
    elif type(th_grd) == list or type(th_grd) == tuple:
        if len(th_grd) == 3:
            grd_ths = {'gap': th_grd[0], 'top': th_grd[1], 'btm': th_grd[2]}
        else:
            raise ValueError("List of greedy thresholds must have a length of 3")
    else:
        raise TypeError("Greedy threshold must be a scalar or a iterable of length 3")
    # Check conservative threshold input
    if type(th_cns) == int or type(th_cns) == float:
        cns_ths = {'gap': th_cns, 'top': th_cns, 'btm': th_cns}
    elif type(th_cns) == list or type(th_cns) == tuple:
        if len(th_cns) == 3:
            cns_ths = {'gap': th_cns[0], 'top': th_cns[1], 'btm': th_cns[2]}
        else:
            raise ValueError("List of conservative thresholds must have a length of 3")
    else:
        raise TypeError("Conservative threshold must be a scalar or a iterable of length 3")
    # Get display settings
    disp_prt = disp[0]
    disp_ind = 0 if disp[1] < 0 else disp[1]
    # Assign data
    gap_avg = np.asarray(roi_int['gap'], dtype=np.float32)
    top_avg = np.asarray(roi_int['top'], dtype=np.float32)
    btm_avg = np.asarray(roi_int['btm'], dtype=np.float32)
    # Greedy detection
    disp_prt and print("%sComputing cross with greedy threshold" % (' ' * disp_ind))
    gap_det_grd = np.where(gap_avg > max(gap_avg) - grd_ths['gap'], 0, 1).tolist()
    top_det_grd = np.where(top_avg > max(top_avg) - grd_ths['top'], 0, 1).tolist()
    btm_det_grd = np.where(btm_avg > max(btm_avg) - grd_ths['btm'], 0, 1).tolist()
    grd = {'gap': gap_det_grd, 'top': top_det_grd, 'btm': btm_det_grd}
    # Conservative detection
    disp_prt and print("%sComputing cross with conservative threshold" % (' ' * disp_ind))
    gap_det_cns = np.where(gap_avg > max(gap_avg) - cns_ths['gap'], 0, 1).tolist()
    top_det_cns = np.where(top_avg > max(top_avg) - cns_ths['top'], 0, 1).tolist()
    btm_det_cns = np.where(btm_avg > max(btm_avg) - cns_ths['btm'], 0, 1).tolist()
    cns = {'gap': gap_det_cns, 'top': top_det_cns, 'btm': btm_det_cns}
    return grd, cns


def grp_conv_hm2js(hml_hdf, conv_meth='blob', smth=False, disp=(True, 4), **kwargs):
    """ Convert all HeatMap labels in the HDF5 to JSON labels.

    Args:
        hml_hdf (str): HeatMap label HDF5 file
        conv_meth (str): ['blob', 'max'] HeatMap to JSON conversion method (default: 'blob')
        smth (bool): Defines if the output JSON label need to be smoothed (default: False)
        disp (tuple[bool, int]): Process print control, flag and indention (default: (True, 4))
        **kwargs: Extra conversion parameters

    Keyword Args:
        return_raw (bool): True - raw JSON labels will be returned, False - None returned (default: True)
        fallback_max (bool): Flag for MAX method will be used for None during conversion (default: True)
        multiselect_max (bool): Flag for MAX method will be used for multipoint during conversion (default: False)
        heatmap_threshold (int or float): HeatMap minimum peak value (default: 5)
        blob_area (tuple[float, float]): Area limits for 'blob' method (default: (25, 100))
        blob_circularity (tuple[float, float]): Circularity limits for 'blob' method (default: (0.4, 1.1))
        blob_inertia (tuple[float, float]): Inertia (0 - 1) limits for 'blob' method (default: (0.2, 1.1))
        blob_convexity (tuple[float, float]): Convexity limits for 'blob' method (default: (0.1, 1000))
        select_search (int): Flanking indices used for process multipoint selection (default: 120)
        miss_search (int): Flanking indices used for process missing value padding (default: 60)
        smooth_window (int): Window size for smoothing median filter (default: 8)

    Returns:
        tuple[dict, dict] or tuple[dict, None]:
            jsl_data (tuple[dict[str, list[float]], list[int], list[int]]): Converted JSON label
            raw_data (dict[int, dict[str, dict[str, float] or list[dict[str, float]] or None]] or None): Raw JSON label
    """
    disp_prt = disp[0]
    disp_ind = 0 if disp[1] < 0 else disp[1]
    # Get keyword argument values
    ret_raw = kwargs.get('return_raw', True)
    fallback_max = kwargs.get('fallback_max', True)
    multiselect_max = kwargs.get('multiselect_max', False)
    hm_th = kwargs.get('heatmap_threshold', 5)
    det_area = kwargs.get('blob_area', (25, 100))
    det_circ = kwargs.get('blob_circularity', (0.4, 1.1))
    det_inrt = kwargs.get('blob_inertia', (0.2, 1.1))
    det_conv = kwargs.get('blob_convexity', (0.1, 1000))
    mtp_srch_rng = kwargs.get('select_search', 120)
    nan_srch_rng = kwargs.get('miss_search', 60)
    smth_win = kwargs.get('smooth_window', 8)

    # Load HeatMap file and get data features
    hml_fp = h5.File(hml_hdf, 'r')
    frm_lst = sorted([int(i) for i in hml_fp.keys()])
    detector = get_lbl_det(det_area, det_circ, det_inrt, det_conv) if conv_meth == 'blob' else None
    # Raw JSON label conversion
    raw_data = {}  # INIT VAR
    for i, frm in enumerate(frm_lst):
        hml_pred = hml_read(hml_fp, str(frm))
        # Process conversion with defined method
        if conv_meth == 'max':
            jsl_pred = conv_hm2js_max(hml_pred, hm_th)  # MAX method only give single prediction
        else:
            if conv_meth == 'blob':
                jsl_pred = conv_hm2js_blob(hml_pred, detector)
            # Add [elif] for possible future conversion methods
            else:
                jsl_pred = None  # Placeholder only
            # Optional fallbacks to MAX method on irregular predictions
            fb_lst = []  # INIT/RESET VAR
            for v in jsl_pred:
                if (jsl_pred[v] is None) and fallback_max:
                    fb_lst.append(v)
                elif (len(jsl_pred[v]) > 1) and multiselect_max:
                    fb_lst.append(v)
            if fb_lst:
                max_pred = conv_hm2js_max(hml_pred, hm_th)
                for v in fb_lst:
                    jsl_pred[v] = copy.deepcopy(max_pred[v])
        raw_data[frm] = jsl_pred
        disp_prt and prog_print(i, len(frm_lst), "%sConverting HeatMap to raw JSON labels:" % (' ' * disp_ind))
    # Close HeatMap HDF5 file
    hml_fp.close()

    # Postprocess raw JSON labels
    jsl_data = {frm_lst[frm_num]: {} for frm_num in range(len(frm_lst))}  # INIT VAR
    for lbl_key in ['nose', 'left_ear', 'right_ear']:
        disp_prt and print("%sPost-processing [%s] data" % (' ' * disp_ind, lbl_key))
        # Arrange converted data
        lbl_kpl, nan_ptl, mtp_ptl = arr_raw_jsl(raw_data, lbl_key)
        # Process multiple value selection
        if (conv_meth != 'max') and (not multiselect_max):
            disp_prt and print("%sProcess multiple value selection" % (' ' * (disp_ind + 2)))
            sel_rng, sel_grp = get_proc_rng(mtp_ptl, frm_lst, mtp_srch_rng)
            for idx in range(len(sel_grp)):
                x = lbl_kpl['x'][sel_rng[idx][0]:sel_rng[idx][1]]
                y = lbl_kpl['y'][sel_rng[idx][0]:sel_rng[idx][1]]
                pos = [p - sel_rng[idx][0] for p in sel_grp[idx]]
                sel_x, sel_y, sel_p = sel_mtp(x, y, pos)
                # Replace values
                for p in range(len(sel_grp[idx])):
                    lbl_kpl['x'][sel_grp[idx][p]] = sel_x[sel_p[p][0]]
                    lbl_kpl['y'][sel_grp[idx][p]] = sel_y[sel_p[p][0]]
                    lbl_kpl['r'][sel_grp[idx][p]] = lbl_kpl['r'][sel_grp[idx][p]][sel_p[p][1]]
        # Process missing value padding
        disp_prt and print("%sProcess missing value padding" % (' ' * (disp_ind + 2)))
        pad_rng, pad_grp = get_proc_rng(nan_ptl, frm_lst, nan_srch_rng)
        for idx in range(len(pad_grp)):
            x = lbl_kpl['x'][pad_rng[idx][0]:pad_rng[idx][1]]
            y = lbl_kpl['y'][pad_rng[idx][0]:pad_rng[idx][1]]
            r = lbl_kpl['r'][pad_rng[idx][0]:pad_rng[idx][1]]
            pad_x, pad_p = pad_nan(x, filt=True)
            pad_y = pad_nan(y, filt=True)[0]
            pad_r = pad_nan(r, filt=True)[0]
            # Replace values
            for p in range(len(pad_grp[idx])):
                lbl_kpl['x'][pad_grp[idx][p]] = pad_x[pad_p[p]]
                lbl_kpl['y'][pad_grp[idx][p]] = pad_y[pad_p[p]]
                lbl_kpl['r'][pad_grp[idx][p]] = pad_r[pad_p[p]]
        # Process label smoothing
        if smth:
            disp_prt and print("%sSmoothing label data..." % (' ' * (disp_ind + 2)))
            x = flt_spl_frm(lbl_kpl['x'], smth_win, frm_lst)
            y = flt_spl_frm(lbl_kpl['y'], smth_win, frm_lst)
            lbl_kpl['x'] = copy.deepcopy(x)
            lbl_kpl['y'] = copy.deepcopy(y)
        # Arrange output data
        for frm_num in range(len(frm_lst)):
            jsl_data[frm_lst[frm_num]][lbl_key] = {k: lbl_kpl[k][frm_num] for k in lbl_kpl}

    # Return results
    if ret_raw:
        return jsl_data, raw_data
    else:
        return jsl_data, None


def det_prdpos(roi_js, lbl_cj, tst=True, th=0, disp=(True, 4)):
    """ Detect crossings based on model prediction positions.

    Args:
        roi_js (str): ROI definition JSON file (*.roi)
        lbl_cj (str): Model prediction label file (*.jsl)
        tst (bool): Define if is a test animal (True) or a by animal (False)
        th (int or float or tuple[int or float, int or float, int or float]): Threshold for detection
        disp (tuple[bool, int]): Process print control, flag and indention (default: (True, 4))

    Returns:
        tuple[dict[str, list[int]], dict[str, list[int]]]: Detection with model prediction positions
            - det (dict[str, list[int]]): Prediction label ROI cross detection results, keys = {'gap', 'top', 'btm'}
            - rer (dict[str, list[int]]): Prediction label wall line cross detection results, keys = {'top', 'btm'}
    """
    # Check threshold input
    if type(th) == int or type(th) == float:
        ths = {'C': th, 'T': th, 'B': th}
    elif type(th) == list or type(th) == tuple:
        if len(th) == 3:
            ths = {'C': th[0], 'T': th[1], 'B': th[2]}
        else:
            raise ValueError("List of thresholds must have a length of 3")
    else:
        raise TypeError("Threshold must be a scalar or a iterable of length 3")
    # Set cross direction features
    sup = {'C': not tst, 'T': False, 'B': True}
    flp = {'C': (True, False, False), 'T': (False, True, True), 'B':  (False, True, True)}
    # Get display settings
    disp_prt = disp[0]
    disp_ind = 0 if disp[1] < 0 else disp[1]

    # Read JSON prediction labels
    disp_prt and print("%sReading predicted labels" % (' ' * disp_ind))
    dat = cjsh_read(lbl_cj)
    pred = [[(dat[n][k]['x'], dat[n][k]['y']) for k in ['nose', 'left_ear', 'right_ear']] for n in dat]

    # Read ROI JSON file
    disp_prt and print("%sComputing ROI features" % (' ' * disp_ind))
    with open(roi_js, 'r') as f:
        roi = json.load(f)
    # Extract ROI features
    feat = {int(frm): {'C': None, 'T': None, 'B': None, 'W': None} for frm in roi}  # INIT VAR
    for frm in roi:
        if roi[frm]['C'] is not None:
            if tst:  # Test target animal, at the right platform by default
                ln = lin2p(roi[frm]['C']['tr'][::-1], roi[frm]['C']['br'][::-1])  # Flip X/Y for near-vertical line
            else:    # By juvenile animal, at the left platform by default
                ln = lin2p(roi[frm]['C']['tl'][::-1], roi[frm]['C']['bl'][::-1])  # Flip X/Y for near-vertical line
            sl = lin2p(roi[frm]['C']['tl'], roi[frm]['C']['tr'])
            sh = lin2p(roi[frm]['C']['bl'], roi[frm]['C']['br'])
            rg = Polygon([roi[frm]['C']['tl'], roi[frm]['C']['tr'], roi[frm]['C']['br'], roi[frm]['C']['bl']])
            feat[int(frm)]['C'] = {'ln': ln, 'sl': sl, 'sh': sh, 'rg': rg}
        if roi[frm]['T'] is not None:
            ln = lin2p(roi[frm]['T']['bl'], roi[frm]['T']['br'])
            sl = lin2p(roi[frm]['T']['tl'][::-1], roi[frm]['T']['bl'][::-1])  # Flip X/Y for near-vertical line
            sh = lin2p(roi[frm]['T']['tr'][::-1], roi[frm]['T']['br'][::-1])  # Flip X/Y for near-vertical line
            rg = Polygon([roi[frm]['T']['tl'], roi[frm]['T']['tr'], roi[frm]['T']['br'], roi[frm]['T']['bl']])
            feat[int(frm)]['T'] = {'ln': ln, 'sl': sl, 'sh': sh, 'rg': rg}
        if roi[frm]['B'] is not None:
            ln = lin2p(roi[frm]['B']['tl'], roi[frm]['B']['tr'])
            sl = lin2p(roi[frm]['B']['tl'][::-1], roi[frm]['B']['bl'][::-1])  # Flip X/Y for near-vertical line
            sh = lin2p(roi[frm]['B']['tr'][::-1], roi[frm]['B']['br'][::-1])  # Flip X/Y for near-vertical line
            rg = Polygon([roi[frm]['B']['tl'], roi[frm]['B']['tr'], roi[frm]['B']['br'], roi[frm]['B']['bl']])
            feat[int(frm)]['B'] = {'ln': ln, 'sl': sl, 'sh': sh, 'rg': rg}
        if tst and roi[frm]['W'] is not None:
            ln = lin2p(roi[frm]['W']['tl'][::-1], roi[frm]['W']['bl'][::-1])  # Flip X/Y for near-vertical line
            feat[int(frm)]['W'] = ln

    # Compute crossings
    ft = {'C': {'ln': [0, 0], 'sl': [0, 0], 'sh': [0, 0], 'rg': None},
          'T': {'ln': [0, 0], 'sl': [0, 0], 'sh': [0, 0], 'rg': None},
          'B': {'ln': [0, 0], 'sl': [0, 0], 'sh': [0, 0], 'rg': None}}  # INIT VAR
    det = {'C': np.zeros(len(feat), dtype=np.uint8),
           'T': np.zeros(len(feat), dtype=np.uint8),
           'B': np.zeros(len(feat), dtype=np.uint8)}  # INIT VAR
    wln = None  # INIT VAR
    rer = {'T': np.zeros(len(feat), dtype=np.uint8),
           'B': np.zeros(len(feat), dtype=np.uint8)}  # INIT VAR
    for i, frm in enumerate(feat):
        if feat[frm]['C'] is not None: ft['C'] = feat[frm]['C']
        if feat[frm]['T'] is not None: ft['T'] = feat[frm]['T']
        if feat[frm]['B'] is not None: ft['B'] = feat[frm]['B']
        if feat[frm]['W'] is not None: wln = feat[frm]['W']
        for k in ['C', 'T', 'B']:
            # Feature pre-check for by-juvenile at 'C' = [gap] region
            if (not tst) and (k == 'C'):
                if pred[i][0][0] < (pred[i][1][0] + pred[i][2][0]) / 2 - 5:  # Check if head is pointing to left
                    continue
            # Check crossing with [left_ear] and [right_ear] key
            wth, crs = poly_area_poschk(ft[k]['ln'], ft[k]['sl'], ft[k]['sh'], pred[i][1:], ths[k], sup[k], flp[k])
            if wth:
                det[k][i] = 1
                break
            else:
                # If [left_ear] and [right_ear] already crossed centre line, but outside of side lines
                if crs:
                    poly = Polygon(pred[i])
                    if poly.area > 0:
                        itsc = poly.intersection(ft[k]['rg']).area
                        # Check if the head has more than 50% inside current ROI
                        if itsc / poly.area >= 0.5:
                            det[k][i] = 1
                            break
        if wln is not None:
            # For top ROI, check if [nose] and [right_ear] key has crossed wall line, flip points
            rer['T'][i] = 1 if poly_lin_poschk(wln, [pred[i][0][::-1], pred[i][2][::-1]], th=0, sup=False) else 0
            # For bottom ROI, check if [nose] and [left_ear] key has crossed wall line, flip points
            rer['B'][i] = 1 if poly_lin_poschk(wln, [pred[i][0][::-1], pred[i][1][::-1]], th=0, sup=False) else 0
        disp_prt and prog_print(i, len(feat), "%sComputing cross:" % (' ' * disp_ind))

    # Covert to binary lists
    disp_prt and print("%sConverting data" % (' ' * disp_ind))
    det = {'gap': det['C'].tolist(), 'top': det['T'].tolist(), 'btm': det['B'].tolist()}
    rer = {'top': rer['T'].tolist(), 'btm': rer['B'].tolist()}
    return det, rer


def comb_det(avg_grd, avg_cns, prd_det, prd_rer, frm_lst, th=6):
    """ Combining detection results of mean intensity and model prediction.

    Args:
        avg_grd (dict[str, list[int]]): Greedy detection with mean intensity results, keys = {'gap', 'top', 'btm'}
        avg_cns (dict[str, list[int]]): Conservative detection with mean intensity results, keys = {'gap', 'top', 'btm'}
        prd_det (dict[str, list[int]]): Cross detection with model prediction positions, keys = {'gap', 'top', 'btm'}
        prd_rer (dict[str, list[int]]): Wall line cross with model prediction positions, keys = {'top', 'btm'}
        frm_lst (list[int]): Input list of frame indices
        th (int): Threshold size for detection (default: 6)

    Returns:
        dict[str, list[int]]: Combined detection, keys = {'gap', 'top', 'btm'}
    """
    # Get frame information
    frm_grp = [[frm_lst[f[0]], frm_lst[f[1] - 1]] for f in get_frm_gap(frm_lst)]
    frm_idx = {f: i for i, f in enumerate(frm_lst)}
    # Analyze results
    res = {k: np.zeros(len(frm_lst), dtype=np.uint8) for k in ['gap', 'top', 'btm']}  # INIT VAR
    for k in ['gap', 'top', 'btm']:
        # Combine results
        dg = np.asarray(avg_grd[k], dtype=np.uint8)
        dp = np.asarray(prd_det[k], dtype=np.uint8)
        crs_lst = dg & dp
        # Detect crossings
        det = crs_det_frm(crs_lst, frm_lst, th=th)
        # Group crossings
        grp = [i for i, g in enumerate(frm_grp) for d in det if g[0] <= d[0] <= g[1]]
        det_grp = {g: [] for g in tuple(set(grp))}  # INIT VAR, use [dict] to avoid IndexError
        [det_grp[g].append(i) for i, g in zip(det, grp)]  # Separate detections by group
        # Detect possible continuous crossings
        dc = np.asarray(avg_cns[k], dtype=np.uint8)
        if k == 'gap':
            pcc_lst = dc
        else:
            # Reject conservative intensity detection when wall cross detected
            dw = np.asarray(prd_rer[k], dtype=np.uint8) ^ 1  # Flip results
            pcc_lst = dc & dw
        for n in det_grp:
            det = det_grp[n]
            if len(det) < 2:
                crs = det
            else:
                tmp = [0]  # INIT VAR
                crs = []  # INIT VAR
                for i in range(len(det) - 1):
                    ait_chk = pcc_lst[frm_idx[det[i][1]]:frm_idx[det[i + 1][0]]]
                    if sum(ait_chk) / len(ait_chk) < 0.95:
                        tmp.append(i)
                        crs.append([det[tmp[0]][0], det[tmp[1]][1]])
                        tmp = [i + 1]
                else:
                    tmp.append(len(det) - 1)
                    crs.append([det[tmp[0]][0], det[tmp[1]][1]])
            # Set results
            for i in crs:
                res[k][frm_idx[i[0]]:frm_idx[i[1]]] = 1
    return {k: res[k].tolist() for k in res}
