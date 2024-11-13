import sys
import os
sys.path.append(os.getcwd())

import argparse
import csv
import numpy as np
import warnings
from megit.fio import cjsh_read, cjsh_write
from megit.batch import avgint_roi, det_avgint, det_prdpos, comb_det, grp_conv_hm2js


# CLI inputs parser  ------------------------------------------------------------------------------------------------- #
parser = argparse.ArgumentParser(prog="MegitCrsDet", description="MEGIT cross detection script",
                                 epilog="Automated detection of animal region cross")
parser.add_argument('-v', '--version', action='version', version="MEGIT - Cross detection: v1.0")
# Detection parameters
parser.add_argument('proc_dir', type=str, metavar="processFolder",
                    help="[%(type)s] Directory containing the inference results")
parser.add_argument('-t', '--threshold', dest='th_prd', type=float, default=3.0, metavar="[float]",
                    help="Cross detection threshold (default: %(default)s)")
# Parse inputs
args = parser.parse_args()
# -------------------------------------------------------------------------------------------------------------------- #


# Get basic info
proc_dir = args.proc_dir
disp = (True, 6)
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
        print("  Processing set [%s]..." % set_tp)
        # Get parameters
        tst = False if set_tp == 'byj' else True
        th_prd = args.th_prd

        # Input files
        frm_hdf = os.path.join(full_set_path, set_tp + '.frm')
        roi_prm = os.path.join(full_set_path, set_tp + '.roi')
        hml_hdf = os.path.join(full_set_path, set_tp + '.hml')
        ait_roi = os.path.join(full_set_path, set_tp + '.ait')
        jsl_prd = os.path.join(full_set_path, set_tp + '.jsl')
        rjl_prd = os.path.join(full_set_path, set_tp + '.rjl')
        # Output files
        crs_out = os.path.join(full_set_path, set_tp + '.csv')

        print("    Detect crossing event based on average intensity of ROIs")
        if os.path.isfile(ait_roi):
            ait = cjsh_read(ait_roi)
        else:
            ait = avgint_roi(roi_prm, frm_hdf, disp)
            cjsh_write(ait_roi, ait)
        grd, cns = det_avgint(ait, 5, 20, disp)
        print("    Detect crossing event based on model prediction positions")
        if os.path.isfile(jsl_prd):
            jsl = cjsh_read(jsl_prd)
        else:
            jsl, rjl = grp_conv_hm2js(hml_hdf, 'blob', False, disp)
            cjsh_write(jsl_prd, jsl)
            cjsh_write(rjl_prd, rjl)
        prd, rer = det_prdpos(roi_prm, jsl_prd, tst, th_prd, disp)
        print("    Combining detection results")
        frm = [int(k) for k in jsl]
        det = comb_det(grd, cns, prd, rer, frm, 6)

        # Write output
        crossing = {'frm': frm, 'gap': det['gap'], 'top': det['top'], 'btm': det['btm']}
        crossing = np.asarray([crossing[k] for k in crossing]).T.tolist()
        # Write CSV file
        print("    Writing output CSV...")
        with open(crs_out, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["frm", "gap", "top", "btm"])
            writer.writerows(crossing)

        print("  %s set [%s] process done!" % (ani_id, set_tp))

    curr_n += 1
    print("[%d / %d] process done!\n" % (curr_n, full_len))
