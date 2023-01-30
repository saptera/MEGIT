import os
import base64
import json
import zlib
import hashlib
import pickle as pkl
import cv2.cv2 as cv
import warnings

"""Function list:
  # Video IO functions
    img2vid(img_list, vid_name, fps=30, vid_path=None): Create a lossless AVI video file with given images.
  # Legacy label file IO functions
    jsl_read(js_lbl_file):  Import standard JSON label file.
    jsl_write(dst_jsl_file, jsl_data):  Write JSON label data to file.
    hml_read(hm_lbl_file):  Import HeatMap label file.
    hml_write(dst_hml_file, hml_data):  Write HeatMap label data to file.
  # Label file IO functions
    cjsh_read(file): Compressed JSON with Secure Hash embedded (CJSH) file, reading function.
    cjsh_write(file, data): Compressed JSON with Secure Hash embedded (CJSH) file, writing function.
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


# Legacy label file IO functions ------------------------------------------------------------------------------------- #

def jsl_read(file):
    """ Import standard JSON label file.

    Args:
        file (str): Labelling file contained with labels

    Returns:
        list[dict]: List of dictionary with label info
    """
    with open(file) as infile:
        jsl_data = json.load(infile)
    return jsl_data


def jsl_write(file, jsl_data):
    """ Write JSON label data to file.

    Args:
        file (str): Labelling file to be write label data (*.json)
        jsl_data (list[dict]): List of dictionary with label info

    Returns:
        bool: File creation status
    """
    if len(jsl_data) != 0:
        try:
            with open(file, 'w') as outfile:
                json.dump(jsl_data, outfile)
            return True
        except OSError as x:
            warnings.warn("[Errno %d] when writing file '%s': %s" % (x.errno, file, x.strerror), Warning, stacklevel=2)
            return False
    else:
        print('Empty label data input, file not created!')
        return False


def hml_read(file):
    """ Import HeatMap label file.

    Args:
        file (str): Labelling file contained with HeatMap labels

    Returns:
        list[dict]: List of dictionary with HeatMap label info
    """
    with open(file, 'rb') as infile:
        comp = pkl.load(infile)
    hml_data = pkl.loads(zlib.decompress(comp))
    return hml_data


def hml_write(file, hml_data):
    """ Write HeatMap label data to file.

    Args:
        file (str): Labelling file to write HeatMap labels (*.pkl)
        hml_data (list[dict]): List of dictionary with HeatMap label info

    Returns:
        bool: File creation status
    """
    if len(hml_data) != 0:
        comp = zlib.compress(pkl.dumps(hml_data, protocol=2))
        try:
            with open(file, 'wb') as outfile:
                pkl.dump(comp, outfile, protocol=2)
            return True
        except OSError as x:
            warnings.warn("[Errno %d] when writing file '%s': %s" % (x.errno, file, x.strerror), Warning, stacklevel=2)
            return False
    else:
        warnings.warn("Empty label data input, file not created!", Warning, stacklevel=2)
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
