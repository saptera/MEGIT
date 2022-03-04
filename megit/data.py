import os
import math
import copy
import json
import numpy as np
import scipy.ndimage as ndi
import scipy.interpolate as itp
import cv2.cv2 as cv


def get_frm(vid_cap, frm_idx):
    """ Get specified frame of video file.

    Args:
        vid_cap (cv.VideoCapture): OpenCV video capture ID.
        frm_idx (int): Index of frame to get.

    Returns:
        np.ndarray: {2D, 3D} Image array of specified frame.
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
        img (np.ndarray): {2D, 3D} Input image.
        brt (int or float): Brightness level [-255, 255] (default: 0).
        con (int or float): Contrast level [-255, 255] (default: 0).

    Returns:
        np.ndarray: {2D, 3D} Adjusted image.
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
        img (np.ndarray): Input image.
        text (str): Input string.
        x (int): Left corner of text (default: 0).
        y (int): Top corner of text (default: 0).
        scale (int or float): Text size (default: 1).
        color (tuple[int, int, int]): Text color, in BGR (default: white - (255, 255, 255)).
        has_bkg (bool): Defines background exist or not (default: True).
        background (tuple[int, int, int] or None): Background color, in BGR (default: black - (0, 0, 0)).

    Returns:
        np.ndarray: Output image.
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
        img_list (list[str]): List of image files to create a video.
        vid_name (str): Output video name, without extension.
        fps (int or float): Output video frame rate (default: 30).
        vid_path (str or None): Output video path, use [img_path] when set to emptystring or None (default: None).

    Returns:
        (bool): True if video successfully created.
    """
    # Get video information
    vid_path = os.path.split(img_list[0])[0] if (vid_path == str()) or (vid_path is None) else vid_path
    vid_file = os.path.join(vid_path, vid_name + ".avi")
    frm_size = cv.imread(img_list[0]).shape[::-1][1:]

    # Write images to a video
    videoWriter = cv.VideoWriter(vid_file, cv.VideoWriter_fourcc(*"FFV1"), fps, frm_size)
    for i in img_list:
        img = cv.imread(i, cv.IMREAD_UNCHANGED)
        videoWriter.write(img)
    return os.path.isfile(vid_file)


def jsl_read(js_lbl_file):
    """ Import a standard JSON label file to a Python list of dictionary.

    Args:
        js_lbl_file (str): Labelling file contained with labels.

    Returns:
        list[dict]: List of dictionary with label info.
    """
    with open(js_lbl_file) as infile:
        jsl_data = json.load(infile)
    return jsl_data


def jsl_write(dst_jsl_file, jsl_data):
    """ Write JSON label data to a standard JSON label file.

    Args:
        dst_jsl_file (str): Labelling file to be write label data (*.json).
        jsl_data (list[dict]): List of dictionary with label info.

    Returns:
        bool: File creation status.
    """
    if len(jsl_data) != 0:
        with open(dst_jsl_file, 'w') as outfile:
            json.dump(jsl_data, outfile)
        return True
    else:
        print('Empty label data input, file not created!')
        return False


def lin2p(pt1, pt2):
    """ Get the slope and the intercept of a line defined by 2 points.

    Args:
        pt1 (tuple[int or float, int or float] or list[int or float, int or float]): 1st point (x1, y1).
        pt2 (tuple[int or float, int or float] or list[int or float, int or float]): 2nd point (x2, y2).

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
    """ Return relative position between a line and a point.

    Args:
        lin (tuple[int or float, int or float] or list[int or float, int or float]): Line definition (slope, intercept).
        pt (tuple[int or float, int or float] or list[int or float, int or float]): Point definition (x, y).

    Returns:
        int: -1: below the line, 0: on the line, 1: above the line.
    """
    if lin[0] is None:
        return np.sign(pt[0] - lin[1])
    else:
        return np.sign(pt[1] - lin[0] * pt[0] - lin[1])


def flt_spl(x, window, padding=None):
    """ Smooth continuous 1D array with median filter and univariate spline.

    Args:
        x (list or np.ndarray): {1D} Input array.
        window (int): Window size for median filter.
        padding (tuple[int or float, int or float] or None): Padding value for edges (default: None - No padding).

    Returns:
        np.ndarray: {1D} Smoothed array/
    """
    # Process edge padding
    if padding is None:
        src = np.asarray(x)
    else:
        pad_l = [padding[0]] * window
        pad_r = [padding[1]] * window
        src = np.concatenate((pad_l, x, pad_r))
    # Process median filter
    flt = ndi.median_filter(src, size=window)
    # Process univariate spline
    z = np.asarray(list(range(len(src))))
    spl = itp.UnivariateSpline(z, flt)
    smt = spl(z)
    # Arrange output
    dst = smt if padding is None else smt[window:-window]
    return dst
