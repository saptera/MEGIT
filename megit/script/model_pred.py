import sys
import os
sys.path.append(os.getcwd())

import argparse
from keras.models import load_model
from megit.model.pred import default_model, inference
import warnings

# CLI inputs parser  ------------------------------------------------------------------------------------------------- #
parser = argparse.ArgumentParser(prog="MegitPosEst", description="MEGIT pose estimation script",
                                 epilog="Automated detection of animal joint positions")
parser.add_argument('-v', '--version', action='version', version="MEGIT - Pose estimation: v1.0")
# Detection parameters
parser.add_argument('proc_dir', type=str, metavar="processFolder",
                    help="[%(type)s] Directory containing the preprocessed frames")
parser.add_argument('-m', '--model', dest='model', type=str, default=default_model, metavar="[str]",
                    help="MEGIT pose estimation model (default: [overview.model]")
parser.add_argument('-s', '--size', dest='size', type=int, default=300, metavar="[int]",
                    help="Model inference batch size (default: %(default)s)")
# Parse inputs
args = parser.parse_args()
# -------------------------------------------------------------------------------------------------------------------- #


# Set basic info
proc_dir = args.proc_dir
model = load_model(args.model)
id_lst = [i for i in os.listdir(proc_dir) if os.path.isdir(os.path.join(proc_dir, i))]
st_lst = ['obj', 'juv', 'byj']

# Process
curr_n = 0
full_len = len(id_lst)
for ani_id in id_lst:
    print("Processing cross detection for %s:" % ani_id)
    for set_tp in st_lst:
        full_set_path = os.path.join(proc_dir, ani_id, set_tp)
        if not os.path.isdir(full_set_path):
            warnings.warn("Set [%s] is missing!" % set_tp, RuntimeWarning, stacklevel=2)
            continue
        # File definition
        frm_hdf = os.path.join(full_set_path, set_tp + '.frm')
        hml_hdf = os.path.join(full_set_path, set_tp + '.hml')
        # Inference
        print("  Tracking set [%s]..." % set_tp)
        inference(model, 2, frm_hdf, hml_hdf, args.size)
        print("  %s set [%s] process done!" % (ani_id, set_tp))

    curr_n += 1
    print("[%d / %d] process done!\n" % (curr_n, full_len))
