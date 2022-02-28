# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\MEGIT\megit\gui\dgn_preproco_ctrl.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ControlViewer(object):
    def setupUi(self, ControlViewer):
        ControlViewer.setObjectName("ControlViewer")
        ControlViewer.resize(1060, 400)
        ControlViewer.setMinimumSize(QtCore.QSize(1060, 400))
        ControlViewer.setMaximumSize(QtCore.QSize(1060, 400))
        self.frmctrlWidget = QtWidgets.QWidget(ControlViewer)
        self.frmctrlWidget.setObjectName("frmctrlWidget")
        self.mainLayout = QtWidgets.QHBoxLayout(self.frmctrlWidget)
        self.mainLayout.setContentsMargins(5, 5, 5, 5)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName("mainLayout")
        self.inputsLayout = QtWidgets.QVBoxLayout()
        self.inputsLayout.setSpacing(5)
        self.inputsLayout.setObjectName("inputsLayout")
        self.frmsldrLayout = QtWidgets.QHBoxLayout()
        self.frmsldrLayout.setSpacing(10)
        self.frmsldrLayout.setObjectName("frmsldrLayout")
        self.frameSlider = QtWidgets.QSlider(self.frmctrlWidget)
        self.frameSlider.setMinimumSize(QtCore.QSize(0, 25))
        self.frameSlider.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frameSlider.setOrientation(QtCore.Qt.Horizontal)
        self.frameSlider.setObjectName("frameSlider")
        self.frmsldrLayout.addWidget(self.frameSlider)
        self.sliderValue = QtWidgets.QSpinBox(self.frmctrlWidget)
        self.sliderValue.setMinimumSize(QtCore.QSize(50, 0))
        self.sliderValue.setObjectName("sliderValue")
        self.frmsldrLayout.addWidget(self.sliderValue)
        self.inputsLayout.addLayout(self.frmsldrLayout)
        self.controlsLayout = QtWidgets.QHBoxLayout()
        self.controlsLayout.setSpacing(5)
        self.controlsLayout.setObjectName("controlsLayout")
        self.prevButton = QtWidgets.QPushButton(self.frmctrlWidget)
        self.prevButton.setMinimumSize(QtCore.QSize(0, 250))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.prevButton.setFont(font)
        self.prevButton.setObjectName("prevButton")
        self.controlsLayout.addWidget(self.prevButton)
        self.settingsLayout = QtWidgets.QVBoxLayout()
        self.settingsLayout.setSpacing(10)
        self.settingsLayout.setObjectName("settingsLayout")
        self.imgadjBox = QtWidgets.QGroupBox(self.frmctrlWidget)
        self.imgadjBox.setMinimumSize(QtCore.QSize(0, 85))
        self.imgadjBox.setMaximumSize(QtCore.QSize(16777215, 85))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.imgadjBox.setFont(font)
        self.imgadjBox.setObjectName("imgadjBox")
        self.imgadjLayout = QtWidgets.QGridLayout(self.imgadjBox)
        self.imgadjLayout.setContentsMargins(10, 10, 10, 10)
        self.imgadjLayout.setSpacing(5)
        self.imgadjLayout.setObjectName("imgadjLayout")
        self.brtLabel = QtWidgets.QLabel(self.imgadjBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.brtLabel.setFont(font)
        self.brtLabel.setObjectName("brtLabel")
        self.imgadjLayout.addWidget(self.brtLabel, 0, 0, 1, 1)
        self.conLabel = QtWidgets.QLabel(self.imgadjBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.conLabel.setFont(font)
        self.conLabel.setObjectName("conLabel")
        self.imgadjLayout.addWidget(self.conLabel, 1, 0, 1, 1)
        self.conValue = QtWidgets.QSpinBox(self.imgadjBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.conValue.setFont(font)
        self.conValue.setMinimum(-100)
        self.conValue.setMaximum(100)
        self.conValue.setObjectName("conValue")
        self.imgadjLayout.addWidget(self.conValue, 1, 2, 1, 1)
        self.brtValue = QtWidgets.QSpinBox(self.imgadjBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.brtValue.setFont(font)
        self.brtValue.setMinimum(-150)
        self.brtValue.setMaximum(150)
        self.brtValue.setObjectName("brtValue")
        self.imgadjLayout.addWidget(self.brtValue, 0, 2, 1, 1)
        self.brtSlider = QtWidgets.QSlider(self.imgadjBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.brtSlider.setFont(font)
        self.brtSlider.setMinimum(-150)
        self.brtSlider.setMaximum(150)
        self.brtSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brtSlider.setObjectName("brtSlider")
        self.imgadjLayout.addWidget(self.brtSlider, 0, 1, 1, 1)
        self.conSlider = QtWidgets.QSlider(self.imgadjBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.conSlider.setFont(font)
        self.conSlider.setMinimum(-100)
        self.conSlider.setMaximum(100)
        self.conSlider.setOrientation(QtCore.Qt.Horizontal)
        self.conSlider.setObjectName("conSlider")
        self.imgadjLayout.addWidget(self.conSlider, 1, 1, 1, 1)
        self.settingsLayout.addWidget(self.imgadjBox)
        self.featuresLayout = QtWidgets.QHBoxLayout()
        self.featuresLayout.setSpacing(10)
        self.featuresLayout.setObjectName("featuresLayout")
        self.frameGroup = QtWidgets.QGroupBox(self.frmctrlWidget)
        self.frameGroup.setMinimumSize(QtCore.QSize(120, 150))
        self.frameGroup.setMaximumSize(QtCore.QSize(120, 150))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.frameGroup.setFont(font)
        self.frameGroup.setObjectName("frameGroup")
        self.frmctrlLayout = QtWidgets.QVBoxLayout(self.frameGroup)
        self.frmctrlLayout.setContentsMargins(10, 5, 10, 10)
        self.frmctrlLayout.setSpacing(10)
        self.frmctrlLayout.setObjectName("frmctrlLayout")
        self.totfrmLayout = QtWidgets.QVBoxLayout()
        self.totfrmLayout.setSpacing(5)
        self.totfrmLayout.setObjectName("totfrmLayout")
        self.totfrmLabel = QtWidgets.QLabel(self.frameGroup)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.totfrmLabel.setFont(font)
        self.totfrmLabel.setObjectName("totfrmLabel")
        self.totfrmLayout.addWidget(self.totfrmLabel)
        self.totfrmBox = QtWidgets.QSpinBox(self.frameGroup)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.totfrmBox.setFont(font)
        self.totfrmBox.setMaximum(16777215)
        self.totfrmBox.setProperty("value", 36000)
        self.totfrmBox.setObjectName("totfrmBox")
        self.totfrmLayout.addWidget(self.totfrmBox)
        self.frmctrlLayout.addLayout(self.totfrmLayout)
        self.cutfrmBox = QtWidgets.QGroupBox(self.frameGroup)
        self.cutfrmBox.setMinimumSize(QtCore.QSize(100, 75))
        self.cutfrmBox.setMaximumSize(QtCore.QSize(100, 75))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cutfrmBox.setFont(font)
        self.cutfrmBox.setObjectName("cutfrmBox")
        self.cutfrmLayout = QtWidgets.QVBoxLayout(self.cutfrmBox)
        self.cutfrmLayout.setContentsMargins(10, 5, 10, 10)
        self.cutfrmLayout.setSpacing(5)
        self.cutfrmLayout.setObjectName("cutfrmLayout")
        self.cutaButton = QtWidgets.QPushButton(self.cutfrmBox)
        self.cutaButton.setObjectName("cutaButton")
        self.cutfrmLayout.addWidget(self.cutaButton)
        self.cutbButton = QtWidgets.QPushButton(self.cutfrmBox)
        self.cutbButton.setObjectName("cutbButton")
        self.cutfrmLayout.addWidget(self.cutbButton)
        self.frmctrlLayout.addWidget(self.cutfrmBox)
        self.featuresLayout.addWidget(self.frameGroup)
        self.frmmrkBox = QtWidgets.QGroupBox(self.frmctrlWidget)
        self.frmmrkBox.setMinimumSize(QtCore.QSize(250, 150))
        self.frmmrkBox.setMaximumSize(QtCore.QSize(250, 150))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.frmmrkBox.setFont(font)
        self.frmmrkBox.setObjectName("frmmrkBox")
        self.frmmrkLayout = QtWidgets.QVBoxLayout(self.frmmrkBox)
        self.frmmrkLayout.setContentsMargins(10, 10, 10, 10)
        self.frmmrkLayout.setSpacing(12)
        self.frmmrkLayout.setObjectName("frmmrkLayout")
        self.mrkCheck = QtWidgets.QCheckBox(self.frmmrkBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.mrkCheck.setFont(font)
        self.mrkCheck.setObjectName("mrkCheck")
        self.frmmrkLayout.addWidget(self.mrkCheck)
        self.textLayout = QtWidgets.QGridLayout()
        self.textLayout.setHorizontalSpacing(10)
        self.textLayout.setVerticalSpacing(2)
        self.textLayout.setObjectName("textLayout")
        self.colourLabel = QtWidgets.QLabel(self.frmmrkBox)
        self.colourLabel.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.colourLabel.setFont(font)
        self.colourLabel.setObjectName("colourLabel")
        self.textLayout.addWidget(self.colourLabel, 0, 0, 1, 1)
        self.sizeLabel = QtWidgets.QLabel(self.frmmrkBox)
        self.sizeLabel.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.sizeLabel.setFont(font)
        self.sizeLabel.setObjectName("sizeLabel")
        self.textLayout.addWidget(self.sizeLabel, 0, 1, 1, 1)
        self.mrkMode = QtWidgets.QComboBox(self.frmmrkBox)
        self.mrkMode.setEnabled(False)
        self.mrkMode.setMinimumSize(QtCore.QSize(100, 20))
        self.mrkMode.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.mrkMode.setFont(font)
        self.mrkMode.setObjectName("mrkMode")
        self.mrkMode.addItem("")
        self.mrkMode.addItem("")
        self.mrkMode.addItem("")
        self.mrkMode.addItem("")
        self.textLayout.addWidget(self.mrkMode, 1, 0, 1, 1)
        self.sizeValue = QtWidgets.QDoubleSpinBox(self.frmmrkBox)
        self.sizeValue.setEnabled(False)
        self.sizeValue.setMinimumSize(QtCore.QSize(100, 20))
        self.sizeValue.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.sizeValue.setFont(font)
        self.sizeValue.setDecimals(1)
        self.sizeValue.setProperty("value", 1.0)
        self.sizeValue.setObjectName("sizeValue")
        self.textLayout.addWidget(self.sizeValue, 1, 1, 1, 1)
        self.frmmrkLayout.addLayout(self.textLayout)
        self.cordLayout = QtWidgets.QGridLayout()
        self.cordLayout.setHorizontalSpacing(10)
        self.cordLayout.setVerticalSpacing(2)
        self.cordLayout.setObjectName("cordLayout")
        self.xLabel = QtWidgets.QLabel(self.frmmrkBox)
        self.xLabel.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.xLabel.setFont(font)
        self.xLabel.setObjectName("xLabel")
        self.cordLayout.addWidget(self.xLabel, 0, 0, 1, 1)
        self.yLabel = QtWidgets.QLabel(self.frmmrkBox)
        self.yLabel.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.yLabel.setFont(font)
        self.yLabel.setObjectName("yLabel")
        self.cordLayout.addWidget(self.yLabel, 0, 1, 1, 1)
        self.xValue = QtWidgets.QSpinBox(self.frmmrkBox)
        self.xValue.setEnabled(False)
        self.xValue.setMinimumSize(QtCore.QSize(100, 20))
        self.xValue.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.xValue.setFont(font)
        self.xValue.setMinimum(-1)
        self.xValue.setProperty("value", 3)
        self.xValue.setObjectName("xValue")
        self.cordLayout.addWidget(self.xValue, 1, 0, 1, 1)
        self.yValue = QtWidgets.QSpinBox(self.frmmrkBox)
        self.yValue.setEnabled(False)
        self.yValue.setMinimumSize(QtCore.QSize(100, 20))
        self.yValue.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.yValue.setFont(font)
        self.yValue.setMinimum(-1)
        self.yValue.setProperty("value", 3)
        self.yValue.setObjectName("yValue")
        self.cordLayout.addWidget(self.yValue, 1, 1, 1, 1)
        self.frmmrkLayout.addLayout(self.cordLayout)
        self.featuresLayout.addWidget(self.frmmrkBox)
        self.labelGroup = QtWidgets.QGroupBox(self.frmctrlWidget)
        self.labelGroup.setMinimumSize(QtCore.QSize(250, 150))
        self.labelGroup.setMaximumSize(QtCore.QSize(250, 150))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelGroup.setFont(font)
        self.labelGroup.setObjectName("labelGroup")
        self.labelLayout = QtWidgets.QVBoxLayout(self.labelGroup)
        self.labelLayout.setContentsMargins(10, 0, 10, 10)
        self.labelLayout.setSpacing(5)
        self.labelLayout.setObjectName("labelLayout")
        self.modeLayout = QtWidgets.QGridLayout()
        self.modeLayout.setContentsMargins(8, -1, 0, -1)
        self.modeLayout.setHorizontalSpacing(5)
        self.modeLayout.setVerticalSpacing(0)
        self.modeLayout.setObjectName("modeLayout")
        self.expLabel = QtWidgets.QLabel(self.labelGroup)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.expLabel.setFont(font)
        self.expLabel.setObjectName("expLabel")
        self.modeLayout.addWidget(self.expLabel, 0, 0, 1, 1)
        self.objButton = QtWidgets.QRadioButton(self.labelGroup)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.objButton.setFont(font)
        self.objButton.setChecked(True)
        self.objButton.setObjectName("objButton")
        self.modeGroup = QtWidgets.QButtonGroup(ControlViewer)
        self.modeGroup.setObjectName("modeGroup")
        self.modeGroup.addButton(self.objButton)
        self.modeLayout.addWidget(self.objButton, 1, 0, 1, 1)
        self.juvButton = QtWidgets.QRadioButton(self.labelGroup)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.juvButton.setFont(font)
        self.juvButton.setObjectName("juvButton")
        self.modeGroup.addButton(self.juvButton)
        self.modeLayout.addWidget(self.juvButton, 1, 1, 1, 1)
        self.labelLayout.addLayout(self.modeLayout)
        self.lblselLayout = QtWidgets.QGridLayout()
        self.lblselLayout.setHorizontalSpacing(10)
        self.lblselLayout.setVerticalSpacing(2)
        self.lblselLayout.setObjectName("lblselLayout")
        self.tgtLabel = QtWidgets.QLabel(self.labelGroup)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tgtLabel.setFont(font)
        self.tgtLabel.setObjectName("tgtLabel")
        self.lblselLayout.addWidget(self.tgtLabel, 0, 0, 1, 1)
        self.juvLabel = QtWidgets.QLabel(self.labelGroup)
        self.juvLabel.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.juvLabel.setFont(font)
        self.juvLabel.setObjectName("juvLabel")
        self.lblselLayout.addWidget(self.juvLabel, 0, 1, 1, 1)
        self.tgtBox = QtWidgets.QComboBox(self.labelGroup)
        self.tgtBox.setMinimumSize(QtCore.QSize(100, 20))
        self.tgtBox.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tgtBox.setFont(font)
        self.tgtBox.setObjectName("tgtBox")
        self.tgtBox.addItem("")
        self.tgtBox.addItem("")
        self.tgtBox.addItem("")
        self.tgtBox.addItem("")
        self.lblselLayout.addWidget(self.tgtBox, 1, 0, 1, 1)
        self.juvBox = QtWidgets.QComboBox(self.labelGroup)
        self.juvBox.setEnabled(False)
        self.juvBox.setMinimumSize(QtCore.QSize(100, 20))
        self.juvBox.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.juvBox.setFont(font)
        self.juvBox.setObjectName("juvBox")
        self.juvBox.addItem("")
        self.juvBox.addItem("")
        self.juvBox.addItem("")
        self.juvBox.addItem("")
        self.lblselLayout.addWidget(self.juvBox, 1, 1, 1, 1)
        self.labelLayout.addLayout(self.lblselLayout)
        self.lblctrlLayout = QtWidgets.QGridLayout()
        self.lblctrlLayout.setContentsMargins(-1, 5, -1, -1)
        self.lblctrlLayout.setHorizontalSpacing(10)
        self.lblctrlLayout.setVerticalSpacing(2)
        self.lblctrlLayout.setObjectName("lblctrlLayout")
        self.labelLine = QtWidgets.QFrame(self.labelGroup)
        self.labelLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.labelLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelLine.setObjectName("labelLine")
        self.lblctrlLayout.addWidget(self.labelLine, 0, 0, 1, 2)
        self.hidButton = QtWidgets.QPushButton(self.labelGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hidButton.sizePolicy().hasHeightForWidth())
        self.hidButton.setSizePolicy(sizePolicy)
        self.hidButton.setMinimumSize(QtCore.QSize(100, 23))
        self.hidButton.setMaximumSize(QtCore.QSize(100, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.hidButton.setFont(font)
        self.hidButton.setObjectName("hidButton")
        self.lblctrlLayout.addWidget(self.hidButton, 1, 0, 1, 1)
        self.updButton = QtWidgets.QPushButton(self.labelGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updButton.sizePolicy().hasHeightForWidth())
        self.updButton.setSizePolicy(sizePolicy)
        self.updButton.setMinimumSize(QtCore.QSize(100, 23))
        self.updButton.setMaximumSize(QtCore.QSize(100, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.updButton.setFont(font)
        self.updButton.setObjectName("updButton")
        self.lblctrlLayout.addWidget(self.updButton, 1, 1, 1, 1)
        self.labelLayout.addLayout(self.lblctrlLayout)
        self.featuresLayout.addWidget(self.labelGroup)
        self.settingsLayout.addLayout(self.featuresLayout)
        self.controlsLayout.addLayout(self.settingsLayout)
        self.nextButton = QtWidgets.QPushButton(self.frmctrlWidget)
        self.nextButton.setMinimumSize(QtCore.QSize(0, 250))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")
        self.controlsLayout.addWidget(self.nextButton)
        self.inputsLayout.addLayout(self.controlsLayout)
        self.progressBar = QtWidgets.QProgressBar(self.frmctrlWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.inputsLayout.addWidget(self.progressBar)
        self.progctrlLayout = QtWidgets.QHBoxLayout()
        self.progctrlLayout.setSpacing(10)
        self.progctrlLayout.setObjectName("progctrlLayout")
        self.startButton = QtWidgets.QPushButton(self.frmctrlWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.progctrlLayout.addWidget(self.startButton)
        spacerItem = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.progctrlLayout.addItem(spacerItem)
        self.exitButton = QtWidgets.QPushButton(self.frmctrlWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.progctrlLayout.addWidget(self.exitButton)
        self.inputsLayout.addLayout(self.progctrlLayout)
        self.mainLayout.addLayout(self.inputsLayout)
        self.frmoutBox = QtWidgets.QGroupBox(self.frmctrlWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.frmoutBox.setFont(font)
        self.frmoutBox.setObjectName("frmoutBox")
        self.frmoutLayout = QtWidgets.QVBoxLayout(self.frmoutBox)
        self.frmoutLayout.setContentsMargins(5, 5, 5, 5)
        self.frmoutLayout.setSpacing(0)
        self.frmoutLayout.setObjectName("frmoutLayout")
        self.frmoutTable = QtWidgets.QTableWidget(self.frmoutBox)
        self.frmoutTable.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frmoutTable.setFont(font)
        self.frmoutTable.setObjectName("frmoutTable")
        self.frmoutTable.setColumnCount(2)
        self.frmoutTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.frmoutTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.frmoutTable.setHorizontalHeaderItem(1, item)
        self.frmoutLayout.addWidget(self.frmoutTable)
        self.mainLayout.addWidget(self.frmoutBox)
        ControlViewer.setCentralWidget(self.frmctrlWidget)
        self.statusBar = QtWidgets.QStatusBar(ControlViewer)
        self.statusBar.setObjectName("statusBar")
        ControlViewer.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(ControlViewer)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1060, 21))
        self.menuBar.setObjectName("menuBar")
        ControlViewer.setMenuBar(self.menuBar)

        self.retranslateUi(ControlViewer)
        self.mrkMode.setCurrentIndex(3)
        self.frameSlider.valueChanged['int'].connect(self.sliderValue.setValue)
        self.sliderValue.valueChanged['int'].connect(self.frameSlider.setValue)
        self.prevButton.clicked.connect(self.sliderValue.stepDown)
        self.nextButton.clicked.connect(self.sliderValue.stepUp)
        self.brtSlider.valueChanged['int'].connect(self.brtValue.setValue)
        self.brtValue.valueChanged['int'].connect(self.brtSlider.setValue)
        self.conSlider.valueChanged['int'].connect(self.conValue.setValue)
        self.conValue.valueChanged['int'].connect(self.conSlider.setValue)
        self.juvButton.toggled['bool'].connect(self.juvBox.setEnabled)
        self.juvButton.toggled['bool'].connect(self.juvLabel.setEnabled)
        self.mrkCheck.clicked['bool'].connect(self.colourLabel.setEnabled)
        self.mrkCheck.clicked['bool'].connect(self.mrkMode.setEnabled)
        self.mrkCheck.clicked['bool'].connect(self.sizeLabel.setEnabled)
        self.mrkCheck.clicked['bool'].connect(self.sizeValue.setEnabled)
        self.mrkCheck.clicked['bool'].connect(self.xLabel.setEnabled)
        self.mrkCheck.clicked['bool'].connect(self.xValue.setEnabled)
        self.mrkCheck.clicked['bool'].connect(self.yLabel.setEnabled)
        self.mrkCheck.clicked['bool'].connect(self.yValue.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ControlViewer)
        ControlViewer.setTabOrder(self.frameSlider, self.sliderValue)
        ControlViewer.setTabOrder(self.sliderValue, self.brtSlider)
        ControlViewer.setTabOrder(self.brtSlider, self.brtValue)
        ControlViewer.setTabOrder(self.brtValue, self.conSlider)
        ControlViewer.setTabOrder(self.conSlider, self.conValue)
        ControlViewer.setTabOrder(self.conValue, self.totfrmBox)
        ControlViewer.setTabOrder(self.totfrmBox, self.cutaButton)
        ControlViewer.setTabOrder(self.cutaButton, self.cutbButton)
        ControlViewer.setTabOrder(self.cutbButton, self.mrkCheck)
        ControlViewer.setTabOrder(self.mrkCheck, self.mrkMode)
        ControlViewer.setTabOrder(self.mrkMode, self.sizeValue)
        ControlViewer.setTabOrder(self.sizeValue, self.xValue)
        ControlViewer.setTabOrder(self.xValue, self.yValue)
        ControlViewer.setTabOrder(self.yValue, self.objButton)
        ControlViewer.setTabOrder(self.objButton, self.juvButton)
        ControlViewer.setTabOrder(self.juvButton, self.tgtBox)
        ControlViewer.setTabOrder(self.tgtBox, self.juvBox)
        ControlViewer.setTabOrder(self.juvBox, self.hidButton)
        ControlViewer.setTabOrder(self.hidButton, self.updButton)
        ControlViewer.setTabOrder(self.updButton, self.startButton)
        ControlViewer.setTabOrder(self.startButton, self.exitButton)
        ControlViewer.setTabOrder(self.exitButton, self.prevButton)
        ControlViewer.setTabOrder(self.prevButton, self.nextButton)
        ControlViewer.setTabOrder(self.nextButton, self.frmoutTable)

    def retranslateUi(self, ControlViewer):
        _translate = QtCore.QCoreApplication.translate
        ControlViewer.setWindowTitle(_translate("ControlViewer", "MEGIT Pre-Processing Control"))
        self.prevButton.setText(_translate("ControlViewer", "◀"))
        self.imgadjBox.setTitle(_translate("ControlViewer", "Image Adjustments"))
        self.brtLabel.setText(_translate("ControlViewer", "Brightness"))
        self.conLabel.setText(_translate("ControlViewer", "Contrast"))
        self.frameGroup.setTitle(_translate("ControlViewer", "Frame Setup"))
        self.totfrmLabel.setText(_translate("ControlViewer", "Total Frames"))
        self.cutfrmBox.setTitle(_translate("ControlViewer", "Cut-out Frames"))
        self.cutaButton.setText(_translate("ControlViewer", "Set A"))
        self.cutbButton.setText(_translate("ControlViewer", "Set B"))
        self.frmmrkBox.setTitle(_translate("ControlViewer", "Frame Marking"))
        self.mrkCheck.setText(_translate("ControlViewer", "Enable Marking"))
        self.colourLabel.setText(_translate("ControlViewer", "Mark Style"))
        self.sizeLabel.setText(_translate("ControlViewer", "Text Size"))
        self.mrkMode.setItemText(0, _translate("ControlViewer", "Black"))
        self.mrkMode.setItemText(1, _translate("ControlViewer", "White"))
        self.mrkMode.setItemText(2, _translate("ControlViewer", "Black on White"))
        self.mrkMode.setItemText(3, _translate("ControlViewer", "White on Black"))
        self.xLabel.setText(_translate("ControlViewer", "X Value"))
        self.yLabel.setText(_translate("ControlViewer", "Y Value"))
        self.labelGroup.setTitle(_translate("ControlViewer", "Label"))
        self.expLabel.setText(_translate("ControlViewer", "Experiment Type"))
        self.objButton.setText(_translate("ControlViewer", "Object"))
        self.juvButton.setText(_translate("ControlViewer", "Juvenile"))
        self.tgtLabel.setText(_translate("ControlViewer", "Test Regions"))
        self.juvLabel.setText(_translate("ControlViewer", "Juvenile Regions"))
        self.tgtBox.setItemText(0, _translate("ControlViewer", "[NONE]"))
        self.tgtBox.setItemText(1, _translate("ControlViewer", "Gap"))
        self.tgtBox.setItemText(2, _translate("ControlViewer", "Top"))
        self.tgtBox.setItemText(3, _translate("ControlViewer", "Bottom"))
        self.juvBox.setItemText(0, _translate("ControlViewer", "[NONE]"))
        self.juvBox.setItemText(1, _translate("ControlViewer", "Gap"))
        self.juvBox.setItemText(2, _translate("ControlViewer", "Top"))
        self.juvBox.setItemText(3, _translate("ControlViewer", "Bottom"))
        self.hidButton.setText(_translate("ControlViewer", "Hide"))
        self.updButton.setText(_translate("ControlViewer", "Update"))
        self.nextButton.setText(_translate("ControlViewer", "▶"))
        self.startButton.setText(_translate("ControlViewer", "Start"))
        self.exitButton.setText(_translate("ControlViewer", "Exit"))
        self.frmoutBox.setTitle(_translate("ControlViewer", "Removed Frames"))
        item = self.frmoutTable.horizontalHeaderItem(0)
        item.setText(_translate("ControlViewer", "From"))
        item = self.frmoutTable.horizontalHeaderItem(1)
        item.setText(_translate("ControlViewer", "To"))