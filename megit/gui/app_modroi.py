import os
import copy
import json
import math
import cv2.cv2 as cv
from PyQt5 import QtCore, QtGui, QtWidgets
from megit.gui.dgn_modroi_ctrl import Ui_ControlViewer
from megit.gui.dgn_preproc_frmv import Ui_FrameViewer
from megit.gui.dgn_modroi_load import Ui_MainLoader

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


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
roi_frm = []  # Preprocessed ROI frames
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
roi_dir = str()  # Preprocessed ROI directory
frm_dig = '%05d'  # Length of frame digits
ani_typ = False  # Animal type: True = Juvenile, False = Test
roi_data = {}  # Process region of interest


# Read ROI information
def load_roi_prop(prop_file):
    global ani_typ, roi_data, roi_grp
    # Define ROI property type
    if os.path.basename(prop_file).startswith('juv'):
        prop_typ = 'JUV'
        ani_typ = True
    else:
        prop_typ = 'TGT'
        ani_typ = False
    # Read property file
    with open(prop_file, 'r') as infile:
        prop = json.load(infile)
    # Convert to GUI format
    i = 0  # INIT VAR
    for n in prop:
        if prop[n]['C'] is not None:
            if int(n) != 0:
                roi_grp.append(int(n))
            roi_data[i] = {}
            for k in prop[n]:
                pos_temp = {pt: [prop[n][k][pt][0] * 2, prop[n][k][pt][1] * 2] for pt in prop[n][k]}
                roi_data[i][prop_typ + '_' + k] = copy.deepcopy(pos_temp)
            i += 1
    return prop


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
        self.rangeGroup.buttonToggled.connect(self.__frame_slider_mode)
        self.frameSlider.valueChanged['int'].connect(self.__frame_slider_control)
        # Experiment type control
        self.tgtButton.clicked.connect(self.__exp_mode_selection)
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

    def __frame_slider_mode(self):
        global roi_frm, roi_grp
        if self.fullmodeButton.isChecked():
            self.frameSlider.setMaximum(len(roi_frm) - 1)
            self.sliderValue.setMaximum(len(roi_frm) - 1)
        if self.selcmodeButton.isChecked():
            self.frameSlider.setMaximum(len(roi_grp) - 1)
            self.sliderValue.setMaximum(len(roi_grp) - 1)

    def __frame_slider_control(self):
        global frm_msg, roi_grp, roi_id
        if self.fullmodeButton.isChecked():
            self.curr_frm = self.frameSlider.value()
        else:
            self.curr_frm = roi_grp[self.frameSlider.value()]
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

    def __exp_mode_selection(self):
        global ani_typ
        ani_typ = self.juvButton.isChecked()
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

    # Main process function
    def __start_func(self):
        global ani_typ, roi_dir, roi_frm, roi_grp, roi_id, roi_data
        # Checking missing ROIs
        err_flag = False
        if len(roi_data) == 0:
            err_flag = True
            err_msg = "Please define at least 1 group of ROIs!"
        else:
            err_msg = "Missing following ROIs:\n"
            err_dic = {'JUV_B': "Juvenile - Bottom", 'JUV_C': "Juvenile - Gap", 'JUV_T': "Juvenile - Top",
                       'TGT_B': "Test Animal - Bottom", 'TGT_C': "Test Animal - Gap", 'TGT_T': "Test Animal - Top",
                       'TGT_W': "Test Animal - Wall"}
            for i in roi_data:
                if ani_typ:
                    for k in ['JUV_C', 'JUV_T', 'JUV_B']:
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
        # Process
        prop_name = "juv_prop.json" if ani_typ else "tst_prop.json"
        prop_feat = {}  # INIT VAR
        # Arrange ROI data
        roi_id = -1  # Loop first call control
        for i in range(len(roi_frm)):
            if find_roi_id(i):
                if ani_typ:
                    prop_feat[i] = {'C': copy.deepcopy(roi_data[roi_id]['JUV_C']),
                                    'T': copy.deepcopy(roi_data[roi_id]['JUV_T']),
                                    'B': copy.deepcopy(roi_data[roi_id]['JUV_B'])}
                else:
                    prop_feat[i] = {'C': copy.deepcopy(roi_data[roi_id]['TGT_C']),
                                    'T': copy.deepcopy(roi_data[roi_id]['TGT_T']),
                                    'B': copy.deepcopy(roi_data[roi_id]['TGT_B']),
                                    'W': copy.deepcopy(roi_data[roi_id]['TGT_W'])}
            else:
                if ani_typ:
                    prop_feat[i] = {'C': None, 'T': None, 'B': None}
                else:
                    prop_feat[i] = {'C': None, 'T': None, 'B': None, 'W': None}
        # Write ROI file
        with open(os.path.join(roi_dir, prop_name), 'w', encoding='utf-8') as prop_file:
            json.dump(prop_feat, prop_file, ensure_ascii=False)
        self.statusBar.showMessage("ROIs updated to file")


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
            'tl': (self.mapToScene(self.rect().topLeft()).x() / 2,
                   self.mapToScene(self.rect().topLeft()).y() / 2),
            'tr': (self.mapToScene(self.rect().topRight()).x() / 2,
                   self.mapToScene(self.rect().topRight()).y() / 2),
            'bl': (self.mapToScene(self.rect().bottomLeft()).x() / 2,
                   self.mapToScene(self.rect().bottomLeft()).y() / 2),
            'br': (self.mapToScene(self.rect().bottomRight()).x() / 2,
                   self.mapToScene(self.rect().bottomRight()).y() / 2)}

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
            'tl': (self.mapToScene(self.rect().topLeft()).x() / 2,
                   self.mapToScene(self.rect().topLeft()).y() / 2),
            'tr': (self.mapToScene(self.rect().topRight()).x() / 2,
                   self.mapToScene(self.rect().topRight()).y() / 2),
            'bl': (self.mapToScene(self.rect().bottomLeft()).x() / 2,
                   self.mapToScene(self.rect().bottomLeft()).y() / 2),
            'br': (self.mapToScene(self.rect().bottomRight()).x() / 2,
                   self.mapToScene(self.rect().bottomRight()).y() / 2)}

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
                'tl': (self.mapToScene(self.rect().topLeft()).x() / 2,
                       self.mapToScene(self.rect().topLeft()).y() / 2),
                'tr': (self.mapToScene(self.rect().topRight()).x() / 2,
                       self.mapToScene(self.rect().topRight()).y() / 2),
                'bl': (self.mapToScene(self.rect().bottomLeft()).x() / 2,
                       self.mapToScene(self.rect().bottomLeft()).y() / 2),
                'br': (self.mapToScene(self.rect().bottomRight()).x() / 2,
                       self.mapToScene(self.rect().bottomRight()).y() / 2)}
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
        global mkr_vis, ani_typ
        for i in self.items():
            if i.type() == QtWidgets.QGraphicsRectItem.UserType + 2:
                i.setVisible(mkr_vis)
                if i.data(1).startswith('JUV'):
                    i.setVisible(mkr_vis and ani_typ)

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
        global frm, frm_list, frm_dig
        if loaded:
            # Convert OpenCV np-array image to QImage
            frm = cv.imread(roi_frm[val], cv.IMREAD_UNCHANGED)
            frm = cv.resize(frm, (0, 0), fx=2, fy=2, interpolation=cv.INTER_NEAREST_EXACT)
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

        self.inputButton.clicked.connect(self.__input_selection)
        self.loadButton.clicked.connect(self.__loading_func)
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

    # File loading button functions
    def __input_selection(self):
        out_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select input Directory')
        self.inputPath.setText(out_path)

    # Main loading function
    def __loading_func(self):
        global ani_typ, roi_frm, roi_dir, roi_data, roi_grp, color_palette, frm_dig, frm_list, loaded
        # Verify GUI inputs
        flag = False
        err_msg = str()
        roi_path = self.inputPath.text()
        if not os.path.isdir(roi_path):
            flag = True
            err_msg += "Invalid input path!\n"
        if flag:
            QtWidgets.QMessageBox.critical(self, "Error", err_msg)
            return
        # File loading
        else:
            roi_dir = roi_path
            self.hide()
            # Load control window
            self.controlWindow.show()
            # Load frame viewer
            self.frameWindow.show()

            # Get required files
            tot_frm = 0  # INIT VAR
            for f in os.listdir(roi_dir):
                if f.endswith('.png'):
                    roi_frm.append(os.path.join(roi_dir, f))
                elif f.endswith('_prop.json'):
                    roi_prop = load_roi_prop(os.path.join(roi_dir, f))
                    tot_frm = len(roi_prop)
            # Rebuild previous ROIs
            for n in roi_data:
                for k in roi_data[n]:
                    # Get top-left corner
                    x = roi_data[n][k]['tl'][0]
                    y = roi_data[n][k]['tl'][1]
                    # Compute width
                    x_diff = roi_data[n][k]['tr'][0] - x
                    y_diff = roi_data[n][k]['tr'][1] - y
                    w = math.sqrt(x_diff ** 2 + y_diff ** 2)
                    a_w = math.atan(y_diff/x_diff) / math.pi * 180  # Rotation angle based on top-left and top-right
                    # Compute height
                    x_diff = roi_data[n][k]['bl'][0] - x
                    y_diff = roi_data[n][k]['bl'][1] - y
                    h = math.sqrt(x_diff ** 2 + y_diff ** 2)
                    a_h = -math.atan(x_diff/y_diff) / math.pi * 180  # Rotation angle based on top-left and bottom-left
                    # Compute rotation angle
                    a = a_h if abs(a_h) > abs(a_w) else a_w  # Select larger angle for rotation
                    # Set item
                    item = RegionRect(x, y, w, h, n, k, color_palette[k])
                    item.setTransformOriginPoint(QtCore.QPointF(x, y))  # Fix top-left corner
                    item.setRotation(a)
                    item.setTransformOriginPoint(item.rect().center())
                    item.updateHandlesPos()
                    item.setVisible(n == 0)
                    # Add to scene
                    self.frameWindow.scene.addItem(item)

            # Send video frame information to controls
            self.controlWindow.tot_frm = tot_frm
            if tot_frm == 0:
                tot_frm = len(roi_frm)
                self.controlWindow.fullmodeButton.setChecked(True)
                self.controlWindow.selcmodeButton.setEnabled(False)
                self.controlWindow.frameSlider.setMaximum(tot_frm - 1)
                self.controlWindow.sliderValue.setMaximum(tot_frm - 1)
            else:
                if tot_frm > len(roi_frm):
                    idx_lst = [str(int(os.path.splitext(os.path.basename(f))[0].split('_')[1])) for f in roi_frm]
                    curr_idx = -1  # INIT VAR
                    temp_flst = []  # INIT VAR
                    for n in roi_prop:
                        if n in idx_lst:
                            curr_idx += 1
                        temp_flst.append(roi_frm[curr_idx])
                    roi_frm = copy.deepcopy(temp_flst)
                self.controlWindow.tgtButton.setDisabled(ani_typ)
                self.controlWindow.juvButton.setEnabled(ani_typ)
                self.controlWindow.juvButton.setChecked(ani_typ)
                self.controlWindow.frameSlider.setMaximum(len(roi_grp) - 1)
                self.controlWindow.sliderValue.setMaximum(len(roi_grp) - 1)
            # Initialize frame processing list
            for i in range(tot_frm):
                frm_feat = {'idx': i, 'keep': 1}
                frm_list.append(copy.deepcopy(frm_feat))
            # Set status, send signal
            loaded = True
            frm_dig = '%%0%dd' % int(math.log10(tot_frm + 1))
            com_sig.frm_info_sig.emit(0, " | Current frame: 0 | Progress: 0 of %d 0.00%%)" % tot_frm)
