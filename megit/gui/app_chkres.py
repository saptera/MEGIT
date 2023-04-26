import os
import copy
import tempfile
import csv
import h5py as h5
import numpy as np
import cv2.cv2 as cv
from megit.fio import cjsh_read, read_roi_poly, read_crscsv_set
from megit.data import draw_text, hml_plt, jsl_plt
from PyQt5 import QtCore, QtGui, QtWidgets
from megit.gui.dgn_chkres_load import Ui_MainLoader
from megit.gui.dgn_chkres_ctrl import Ui_CrossVerifier


# Global definitions  -----------------------------------------------------------------------------------------------  #
# Define colour palettes
color_palette = {'tst_gap': (0, 158, 115), 'tst_top': (0, 114, 178), 'tst_btm': (213, 94, 0), 'tst_wal': (75, 0, 146),
                 'byj_gap': (204, 121, 167), 'byj_top': (86, 180, 233), 'byj_btm': (230, 159, 0)}  # Colourblind safe
color_labels = {"nose": (255, 0, 0), "left_ear": (0, 255, 0), "right_ear": (0, 0, 255)}
color_labels_alt = {"nose": (31, 119, 180), "left_ear": (255, 127, 14), "right_ear": (214, 39, 40)}

# Global data pipeline variables
curr_frm = 0  # Current frame index
frm_fp = h5.File(tempfile.TemporaryFile(), 'w')  # Frame data file pointer
res = {}  # Cross detection results
ait = {}  # Average intensity data
roi = {}  # ROI information
set_flg = False  # Set type information
clr_key = str()  # Set colour key
hml_fp = h5.File(tempfile.TemporaryFile(), 'w')  # Prediction HeatMap file pointer
jsl_pd = {}  # Prediction JSON labels
man_crs = {}  # Manual correction data


# [CrossVerifier] MEGIT Cross-Verifier main GUI  --------------------------------------------------------------------  #
class CrossVerifier(QtWidgets.QMainWindow, Ui_CrossVerifier):
    def __init__(self, parent=None):
        global set_flg
        # Set up GUI elements
        super(CrossVerifier, self).__init__(parent)
        self.setupUi(self)
        set_flg and self.dispRoiBox.addItem('Wall')  # Add WALL region for test animal
        # Set frame display scene
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 600, 600)  # Frame size 600 * 600
        self.frameDisplay.setScene(self.scene)
        # Set status bar
        self.modeLine = QtWidgets.QLineEdit()
        self.modeLine.setReadOnly(True)
        self.modeLine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.modeLine.setText("Manual mode: Use buttons to set crossings")
        self.statusBar().addPermanentWidget(self.modeLine)
        # Set local control flags
        self.__disp_roi = None
        self.__disp_hml = False
        self.__disp_jsl = False
        self.__rng_init = None
        self.__int_flag = False
        self.__roi_ths = None
        self.__int_init = [None, None, None]
        self.out_csv = str()
        # Display control connections
        self.frmSlider.valueChanged.connect(self.__frame_slider_control)
        self.dispRoiCheckBox.toggled.connect(self.__set_disp_roi)
        self.dispRoiBox.currentIndexChanged.connect(self.__set_disp_roi)
        self.dispHmlCheckBox.toggled.connect(self.__toggle_disp_hml)
        self.dispJslCheckBox.toggled.connect(self.__toggle_disp_jsl)
        # Manual verification single frame button connections
        self.gapBtnSgnT.clicked.connect(lambda: self.__set_single_frame('gap', 1))
        self.gapBtnSgnF.clicked.connect(lambda: self.__set_single_frame('gap', 0))
        self.topBtnSgnT.clicked.connect(lambda: self.__set_single_frame('top', 1))
        self.topBtnSgnF.clicked.connect(lambda: self.__set_single_frame('top', 0))
        self.btmBtnSgnT.clicked.connect(lambda: self.__set_single_frame('btm', 1))
        self.btmBtnSgnF.clicked.connect(lambda: self.__set_single_frame('btm', 0))
        # Manual verification frame range button connections
        self.gapBtnRgnTS.clicked.connect(lambda: self.__frame_range_start(self.gapBtnRgnTS.isChecked()))
        self.gapBtnRgnTE.clicked.connect(lambda: self.__frame_range_stop('gap', 1))
        self.gapBtnRgnFS.clicked.connect(lambda: self.__frame_range_start(self.gapBtnRgnFS.isChecked()))
        self.gapBtnRgnFE.clicked.connect(lambda: self.__frame_range_stop('gap', 0))
        self.topBtnRgnTS.clicked.connect(lambda: self.__frame_range_start(self.topBtnRgnTS.isChecked()))
        self.topBtnRgnTE.clicked.connect(lambda: self.__frame_range_stop('top', 1))
        self.topBtnRgnFS.clicked.connect(lambda: self.__frame_range_start(self.topBtnRgnFS.isChecked()))
        self.topBtnRgnFE.clicked.connect(lambda: self.__frame_range_stop('top', 0))
        self.btmBtnRgnTS.clicked.connect(lambda: self.__frame_range_start(self.btmBtnRgnTS.isChecked()))
        self.btmBtnRgnTE.clicked.connect(lambda: self.__frame_range_stop('btm', 1))
        self.btmBtnRgnFS.clicked.connect(lambda: self.__frame_range_start(self.btmBtnRgnFS.isChecked()))
        self.btmBtnRgnFE.clicked.connect(lambda: self.__frame_range_stop('btm', 0))
        # Intelligent mode control connections
        self.intModeCheckBox.toggled.connect(self.__intelligent_mode_switch)
        self.intThsSpinBox.valueChanged.connect(self.__intelligent_mode_threshold)
        # Set main control buttons
        self.discardButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.saveButton.clicked.connect(self. __save_results)
        # Initialize frame view
        self.__update_frame(curr_frm)
        self.statusBar().showMessage("Ready")

    def keyPressEvent(self, event):
        global curr_frm
        if type(event) == QtGui.QKeyEvent:
            if event.key() == QtCore.Qt.Key_A or event.key() == QtCore.Qt.Key_Left:
                curr_frm -= 1
                self.frmSlider.setValue(curr_frm)
            elif event.key() == QtCore.Qt.Key_D or event.key() == QtCore.Qt.Key_Right:
                curr_frm += 1
                self.frmSlider.setValue(curr_frm)
            elif event.key() == QtCore.Qt.Key_V:  # Intelligent mode single frame cross
                if self.__int_flag:
                    self.__intelligent_mode_single_true()
            elif event.key() == QtCore.Qt.Key_X:  # Intelligent mode single frame no-cross
                if self.__int_flag:
                    self.__intelligent_mode_single_false()
            elif event.key() == QtCore.Qt.Key_Comma:  # Intelligent mode frame range cross start
                if self.__int_flag:
                    self.__intelligent_mode_range_start(True)
            elif event.key() == QtCore.Qt.Key_Period:  # Intelligent mode frame range cross stop
                if self.__int_flag:
                    self.__intelligent_mode_range_stop(True)
            elif event.key() == QtCore.Qt.Key_BracketLeft:  # Intelligent mode frame range no-cross start
                if self.__int_flag:
                    self.__intelligent_mode_range_start(False)
            elif event.key() == QtCore.Qt.Key_BracketRight:  # Intelligent mode frame range no-cross stop
                if self.__int_flag:
                    self.__intelligent_mode_range_stop(False)
            else:
                QtWidgets.QMainWindow.keyPressEvent(self, event)
        else:
            QtWidgets.QMainWindow.keyPressEvent(self, event)

    def closeEvent(self, event):
        global frm_fp, hml_fp
        frm_fp.close()
        hml_fp.close()

    @staticmethod
    def plot_frame(frm_idx, plt_roi=None, plt_hml=True, plt_jsl=True):
        """ Plot frame with information.

        Args:
            frm_idx (int): Index of frame to be plotted (not the actual frame number)
            plt_roi (bool or str): ROI plot flag
            plt_hml (bool): HeatMap label plot flag
            plt_jsl (bool): JSON label plot flag

        Returns:
            Plotted image in BGR color space
        """
        global frm_fp, roi, clr_key, res, hml_fp, jsl_pd, man_crs, color_palette, color_labels, color_labels_alt
        frm_key = str(res['frm'][frm_idx])
        # Read frame image
        pfr = cv.cvtColor(frm_fp[frm_key][()], cv.COLOR_GRAY2BGR)
        # Plot predictions
        if plt_hml:
            hml = {kn: hml_fp[frm_key][kn][()] for kn in hml_fp[frm_key].keys()}
            pfr = hml_plt(hml, pfr, clst=color_labels)
        if plt_jsl:
            jsl_clst = color_labels_alt if plt_hml else color_labels
            pfr = jsl_plt(jsl_pd[frm_key], pfr, raw=False, clst=jsl_clst)
        # Put frame number
        pfr = draw_text(pfr, "%05d" % res['frm'][frm_idx], 10, 10, scale=0.5)
        # Put detection results
        roi_det = None
        for cfd in ['gap', 'top', 'btm']:
            if res[cfd][frm_idx] == 1:
                pfr = draw_text(pfr, cfd.upper(), 10, 35, scale=0.5, color=color_palette[clr_key + cfd])
                roi_det = cfd
                break
        # Plot ROI
        plt_roi = roi_det if plt_roi == 'det' else plt_roi
        if plt_roi is not None:
            roi_ply = \
                [np.rint(roi[frm_key].get(plt_roi, roi[roi[frm_key][None]][plt_roi])).astype(int).reshape((-1, 1, 2))]
            pfr = cv.polylines(pfr, roi_ply, isClosed=True, color=color_palette[clr_key + plt_roi], thickness=1)
        # Put manual verification results
        for cfd in ['gap', 'top', 'btm']:
            if man_crs[cfd][frm_idx] == 1:
                pfr = draw_text(pfr, 'V ' + cfd.upper(), 10, 220, scale=0.5, color=(34, 139, 34))
                break
            elif man_crs[cfd][frm_idx] == 0:
                pfr = draw_text(pfr, 'X ' + cfd.upper(), 10, 220, scale=0.5, color=(60, 20, 220))
                break
            elif man_crs[cfd][frm_idx] == -1:
                pfr = draw_text(pfr, "No Diff", 10, 220, scale=0.5, color=(0, 215, 255))
                break
        # Resize and return
        pfr = cv.resize(pfr, (600, 600), interpolation=cv.INTER_CUBIC)  # Frame size 600 * 600
        return pfr

    def __frame_slider_control(self):
        global curr_frm
        curr_frm = self.frmSlider.value()
        self.__update_frame(curr_frm)  # Update frame viewer

    def __set_disp_roi(self):
        curr_roi_mode = ['det', 'gap', 'top', 'btm', 'wal'][self.dispRoiBox.currentIndex()]
        self.__disp_roi = curr_roi_mode if self.dispRoiCheckBox.isChecked() else None
        self.__update_frame(curr_frm)  # Update frame viewer

    def __toggle_disp_hml(self):
        self.__disp_hml = self.dispHmlCheckBox.isChecked()
        self.__update_frame(curr_frm)  # Update frame viewer

    def __toggle_disp_jsl(self):
        self.__disp_jsl = self.dispJslCheckBox.isChecked()
        self.__update_frame(curr_frm)  # Update frame viewer

    def __update_frame(self, val):
        # Convert OpenCV np-array image to QImage
        frm = self.plot_frame(val, self.__disp_roi, self.__disp_hml, self.__disp_jsl)
        lbl_img = QtGui.QImage(frm, frm.shape[1], frm.shape[0], frm.shape[1] * 3, QtGui.QImage.Format_RGB888)
        # Delete previous frame
        for i in self.scene.items():
            if i.type() == 7:  # QGraphicsPixmapItem::Type = 7
                self.scene.removeItem(i)
        # Add new frame
        self.scene.addPixmap(QtGui.QPixmap(lbl_img.rgbSwapped()))

    def __set_single_frame(self, key, val):
        global curr_frm, res, man_crs
        chk_val = -1 if res[key][curr_frm] == val else val
        for k in man_crs:
            man_crs[k][curr_frm] = chk_val if k == key else None
        self.__update_frame(curr_frm)  # Update frame viewer
        self.statusBar().showMessage("Frame [IDX: %05d] corrected" % curr_frm, 5000)

    def __frame_range_start(self, val):
        global curr_frm
        self.__rng_init = curr_frm if val else None
        self.statusBar().showMessage("Frame range manual correction started at [IDX: %05d]" % curr_frm)

    def __frame_range_stop(self, key, val):
        global curr_frm, res, man_crs
        frm_init = min(curr_frm, self.__rng_init)
        frm_stop = max(curr_frm, self.__rng_init) + 1
        for k in man_crs:
            if k == key:
                man_crs[k][frm_init:frm_stop] = [-1 if res[k][i] == val else val for i in range(frm_init, frm_stop)]
            else:
                man_crs[k][frm_init:frm_stop] = [None] * (frm_stop - frm_init)
        self.__rng_init = None  # Reset value
        self.__update_frame(curr_frm)  # Update frame viewer
        self.statusBar().showMessage("Frame range manual correction stop at [IDX: %05d]" % curr_frm, 5000)

    def __intelligent_mode_switch(self):
        global ait
        self.__int_flag = self.intModeCheckBox.isChecked()
        if self.__int_flag:
            self.modeLine.setText("Intelligent mode: V = CrS | X = NcS | Comma = CrRs | Period = CrRe | "
                                  "BracketLeft = NcRs | BracketRight = NcRe")
        else:
            self.modeLine.setText("Manual mode: Use buttons to set crossings")
        if self.__roi_ths is None:
            self.__roi_ths = {k: max(ait[k]) - self.intThsSpinBox.value() for k in ait}

    def __intelligent_mode_threshold(self):
        global ait
        self.__roi_ths = {k: max(ait[k]) - self.intThsSpinBox.value() for k in ait}

    def __check_possible_region(self, val):
        global ait
        tmp = {k: self.__roi_ths[k] - ait[k][val] for k in ait}
        if all(val <= 0 for val in tmp.values()):
            return None
        else:
            return max(tmp, key=tmp.get)

    def __check_current_frame(self, val, flag):
        key = self.__check_possible_region(val)
        if flag:
            if key is None:
                QtWidgets.QMessageBox.warning(self, "Warning", "No possible region found!\n"
                                                               "Try a lower threshold or use manual mode.",
                                              QtWidgets.QMessageBox.Ok)
            return key
        else:
            if key:
                reply = QtWidgets.QMessageBox.warning(self, "Warning", "Possible crossing [%s] detected.\n"
                                                                       "Do you wish to continue?" % key.upper(),
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                      QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.No:
                    return None
            return 'all'

    def __intelligent_mode_single_true(self):
        global curr_frm
        key = self.__check_current_frame(curr_frm, True)
        if key:
            self.__set_single_frame(key, 1)

    def __intelligent_mode_single_false(self):
        global curr_frm
        key = self.__check_current_frame(curr_frm, False)
        if key:
            for k in ['gap', 'top', 'btm']:
                self.__set_single_frame(k, 0)

    def __intelligent_mode_range_start(self, flag):
        global curr_frm
        if self.__int_init[0] is flag:
            msg = "Manual correction [CROSS] for [%s] cancelled" % self.__int_init[2].upper() \
                if flag else "Manual correction [NO-CROSS] cancelled"
            self.statusBar().showMessage(msg, 5000)
            self.__int_init = [None, None, None]
            self.intThsSpinBox.setEnabled(True)
        else:
            key = self.__check_current_frame(curr_frm, flag)
            if key:
                self.__int_init = [flag, curr_frm, key]
                msg = "Manual correction [CROSS] for [%s] started at [IDX: %05d]" % (key.upper(), curr_frm) \
                    if flag else "Manual correction [NO-CROSS] started at [IDX: %05d]" % curr_frm
                self.statusBar().showMessage(msg)
                self.intThsSpinBox.setEnabled(False)

    def __intelligent_mode_range_stop(self, flag):
        global curr_frm, res, man_crs
        if self.__int_init[0] is flag:
            frm_init = min(curr_frm, self.__int_init[1])
            frm_stop = max(curr_frm, self.__int_init[1]) + 1
            key = self.__int_init[2]
            chk_lst = [self.__check_possible_region(i) for i in range(frm_init, frm_stop)]
            if flag:
                if any(val is None for val in chk_lst):
                    reply = QtWidgets.QMessageBox.warning(self, "Warning",
                                                          "No cross detected in some frames within the selection .\n"
                                                          "Do you wish to continue?",
                                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                          QtWidgets.QMessageBox.No)
                    if reply == QtWidgets.QMessageBox.No:
                        return
                for k in man_crs:
                    if k == key:
                        man_crs[k][frm_init:frm_stop] = [-1 if res[k][i] == 1 else 1 for i in range(frm_init, frm_stop)]
                    else:
                        man_crs[k][frm_init:frm_stop] = [None] * (frm_stop - frm_init)
                self.statusBar().showMessage("Manual correction [CROSS] for [%s] stop at [IDX: %05d]" %
                                             (key.upper(), curr_frm), 5000)
            else:
                if any(val is not None for val in chk_lst):
                    reply = QtWidgets.QMessageBox.warning(self, "Warning",
                                                          "Cross detected in some frames within the selection .\n"
                                                          "Do you wish to continue?",
                                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                          QtWidgets.QMessageBox.No)
                    if reply == QtWidgets.QMessageBox.No:
                        return
                for i in range(frm_init, frm_stop):
                    res_slc = [res[k][i] for k in ['gap', 'top', 'btm']]
                    if all(val == 0 for val in res_slc):
                        for k in man_crs:
                            man_crs[k][i] = -1
                    else:
                        for k in man_crs:
                            man_crs[k][i] = None if res[k][i] == 0 else 0
                self.statusBar().showMessage("Manual correction [NO-CROSS] stop at [IDX: %05d]" % curr_frm, 5000)
            # GUI updates
            self.__int_init = [None, None, None]
            self.__update_frame(curr_frm)  # Update frame viewer
            self.intThsSpinBox.setEnabled(True)

    def __save_results(self):
        global res, man_crs
        # Arrange data
        fin_res = copy.deepcopy(res)
        for k in man_crs:
            for i, val in enumerate(man_crs[k]):
                if val == 0 or val == 1:
                    fin_res[k][i] = val
        # Set output file
        res_lst = [[fin_res[k][i] for k in fin_res] for i in range(len(res['frm']))]
        with open(self.out_csv, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['frm', 'gap', 'top', 'btm'])
            writer.writerows(res_lst)
        # Exit application
        self.close()


# [MainLoader] MEGIT Cross-Verifier main loader  --------------------------------------------------------------------  #
class MainLoader(QtWidgets.QMainWindow, Ui_MainLoader):
    def __init__(self, parent=None):
        super(MainLoader, self).__init__(parent)
        self.setupUi(self)
        self.applicationWindow = None

        self.frmButton.clicked.connect(self.__frame_selection)
        self.crsButton.clicked.connect(self.__cross_selection)
        self.roiButton.clicked.connect(self.__roiproperty_selection)
        self.aitButton.clicked.connect(self.__intensity_selection)
        self.hmlButton.clicked.connect(self.__hmlabel_selection)
        self.jslButton.clicked.connect(self.__jslabel_selection)
        self.loadButton.clicked.connect(self.__loading_func)
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

    # File loading button functions
    def __frame_selection(self):
        frm_dat, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Preprocessed Frames", filter="Frames (*.frm)")
        self.frmPath.setText(frm_dat)

    def __cross_selection(self):
        crs_csv, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Detected Crossings", filter="CSV File (*.csv)")
        self.crsPath.setText(crs_csv)

    def __roiproperty_selection(self):
        roi_jsn, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select ROI Properties", filter="ROI File (*.roi)")
        self.roiPath.setText(roi_jsn)

    def __intensity_selection(self):
        avg_int, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Average Intensity", filter="AIT File (*.ait)")
        self.aitPath.setText(avg_int)

    def __hmlabel_selection(self):
        prd_hml, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select HeatMap Labels", filter="HML File (*.hml)")
        self.hmlPath.setText(prd_hml)

    def __jslabel_selection(self):
        prd_jsl, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select JSON Labels", filter="JSL File (*.jsl)")
        self.jslPath.setText(prd_jsl)

    # Main loading function
    def __loading_func(self):
        global frm_fp, res, ait, roi, set_flg, clr_key, hml_fp, jsl_pd, man_crs
        # Verify GUI inputs
        flag = ait_flag = hml_flag = jsl_flag = False
        err_msg = str()
        # Check required files
        if not os.path.isfile(self.frmPath.text()):
            flag = True
            err_msg += "Frame file does not exist!\n"
        if not os.path.isfile(self.crsPath.text()):
            flag = True
            err_msg += "Detected crossing data does not exist!\n"
        if not os.path.isfile(self.roiPath.text()):
            flag = True
            err_msg += "ROI properties file does not exist!\n"
        # Check optional files
        if self.aitPath.text() != str():
            if os.path.isfile(self.aitPath.text()):
                ait_flag = True
            else:
                flag = True
                err_msg += "Defined average intensity data file does not exist!\n"
        if self.hmlPath.text() != str():
            if os.path.isfile(self.hmlPath.text()):
                hml_flag = True
            else:
                flag = True
                err_msg += "Defined HeatMap prediction data file does not exist!\n"
        if self.jslPath.text() != str():
            if os.path.isfile(self.jslPath.text()):
                jsl_flag = True
            else:
                flag = True
                err_msg += "Defined JSON prediction data file does not exist!\n"
        # Error report
        if flag:
            QtWidgets.QMessageBox.critical(self, "Error", err_msg)
            return

        # Get frame data
        frm_fp.close()  # Close tempfile
        frm_fp = h5.File(self.frmPath.text(), 'r')
        # Get cross detection results
        res = read_crscsv_set(self.crsPath.text())
        out_csv = os.path.splitext(self.crsPath.text())[0] + '_ver.csv'
        # Get ROI information
        roi = read_roi_poly(self.roiPath.text())
        # Get set information
        rik = list(roi.keys())[0]
        set_flg = sum([roi[rik]['gap'][_][0] for _ in range(4)]) < sum([roi[rik]['top'][_][0] for _ in range(4)])
        clr_key = 'tst_' if set_flg else 'byj_'
        # Get average intensity data
        if ait_flag:
            ait = cjsh_read(self.aitPath.text())
        # Read prediction labels
        if hml_flag:
            hml_fp.close()  # Close tempfile
            hml_fp = h5.File(self.hmlPath.text(), 'r')
        if jsl_flag:
            jsl_pd = cjsh_read(self.jslPath.text())
        # Initialize manual correction recorder
        man_crs = {k: [None] * len(roi) for k in ['gap', 'top', 'btm']}

        # Initialize controller GUI
        self.applicationWindow = CrossVerifier()
        self.applicationWindow.out_csv = out_csv
        self.applicationWindow.frmSlider.setMaximum(len(roi) - 1)
        self.applicationWindow.sldrValue.setMaximum(len(roi) - 1)
        self.applicationWindow.intModeCheckBox.setEnabled(ait_flag)
        self.applicationWindow.dispHmlCheckBox.setEnabled(hml_flag)
        self.applicationWindow.dispJslCheckBox.setEnabled(jsl_flag)
        self.applicationWindow.show()
        self.hide()
