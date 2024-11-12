import os
import cv2 as cv
from megit.data import get_frm, brt_con, draw_text
from PySide6 import QtCore, QtGui, QtWidgets
from megit.gui.dgn_preprocz_ctrl import Ui_ControlViewer
from megit.gui.dgn_preproc_frmv import Ui_FrameViewer
from megit.gui.dgn_preproc_load import Ui_MainLoader


# Global definitions  -----------------------------------------------------------------------------------------------  #
# Define a class to handle cross window signals
class ComSig(QtCore.QObject):
    frm_ctrl_sig = QtCore.Signal(int)  # Frame selection operation synchronizer
    frm_info_sig = QtCore.Signal(int, str)  # Current frame information messenger


# Define global control variables
com_sig = ComSig()  # Global signals
vid_cap = cv.VideoCapture()  # OpenCV video capture
loaded = False  # File loading status flag
frm = None  # Current frame image
frm_msg = str()  # Information message of current frame

# Define global process variables
out_dir = str()  # Output directory
brt = 0  # Brightness level
con = 0  # Contrast level
txt_mark = False  # Define frame index text exist or not
txt_linc = (255, 255, 255)  # Frame index text colour
txt_hbkg = True  # Defines text background exist or not
txt_bkgc = (0, 0, 0)  # Frame index background colour
txt_size = 1  # Frame index text size
txt_xval = 0  # Frame index text left corner
txt_yval = 0  # Frame index text right corner
flp = None  # Frame flipping value


# Main process worker class  ----------------------------------------------------------------------------------------  #
class ProcWorker(QtCore.QObject):
    finished = QtCore.Signal()
    progress = QtCore.Signal(int)

    def run(self):
        global out_dir, vid_cap, brt, con, txt_mark, txt_linc, txt_hbkg, txt_bkgc, txt_size, txt_xval, txt_yval, flp

        # Get basic parameters
        width = int(vid_cap.get(cv.CAP_PROP_FRAME_WIDTH))
        height = int(vid_cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        frm_size = (width, height)
        # Set output video
        vid_file = os.path.join(out_dir, "zoom.avi")
        vid_writer = cv.VideoWriter(vid_file, cv.VideoWriter_fourcc(*"FFV1"), vid_cap.get(cv.CAP_PROP_FPS), frm_size)

        # Main process loop
        count = 0  # INIT VAR
        for i in range(int(vid_cap.get(cv.CAP_PROP_FRAME_COUNT))):
            img = get_frm(vid_cap, i)
            # Process and write frames
            img = brt_con(img, brt, con)
            if flp is not None:
                img = cv.flip(img, flp)
            if txt_mark:
                img = draw_text(img, "%06d" % i, txt_xval, txt_yval, txt_size, txt_linc, txt_hbkg, txt_bkgc)
            vid_writer.write(img)
            # Progress report, set here as this is the most cost section
            count += 1
            self.progress.emit(count)

        self.finished.emit()


# [ControlViewer] MEGIT Zoom-Video main controller  -----------------------------------------------------------------  #
class ControlViewer(QtWidgets.QMainWindow, Ui_ControlViewer):
    tot_frm = 1  # Total frames to label
    curr_frm = 0  # Frame currently operating
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
        # Frame tagging control
        self.mrkMode.currentIndexChanged.connect(self.__set_text_color)
        self.sizeValue.valueChanged.connect(self.__set_text_size)
        self.xValue.valueChanged.connect(self.__set_text_loc)
        self.yValue.valueChanged.connect(self.__set_text_loc)
        self.mrkCheck.clicked.connect(self.__set_frm_text)
        # Frame flip control
        self.hflpBox.clicked.connect(self.__set_flip_val)
        self.vflpBox.clicked.connect(self.__set_flip_val)
        # Signal receiver
        com_sig.frm_info_sig.connect(self.__status_report)
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

    def __status_report(self):
        self.statusBar.showMessage(frm_msg)

    def __frame_slider_control(self):
        global frm_msg
        self.curr_frm = self.frameSlider.value()
        frm_msg = " | Current frame index: %d" % self.curr_frm
        com_sig.frm_info_sig.emit(self.curr_frm, frm_msg)

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

    def __set_flip_val(self):
        global flp
        hflp = self.hflpBox.isChecked()
        vflp = self.vflpBox.isChecked()
        if hflp:
            flp = -1 if vflp else 0
        else:
            flp = 1 if vflp else None
        com_sig.frm_info_sig.emit(self.curr_frm, frm_msg)

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
        # Disable Controls
        self.frameSlider.setEnabled(False)
        self.sliderValue.setEnabled(False)
        self.brtSlider.setEnabled(False)
        self.brtValue.setEnabled(False)
        self.conSlider.setEnabled(False)
        self.conValue.setEnabled(False)
        self.mrkCheck.setEnabled(False)
        self.mrkMode.setEnabled(False)
        self.sizeValue.setEnabled(False)
        self.xValue.setEnabled(False)
        self.yValue.setEnabled(False)
        self.hflpBox.setEnabled(False)
        self.vflpBox.setEnabled(False)
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
        self.thread.finished.connect(lambda: self.mrkCheck.setEnabled(True))
        self.thread.finished.connect(lambda: self.mrkMode.setEnabled(mk_flag))
        self.thread.finished.connect(lambda: self.sizeValue.setEnabled(sz_flag))
        self.thread.finished.connect(lambda: self.xValue.setEnabled(x_flag))
        self.thread.finished.connect(lambda: self.yValue.setEnabled(y_flag))
        self.thread.finished.connect(lambda: self.hflpBox.setEnabled(True))
        self.thread.finished.connect(lambda: self.vflpBox.setEnabled(True))
        self.thread.finished.connect(lambda: self.prevButton.setEnabled(True))
        self.thread.finished.connect(lambda: self.nextButton.setEnabled(True))
        self.thread.finished.connect(lambda: self.startButton.setEnabled(True))

    # Main process function
    def __start_func(self):
        # Set progress bar
        self.prog_steps = self.tot_frm
        # Execute main task
        self.__main_proc_task()


# [FrameViewer] MEGIT Zoom-Video frame display and region marker ----------------------------------------------------  #
class FrameViewer(QtWidgets.QMainWindow, Ui_FrameViewer):
    first_call = True

    def __init__(self, parent=None):
        super(FrameViewer, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.scene = QtWidgets.QGraphicsScene(self)
        com_sig.frm_info_sig.connect(self.__frame_loader)
        # Status signal receiver
        com_sig.frm_info_sig.connect(self.__status_report)

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

    def __status_report(self):
        self.statusBar.showMessage(frm_msg)

    def __frame_loader(self, val, _):
        global frm, brt, con, txt_mark, txt_linc, txt_bkgc, txt_hbkg, txt_size, txt_xval, txt_yval, flp
        if loaded:
            # Convert OpenCV np-array image to QImage
            frm = get_frm(vid_cap, val)
            frm = brt_con(frm, brt, con)
            if flp is not None:
                frm = cv.flip(frm, flp)
            if txt_mark:
                frm = draw_text(frm, "%06d" % val, txt_xval, txt_yval, txt_size, txt_linc, txt_hbkg, txt_bkgc)
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


# [MainLoader] MEGIT Zoom-Video main loader  ------------------------------------------------------------------------  #
class MainLoader(QtWidgets.QMainWindow, Ui_MainLoader):
    def __init__(self, parent=None):
        super(MainLoader, self).__init__(parent)
        self.setupUi(self)
        self.controlWindow = ControlViewer()
        self.frameWindow = FrameViewer(self.controlWindow)

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
        global vid_cap, out_dir, loaded
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
            # Set status, send signal
            loaded = True
            com_sig.frm_info_sig.emit(0, " | Current frame: 0 | Progress: 0 of %d 0.00%%)" % vid_cap.get(7))
