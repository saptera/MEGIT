import os
import math
import copy
import base64
import json
import zlib
import hashlib
import pickle as pkl
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
    img2vid(img_list, vid_name, fps=30, vid_path=None): Create a lossless AVI video file with given images.
  # Legacy label file IO functions
    jsl_read(js_lbl_file):  Import a standard JSON label file to a Python list of dictionary.
    jsl_write(dst_jsl_file, jsl_data):  Write JSON label data to a standard JSON label file.
    hml_read(hm_lbl_file):  Import a PICKLE HeatMap label file to a Python list of dictionary.
    hml_write(dst_hml_file, hml_data):  Write HeatMap label data to a PICKLE label file.
  # Label file IO functions
    cjsh_read(file): Compressed JSON with Secure Hash embedded (CJSH) file, reading function.
    cjsh_write(file, data): Compressed JSON with Secure Hash embedded (CJSH) file, writing function.
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


def img2vid(img_list, vid_name, fps=30, vid_path=None):
    """Create a lossless AVI video file with given images.

    Args:
        img_list (list[str]): List of image files to create a video
        vid_name (str): Output video name, without extension
        fps (int or float): Output video frame rate (default: 30)
        vid_path (str or None): Output video path, use [img_path] when set to emptystring or None (default: None)

    Returns:
        (bool): True if video successfully created
    """
    # Get video information
    vid_path = os.path.split(img_list[0])[0] if (vid_path == str()) or (vid_path is None) else vid_path
    vid_file = os.path.join(vid_path, vid_name + ".avi")
    frm_size = cv.imread(img_list[0]).shape[::-1][1:]

    # Write images to a video
    writer = cv.VideoWriter(vid_file, cv.VideoWriter_fourcc(*"FFV1"), fps, frm_size)
    for i in img_list:
        img = cv.imread(i, cv.IMREAD_UNCHANGED)
        writer.write(img)
    return os.path.isfile(vid_file)


# Legacy label file IO functions ------------------------------------------------------------------------------------- #

def jsl_read(js_lbl_file):
    """ Import a standard JSON label file to a Python list of dictionary.

    Args:
        js_lbl_file (str): Labelling file contained with labels

    Returns:
        list[dict]: List of dictionary with label info
    """
    with open(js_lbl_file) as infile:
        jsl_data = json.load(infile)
    return jsl_data


def jsl_write(dst_jsl_file, jsl_data):
    """ Write JSON label data to a standard JSON label file.

    Args:
        dst_jsl_file (str): Labelling file to be write label data (*.json)
        jsl_data (list[dict]): List of dictionary with label info

    Returns:
        bool: File creation status
    """
    if len(jsl_data) != 0:
        with open(dst_jsl_file, 'w') as outfile:
            json.dump(jsl_data, outfile)
        return True
    else:
        print('Empty label data input, file not created!')
        return False


def hml_read(hm_lbl_file):
    """ Import a PICKLE HeatMap label file to a Python list of dictionary.

    Args:
        hm_lbl_file (str): Labelling file contained with HeatMap labels

    Returns:
        list[dict]: List of dictionary with HeatMap label info
    """
    with open(hm_lbl_file, 'rb') as infile:
        comp = pkl.load(infile)
    hml_data = pkl.loads(zlib.decompress(comp))
    return hml_data


def hml_write(dst_hml_file, hml_data):
    """ Write HeatMap label data to a PICKLE label file.

    Args:
        dst_hml_file (str): Labelling file to write HeatMap labels (*.pkl)
        hml_data (list[dict]): List of dictionary with HeatMap label info

    Returns:
        bool: File creation status
    """
    if len(hml_data) != 0:
        comp = zlib.compress(pkl.dumps(hml_data, protocol=2))
        with open(dst_hml_file, 'wb') as outfile:
            pkl.dump(comp, outfile, protocol=2)
        return True
    else:
        print('Empty label data input, file not created!')
        return False


# Label file IO functions -------------------------------------------------------------------------------------------- #

def cjsh_read(file):
    """ Compressed JSON with Secure Hash embedded (CJSH) file, reading function.

    Args:
        file (str): File contained compressed JSON data (*.*)

    Returns:
        Imported data
    """
    # Read data from the file
    with open(file, 'r') as infile:
        indata = json.load(infile)
    # Decode the data and compute the hash value
    serialized = zlib.decompress(base64.b64decode(indata['arc'].encode('ascii')))
    checksum = hashlib.sha256(serialized).hexdigest()
    # Verify and output the decoded data
    if checksum == indata['cks']:
        data = json.loads(serialized.decode('utf-8'))
    else:
        warnings.warn('Data corrupted in file: %s!' % file, Warning, stacklevel=2)
        data = None
    return data


def cjsh_write(file, data):
    """ Compressed JSON with Secure Hash embedded (CJSH) file, writing function.

    Args:
        file (str): Output file name
        data: Any type of data that is JSON serializable

    Returns:
        bool: File creation status
    """
    # Serialize input data to JSON format
    serialized = json.dumps(data, skipkeys=False, ensure_ascii=False, allow_nan=True).encode('utf-8')
    # Compress and hash the serialized data
    compressed = base64.b64encode(zlib.compress(serialized, level=9)).decode('ascii')
    checksum = hashlib.sha256(serialized).hexdigest()
    # Write to the file
    try:
        with open(file, 'w') as outfile:
            json.dump({'arc': compressed, 'cks': checksum}, outfile)
        return True
    except OSError as x:
        warnings.warn("[Errno %d] when writing file '%s': %s" % (x.errno, file, x.strerror), Warning, stacklevel=2)
        return False


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

    Args:
        frm_lst (list[int]): Input list of frame indices

    Returns:
        list[list[int]]: Frame indices seperated by gaps
    """
    sep_init = 0  # INIT VAR
    sep_idx = []  # INIT VAR
    for i in range(len(frm_lst) - 1):
        if (frm_lst[i + 1] - frm_lst[i]) != 1:
            sep_idx.append([sep_init, i + 1])
            sep_init = i + 1
    sep_idx.append([sep_init, len(frm_lst)])
    return sep_idx


def get_proc_rng(proc_idx, frm_lst, flk_size=60):
    """ Get valid and merged window for list process based on frame indices.

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
            if sep[0] <= i <= sep[1]:
                rl = sep[0] if i - flk_size < sep[0] else i - flk_size
                rr = sep[1] if i + flk_size + 1 > sep[1] else i + flk_size + 1
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
    elif x.dtype != float:
        src = x.astype(np.float64)
    else:
        src = x
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
        # Extract padded NaN values and position
        val = np.where(mask, smt, src).tolist()
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
