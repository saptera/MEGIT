import os
import json
import numpy as np
import cv2.cv2 as cv
from shapely.geometry import Point, Polygon
from megit.fio import cjsh_read
from megit.data import lin2p, ploy_area_poschk, get_frm_gap, crs_det_frm
from megit.utils import prog_print

"""Function list:
    avgint_roi(roi_js, im_dir, im_ext='png', disp=(True, 4)): Compute average intensity of ROIs.
    det_avgint(roi_int, th=5, disp=(True, 4)): Detect crossings based on average intensity of ROIs.
    det_prdpos(roi_js, lbl_cj, tst=True, th=0, disp=(True, 4)): Detect crossings based on model prediction positions.
    comb_det(ai_grd, ai_cns, prd, frm_lst, th=6): Combining detection results of mean intensity and model prediction.
"""


def avgint_roi(roi_js, im_dir, im_ext='png', disp=(True, 4)):
    """ Compute average intensity of ROIs.

    Args:
        roi_js (str): ROI definition JSON file (*.json)
        im_dir (str): Image directory
        im_ext (str): Image extension (default: png)
        disp (tuple[bool, int]): Process print control, flag and indention (default: (True, 4))

    Returns:
        dict[str, list[int]]: Mean intensity of ROIs, keys = {'gap', 'top', 'btm'}
    """
    disp_prt = disp[0]
    disp_ind = 0 if disp[1] < 0 else disp[1]

    # Read image file list
    disp_prt and print("%sAcquiring input frame files" % (' ' * disp_ind))
    im_lst = [os.path.join(im_dir, f) for f in os.listdir(im_dir) if f.endswith(im_ext)]
    height, width = cv.imread(im_lst[0], cv.IMREAD_GRAYSCALE).shape

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
        img = cv.imread(im_lst[i], cv.IMREAD_GRAYSCALE)
        gap_avg[i] = np.mean(img[rc[1], rc[0]])
        top_avg[i] = np.mean(img[rt[1], rt[0]])
        btm_avg[i] = np.mean(img[rb[1], rb[0]])
        disp_prt and prog_print(i, len(idx), "%sComputing average intensity:" % (' ' * disp_ind))
    # Covert to binary lists
    disp_prt and print("%sConverting data" % (' ' * disp_ind))
    gap_avg = gap_avg.tolist()
    top_avg = top_avg.tolist()
    btm_avg = btm_avg.tolist()

    return {'gap': gap_avg, 'top': top_avg, 'btm': btm_avg}


def det_avgint(roi_int, th_grd=5, th_cns=10, disp=(True, 4)):
    """ Detect crossings based on average intensity of ROIs.

    Args:
        roi_int (dict[str, list[int]]): Mean intensity of ROIs, keys = {'gap', 'top', 'btm'}
        th_grd (int or float): Threshold for greedy no-false-negative detection (default: 5)
        th_cns (int or float): Threshold for conservative no-false-positive detection (default: 10)
        disp (tuple[bool, int]): Process print control, flag and indention (default: (True, 4))

    Returns:
        tuple[dict[str, list[int]], dict[str, list[int]]]: Detection with mean intensity of ROIs
            - grd (dict[str, list[int]]): Greedy threshold detection results, keys = {'gap', 'top', 'btm'}
            - cns (dict[str, list[int]]): Conservative threshold detection, keys = {'gap', 'top', 'btm'}
    """
    disp_prt = disp[0]
    disp_ind = 0 if disp[1] < 0 else disp[1]
    # Assign data
    gap_avg = np.asarray(roi_int['gap'], dtype=np.float32)
    top_avg = np.asarray(roi_int['top'], dtype=np.float32)
    btm_avg = np.asarray(roi_int['btm'], dtype=np.float32)
    # Greedy detection
    disp_prt and print("%sComputing cross with greedy threshold" % (' ' * disp_ind))
    gap_det_grd = np.where(gap_avg > max(gap_avg) - th_grd, 0, 1).tolist()
    top_det_grd = np.where(top_avg > max(top_avg) - th_grd, 0, 1).tolist()
    btm_det_grd = np.where(btm_avg > max(btm_avg) - th_grd, 0, 1).tolist()
    grd = {'gap': gap_det_grd, 'top': top_det_grd, 'btm': btm_det_grd}
    # Conservative detection
    disp_prt and print("%sComputing cross with conservative threshold" % (' ' * disp_ind))
    gap_det_cns = np.where(gap_avg > max(gap_avg) - th_cns, 0, 1).tolist()
    top_det_cns = np.where(top_avg > max(top_avg) - th_cns, 0, 1).tolist()
    btm_det_cns = np.where(btm_avg > max(btm_avg) - th_cns, 0, 1).tolist()
    cns = {'gap': gap_det_cns, 'top': top_det_cns, 'btm': btm_det_cns}
    return grd, cns


def det_prdpos(roi_js, lbl_cj, tst=True, th=0, disp=(True, 4)):
    """ Detect crossings based on model prediction positions.

    Args:
        roi_js (str): ROI definition JSON file (*.json)
        lbl_cj (str): Model prediction label file (*.jsl)
        tst (bool): Define if is a test animal (True) or a by animal (False)
        th (int or float or tuple[int or float, int or float, int or float]): Threshold for detection
        disp (tuple[bool, int]): Process print control, flag and indention (default: (True, 4))

    Returns:
        dict[str, list[int]]: Detection with model prediction positions, keys = {'gap', 'top', 'btm'}
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
    feat = {int(frm): {'C': None, 'T': None, 'B': None} for frm in roi}  # INIT VAR
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

    # Compute crossings
    ft = {'C': {'ln': [0, 0], 'sl': [0, 0], 'sh': [0, 0], 'rg': None},
          'T': {'ln': [0, 0], 'sl': [0, 0], 'sh': [0, 0], 'rg': None},
          'B': {'ln': [0, 0], 'sl': [0, 0], 'sh': [0, 0], 'rg': None}}  # INIT VAR
    det = {'C': np.zeros(len(feat), dtype=np.uint8),
           'T': np.zeros(len(feat), dtype=np.uint8),
           'B': np.zeros(len(feat), dtype=np.uint8)}  # INIT VAR
    for i, frm in enumerate(feat):
        if feat[frm]['C'] is not None: ft['C'] = feat[i]['C']
        if feat[frm]['T'] is not None: ft['T'] = feat[i]['T']
        if feat[frm]['B'] is not None: ft['B'] = feat[i]['B']
        for k in ['C', 'T', 'B']:
            wth, crs = ploy_area_poschk(ft[k]['ln'], ft[k]['sl'], ft[k]['sh'], pred[i], ths[k], sup[k], flp[k])
            if wth:
                det[k][i] = 1
                break
            else:
                if crs:
                    poly = Polygon(pred[i])
                    itsc = poly.intersection(ft[k]['rg']).area
                    if itsc / poly.area >= 0.5:
                        det[k][i] = 1
                        break
        disp_prt and prog_print(i, len(feat), "%sComputing cross:" % (' ' * disp_ind))

    # Covert to binary lists
    disp_prt and print("%sConverting data" % (' ' * disp_ind))
    return {'gap': det['C'].tolist(), 'top': det['T'].tolist(), 'btm': det['B'].tolist()}


def comb_det(ai_grd, ai_cns, prd, frm_lst, th=6):
    """ Combining detection results of mean intensity and model prediction.

    Args:
        ai_grd (dict[str, list[int]]): Greedy detection with mean intensity results, keys = {'gap', 'top', 'btm'}
        ai_cns (dict[str, list[int]]): Conservative detection with mean intensity results, keys = {'gap', 'top', 'btm'}
        prd (dict[str, list[int]]): Detection with model prediction positions,, keys = {'gap', 'top', 'btm'}
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
        dg = np.asarray(ai_grd[k], dtype=np.uint8)
        dp = np.asarray(prd[k], dtype=np.uint8)
        crs_lst = dg & dp
        # Detect crossings
        det = crs_det_frm(crs_lst, frm_lst, th=th)
        # Group crossings
        grp = [i for i, g in enumerate(frm_grp) for d in det if g[0] <= d[0] <= g[1]]
        det_grp = {g: [] for g in tuple(set(grp))}  # INIT VAR, use [dict] to avoid IndexError
        [det_grp[g].append(i) for i, g in zip(det, grp)]  # Separate detections by group
        # Detect possible continuous crossings
        dc = np.asarray(ai_cns[k], dtype=np.uint8)
        for n in det_grp:
            det = det_grp[n]
            if len(det) < 2:
                crs = det
            else:
                tmp = [0]  # INIT VAR
                mrg = []  # INIT VAR
                for i in range(len(det) - 1):
                    ait_chk = dc[frm_idx[det[i][1]]:frm_idx[det[i + 1][0]]]
                    if sum(ait_chk) / len(ait_chk) < 0.95:
                        tmp.append(i)
                        mrg.append(tmp)
                        tmp = [i + 1]
                else:
                    tmp.append(len(det) - 1)
                    mrg.append(tmp)
                crs = [[det[i[0]][0], det[i[1]][1]] for i in mrg]
            # Set results
            for i in crs:
                res[k][frm_idx[i[0]]:frm_idx[i[1]]] = 1
    return {k: res[k].tolist() for k in res}
