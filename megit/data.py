import os
import math
import copy
import numpy as np
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
