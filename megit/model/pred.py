import os
import numpy as np
import cv2 as cv
import h5py as h5
import keras
from ..utils import prog_print

"""Constant list:
    default_model: MEGIT default pose estimation model 
   Function list:
    images_to_tensor(frm_fp, idx): Collect images into a {4D} tensor.
    save_heatmap_result(pred, hml_fp, idx, lbl): Store heatmap predictions into a HDF5 file.
    inference(model, num_stg, frm_file, out_file, size, lbl): Use trained model to make predictions on images.
"""


default_model = os.path.abspath('overview.model')


def images_to_tensor(frm_fp, idx):
    """ Collect images into a {4D} tensor.

    Args:
        frm_fp (h5.File): Frame data HDF5 file reference
        idx (list[str]): Frame index keys

    Returns:
        np.ndarray: {4D} Tensor of images in the given indices
    """
    tensor = []  # INIT VAR
    for f in idx:
        img = cv.cvtColor(frm_fp[f][()], cv.COLOR_GRAY2BGR)
        img = cv.normalize(img, None, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)
        tensor.append(img)
    return np.array(tensor)


def save_heatmap_result(pred, hml_fp, idx, lbl):
    """ Store heatmap predictions into a HDF5 file.

    Args:
        pred (np.ndarray): {4D} tensor with each slice of {3D} tensor being the heatmap prediction of an image
        hml_fp (h5.File): HeatMap output HDF5 file reference
        idx (list[str]): Frame index keys
        lbl (tuple[str] | list[str]): Sorted list of filenames for the prediction results
    """
    for i, f in enumerate(idx):
        grp = hml_fp.create_group(f)
        for j, b in enumerate(lbl):
            grp.create_dataset(b, data=pred[i][..., j], compression="gzip", compression_opts=9)


def inference(model, num_stg, frm_file, out_file, size, lbl=("nose", "left_ear", "right_ear")):
    """ Use trained model to make predictions on images.

    Args:
        model (keras.Model): Trained model for inference predictions
        num_stg (int): Number of stages of the trained model
        frm_file (str): Complete test image folder path
        out_file (str): Complete path to the dataset folder
        size (int): Step size
        lbl (tuple[str]): Tuple of predicted joints
    """
    # File IO initialize
    dat = h5.File(frm_file, 'r')
    out = h5.File(out_file, 'w')
    # Get steps
    frm = sorted(dat.keys(), key=int)
    n = len(range(0, len(frm), size))
    count = 0  # INIT VAR
    # Inference loop
    for i in range(0, len(frm), size):
        img_tsr = images_to_tensor(dat, frm[i: i + size])
        stages = model.predict(img_tsr)
        tensors = stages[-1] if num_stg > 1 else stages
        # Output files
        save_heatmap_result(tensors, out, frm[i: i + size], lbl)
        # Progress report
        prog_print(count, n, "Prediction:", "done.")
        count += 1
    # Close files
    dat.close()
    out.close()
