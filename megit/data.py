import math
import copy
import numpy as np
import scipy.ndimage as ndi
import scipy.interpolate as itp
import cv2.cv2 as cv
import warnings

"""Function list:
  # Image/Video processing functions
    get_frm(vid_cap, frm_idx): Get specified frame of video file.
    brt_con(img, brt=0, con=0): Adjust image brightness and contrast.
    draw_text(img, text, x=0, y=0, scale=1, color='w', has_bkg=True, background='b'): Put text with background.
  # Label data structure conversion functions
    get_lbl_det(area, circularity, inertia, convexity): Generate a detector for extracting blobs from 2D matrix.
    conv_hm2js_blob(hml_data, detector): Convert JSON type label to HeatMap type label with simple blob detector.
    arr_raw_jsl(jsl_data, lbl_key): Arrange raw HeatMap converted JSON labels
  # Label post-processing functions
    get_frm_gap(frm_lst): Detect separation points of frame number.
    get_proc_rng(proc_idx, frm_lst, flk_size=60): Get valid and merged window for list process based on frame indices.
    flt_spl(x, window, padding=None): Smooth continuous 1D array with median filter and univariate spline.
    flt_spl_frm(x, window, frm_lst): [flt_spl] with frame information.
    pad_nan(x, filt=True): Pad missing values in a 1D array with univariate spline.
    sel_mtp(x, y, pos=None): Select best prediction point with least l2-norm of univariate spline estimation.
    diff_flt_frm(x, frm_lst, level=20, window=60): Replace values when the distance between points exceeds threshold.
  # Geometric feature functions
    lin2p(pt1, pt2): Get the slope and the intercept of a line defined by 2 points.
    rel_pos(lin, pt): Return distance from a point to a line.
    poly_lin_poschk(lin, poly, th=0, sup=True): Check if a polygon has a relative position meets the defined threshold.
  # Animal behaviour detection functions
    cross_detect(crs_lst, th=6, frm_lst=None): Detect animal crossing behaviour.
"""


# Image/Video processing functions ----------------------------------------------------------------------------------- #

def get_frm(vid_cap, frm_idx):
    """ Get specified frame of video file.

    Args:
        vid_cap (cv.VideoCapture): OpenCV video capture ID
        frm_idx (int): Index of frame to get

    Returns:
        np.ndarray: {2D, 3D} Image array of specified frame
    """
    # Verify frame index input
    tot_frm = int(vid_cap.get(cv.CAP_PROP_FRAME_COUNT)) - 1
    if frm_idx < 0:
        print("Frame index must be positive integer, force to 0.")
        frm_idx = 0
    elif frm_idx > tot_frm:
        print("Input frame index larger than total frames, get last frame.")
        frm_idx = tot_frm
    # Get frame
    vid_cap.set(cv.CAP_PROP_POS_FRAMES, frm_idx)
    _, frm = vid_cap.read()
    return frm


def brt_con(img, brt=0, con=0):
    """ Adjust image brightness and contrast.

    Args:
        img (np.ndarray): {2D, 3D} Input image
        brt (int or float): Brightness level [-255, 255] (default: 0)
        con (int or float): Contrast level [-255, 255] (default: 0)

    Returns:
        np.ndarray: {2D, 3D} Adjusted image
    """
    ha = 127.5 * (1 - brt / 255)
    hb = 127.5 * (1 + brt / 255)
    k = math.tan((45 + 44 * con / 255) / 180 * math.pi)
    adj = np.add(np.multiply(np.subtract(img, ha), k), hb)
    out = np.clip(adj, 0, 255).astype('uint8')
    return out


def draw_text(img, text, x=0, y=0, scale=1, color=(255, 255, 255), has_bkg=True, background=(0, 0, 0)):
    """ Put text on an image with background.

    Args:
        img (np.ndarray): Input image
        text (str): Input string
        x (int): Left corner of text (default: 0)
        y (int): Top corner of text (default: 0)
        scale (int or float): Text size (default: 1)
        color (tuple[int, int, int]): Text color, in BGR (default: white - (255, 255, 255))
        has_bkg (bool): Defines background exist or not (default: True)
        background (tuple[int, int, int] or None): Background color, in BGR (default: black - (0, 0, 0))

    Returns:
        np.ndarray: Output image
    """
    dst = copy.deepcopy(img)  # Make a copy of original image
    thickness = 1 if scale <= 0.5 else 2
    text_size, _ = cv.getTextSize(text, cv.FONT_HERSHEY_SIMPLEX, scale, thickness=thickness)
    if has_bkg:
        cv.rectangle(dst, (x, y), (x + text_size[0] + 4, y + text_size[1] + 8), background, -1)
    cv.putText(dst, text, (x + 2, y + text_size[1] + 4), cv.FONT_HERSHEY_SIMPLEX, scale, color, thickness=thickness)
    return dst


# Label data structure conversion functions -------------------------------------------------------------------------- #

def get_lbl_det(area, circularity, inertia, convexity):
    """ Generate a detector for extracting blobs from 2D matrix.

    Args:
        area (tuple[float, float]): Extracted blobs area threshold limit
        circularity (tuple[float, float]): Extracted blobs circularity (4pi * Area / Perimeter ^ 2) threshold limit
        inertia (tuple[float, float]): Extracted blobs inertia (0 - 1) threshold limit
        convexity (tuple[float, float]): Extracted blobs circularity (4pi * Area / Perimeter ^ 2) threshold limit

    Returns:
        cv.SimpleBlobDetector: OpenCV simple blob detector
    """
    # Initialize parameter setting using cv2.SimpleBlobDetector
    params = cv.SimpleBlobDetector_Params()

    # Set area filtering parameters
    params.filterByArea = True
    params.minArea = area[0]
    params.maxArea = area[1]
    # Set circularity filtering parameters
    params.filterByCircularity = True
    params.minCircularity = circularity[0]
    params.maxCircularity = circularity[1]
    # Set inertia filtering parameters
    params.filterByInertia = True
    params.minInertiaRatio = inertia[0]
    params.maxInertiaRatio = inertia[1]
    # Set convexity filtering parameters
    params.filterByConvexity = True
    params.minConvexity = convexity[0]
    params.maxConvexity = convexity[1]

    # Create a detector with the parameters
    detector = cv.SimpleBlobDetector_create(params)
    return detector


def conv_hm2js_blob(hml_data, detector):
    """ Convert JSON type label to HeatMap type label with simple blob detector.

    Args:
        hml_data (list[dict]): List of dictionary with HeatMap type label info
        detector (cv.SimpleBlobDetector): OpenCV simple blob detector for HeatMap

    Returns:
        dict[str, list[dict[str, float]] or None]: List of dictionary with JSON label info
    """
    jsl_data = {}  # INIT VAR
    for lbl in hml_data:
        hm = lbl['heatmap']
        hm = np.where(hm < hm.max() * 0.5, 255, 0).astype(np.uint8)
        keypoint = detector.detect(hm)
        kp_lst = []  # INIT/RESET VAR
        for kp in keypoint:
            kp_lst.append({'x': kp.pt[0], 'y': kp.pt[1], 'r': kp.size / 2})
        jsl_data[lbl['label']] = copy.deepcopy(kp_lst) if kp_lst else None
    return jsl_data


def arr_raw_jsl(jsl_data, lbl_key):
    """ Arrange raw HeatMap converted JSON labels

    Args:
        jsl_data (dict[int, dict[str, dict[str, float] or list[dict[str, float]] or None]]): Input JSON label data
            - key (int): frame number
            - val (dict): predictions of defined frame
                -- key (str): label name
                -- val (dict): label predictions, possibly None
                    --- key (str): 'x' = x-position, 'y' = y-position, 'r' = label radius
                    --- val (float): prediction values
        lbl_key (str): Joint name to be processed

    Returns:
        tuple[dict[str, list[float]], list[int], list[int]]: Arranged data
            - lbl_kpl (dict[str, list[float or list[float] or None]): Arrange label data with 'x', 'y', 'r' in lists
            - nan_ptl (list[int]): Indices in arranged label data where have missing prediction values
            - mtp_ptl (list[int]): Indices in arranged label data where have multiple prediction values
    """
    # Get keypoint list
    lbl_kpl = {'x': [], 'y': [], 'r': []}  # INIT VAR, defined keypoint feature lists
    nan_ptl = []  # INIT VAR, missing keypoint frame indices
    mtp_ptl = []  # INIT VAR, multi-prediction keypoint frame indices
    for frm in jsl_data:
        if jsl_data[frm][lbl_key] is None:
            [lbl_kpl[k].append(None) for k in lbl_kpl]
            nan_ptl.append(int(frm))
        elif len(jsl_data[frm][lbl_key]) == 1:
            [lbl_kpl[k].append(jsl_data[frm][lbl_key][0][k]) for k in lbl_kpl]
        else:
            [lbl_kpl[k].append([p[k] for p in jsl_data[frm][lbl_key]]) for k in lbl_kpl]
            mtp_ptl.append(int(frm))
    return lbl_kpl, nan_ptl, mtp_ptl


# Label post-processing functions ------------------------------------------------------------------------------------ #

def get_frm_gap(frm_lst):
    """ Detect separation points of frame number.
        - [frm_lst] must be pre-sorted, call sort() when necessary

    Args:
        frm_lst (list[int]): Input list of frame indices

    Returns:
        list[list[int]]: Frame indices seperated by gaps
    """
    sep_init = 0  # INIT VAR
    sep_idx = []  # INIT VAR
    for i in range(len(frm_lst) - 1):
        if (frm_lst[i + 1] - frm_lst[i]) != 1:
            sep_idx.append([sep_init, i + 1])  # [i + 1] to produce correct slicing results
            sep_init = i + 1
    sep_idx.append([sep_init, len(frm_lst)])
    return sep_idx


def get_proc_rng(proc_idx, frm_lst, flk_size=60):
    """ Get valid and merged window for list process based on frame indices.
        - Both [proc_idx] and [frm_lst] must be pre-sorted, call sort() when necessary

    Args:
        proc_idx (list[int]): Input list of requested value indices
        frm_lst (list[int]): Input list of frame indices
        flk_size (int): Flanking indices used for processing (default: 60)

    Returns:
        tuple[list[list[int, int]] or None, list[list[int]] or list]:
            proc_rng (list[list[int, int]]) - Optimized range for process, return None if no valid range
            proc_grp (list[list[int]]) - Grouped indices based on the range, return empty list [] if no valid range
    """
    # Return None when empty input list encountered
    if not (proc_idx and frm_lst):
        return None, []
    # Detect separation points of frame number
    sep_idx = get_frm_gap(frm_lst)
    # Get processing interval
    rng_lst = []
    for i in proc_idx:
        for sep in sep_idx:
            if sep[0] <= i < sep[1]:
                rl = sep[0] if i - flk_size < sep[0] else i - flk_size
                rr = sep[1] if i + flk_size + 1 > sep[1] else i + flk_size + 1  # +1 to produce correct slicing results
                rng_lst.append([rl, rr])
                break
    # Merge overlapped intervals
    proc_rng = [[rng_lst[0][0], rng_lst[0][1]]]  # INIT VAR
    proc_grp = [[proc_idx[0]]]  # INIT VAR
    for i in range(1, len(rng_lst)):  # 1st value included in the initialization
        if proc_rng[-1][1] > rng_lst[i][0]:
            proc_rng[-1][1] = rng_lst[i][1]
            proc_grp[-1].append(proc_idx[i])
        else:
            proc_rng.append(rng_lst[i])
            proc_grp.append([proc_idx[i]])
    return proc_rng, proc_grp


def flt_spl(x, window, padding=None):
    """ Smooth continuous 1D array with median filter and univariate spline.

    Args:
        x (list or np.ndarray): {1D} Input array
        window (int): Window size for median filter
        padding (tuple[int or float, int or float] or None): Padding value for edges (default: None - No padding)

    Returns:
        np.ndarray: {1D} Smoothed array
    """
    # Process edge padding
    if padding is None:
        src = np.asarray(x)
    else:
        pad_l = [padding[0]] * window
        pad_r = [padding[1]] * window
        src = np.concatenate((pad_l, x, pad_r))
    # Process median filter
    flt = ndi.median_filter(src, size=window, mode='nearest')
    # Process univariate spline
    z = np.asarray(list(range(len(src))))
    spl = itp.UnivariateSpline(z, flt)
    smt = spl(z)
    # Arrange output
    dst = smt if padding is None else smt[window:-window]
    return dst


def flt_spl_frm(x, window, frm_lst):
    """ Smooth continuous 1D array with median filter and univariate spline, with frame information.
        - Different from [flt_spl] function, this function make segmentation of array based on frame information
        - Discontinued frame number will split the array and the separated arrays will be smoothed independently
        - Paddings are automatic generated by the first and last values of the separated arrays

    Args:
        x (list or np.ndarray): {1D} Input array
        window (int): Window size for median filter
        frm_lst (list[int]): Input list of frame indices

    Returns:
        np.ndarray: {1D} Smoothed array
    """
    # Detect separation points of frame number
    sep_idx = get_frm_gap(frm_lst)
    # Separate and smooth the input array
    dst = np.zeros(len(x))  # INIT VAR
    for i in range(len(sep_idx)):
        src = x[sep_idx[i][0]:sep_idx[i][1]]
        dst[sep_idx[i][0]:sep_idx[i][1]] = flt_spl(src, window, (src[0], src[-1]))
    return dst


def pad_nan(x, filt=True):
    """ Pad missing values in a 1D array with univariate spline.

    Args:
        x (list or np.ndarray): {1D} Input array
        filt (bool): Median filter processing flag (default: True)

    Returns:
        tuple[list[float], list[int]]: Padded array and NaN value positions
    """
    # Cast input type
    if type(x) != np.ndarray:
        src = np.asarray(x, dtype=np.float64)
    else:
        src = copy.deepcopy(x)  # Avoid changing input array
        if src.dtype != float:
            src = src.astype(np.float64)
    # Detect NaN values
    mask = np.isnan(src)
    if np.any(mask):
        src[mask] = 0.0
        # Filter padded array to avoid salt-and-pepper noise
        if filt:
            src = ndi.median_filter(src, size=5, mode='nearest')
        # Pad NaN with spline
        z = np.asarray(list(range(len(src))), dtype=np.int32)
        spl = itp.UnivariateSpline(z, src, w=~mask)
        smt = spl(z)
        # Check if spline still produces NaNs
        if np.any(np.isnan(smt)):
            warnings.warn("Failed to estimate with spline, using linear interpolation", RuntimeWarning, stacklevel=2)
            src[mask] = np.interp(np.flatnonzero(mask), np.flatnonzero(~mask), src[~mask])
            # Extract padded NaN values
            val = src.tolist()
        else:
            # Extract padded NaN values
            val = np.where(mask, smt, src).tolist()
        # Extract padded NaN position
        pos = [i.item() for i in z[mask]]
    else:
        val = src.tolist()
        pos = []
    return val, pos


def sel_mtp(x, y, pos=None):
    """ Select best prediction point with least l2-norm of univariate spline estimation.
        - The length of input list [x] and [y] must be the same
        - The indices where the multiple values occur in [x] and [y] must be the same
        - The number of multiple values at certain index of [x] and [y] must be the same

    Args:
        x (list[float or list[float] or None]): X-positions that may contain multiple values in single index
        y (list[float or list[float] or None]): Y-positions that may contain multiple values in single index
        pos (list[int] or None): Indices where the multiple values occur (default: None = auto detect)

    Returns:
        tuple[list[float], list[float], list[tuple[int, int]] or None]:
            X and Y positions with selected single value and selected positions
    """
    # Check the occurrence of multiple values if [pos] is undefined
    if not pos:
        pos = [i for i in range(len(x)) if type(x[i]) == list]
    if pos:
        # Cast input type
        ref_x = np.asarray([None if p in pos else x[p] for p in range(len(x))], dtype=np.float64)
        ref_y = np.asarray([None if p in pos else y[p] for p in range(len(y))], dtype=np.float64)
        # Get output array
        dst_x = ref_x.tolist()
        dst_y = ref_y.tolist()
        # Estimate value where multi-value occur and pad possible NaN values
        ref_x = pad_nan(ref_x, filt=True)[0]
        ref_y = pad_nan(ref_y, filt=True)[0]
        # Select values from multi-value with least l2-norm with estimation
        sel = []  # INIT VAR
        for p in pos:
            pts_x = x[p]
            pts_y = y[p]
            pt_ref = (ref_x[p], ref_y[p])
            dist = float('inf')  # INIT VAR
            idx = 0  # INIT VAR
            for i in range(len(pts_x)):
                tmp = (pts_x[i] - pt_ref[0]) ** 2 + (pts_y[i] - pt_ref[1]) ** 2
                if tmp < dist:
                    dist = tmp
                    idx = i
            else:
                sel.append((p, idx))
                # Replace value
                dst_x[p] = x[p][idx]
                dst_y[p] = y[p][idx]
        return dst_x, dst_y, sel
    else:
        return x, y, None


def diff_flt_frm(x, y, frm_lst, level=20, window=60):
    """ Replace elements when the distance between consecutive points exceeds threshold.
        - Threshold is defined by the median(l2-norm([x], [y])) * [level]
        - [frm_lst] must be pre-sorted, call sort() when necessary

    Args:
        x (list[float] or np.ndarray): {1D} Input array of X positions
        y (list[float] or np.ndarray): {1D} Input array of Y positions
        frm_lst (list[int]): Input list of frame indices
        level (int or float): Multiplier to the median of element-wise distance of input arrays (default: 20)
        window (int): Flanking indices used for processing (default: 60)

    Returns:
        tuple[list[float], list[float]]: Filtered values (X, Y)
    """
    # Cast input type
    if type(x) != np.ndarray:
        x_src = np.asarray(x, dtype=np.float64)
    else:
        x_src = copy.deepcopy(x)  # Avoid changing input array
        if x_src.dtype != float:
            x_src = x_src.astype(np.float64)
    if type(y) != np.ndarray:
        y_src = np.asarray(y, dtype=np.float64)
    else:
        y_src = copy.deepcopy(y)  # Avoid changing input array
        if y_src.dtype != float:
            y_src = y_src.astype(np.float64)
    # Get filtering threshold
    x_diff = np.ediff1d(x_src, to_end=None, to_begin=0.0)
    y_diff = np.ediff1d(y_src, to_end=None, to_begin=0.0)
    norm = np.sqrt(np.square(x_diff) + np.square(y_diff))
    th = np.median(norm) * level
    # Get filtering range
    gap = get_frm_gap(frm_lst)
    err = np.argwhere(norm > th).flatten().tolist()
    err_flt = [err[i] for i in range(len(err)) if err[i] not in [frm[0] for frm in gap]]  # Remove initial frames
    pad_rng, grp = get_proc_rng(err_flt, frm_lst, window)
    nan_rng = [[i[0], i[-1] + 1] for i in grp]  # Get rejected value range by the first and last elements of each group
    # Padding filtered data
    pad_idx = []  # INIT VAR
    for idx in nan_rng:
        x_src[idx[0]:idx[1]] = np.nan
        y_src[idx[0]:idx[1]] = np.nan
        pad_idx.extend(list(range(idx[0], idx[1])))
    x_pad = []  # INIT VAR
    y_pad = []  # INIT VAR
    for idx in pad_rng:
        # Pad X values
        pad_tmp, pos_tmp = pad_nan(x_src[idx[0]:idx[1]], filt=False)
        x_pad.extend(([pad_tmp[i] for i in pos_tmp]))
        # Pad Y values
        pad_tmp, pos_tmp = pad_nan(y_src[idx[0]:idx[1]], filt=False)
        y_pad.extend(([pad_tmp[i] for i in pos_tmp]))
    x_src[pad_idx] = x_pad
    y_src[pad_idx] = y_pad
    return x_src.tolist(), y_src.tolist()


# Geometric feature functions ---------------------------------------------------------------------------------------- #

def lin2p(pt1, pt2):
    """ Get the slope and the intercept of a line defined by 2 points.

    Args:
        pt1 (tuple[int or float, int or float] or list[int or float, int or float]): 1st point (x1, y1)
        pt2 (tuple[int or float, int or float] or list[int or float, int or float]): 2nd point (x2, y2)

    Returns:
        tuple[float, float] or tuple[None, float]: Slope and intercept of defined line
    """
    if pt1[0] == pt2[0]:
        return None, pt1[0]
    else:
        k = (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])
        h = (pt2[0] * pt1[1] - pt1[0] * pt2[1]) / (pt2[0] - pt1[0])
        return k, h


def rel_pos(lin, pt):
    """ Return distance from a point to a line.

    Args:
        lin (tuple[int or float, int or float] or list[int or float, int or float]): Line definition (slope, intercept)
        pt (tuple[int or float, int or float] or list[int or float, int or float]): Point definition (x, y)

    Returns:
        float: Distance from the point to the line, negative: below the line, 0: on the line, positive: above the line
    """
    if lin[0] is None:
        dist = pt[0] - lin[1]
    else:
        dist = (pt[1] - lin[0] * pt[0] - lin[1]) / np.sqrt(lin[0] ** 2 + 1).item()
    return dist


def poly_lin_poschk(lin, poly, th=0, sup=True):
    """ Check if a polygon has a relative position meets the defined threshold.

    Args:
        lin (tuple[int or float, int or float] or list[int or float, int or float]): Line definition (slope, intercept)
        poly (list[tuple[int or float, int or float]]): Point (x, y) list defined polygon
        th (int or float): Threshold
        sup (bool): True: above threshold, False: below threshold

    Returns:
        bool: Checked status
    """
    for pt in poly:
        dist = rel_pos(lin, pt)
        if sup:
            if dist <= th:
                return False
        else:
            if dist >= th:
                return False
    return True


# Animal behaviour detection functions ------------------------------------------------------------------------------- #

def cross_detect(crs_lst, th=6, frm_lst=None):
    """ Detect animal crossing behaviour.

    Args:
        crs_lst (list[int]): Input list of ROI cross
        th (int): Threshold size for detection
        frm_lst (list[int] or None): Input list of frame indices, auto-numbering if None

    Returns:
        list[list[int, int]]: Detected crossing behaviour
    """
    accu = 0  # INIT VAR
    started = False  # INIT VAR
    init = 0  # INIT VAR
    crs_range = []  # INIT VAR
    for n in range(len(crs_lst) - th):
        # Compute window value
        if n == 0:
            accu = sum(crs_lst[0:th])
        else:
            accu = accu - crs_lst[n - 1] + crs_lst[n + th - 1]
        # Check crossing
        if started:
            if accu == 0:
                started = False
                if frm_lst is None:
                    crs_range.append([init, n])
                else:
                    crs_range.append([frm_lst[init], frm_lst[n]])
        else:
            if accu >= th:
                started = True
                init = n
    return crs_range
