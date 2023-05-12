import os
import copy
import json
import h5py as h5
import math
import numpy as np
import cv2 as cv
from megit.data import get_frm, brt_con, draw_text
from megit.utils import mk_outdir
from PyQt5 import QtCore, QtGui, QtWidgets
from megit.gui.dgn_preproco_ctrl import Ui_ControlViewer
from megit.gui.dgn_preproc_frmv import Ui_FrameViewer
from megit.gui.dgn_preproc_load import Ui_MainLoader


# Global definitions  -----------------------------------------------------------------------------------------------  #
# Define a class to handle cross window signals
class ComSig(QtCore.QObject):
    win_stat_sig = QtCore.pyqtSignal(QtCore.Qt.WindowStates)  # Cross window state settings
    frm_ctrl_sig = QtCore.pyqtSignal(int)  # Frame selection operation synchronizer
    frm_info_sig = QtCore.pyqtSignal(int, str)  # Current frame information messenger
    mkr_disp_sig = QtCore.pyqtSignal()  # Marker display messenger
    mkr_ctrl_sig = QtCore.pyqtSignal()  # Marker group control operation messenger
    mkr_updt_sig = QtCore.pyqtSignal(int)  # Marker item group updating messenger
    mkr_info_sig = QtCore.pyqtSignal(int, int, str)  # Current marker information messenger


# Define global control variables
com_sig = ComSig()  # Global signals
vid_cap = cv.VideoCapture()  # OpenCV video capture
loaded = False  # File loading status flag
frm = None  # Current frame image
frm_msg = str()  # Information message of current frame
frm_list = []  # Frame selection list
mk_mode = 'NONE'  # Current marking mode
roi_id = 0  # ROI item unique IDs
roi_grp = [0]  # ROI item group
color_palette = {'TGT_C': (0, 158, 115), 'TGT_T': (0, 114, 178), 'TGT_B': (213, 94, 0), 'TGT_W': (75, 0, 146),
                 'JUV_C': (204, 121, 167), 'JUV_T': (86, 180, 233), 'JUV_B': (230, 159, 0)}  # Colourblind safe palette
mkr_vis = True  # Marker visibility flag
mkr_msg = "No Marker Selected"  # Information message of current label

# Define global process variables
out_dir = str()  # Output directory
frm_dig = '%05d'  # Length of frame digits
brt = 0  # Brightness level
con = 0  # Contrast level
txt_mark = False  # Define frame index text exist or not
txt_linc = (255, 255, 255)  # Frame index text colour
txt_hbkg = True  # Defines text background exist or not
txt_bkgc = (0, 0, 0)  # Frame index background colour
txt_size = 1  # Frame index text size
txt_xval = 0  # Frame index text left corner
txt_yval = 0  # Frame index text right corner
exp_typ = False  # Experiment type: True = Juvenile, False = Object
frm_num = 0  # Number of frames to keep
frm_esc = []  # Excluded frames
roi_data = {}  # Process region of interest


# Frame selection list operation function
def update_frame_selection():
    global frm_num, frm_esc, frm_list
    count = 0  # Total frame counter
    # Return selected and unselected indices of a list.
    for i in range(len(frm_list)):
        if any(lower <= i <= upper for [lower, upper] in frm_esc):
            frm_list[i]['keep'] = -1  # -1: Frame to be removed
        else:
            if count < frm_num:
                frm_list[i]['keep'] = 1  # 1: Frame to keep
            else:
                frm_list[i]['keep'] = 0  # 0: Extra frame
            count += 1


# Current ROI ID detection function
def find_roi_id(frm_idx):
    global roi_id, roi_grp
    new_id = -1
    for i in roi_grp:
        if frm_idx >= i:
            new_id += 1
        else:
            break
    id_flag = new_id != roi_id
    roi_id = new_id
    return id_flag


# ROI group operation function
def update_roi_group(frm_idx):
    global roi_grp, roi_data
    in_id = -1  # INIT VAR
    if frm_idx not in roi_grp:
        roi_grp.append(frm_idx)
        roi_grp = sorted(roi_grp)
        in_id = roi_grp.index(frm_idx)
        if in_id < len(roi_data):
            for i in range(len(roi_data) - 1, in_id - 1, -1):
                roi_data[i+1] = copy.deepcopy(roi_data[i])
        roi_data[in_id] = {}
    return in_id


# Main process worker class  ----------------------------------------------------------------------------------------  #
class ProcWorker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(int)

    def run(self):
        global out_dir, vid_cap, brt, con, exp_typ, frm_dig, frm_num, frm_list, roi_id, roi_data,\
            txt_mark, txt_linc, txt_hbkg, txt_bkgc, txt_size, txt_xval, txt_yval

        # Make output directories and file names
        if exp_typ:
            vid_file = os.path.join(out_dir, "test_juv.avi")
            tgt_dir = mk_outdir(os.path.join(out_dir, "juv/"), "Invalid juvenile test animal scene output directory!")
            tgt_file = os.path.join(tgt_dir, "juv.frm")
            tgt_roi = os.path.join(tgt_dir, "juv.roi")
            juv_dir = mk_outdir(os.path.join(out_dir, "byj/"), "Invalid by juvenile animal scene output directory!")
            juv_file = os.path.join(juv_dir, "byj.frm")
            juv_roi = os.path.join(juv_dir, "byj.roi")
        else:
            vid_file = os.path.join(out_dir, "test_obj.avi")
            tgt_dir = mk_outdir(os.path.join(out_dir, "obj/"), "Invalid object test animal scene output directory!")
            tgt_file = os.path.join(tgt_dir, "obj.frm")
            tgt_roi = os.path.join(tgt_dir, "obj.roi")
        # Get basic parameters
        width = int(vid_cap.get(cv.CAP_PROP_FRAME_WIDTH))
        height = int(vid_cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        frm_size = (width, height)

        # Compute frame crop region
        roi_crop = {}  # INIT VAR
        for i in roi_data:
            tgt_l = width  # INIT/RESET VAR
            tgt_r = 0  # INIT/RESET VAR
            tgt_t = height  # INIT/RESET VAR
            tgt_b = 0  # INIT/RESET VAR
            juv_l = width  # INIT/RESET VAR
            juv_r = 0  # INIT/RESET VAR
            juv_t = height  # INIT/RESET VAR
            juv_b = 0  # INIT/RESET VAR
            for k in roi_data[i]:
                if k.startswith('TGT'):
                    tgt_l = round(min(roi_data[i][k]['tl'][0] - 5, roi_data[i][k]['bl'][0] - 5, tgt_l))
                    tgt_r = round(max(roi_data[i][k]['tr'][0] + 5, roi_data[i][k]['br'][0] + 5, tgt_r))
                    tgt_t = round(min(roi_data[i][k]['tl'][1] - 5, roi_data[i][k]['tr'][1] - 5, tgt_t))
                    tgt_b = round(max(roi_data[i][k]['bl'][1] + 5, roi_data[i][k]['br'][1] + 5, tgt_b))
                if exp_typ and k.startswith('JUV'):
                    juv_l = round(min(roi_data[i][k]['tl'][0] - 50, roi_data[i][k]['bl'][0] - 50, juv_l))
                    juv_r = round(max(roi_data[i][k]['tr'][0] + 5, roi_data[i][k]['br'][0] + 5, juv_r))
                    juv_t = round(min(roi_data[i][k]['tl'][1] - 5, roi_data[i][k]['tr'][1] - 5, juv_t))
                    juv_b = round(max(roi_data[i][k]['bl'][1] + 5, roi_data[i][k]['br'][1] + 5, juv_b))
            if exp_typ:
                roi_crop[i] = {'TGT': [max(tgt_l, 0), min(tgt_r, width), max(tgt_t, 0), min(tgt_b, height)],
                               'JUV': [max(juv_l, 0), min(juv_r, width), max(juv_t, 0), min(juv_b, height)]}
            else:
                roi_crop[i] = {'TGT': [max(tgt_l, 0), min(tgt_r, width), max(tgt_t, 0), min(tgt_b, height)]}

        # Compute adjusted ROIs
        roi_adj = {}  # INIT VAR
        for i in roi_data:
            roi_adj[i] = {}
            # Get frame crop/resize information
            if exp_typ:
                resize_mat = {'TGT': np.array([256 / (roi_crop[i]['TGT'][1] - roi_crop[i]['TGT'][0]),
                                               256 / (roi_crop[i]['TGT'][3] - roi_crop[i]['TGT'][2])]),
                              'JUV': np.array([256 / (roi_crop[i]['JUV'][1] - roi_crop[i]['JUV'][0]),
                                               256 / (roi_crop[i]['JUV'][3] - roi_crop[i]['JUV'][2])])}
            else:
                resize_mat = {'TGT': np.array([256 / (roi_crop[i]['TGT'][1] - roi_crop[i]['TGT'][0]),
                                               256 / (roi_crop[i]['TGT'][3] - roi_crop[i]['TGT'][2])])}
            # Compute new ROIs
            for k in roi_data[i]:
                if k.startswith('TGT'):
                    roi_adj[i][k] = {}
                    for pos in roi_data[i][k]:
                        crop = np.array([roi_data[i][k][pos][0] - roi_crop[i]['TGT'][0],
                                         roi_data[i][k][pos][1] - roi_crop[i]['TGT'][2]])
                        new_pos = [pt.item() for pt in (resize_mat['TGT'] * crop)]
                        roi_adj[i][k][pos] = new_pos
                if exp_typ and k.startswith('JUV'):
                    roi_adj[i][k] = {}
                    for pos in roi_data[i][k]:
                        crop = np.array([roi_data[i][k][pos][0] - roi_crop[i]['JUV'][0],
                                         roi_data[i][k][pos][1] - roi_crop[i]['JUV'][2]])
                        new_pos = [pt.item() for pt in (resize_mat['JUV'] * crop)]
                        roi_adj[i][k][pos] = new_pos

        # Main process loop
        roi_id = -1  # Loop first call control
        count = 0  # INIT VAR
        tgt_feat = {}  # INIT VAR
        juv_feat = {}  # INIT VAR

        # Open files for writing
        vid_writer = cv.VideoWriter(vid_file, cv.VideoWriter_fourcc(*"FFV1"), vid_cap.get(cv.CAP_PROP_FPS), frm_size)
        tgt_hdf = h5.File(tgt_file, 'w')
        if exp_typ:
            juv_hdf = h5.File(juv_file, 'w')
        for i in range(len(frm_list)):
            # Get current ROI index
            data_flag = find_roi_id(i)

            # Process and save selected frames
            if frm_list[i]['keep'] == 1:
                img = get_frm(vid_cap, i)
                # Process and write frames
                img = brt_con(img, brt, con)
                if txt_mark:
                    img = draw_text(img, frm_dig % i, txt_xval, txt_yval, txt_size, txt_linc, txt_hbkg, txt_bkgc)
                vid_writer.write(img)
                # Process target animal region
                if data_flag:
                    tgt_feat[i] = {'C': copy.deepcopy(roi_adj[roi_id]['TGT_C']),
                                   'T': copy.deepcopy(roi_adj[roi_id]['TGT_T']),
                                   'B': copy.deepcopy(roi_adj[roi_id]['TGT_B']),
                                   'W': copy.deepcopy(roi_adj[roi_id]['TGT_W'])}
                else:
                    tgt_feat[i] = {'C': None, 'T': None, 'B': None, 'W': None}
                tgt = img[roi_crop[roi_id]['TGT'][2]:roi_crop[roi_id]['TGT'][3],
                          roi_crop[roi_id]['TGT'][0]:roi_crop[roi_id]['TGT'][1]]
                tgt = cv.resize(tgt, (256, 256), interpolation=cv.INTER_AREA)
                tgt = cv.cvtColor(tgt, cv.COLOR_BGR2GRAY)
                tgt_hdf.create_dataset(str(i), data=tgt, compression='gzip', compression_opts=9)
                # Process juvenile animal region
                if exp_typ:
                    if data_flag:
                        juv_feat[i] = {'C': copy.deepcopy(roi_adj[roi_id]['JUV_C']),
                                       'T': copy.deepcopy(roi_adj[roi_id]['JUV_T']),
                                       'B': copy.deepcopy(roi_adj[roi_id]['JUV_B'])}
                    else:
                        juv_feat[i] = {'C': None, 'T': None, 'B': None}
                    juv = img[roi_crop[roi_id]['JUV'][2]:roi_crop[roi_id]['JUV'][3],
                              roi_crop[roi_id]['JUV'][0]:roi_crop[roi_id]['JUV'][1]]
                    juv = cv.resize(juv, (256, 256), interpolation=cv.INTER_AREA)
                    juv = cv.cvtColor(juv, cv.COLOR_BGR2GRAY)
                    juv_hdf.create_dataset(str(i), data=juv, compression='gzip', compression_opts=9)
                # Progress report, set here as this is the most cost section
                count += 1
                self.progress.emit(count)

        # Write process details to file
        tgt_hdf.close()
        with open(tgt_roi, 'w', encoding='utf-8') as tgt_file:
            json.dump(tgt_feat, tgt_file, ensure_ascii=False)
        if exp_typ:
            juv_hdf.close()
            with open(juv_roi, 'w', encoding='utf-8') as juv_file:
                json.dump(juv_feat, juv_file, ensure_ascii=False)

        self.finished.emit()


# [ControlViewer] MEGIT Overview-Video main controller  -------------------------------------------------------------  #
class ControlViewer(QtWidgets.QMainWindow, Ui_ControlViewer):
    tot_frm = 1  # Total frames to label
    curr_frm = 0  # Frame currently operating
    curr_cut = 'INIT'  # Current frame removing status
    curr_row = 0  # Current row in removed frames list
    curr_a = 0  # Current removing FROM value
    prog_steps = 0  # Total step for the main function

    def __init__(self, parent=None):
        super(ControlViewer, self).__init__(parent)
        self.setupUi(self)
        self.statusBar.showMessage("Ready!")
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        # Slider value control
        self.frameSlider.valueChanged['int'].connect(self.__frame_slider_control)
        # Brightness and contrast control
        self.brtSlider.valueChanged['int'].connect(self.__adj_frm_brtcon)
        self.conSlider.valueChanged['int'].connect(self.__adj_frm_brtcon)
        # Frame selection controls
        self.totfrmBox.valueChanged.connect(self.__frame_number_check)
        self.cutaButton.clicked.connect(self.__cut_from)
        self.cutbButton.clicked.connect(self.__cut_to)
        self.frmoutTable.cellChanged.connect(self.__table_input_validation)
        # Frame tagging control
        self.mrkMode.currentIndexChanged.connect(self.__set_text_color)
        self.sizeValue.valueChanged.connect(self.__set_text_size)
        self.xValue.valueChanged.connect(self.__set_text_loc)
        self.yValue.valueChanged.connect(self.__set_text_loc)
        self.mrkCheck.clicked.connect(self.__set_frm_text)
        # Experiment type control
        self.objButton.clicked.connect(self.__exp_mode_selection)
        self.juvButton.clicked.connect(self.__exp_mode_selection)
        # Marking mode selection control
        self.tgtBox.currentIndexChanged.connect(self.__tgt_mark_mode_change)
        self.juvBox.currentIndexChanged.connect(self.__juv_mark_mode_change)
        self.hidButton.clicked.connect(self.__mrk_disp_ctrl)
        self.updButton.clicked.connect(self.__mrk_grp_update)
        # Signal receiver
        com_sig.frm_info_sig.connect(self.__status_report)
        com_sig.mkr_info_sig.connect(self.__status_report)
        com_sig.frm_ctrl_sig.connect(self.__frame_signal)
        # Main buttons
        self.startButton.clicked.connect(self.__start_func)
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

    # Custom signals between different windows
    def keyPressEvent(self, event):
        if type(event) == QtGui.QKeyEvent:
            if event.key() == QtCore.Qt.Key_A or event.key() == QtCore.Qt.Key_Left:
                com_sig.frm_ctrl_sig.emit(-1)
            elif event.key() == QtCore.Qt.Key_D or event.key() == QtCore.Qt.Key_Right:
                com_sig.frm_ctrl_sig.emit(1)
            else:
                QtWidgets.QMainWindow.keyPressEvent(self, event)
        else:
            QtWidgets.QMainWindow.keyPressEvent(self, event)

    # Window status synchronization signal
    def changeEvent(self, event):
        com_sig.win_stat_sig.emit(self.windowState())
        QtWidgets.QMainWindow.changeEvent(self, event)

    def __status_report(self):
        self.statusBar.showMessage(mkr_msg + frm_msg)

    def __frame_slider_control(self):
        global frm_msg, roi_id
        self.curr_frm = self.frameSlider.value()
        frm_msg = " | Current frame index: %d" % self.curr_frm
        com_sig.frm_info_sig.emit(self.curr_frm, frm_msg)
        # Check if ROI ID changed
        if find_roi_id(self.curr_frm):
            com_sig.mkr_ctrl_sig.emit()

    def __frame_signal(self, val):
        if val == -1:
            self.sliderValue.stepDown()
        elif val == 1:
            self.sliderValue.stepUp()
        else:
            pass

    def __adj_frm_brtcon(self):
        global brt, con
        brt = self.brtSlider.value()
        con = self.conSlider.value()
        com_sig.frm_info_sig.emit(self.curr_frm, frm_msg)

    def __frame_number_check(self):
        global frm_num, frm_esc
        frm_num = self.totfrmBox.value()
        frm_avbl = self.tot_frm - sum([i[1] - i[0] + 1 for i in frm_esc])
        if frm_avbl < frm_num:
            self.startButton.setEnabled(False)  # Disable START until requirements meet
            QtWidgets.QMessageBox.critical(self, "Warning",
                                           "Insufficient remaining frames!\nPlease verify frame settings.")
            return False
        else:
            if self.curr_cut != 'ASET':  # Check cut list status
                self.startButton.setEnabled(True)
            update_frame_selection()  # Update frames
            return True

    def __cut_from(self):
        global frm_esc
        self.frmoutTable.blockSignals(True)
        item = QtWidgets.QTableWidgetItem(str(self.curr_frm))
        if self.curr_cut == 'INIT':
            self.curr_a = self.curr_frm  # Save current FROM value
            self.frmoutTable.insertRow(0)  # Add initial ROW
            self.frmoutTable.setItem(0, 0, item)
            self.curr_cut = 'ASET'
            self.startButton.setEnabled(False)  # Disable START until B set
        elif self.curr_cut == 'ASET':
            if any(lower <= self.curr_frm <= upper for [lower, upper] in frm_esc):
                QtWidgets.QMessageBox.critical(self, "Warning", "New value should not be within any previous ranges!")
            else:
                self.curr_a = self.curr_frm  # Save current FROM value
                self.frmoutTable.setItem(self.curr_row, 0, item)  # Update current A value
                self.startButton.setEnabled(False)  # Disable START until B set
        elif self.curr_cut == 'BSET':
            if any(lower <= self.curr_frm <= upper for [lower, upper] in frm_esc):
                QtWidgets.QMessageBox.critical(self, "Warning", "New value should not be within any previous ranges!")
            else:
                self.curr_a = self.curr_frm  # Save current FROM value
                self.frmoutTable.insertRow(self.curr_row)  # Add ROW for a new pair
                self.frmoutTable.setItem(self.curr_row, 0, item)
                self.curr_cut = 'ASET'
                self.startButton.setEnabled(False)  # Disable START until B set
        self.frmoutTable.blockSignals(False)

    def __cut_to(self):
        global frm_esc
        self.frmoutTable.blockSignals(True)
        item = QtWidgets.QTableWidgetItem(str(self.curr_frm))
        if self.curr_cut == 'INIT':
            frm_esc.append([0, self.curr_frm])  # Set global variable
            if self.__frame_number_check():
                self.frmoutTable.insertRow(0)  # Add initial ROW
                self.frmoutTable.setItem(0, 0, QtWidgets.QTableWidgetItem('0'))  # Auto set cut FROM first frame
                self.frmoutTable.setItem(0, 1, item)
                self.curr_row += 1  # Increase ROW when an A-B pair is done
                self.curr_cut = 'BSET'
                update_frame_selection()  # Update frames
                self.startButton.setEnabled(True)  # Re-enable START
            else:
                frm_esc.pop(-1)
        elif self.curr_cut == 'ASET':
            if self.curr_frm < self.curr_a:
                QtWidgets.QMessageBox.critical(self, "Warning", "New TO value should not be less than current FROM!")
            elif any(lower <= self.curr_frm <= upper for [lower, upper] in frm_esc):
                QtWidgets.QMessageBox.critical(self, "Warning", "New value should not be within any previous ranges!")
            else:
                frm_esc.append([self.curr_a, self.curr_frm])  # Set global variable
                if self.__frame_number_check():
                    self.frmoutTable.setItem(self.curr_row, 1, item)
                    self.curr_row += 1  # Increase ROW when an A-B list is done
                    self.curr_cut = 'BSET'
                    update_frame_selection()  # Update frames
                    self.startButton.setEnabled(True)  # Re-enable START
                else:
                    frm_esc.pop(-1)
        elif self.curr_cut == 'BSET':
            if self.curr_frm < self.curr_a:
                QtWidgets.QMessageBox.critical(self, "Warning", "New TO value should not be less than current FROM!")
            elif any(lower <= self.curr_frm <= upper for [lower, upper] in frm_esc):
                QtWidgets.QMessageBox.critical(self, "Warning", "New value should not be within any previous ranges!")
            else:
                frm_esc[-1] = [self.curr_a, self.curr_frm]  # Set global variable
                if self.__frame_number_check():
                    self.frmoutTable.setItem(self.curr_row - 1, 1, item)  # Update current B value
                    update_frame_selection()  # Update frames
                    self.startButton.setEnabled(True)  # Re-enable START
                else:
                    frm_esc.pop(-1)
        self.frmoutTable.blockSignals(False)
        # Update frame scene
        com_sig.frm_info_sig.emit(self.curr_frm, frm_msg)

    def __table_input_validation(self, row, col):
        global frm_esc
        self.frmoutTable.blockSignals(True)
        # Check current existing values
        if row < len(frm_esc):
            temp_val = frm_esc[row][col]
        else:
            if col == 0:
                temp_val = self.curr_a
            else:
                temp_val = None
        # Check value data format
        val = self.frmoutTable.item(row, col).text()
        try:
            data = int(val)
        except ValueError:
            if temp_val is None:
                self.frmoutTable.setItem(row, col, None)
            else:
                self.frmoutTable.setItem(row, col, QtWidgets.QTableWidgetItem(str(temp_val)))
            QtWidgets.QMessageBox.critical(self, "Error", "Must use integers for frame index!")
        else:
            # Get required index
            if col == 0:
                prev_row = row - 1
                prev_col = 1
                next_row = row
                next_col = 1
            else:
                prev_row = row
                prev_col = 0
                next_row = row + 1
                next_col = 0
            # Handel with previous value
            if self.frmoutTable.item(prev_row, prev_col) is None:
                if data < 0:
                    QtWidgets.QMessageBox.critical(self, "Warning",
                                                   "New FROM value should be greater than zero!")
                    data = temp_val
            else:
                prev_val = int(self.frmoutTable.item(prev_row, prev_col).text())
                if col == 0:  # Data at FROM
                    if data <= prev_val:
                        QtWidgets.QMessageBox.critical(self, "Warning",
                                                       "New FROM value should be greater than previous TO!")
                        data = temp_val
                else:  # Data at TO
                    if data < prev_val:
                        QtWidgets.QMessageBox.critical(self, "Warning",
                                                       "New TO value should not be less than current FROM!")
                        data = temp_val
            # Handel with next value
            if self.frmoutTable.item(next_row, next_col) is None:
                if data >= self.tot_frm:
                    QtWidgets.QMessageBox.critical(self, "Warning",
                                                   "New TO value should be less than total frames!")
                    data = temp_val
            else:
                next_val = int(self.frmoutTable.item(next_row, next_col).text())
                if col == 0:  # Data at FROM
                    if data > next_val:
                        QtWidgets.QMessageBox.critical(self, "Warning",
                                                       "New FROM value should not be greater than current TO!")
                        data = temp_val
                else:  # Data at TO
                    if data >= next_val:
                        QtWidgets.QMessageBox.critical(self, "Warning",
                                                       "New TO value should be less than next FROM!")
                        data = temp_val
            # Set new data
            if data is None:
                self.frmoutTable.setItem(row, col, None)
            else:
                self.frmoutTable.setItem(row, col, QtWidgets.QTableWidgetItem(str(data)))
                # Transfer new data to global/local variables
                if temp_val is None:  # Assigned to new B value
                    frm_esc.append([self.curr_a, data])
                    self.curr_row += 1  # Increase ROW when an A-B list is done
                    self.curr_cut = 'BSET'
                    update_frame_selection()  # Update frames
                    self.startButton.setEnabled(True)  # Re-enable START
                else:
                    if row < len(frm_esc):  # Update existing A-B pair
                        frm_esc[row][col] = data
                        update_frame_selection()  # Update frames
                    else:  # Update new A value
                        self.curr_a = data
        self.frmoutTable.blockSignals(False)
        # Update frame scene
        com_sig.frm_info_sig.emit(self.curr_frm, frm_msg)

    def __set_text_color(self):
        global txt_linc, txt_bkgc, txt_hbkg
        if self.mrkMode.currentIndex() == 0:
            txt_linc = (0, 0, 0)
            txt_bkgc = None
            txt_hbkg = False
        elif self.mrkMode.currentIndex() == 1:
            txt_linc = (255, 255, 255)
            txt_bkgc = None
            txt_hbkg = False
        elif self.mrkMode.currentIndex() == 2:
            txt_linc = (0, 0, 0)
            txt_bkgc = (255, 255, 255)
            txt_hbkg = True
        else:
            txt_linc = (255, 255, 255)
            txt_bkgc = (0, 0, 0)
            txt_hbkg = True
        # Update frame scene
        com_sig.frm_info_sig.emit(self.curr_frm, frm_msg)

    def __set_text_size(self):
        global txt_size
        txt_size = self.sizeValue.value()
        # Update frame scene
        com_sig.frm_info_sig.emit(self.curr_frm, frm_msg)

    def __set_text_loc(self):
        global txt_xval, txt_yval
        txt_xval = self.xValue.value()
        txt_yval = self.yValue.value()
        # Update frame scene
        com_sig.frm_info_sig.emit(self.curr_frm, frm_msg)

    def __set_frm_text(self):
        global txt_mark
        txt_mark = self.mrkCheck.isChecked()
        self.__set_text_color()
        self.__set_text_size()
        self.__set_text_loc()
        # Update frame scene
        com_sig.frm_info_sig.emit(self.curr_frm, frm_msg)

    def __exp_mode_selection(self):
        global exp_typ
        exp_typ = self.juvButton.isChecked()
        com_sig.mkr_disp_sig.emit()

    def __tgt_mark_mode_change(self):
        global mk_mode, mkr_msg
        # Set current target animal labelling method
        if self.tgtBox.currentIndex() == 1:
            mk_mode = 'TGT_C'
            mkr_msg = "Current Marker: Test Animal - Gap"
            com_sig.mkr_info_sig.emit(0, 0, mk_mode)  # Disable juvenile animal labelling
            self.juvBox.setCurrentIndex(0)
        elif self.tgtBox.currentIndex() == 2:
            mk_mode = 'TGT_T'
            mkr_msg = "Current Marker: Test Animal - Top"
            com_sig.mkr_info_sig.emit(0, 1, mk_mode)
            self.juvBox.setCurrentIndex(0)  # Disable juvenile animal labelling
        elif self.tgtBox.currentIndex() == 3:
            mk_mode = 'TGT_B'
            mkr_msg = "Current Marker: Test Animal - Bottom"
            com_sig.mkr_info_sig.emit(0, 2, mk_mode)
            self.juvBox.setCurrentIndex(0)  # Disable juvenile animal labelling
        elif self.tgtBox.currentIndex() == 4:
            mk_mode = 'TGT_W'
            mkr_msg = "Current Marker: Test Animal - Wall"
            com_sig.mkr_info_sig.emit(0, 3, mk_mode)
            self.juvBox.setCurrentIndex(0)  # Disable juvenile animal labelling
        else:
            if self.juvBox.currentIndex() == 0:  # Set signal to 'NONE' if both TGT/JUV disabled
                mk_mode = 'NONE'
                mkr_msg = "No Marker Selected"
                com_sig.mkr_info_sig.emit(-1, -1, mk_mode)

    def __juv_mark_mode_change(self):
        global mk_mode, mkr_msg
        # Set current juvenile animal labelling method
        if self.juvBox.currentIndex() == 1:
            mk_mode = 'JUV_C'
            mkr_msg = "Current Marker: Juvenile Animal - Gap"
            com_sig.mkr_info_sig.emit(1, 0, mk_mode)
            self.tgtBox.setCurrentIndex(0)  # Disable target animal labelling
        elif self.juvBox.currentIndex() == 2:
            mk_mode = 'JUV_T'
            mkr_msg = "Current Marker: Juvenile Animal - Top"
            com_sig.mkr_info_sig.emit(1, 1, mk_mode)
            self.tgtBox.setCurrentIndex(0)  # Disable target animal labelling
        elif self.juvBox.currentIndex() == 3:
            mk_mode = 'JUV_B'
            mkr_msg = "Current Marker: Juvenile Animal - Bottom"
            com_sig.mkr_info_sig.emit(1, 2, mk_mode)
            self.tgtBox.setCurrentIndex(0)  # Disable target animal labelling
        else:
            if self.tgtBox.currentIndex() == 0:  # Set signal to 'NONE' if both TGT/JUV disabled
                mk_mode = 'NONE'
                mkr_msg = "No Marker Selected"
                com_sig.mkr_info_sig.emit(-1, -1, mk_mode)

    def __mrk_disp_ctrl(self):
        global mkr_vis
        mkr_vis = not mkr_vis
        if mkr_vis:
            self.hidButton.setText("Hide")
        else:
            self.hidButton.setText("Show")
        com_sig.mkr_disp_sig.emit()

    def __mrk_grp_update(self):
        global mkr_vis, roi_id, roi_grp
        if not mkr_vis:
            self.__mrk_disp_ctrl()
        com_sig.mkr_updt_sig.emit(update_roi_group(self.curr_frm))
        find_roi_id(self.curr_frm)
        com_sig.mkr_ctrl_sig.emit()

    # Progress display
    def __prog_disp(self, val):
        percent = int(val / self.prog_steps * 100)
        self.progressBar.setValue(percent)

    # Main process function
    def __main_proc_task(self):
        self.progressBar.setValue(0)
        # Assign thread and worker
        self.thread = QtCore.QThread()
        self.worker = ProcWorker()
        self.worker.moveToThread(self.thread)
        # Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.__prog_disp)
        # Start the thread
        self.thread.start()
        # Get switchable controls status
        mk_flag = self.mrkMode.isEnabled()
        sz_flag = self.sizeValue.isEnabled()
        x_flag = self.xValue.isEnabled()
        y_flag = self.yValue.isEnabled()
        jv_flag = self.juvBox.isEnabled()
        # Disable Controls
        self.frameSlider.setEnabled(False)
        self.sliderValue.setEnabled(False)
        self.brtSlider.setEnabled(False)
        self.brtValue.setEnabled(False)
        self.conSlider.setEnabled(False)
        self.conValue.setEnabled(False)
        self.totfrmBox.setEnabled(False)
        self.cutaButton.setEnabled(False)
        self.cutbButton.setEnabled(False)
        self.mrkCheck.setEnabled(False)
        self.mrkMode.setEnabled(False)
        self.sizeValue.setEnabled(False)
        self.xValue.setEnabled(False)
        self.yValue.setEnabled(False)
        self.objButton.setEnabled(False)
        self.juvButton.setEnabled(False)
        self.tgtBox.setEnabled(False)
        self.juvBox.setEnabled(False)
        self.hidButton.setEnabled(False)
        self.updButton.setEnabled(False)
        self.prevButton.setEnabled(False)
        self.nextButton.setEnabled(False)
        self.startButton.setEnabled(False)
        # Final resets
        self.thread.finished.connect(lambda: self.frameSlider.setEnabled(True))
        self.thread.finished.connect(lambda: self.sliderValue.setEnabled(True))
        self.thread.finished.connect(lambda: self.brtSlider.setEnabled(True))
        self.thread.finished.connect(lambda: self.brtValue.setEnabled(True))
        self.thread.finished.connect(lambda: self.conSlider.setEnabled(True))
        self.thread.finished.connect(lambda: self.conValue.setEnabled(True))
        self.thread.finished.connect(lambda: self.totfrmBox.setEnabled(True))
        self.thread.finished.connect(lambda: self.cutaButton.setEnabled(True))
        self.thread.finished.connect(lambda: self.cutbButton.setEnabled(True))
        self.thread.finished.connect(lambda: self.mrkCheck.setEnabled(True))
        self.thread.finished.connect(lambda: self.mrkMode.setEnabled(mk_flag))
        self.thread.finished.connect(lambda: self.sizeValue.setEnabled(sz_flag))
        self.thread.finished.connect(lambda: self.xValue.setEnabled(x_flag))
        self.thread.finished.connect(lambda: self.yValue.setEnabled(y_flag))
        self.thread.finished.connect(lambda: self.objButton.setEnabled(True))
        self.thread.finished.connect(lambda: self.juvButton.setEnabled(True))
        self.thread.finished.connect(lambda: self.tgtBox.setEnabled(True))
        self.thread.finished.connect(lambda: self.juvBox.setEnabled(jv_flag))
        self.thread.finished.connect(lambda: self.hidButton.setEnabled(True))
        self.thread.finished.connect(lambda: self.updButton.setEnabled(True))
        self.thread.finished.connect(lambda: self.prevButton.setEnabled(True))
        self.thread.finished.connect(lambda: self.nextButton.setEnabled(True))
        self.thread.finished.connect(lambda: self.startButton.setEnabled(True))

    # Main process function
    def __start_func(self):
        global frm_num, exp_typ, roi_grp, roi_data
        # Checking missing ROIs
        err_flag = False
        if len(roi_data) == 0:
            err_flag = True
            if exp_typ:
                err_msg = "Please define ROIs for both Target and Juvenile animals!"
            else:
                err_msg = "Please define ROIs for Target animal!"
        else:
            err_msg = "Missing following ROIs:\n"
            err_dic = {'JUV_B': "Juvenile - Bottom", 'JUV_C': "Juvenile - Gap", 'JUV_T': "Juvenile - Top",
                       'TGT_B': "Test Animal - Bottom", 'TGT_C': "Test Animal - Gap", 'TGT_T': "Test Animal - Top",
                       'TGT_W': "Test Animal - Wall"}
            for i in roi_data:
                if exp_typ:
                    for k in ['TGT_C', 'TGT_T', 'TGT_B', 'JUV_C', 'JUV_T', 'JUV_B']:
                        if k not in roi_data[i]:
                            err_flag = True
                            err_msg += "  Frame - %d : %s\n" % (roi_grp[i], err_dic[k])
                else:
                    for k in ['TGT_C', 'TGT_T', 'TGT_B', 'TGT_W']:
                        if k not in roi_data[i]:
                            err_flag = True
                            err_msg += "  Frame - %d : %s\n" % (roi_grp[i], err_dic[k])
        # Send process signal
        if err_flag:
            QtWidgets.QMessageBox.critical(self, "Error", err_msg)
            return
        else:
            # Set progress bar
            self.prog_steps = frm_num
            # Execute main task
            self.__main_proc_task()


# [FrameViewer] MEGIT Overview-Video frame display and region marker ------------------------------------------------  #
# [FrameViewer] Visualization item definition
class DisplayRect(QtWidgets.QGraphicsRectItem):
    def __init__(self, x, y, w, h, color, parent=None):
        """ Custom label rectangle item.
        Args:
            x (int or float): Label X coordinate.
            y (int or float): Label Y coordinate.
            w (int or float): Label width.
            h (int or float): Label height.
            color (tuple[int, int, int]): Label RGB color code.
            parent (None): None.
        """
        super(DisplayRect, self).__init__(parent)
        # Set item properties
        self.setData(0, -255)
        self.setData(1, None)
        # Set frame of item
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor(color[0], color[1], color[2], 125))
        self.setPen(pen)
        # Set item geometry
        self.setRect(x, y, w, h)
        self.setZValue(2)  # Layer 2 for labels

    # Define a UserType for label items
    def type(self):
        return QtWidgets.QGraphicsRectItem.UserType + 1


# [FrameViewer] ROI marking item definition
class RegionRect(QtWidgets.QGraphicsRectItem):
    # Set graphical limitations
    minWidth = 20
    minHeight = 20
    maxAngle = 45
    # Define ROI colour variables
    colorEdge = QtGui.QColor(0, 0, 0, 255)
    colorFace = QtGui.QColor(0, 0, 0, 125)

    # Mouse control flag
    hoverFlag = False
    angleHold = 0

    # Define handle features
    handleSize = 8.0
    handleSpace = -4.0
    # Define handle IDs
    handleTopLeft = 1
    handleTopMiddle = 2
    handleTopRight = 3
    handleMiddleLeft = 4
    handleMiddleRight = 5
    handleBottomLeft = 6
    handleBottomMiddle = 7
    handleBottomRight = 8
    # Define handle cursors
    handleCursors = {
        handleTopLeft: QtCore.Qt.CrossCursor,
        handleTopMiddle: QtCore.Qt.SizeVerCursor,
        handleTopRight: QtCore.Qt.CrossCursor,
        handleMiddleLeft: QtCore.Qt.SizeHorCursor,
        handleMiddleRight: QtCore.Qt.SizeHorCursor,
        handleBottomLeft: QtCore.Qt.CrossCursor,
        handleBottomMiddle: QtCore.Qt.SizeVerCursor,
        handleBottomRight: QtCore.Qt.CrossCursor,
    }

    def __init__(self, x, y, w, h, lid, ltg, color, parent=None):
        """ Custom label rectangle item.
        Args:
            x (int or float): Label X coordinate.
            y (int or float): Label Y coordinate.
            w (int or float): Label width.
            h (int or float): Label height.
            lid (int): Label sequential ID.
            ltg (str): Label name.
            color (tuple[int, int, int]): Label RGB color code.
            parent (None): None.
        """
        super(RegionRect, self).__init__(parent)
        global roi_data
        # Set item properties
        self.setData(0, lid)
        self.setData(1, ltg)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        # Set item graphical features
        self.colorEdge = QtGui.QColor(color[0], color[1], color[2], 255)
        self.colorFace = QtGui.QColor(color[0], color[1], color[2], 125)
        self.setRect(x, y, w, h)
        self.setZValue(16)  # Layer 16 for labels
        # Set geometry controls
        self.handles = {}
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressRect = None
        self.setAcceptHoverEvents(True)
        self.updateHandlesPos()
        # Set global variable
        if lid not in roi_data:
            roi_data[lid] = {}
        roi_data[lid][ltg] = {
            'tl': (self.mapToScene(self.rect().topLeft()).x(),
                   self.mapToScene(self.rect().topLeft()).y()),
            'tr': (self.mapToScene(self.rect().topRight()).x(),
                   self.mapToScene(self.rect().topRight()).y()),
            'bl': (self.mapToScene(self.rect().bottomLeft()).x(),
                   self.mapToScene(self.rect().bottomLeft()).y()),
            'br': (self.mapToScene(self.rect().bottomRight()).x(),
                   self.mapToScene(self.rect().bottomRight()).y())}

    # Define a UserType for label items
    def type(self):
        return QtWidgets.QGraphicsRectItem.UserType + 2

    def handleAt(self, point):
        """
        Returns the resize handle below the given point.
        """
        for k, v, in self.handles.items():
            if v.contains(point):
                return k
        return None

    def hoverMoveEvent(self, hoverEvent):
        self.hoverFlag = True
        handle = self.handleAt(hoverEvent.pos())
        cursor = QtCore.Qt.ArrowCursor if handle is None else self.handleCursors[handle]
        self.setCursor(cursor)
        super().hoverMoveEvent(hoverEvent)

    def hoverLeaveEvent(self, hoverEvent):
        self.hoverFlag = False
        self.setCursor(QtCore.Qt.ArrowCursor)
        super().hoverLeaveEvent(hoverEvent)

    def mousePressEvent(self, mouseEvent):
        self.handleSelected = self.handleAt(mouseEvent.pos())
        if self.handleSelected:
            self.mousePressPos = mouseEvent.pos()
            self.mousePressRect = self.boundingRect()
        super().mousePressEvent(mouseEvent)

    def mouseMoveEvent(self, mouseEvent):
        if self.handleSelected is not None:
            self.interactiveTransform(mouseEvent.pos())
        else:
            super().mouseMoveEvent(mouseEvent)

    def mouseReleaseEvent(self, mouseEvent):
        super().mouseReleaseEvent(mouseEvent)
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressRect = None
        self.update()

    def boundingRect(self):
        o = self.handleSize + self.handleSpace
        return self.rect().adjusted(-o, -o, o, o)

    def updateHandlesPos(self):
        """
        Update current resize handles according to the shape size and position.
        """
        s = self.handleSize
        b = self.boundingRect()
        self.handles[self.handleTopLeft] = QtCore.QRectF(b.left(), b.top(), s, s)
        self.handles[self.handleTopMiddle] = QtCore.QRectF(b.center().x() - s / 2, b.top(), s * 0.8, s * 0.8)
        self.handles[self.handleTopRight] = QtCore.QRectF(b.right() - s, b.top(), s, s)
        self.handles[self.handleMiddleLeft] = QtCore.QRectF(b.left(), b.center().y() - s / 2, s * 0.8, s * 0.8)
        self.handles[self.handleMiddleRight] = QtCore.QRectF(b.right() - s, b.center().y() - s / 2, s * 0.8, s * 0.8)
        self.handles[self.handleBottomLeft] = QtCore.QRectF(b.left(), b.bottom() - s, s, s)
        self.handles[self.handleBottomMiddle] = QtCore.QRectF(b.center().x() - s / 2, b.bottom() - s, s * 0.8, s * 0.8)
        self.handles[self.handleBottomRight] = QtCore.QRectF(b.right() - s, b.bottom() - s, s, s)

    def interactiveTransform(self, mousePos):
        """
        Perform shape interactive transformation to ROI.
        """
        global roi_data
        # Get basic info
        offset = self.handleSize + self.handleSpace
        boundingRect = self.boundingRect()
        rect = self.rect()
        # Process transformation
        self.prepareGeometryChange()
        if self.handleSelected == self.handleMiddleLeft:
            fromX = self.mousePressRect.left()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            # Limit ROI width minimum
            if boundingRect.right() - toX < self.minWidth:
                toX = boundingRect.right() - self.minWidth
            # Set resize
            boundingRect.setLeft(toX)
            rect.setLeft(boundingRect.left() + offset)
            self.setRect(rect)
        elif self.handleSelected == self.handleMiddleRight:
            fromX = self.mousePressRect.right()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            # Limit ROI width minimum
            if toX - boundingRect.left() < self.minWidth:
                toX = boundingRect.left() + self.minWidth
            # Set resize
            boundingRect.setRight(toX)
            rect.setRight(boundingRect.right() - offset)
            self.setRect(rect)
        elif self.handleSelected == self.handleTopMiddle:
            fromY = self.mousePressRect.top()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            # Limit ROI height minimum
            if boundingRect.bottom() - toY < self.minHeight:
                toY = boundingRect.bottom() - self.minHeight
            # Set resize
            boundingRect.setTop(toY)
            rect.setTop(boundingRect.top() + offset)
            self.setRect(rect)
        elif self.handleSelected == self.handleBottomMiddle:
            fromY = self.mousePressRect.bottom()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            # Limit ROI height minimum
            if toY - boundingRect.top() < self.minHeight:
                toY = boundingRect.top() + self.minHeight
            # Set resize
            boundingRect.setBottom(toY)
            rect.setBottom(boundingRect.bottom() - offset)
            self.setRect(rect)
        else:
            self.setTransformOriginPoint(self.rect().center())
            if self.handleSelected == self.handleTopLeft:
                fromPos = self.rect().center() - self.rect().topLeft()
                toPos = self.mapToScene(self.rect().center()) - self.mapToScene(mousePos)
            elif self.handleSelected == self.handleTopRight:
                fromPos = self.rect().topRight() - self.rect().center()
                toPos = self.mapToScene(mousePos) - self.mapToScene(self.rect().center())
            elif self.handleSelected == self.handleBottomLeft:
                fromPos = self.rect().center() - self.rect().bottomLeft()
                toPos = self.mapToScene(self.rect().center()) - self.mapToScene(mousePos)
            elif self.handleSelected == self.handleBottomRight:
                fromPos = self.rect().bottomRight() - self.rect().center()
                toPos = self.mapToScene(mousePos) - self.mapToScene(self.rect().center())
            fromAngle = math.atan2(fromPos.y(), fromPos.x()) / math.pi * 180
            angle = math.atan2(toPos.y(), toPos.x()) / math.pi * 180 - fromAngle
            # Limit rotation range
            if angle < -self.maxAngle:
                if self.angleHold == 0:
                    angle = -self.maxAngle
                    self.angleHold = -self.maxAngle
                else:
                    angle = self.angleHold
            elif angle > self.maxAngle:
                if self.angleHold == 0:
                    angle = self.maxAngle
                    self.angleHold = self.maxAngle
                else:
                    angle = self.angleHold
            else:
                self.angleHold = 0
            # Set rotation
            self.setRotation(angle)
        # Update related features
        self.updateHandlesPos()
        roi_data[self.data(0)][self.data(1)] = {
            'tl': (self.mapToScene(self.rect().topLeft()).x(),
                   self.mapToScene(self.rect().topLeft()).y()),
            'tr': (self.mapToScene(self.rect().topRight()).x(),
                   self.mapToScene(self.rect().topRight()).y()),
            'bl': (self.mapToScene(self.rect().bottomLeft()).x(),
                   self.mapToScene(self.rect().bottomLeft()).y()),
            'br': (self.mapToScene(self.rect().bottomRight()).x(),
                   self.mapToScene(self.rect().bottomRight()).y())}

    def paint(self, painter, option, widget=None):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        # Draw main rectangle
        painter.setPen(QtGui.QPen(self.colorEdge, 2.0, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        painter.drawRect(self.rect())
        # Draw handles
        painter.setPen(QtGui.QPen(self.colorEdge, 1.0, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        painter.setBrush(QtGui.QBrush(self.colorFace))
        if self.hoverFlag or self.isSelected():
            for handle, rect in self.handles.items():
                if self.handleSelected is None or handle == self.handleSelected:
                    if handle in [1, 3, 6, 8]:
                        painter.drawEllipse(rect)
                    else:
                        painter.drawRect(rect)

    def itemChange(self, change, value):
        global roi_data
        # Generate a report when label item changed in position
        if change == QtWidgets.QGraphicsItem.ItemPositionHasChanged:
            roi_data[self.data(0)][self.data(1)] = {
                'tl': (self.mapToScene(self.rect().topLeft()).x(),
                       self.mapToScene(self.rect().topLeft()).y()),
                'tr': (self.mapToScene(self.rect().topRight()).x(),
                       self.mapToScene(self.rect().topRight()).y()),
                'bl': (self.mapToScene(self.rect().bottomLeft()).x(),
                       self.mapToScene(self.rect().bottomLeft()).y()),
                'br': (self.mapToScene(self.rect().bottomRight()).x(),
                       self.mapToScene(self.rect().bottomRight()).y())}
        # Default return
        return QtWidgets.QGraphicsRectItem.itemChange(self, change, value)


# [FrameViewer] Label scene definition
class LabelScene(QtWidgets.QGraphicsScene):
    tgt_cnt = 0
    curr_tid = 0
    # Mouse left key flag
    left_clicked = False

    def __init__(self, parent=None):
        super(LabelScene, self).__init__(parent)
        self.ini_loc = [0., 0.]
        self.disp_rect = DisplayRect(0, 0, 0, 0, (0, 0, 0))
        self.disp_rect_enable = False
        # Marker signal connection
        com_sig.mkr_disp_sig.connect(self.__roi_visible)
        com_sig.mkr_updt_sig.connect(self.__roi_grp_upd)
        com_sig.mkr_ctrl_sig.connect(self.__roi_grp_sel)

    def __coord_chk(self, event_pos_x, event_pos_y):
        # Checking for X positions
        left = max(min(self.ini_loc[0], event_pos_x), 0)
        right = min(max(self.ini_loc[0], event_pos_x), self.width())
        # Checking for Y positions
        top = max(min(self.ini_loc[1], event_pos_y), 0)
        bottom = min(max(self.ini_loc[1], event_pos_y), self.height())
        # Return rectangle coordinates
        return left, top, right - left, bottom - top

    def mousePressEvent(self, event):
        global mk_mode, color_palette, roi_id, roi_data
        # LEFT PRESS to update initial position
        if event.button() == QtCore.Qt.LeftButton:
            self.left_clicked = True
            self.ini_loc[0] = max(event.scenePos().x(), 0.)
            self.ini_loc[1] = max(event.scenePos().y(), 0.)
            # SHIFT MODIFIER to initiate rectangle display when adding new items
            if event.modifiers() == QtCore.Qt.ShiftModifier:
                if mk_mode != 'NONE':
                    self.disp_rect = DisplayRect(0, 0, 0, 0, color_palette[mk_mode])
            else:
                QtWidgets.QGraphicsScene.mousePressEvent(self, event)
        # RIGHT PRESS to delete all selected items
        elif event.button() == QtCore.Qt.RightButton:
            self.left_clicked = False
            for i in self.selectedItems():
                roi_data[roi_id].pop(i.data(1), None)
                self.removeItem(i)
        else:
            self.left_clicked = False
            QtWidgets.QGraphicsScene.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        global mk_mode
        # SHIFT MODIFIER to display rectangle when adding new items
        if event.modifiers() == QtCore.Qt.ShiftModifier:
            if mk_mode != 'NONE' and self.left_clicked:
                x, y, w, h = self.__coord_chk(event.scenePos().x(), event.scenePos().y())
                self.disp_rect.setRect(x, y, w, h)
                if not self.disp_rect_enable:
                    self.addItem(self.disp_rect)
                    self.disp_rect_enable = True
        else:
            QtWidgets.QGraphicsScene.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        global mk_mode, roi_id, color_palette, mkr_vis
        self.left_clicked = False
        # LEFT RELEASE + SHIFT MODIFIER to add new items
        if event.button() == QtCore.Qt.LeftButton:
            if event.modifiers() == QtCore.Qt.ShiftModifier:
                if mk_mode != 'NONE':
                    # Remove old ROI
                    for i in self.items():
                        if i.data(0) == roi_id and i.data(1) == mk_mode:
                            self.removeItem(i)
                            break
                    x, y, w, h = self.__coord_chk(event.scenePos().x(), event.scenePos().y())
                    item = RegionRect(x, y, w, h, roi_id, mk_mode, color_palette[mk_mode])
                    self.addItem(item)
                    item.setVisible(mkr_vis)  # Check ROI visibility setting
            else:
                QtWidgets.QGraphicsScene.mouseReleaseEvent(self, event)
        else:
            QtWidgets.QGraphicsScene.mouseReleaseEvent(self, event)
        # Remove display rectangle
        if self.disp_rect_enable:
            self.removeItem(self.disp_rect)
            self.disp_rect_enable = False

    def __roi_visible(self):
        global mkr_vis, exp_typ
        for i in self.items():
            if i.type() == QtWidgets.QGraphicsRectItem.UserType + 2:
                i.setVisible(mkr_vis)
                if i.data(1).startswith('JUV'):
                    i.setVisible(mkr_vis and exp_typ)

    def __roi_grp_upd(self, var):
        for i in self.items():
            if i.type() == QtWidgets.QGraphicsRectItem.UserType + 2:
                item_lid = i.data(0)
                if item_lid >= var:
                    i.setData(0, item_lid + 1)

    def __roi_grp_sel(self):
        global roi_id
        for i in self.items():
            if i.type() == QtWidgets.QGraphicsRectItem.UserType + 2:
                i.setVisible(i.data(0) == roi_id)


# [FrameViewer] Label window definition
class FrameViewer(QtWidgets.QMainWindow, Ui_FrameViewer):
    first_call = True

    def __init__(self, parent=None):
        super(FrameViewer, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.scene = LabelScene(self)
        com_sig.frm_info_sig.connect(self.__frame_loader)
        # Status signal receiver
        com_sig.win_stat_sig.connect(self.__set_win_stat)
        com_sig.frm_info_sig.connect(self.__status_report)
        com_sig.mkr_info_sig.connect(self.__status_report)

    # Custom signals between different windows
    def keyPressEvent(self, event):
        if type(event) == QtGui.QKeyEvent:
            if event.key() == QtCore.Qt.Key_A or event.key() == QtCore.Qt.Key_Left:
                com_sig.frm_ctrl_sig.emit(-1)
            elif event.key() == QtCore.Qt.Key_D or event.key() == QtCore.Qt.Key_Right:
                com_sig.frm_ctrl_sig.emit(1)
            else:
                QtWidgets.QMainWindow.keyPressEvent(self, event)
        else:
            QtWidgets.QMainWindow.keyPressEvent(self, event)

    # Synchronize window status
    def __set_win_stat(self, stat):
        self.setWindowState(stat)

    def __status_report(self):
        self.statusBar.showMessage(mkr_msg + frm_msg)

    def __frame_loader(self, val, _):
        global frm, frm_list, frm_dig, brt, con, txt_mark, txt_linc, txt_bkgc, txt_hbkg, txt_size, txt_xval, txt_yval
        if loaded:
            # Convert OpenCV np-array image to QImage
            frm = get_frm(vid_cap, val)
            frm = brt_con(frm, brt, con)
            if txt_mark:
                if frm_list[val]['keep'] == 1:
                    frm = draw_text(frm, frm_dig % val, txt_xval, txt_yval, txt_size, txt_linc, txt_hbkg, txt_bkgc)
                elif frm_list[val]['keep'] == 0:  # Mark extra frames
                    frm = draw_text(frm, frm_dig % val, txt_xval, txt_yval, txt_size, (255, 0, 0), txt_hbkg, txt_bkgc)
                else:  # Mark removed frames
                    frm = draw_text(frm, frm_dig % val, txt_xval, txt_yval, txt_size, (0, 0, 255), txt_hbkg, txt_bkgc)
            else:
                if frm_list[val]['keep'] == 0:  # Mark extra frames
                    frm = draw_text(frm, "X", 1, 1, 2, (255, 0, 0), True, (255, 255, 255))
                elif frm_list[val]['keep'] == -1:  # Mark removed frames
                    frm = draw_text(frm, "X", 1, 1, 2, (0, 0, 255), True, (255, 255, 255))
            lbl_img = QtGui.QImage(frm, frm.shape[1], frm.shape[0], frm.shape[1] * 3, QtGui.QImage.Format_RGB888)
            if self.first_call:
                # Setup QGraphicsScene
                self.scene.setSceneRect(0, 0, lbl_img.width(), lbl_img.height())
                # Setup QGraphicsView
                scroll_bar_size = self.frameDisplay.style().pixelMetric(QtWidgets.QStyle.PM_ScrollBarExtent)
                self.frameDisplay.setFixedSize(lbl_img.width() + scroll_bar_size, lbl_img.height() + scroll_bar_size)
                self.frameDisplay.setScene(self.scene)
                # Change flag
                self.first_call = False
            else:
                # Delete previous frame, avoid memory leak
                for i in self.scene.items():
                    if i.type() == 7:  # QGraphicsPixmapItem::Type = 7
                        self.scene.removeItem(i)
            # Add new frame, send to background
            self.scene.addPixmap(QtGui.QPixmap(lbl_img.rgbSwapped()))
            for i in self.scene.items():
                if i.type() == 7:  # QGraphicsPixmapItem::Type = 7
                    i.setZValue(-1)


# [MainLoader] MEGIT Overview-Video main loader  --------------------------------------------------------------------  #
class MainLoader(QtWidgets.QMainWindow, Ui_MainLoader):
    def __init__(self, parent=None):
        super(MainLoader, self).__init__(parent)
        self.setupUi(self)
        self.controlWindow = ControlViewer()
        self.frameWindow = FrameViewer(self)

        self.videoButton.clicked.connect(self.__video_selection)
        self.outputButton.clicked.connect(self.__output_selection)
        self.loadButton.clicked.connect(self.__loading_func)
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

    # File loading button functions
    def __video_selection(self):
        vid_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Video File",
                                                            filter="Videos (*.avi *.mp4 *.mov *.mpeg)")
        self.videoPath.setText(vid_name)

    def __output_selection(self):
        out_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Output Directory')
        self.outputPath.setText(out_path)

    # Main loading function
    def __loading_func(self):
        global vid_cap, out_dir, frm_num, frm_dig, frm_list, loaded
        # Verify GUI inputs
        flag = False
        err_msg = str()
        vid_path = self.videoPath.text()
        if not os.path.isfile(vid_path):
            flag = True
            err_msg += "Video file does not exist!\n"
        out_path = self.outputPath.text()
        if not os.path.isdir(out_path):
            flag = True
            err_msg += "Invalid output path!\n"
        if flag:
            QtWidgets.QMessageBox.critical(self, "Error", err_msg)
            return
        # File loading
        else:
            out_dir = out_path
            self.hide()
            # Load control window
            self.controlWindow.show()
            # Load frame viewer and video
            self.frameWindow.show()
            vid_cap = cv.VideoCapture(vid_path)
            # Send video frame information to controls
            self.controlWindow.tot_frm = int(vid_cap.get(cv.CAP_PROP_FRAME_COUNT))
            self.controlWindow.xValue.setMaximum(int(vid_cap.get(cv.CAP_PROP_FRAME_WIDTH)))
            self.controlWindow.yValue.setMaximum(int(vid_cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
            self.controlWindow.frameSlider.setMaximum(int(vid_cap.get(cv.CAP_PROP_FRAME_COUNT) - 1))
            self.controlWindow.sliderValue.setMaximum(int(vid_cap.get(cv.CAP_PROP_FRAME_COUNT) - 1))
            self.controlWindow.totfrmBox.setMaximum(int(vid_cap.get(cv.CAP_PROP_FRAME_COUNT)))
            # Initialize frame processing list
            for i in range(int(vid_cap.get(cv.CAP_PROP_FRAME_COUNT))):
                frm_feat = {'idx': i, 'keep': 1}
                frm_list.append(copy.deepcopy(frm_feat))
            # Set status, send signal
            loaded = True
            frm_num = self.controlWindow.totfrmBox.value()
            frm_dig = '%%0%dd' % int(math.log10(vid_cap.get(cv.CAP_PROP_FRAME_COUNT)) + 1)
            com_sig.frm_info_sig.emit(0, " | Current frame: 0 | Progress: 0 of %d 0.00%%)" % vid_cap.get(7))
