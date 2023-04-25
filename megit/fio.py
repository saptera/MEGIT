import os
import base64
import copy
import csv
import json
import h5py as h5
import zlib
import hashlib
import numpy as np
import cv2.cv2 as cv
import warnings

"""Function list:
  # Video IO functions
    img2vid(img_list, vid_name, fps=30, vid_path=None): Create a lossless AVI video file with given images.
  # Label file IO functions
    hml_read(hml_fp, key): Retrieve single HeatMap label from stored HDF5 file.
    cjsh_read(file): Compressed JSON with Secure Hash embedded (CJSH) file, reading function.
    cjsh_write(file, data): Compressed JSON with Secure Hash embedded (CJSH) file, writing function.
  # Experiment result file IO functions
    read_roi_poly(roi_json): Import ROI definition JSON file as list of polygon points.
    read_crscsv_set(crs_csv): Import crossing detection results for a single set.
    read_crscsv_mrg(crs_csv): Import merged crossing detection results for whole experiment.
"""


# Video IO functions ------------------------------------------------------------------------------------------------- #

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


# Label file IO functions -------------------------------------------------------------------------------------------- #

def hml_read(hml_fp, key):
    """ Retrieve single HeatMap label from stored HDF5 file.

    Args:
        hml_fp (h5.File): HeatMap label HDF5 file pointer
        key (str): Specific key to retrieve certain predictions

    Returns:
        dict[str, np.ndarray]: HeatMap format prediction label
    """
    lbl_lst = list(hml_fp[key].keys())
    hml = {k: None for k in lbl_lst}  # INIT VAR
    for lbl in lbl_lst:
        hml[lbl] = hml_fp[key][lbl][()]
    return hml


def cjsh_read(file):
    """ Compressed JSON with Secure Hash embedded (CJSH) file, reading function.

    Args:
        file (str): File contained compressed JSON data (*.*)

    Returns:
        Imported data
    """
    # Read data from the file
    with open(file, 'rb') as infile:
        indata = json.loads(zlib.decompress(infile.read()).decode('ascii'))
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
    # Archive the processed data with its hash value
    outdata = zlib.compress(json.dumps({'arc': compressed, 'cks': checksum}).encode('ascii'), level=0)
    # Write to the file
    try:
        with open(file, 'wb') as outfile:
            outfile.write(outdata)
        return True
    except OSError as x:
        warnings.warn("[Errno %d] when writing file '%s': %s" % (x.errno, file, x.strerror), Warning, stacklevel=2)
        return False


# Experiment result file IO functions -------------------------------------------------------------------------------- #

def read_roi_poly(roi_json):
    """ Import ROI definition JSON file as list of polygon points.

    Args:
        roi_json (str): ROI definition JSON file

    Returns:
        Polygon points of ROI, recommended access of (frame: i, region, r) by: ply[i].get(r, ply[ply[i][None]][r])
    """
    with open(roi_json, 'r') as jsonfile:
        roi = json.load(jsonfile)
    key = {'C': 'gap', 'T': 'top', 'B': 'btm', 'W': 'wal'}
    rgn = {'C': None, 'T': None, 'B': None, 'W': None}  # INIT VAR
    ply = {}  # INIT VAR
    curr = list(roi.keys())[0]  # INIT VAR
    for frm in roi:
        ply[frm] = {None: frm, 'gap': None, 'top': None, 'btm': None}  # [None] for default, optional [wal] is omitted
        for k in roi[frm]:
            rect = roi[frm][k]
            # This logical operation is safe as the raw JSON ROI data will have either all None or all not None
            if rect is None:
                ply[frm] = {None: curr}
            else:
                rgn[k] = [rect['tl'], rect['tr'], rect['br'], rect['bl']]
                ply[frm][key[k]] = copy.deepcopy(rgn[k])
                curr = frm
    return ply


def read_crscsv_set(crs_csv):
    """ Import crossing detection results for a single set.

    Args:
        crs_csv (str): Crossing detection results of set

    Returns:
        dict[str, list]: Results, keys = ['frm', 'gap', 'top', 'btm']
    """
    res = {'frm': [], 'gap': [], 'top': [], 'btm': []}  # INIT VAR
    with open(crs_csv, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        idx = 0
        for row in reader:
            if idx > 0:  # Escape header
                # Get object test crossings
                res['frm'].append(int(row[0]))
                res['gap'].append(int(row[1]))
                res['top'].append(int(row[2]))
                res['btm'].append(int(row[3]))
            idx += 1
    return res


def read_crscsv_mrg(crs_csv):
    """ Import merged crossing detection results for whole experiment.

    Args:
        crs_csv (str): Merged crossing detection results for whole experiment

    Returns:
        tuple[dict[str, list], dict[str, list], dict[str, list]]: Results, keys = ['frm', 'gap', 'top', 'btm']
            - obj (dict[str, list]): Object test crossings
            - juv (dict[str, list]): Juvenile test crossings
            - byj (dict[str, list]): By juvenile crossings (['top'] and ['btm'] are list of zeros)
    """
    obj = {'frm': [], 'gap': [], 'top': [], 'btm': []}  # INIT VAR
    juv = {'frm': [], 'gap': [], 'top': [], 'btm': []}  # INIT VAR
    byj = {'frm': [], 'gap': [], 'top': [], 'btm': []}  # INIT VAR
    with open(crs_csv, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        idx = 0
        for row in reader:
            if idx > 1:  # Escape header
                # Get object test crossings
                obj['frm'].append(int(row[0]))
                obj['gap'].append(int(row[1]))
                obj['top'].append(int(row[2]))
                obj['btm'].append(int(row[3]))
                # Get juvenile test crossings
                juv['frm'].append(int(row[4]))
                juv['gap'].append(int(row[5]))
                juv['top'].append(int(row[6]))
                juv['btm'].append(int(row[7]))
                # Get by juvenile crossings
                byj['frm'].append(int(row[4]))
                byj['gap'].append(int(row[8]))
                byj['top'].append(0)
                byj['btm'].append(0)
            idx += 1
    return obj, juv, byj
