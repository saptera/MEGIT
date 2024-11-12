# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dgn_preproco_ctrl.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QButtonGroup, QCheckBox, QComboBox, QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
                               QHBoxLayout, QLabel, QMenuBar, QProgressBar, QPushButton, QRadioButton, QSizePolicy,
                               QSlider, QSpacerItem, QSpinBox, QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
                               QWidget)


class Ui_ControlViewer(object):
    def setupUi(self, ControlViewer):
        if not ControlViewer.objectName():
            ControlViewer.setObjectName(u"ControlViewer")
        ControlViewer.resize(1060, 400)
        ControlViewer.setMinimumSize(QSize(1060, 400))
        ControlViewer.setMaximumSize(QSize(1060, 400))
        self.frmctrlWidget = QWidget(ControlViewer)
        self.frmctrlWidget.setObjectName(u"frmctrlWidget")
        self.mainLayout = QHBoxLayout(self.frmctrlWidget)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(5, 5, 5, 5)
        self.inputsLayout = QVBoxLayout()
        self.inputsLayout.setSpacing(5)
        self.inputsLayout.setObjectName(u"inputsLayout")
        self.frmsldrLayout = QHBoxLayout()
        self.frmsldrLayout.setSpacing(10)
        self.frmsldrLayout.setObjectName(u"frmsldrLayout")
        self.frameSlider = QSlider(self.frmctrlWidget)
        self.frameSlider.setObjectName(u"frameSlider")
        self.frameSlider.setMinimumSize(QSize(0, 25))
        self.frameSlider.setMaximumSize(QSize(16777215, 25))
        self.frameSlider.setOrientation(Qt.Horizontal)

        self.frmsldrLayout.addWidget(self.frameSlider)

        self.sliderValue = QSpinBox(self.frmctrlWidget)
        self.sliderValue.setObjectName(u"sliderValue")
        self.sliderValue.setMinimumSize(QSize(50, 0))

        self.frmsldrLayout.addWidget(self.sliderValue)


        self.inputsLayout.addLayout(self.frmsldrLayout)

        self.controlsLayout = QHBoxLayout()
        self.controlsLayout.setSpacing(5)
        self.controlsLayout.setObjectName(u"controlsLayout")
        self.prevButton = QPushButton(self.frmctrlWidget)
        self.prevButton.setObjectName(u"prevButton")
        self.prevButton.setMinimumSize(QSize(0, 250))
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.prevButton.setFont(font)

        self.controlsLayout.addWidget(self.prevButton)

        self.settingsLayout = QVBoxLayout()
        self.settingsLayout.setSpacing(10)
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.imgadjBox = QGroupBox(self.frmctrlWidget)
        self.imgadjBox.setObjectName(u"imgadjBox")
        self.imgadjBox.setMinimumSize(QSize(0, 85))
        self.imgadjBox.setMaximumSize(QSize(16777215, 85))
        font1 = QFont()
        font1.setBold(True)
        self.imgadjBox.setFont(font1)
        self.imgadjLayout = QGridLayout(self.imgadjBox)
        self.imgadjLayout.setSpacing(5)
        self.imgadjLayout.setObjectName(u"imgadjLayout")
        self.imgadjLayout.setContentsMargins(10, 10, 10, 10)
        self.brtLabel = QLabel(self.imgadjBox)
        self.brtLabel.setObjectName(u"brtLabel")
        font2 = QFont()
        font2.setBold(False)
        self.brtLabel.setFont(font2)

        self.imgadjLayout.addWidget(self.brtLabel, 0, 0, 1, 1)

        self.conLabel = QLabel(self.imgadjBox)
        self.conLabel.setObjectName(u"conLabel")
        self.conLabel.setFont(font2)

        self.imgadjLayout.addWidget(self.conLabel, 1, 0, 1, 1)

        self.conValue = QSpinBox(self.imgadjBox)
        self.conValue.setObjectName(u"conValue")
        self.conValue.setFont(font2)
        self.conValue.setMinimum(-100)
        self.conValue.setMaximum(100)

        self.imgadjLayout.addWidget(self.conValue, 1, 2, 1, 1)

        self.brtValue = QSpinBox(self.imgadjBox)
        self.brtValue.setObjectName(u"brtValue")
        self.brtValue.setFont(font2)
        self.brtValue.setMinimum(-150)
        self.brtValue.setMaximum(150)

        self.imgadjLayout.addWidget(self.brtValue, 0, 2, 1, 1)

        self.brtSlider = QSlider(self.imgadjBox)
        self.brtSlider.setObjectName(u"brtSlider")
        self.brtSlider.setFont(font2)
        self.brtSlider.setMinimum(-150)
        self.brtSlider.setMaximum(150)
        self.brtSlider.setOrientation(Qt.Horizontal)

        self.imgadjLayout.addWidget(self.brtSlider, 0, 1, 1, 1)

        self.conSlider = QSlider(self.imgadjBox)
        self.conSlider.setObjectName(u"conSlider")
        self.conSlider.setFont(font2)
        self.conSlider.setMinimum(-100)
        self.conSlider.setMaximum(100)
        self.conSlider.setOrientation(Qt.Horizontal)

        self.imgadjLayout.addWidget(self.conSlider, 1, 1, 1, 1)


        self.settingsLayout.addWidget(self.imgadjBox)

        self.featuresLayout = QHBoxLayout()
        self.featuresLayout.setSpacing(10)
        self.featuresLayout.setObjectName(u"featuresLayout")
        self.frameGroup = QGroupBox(self.frmctrlWidget)
        self.frameGroup.setObjectName(u"frameGroup")
        self.frameGroup.setMinimumSize(QSize(120, 150))
        self.frameGroup.setMaximumSize(QSize(120, 150))
        self.frameGroup.setFont(font1)
        self.frmctrlLayout = QVBoxLayout(self.frameGroup)
        self.frmctrlLayout.setSpacing(10)
        self.frmctrlLayout.setObjectName(u"frmctrlLayout")
        self.frmctrlLayout.setContentsMargins(10, 5, 10, 10)
        self.totfrmLayout = QVBoxLayout()
        self.totfrmLayout.setSpacing(5)
        self.totfrmLayout.setObjectName(u"totfrmLayout")
        self.totfrmLabel = QLabel(self.frameGroup)
        self.totfrmLabel.setObjectName(u"totfrmLabel")
        self.totfrmLabel.setFont(font2)

        self.totfrmLayout.addWidget(self.totfrmLabel)

        self.totfrmBox = QSpinBox(self.frameGroup)
        self.totfrmBox.setObjectName(u"totfrmBox")
        self.totfrmBox.setFont(font2)
        self.totfrmBox.setMaximum(16777215)
        self.totfrmBox.setValue(36000)

        self.totfrmLayout.addWidget(self.totfrmBox)


        self.frmctrlLayout.addLayout(self.totfrmLayout)

        self.cutfrmBox = QGroupBox(self.frameGroup)
        self.cutfrmBox.setObjectName(u"cutfrmBox")
        self.cutfrmBox.setMinimumSize(QSize(100, 75))
        self.cutfrmBox.setMaximumSize(QSize(100, 75))
        self.cutfrmBox.setFont(font2)
        self.cutfrmLayout = QVBoxLayout(self.cutfrmBox)
        self.cutfrmLayout.setSpacing(5)
        self.cutfrmLayout.setObjectName(u"cutfrmLayout")
        self.cutfrmLayout.setContentsMargins(10, 5, 10, 10)
        self.cutaButton = QPushButton(self.cutfrmBox)
        self.cutaButton.setObjectName(u"cutaButton")

        self.cutfrmLayout.addWidget(self.cutaButton)

        self.cutbButton = QPushButton(self.cutfrmBox)
        self.cutbButton.setObjectName(u"cutbButton")

        self.cutfrmLayout.addWidget(self.cutbButton)


        self.frmctrlLayout.addWidget(self.cutfrmBox)


        self.featuresLayout.addWidget(self.frameGroup)

        self.frmmrkBox = QGroupBox(self.frmctrlWidget)
        self.frmmrkBox.setObjectName(u"frmmrkBox")
        self.frmmrkBox.setMinimumSize(QSize(250, 150))
        self.frmmrkBox.setMaximumSize(QSize(250, 150))
        self.frmmrkBox.setFont(font1)
        self.frmmrkLayout = QVBoxLayout(self.frmmrkBox)
        self.frmmrkLayout.setSpacing(12)
        self.frmmrkLayout.setObjectName(u"frmmrkLayout")
        self.frmmrkLayout.setContentsMargins(10, 10, 10, 10)
        self.mrkCheck = QCheckBox(self.frmmrkBox)
        self.mrkCheck.setObjectName(u"mrkCheck")
        self.mrkCheck.setFont(font2)

        self.frmmrkLayout.addWidget(self.mrkCheck)

        self.textLayout = QGridLayout()
        self.textLayout.setObjectName(u"textLayout")
        self.textLayout.setHorizontalSpacing(10)
        self.textLayout.setVerticalSpacing(2)
        self.colourLabel = QLabel(self.frmmrkBox)
        self.colourLabel.setObjectName(u"colourLabel")
        self.colourLabel.setEnabled(False)
        self.colourLabel.setFont(font2)

        self.textLayout.addWidget(self.colourLabel, 0, 0, 1, 1)

        self.sizeLabel = QLabel(self.frmmrkBox)
        self.sizeLabel.setObjectName(u"sizeLabel")
        self.sizeLabel.setEnabled(False)
        self.sizeLabel.setFont(font2)

        self.textLayout.addWidget(self.sizeLabel, 0, 1, 1, 1)

        self.mrkMode = QComboBox(self.frmmrkBox)
        self.mrkMode.addItem("")
        self.mrkMode.addItem("")
        self.mrkMode.addItem("")
        self.mrkMode.addItem("")
        self.mrkMode.setObjectName(u"mrkMode")
        self.mrkMode.setEnabled(False)
        self.mrkMode.setMinimumSize(QSize(100, 20))
        self.mrkMode.setMaximumSize(QSize(100, 20))
        self.mrkMode.setFont(font2)

        self.textLayout.addWidget(self.mrkMode, 1, 0, 1, 1)

        self.sizeValue = QDoubleSpinBox(self.frmmrkBox)
        self.sizeValue.setObjectName(u"sizeValue")
        self.sizeValue.setEnabled(False)
        self.sizeValue.setMinimumSize(QSize(100, 20))
        self.sizeValue.setMaximumSize(QSize(100, 20))
        self.sizeValue.setFont(font2)
        self.sizeValue.setDecimals(1)
        self.sizeValue.setValue(1.000000000000000)

        self.textLayout.addWidget(self.sizeValue, 1, 1, 1, 1)


        self.frmmrkLayout.addLayout(self.textLayout)

        self.cordLayout = QGridLayout()
        self.cordLayout.setObjectName(u"cordLayout")
        self.cordLayout.setHorizontalSpacing(10)
        self.cordLayout.setVerticalSpacing(2)
        self.xLabel = QLabel(self.frmmrkBox)
        self.xLabel.setObjectName(u"xLabel")
        self.xLabel.setEnabled(False)
        self.xLabel.setFont(font2)

        self.cordLayout.addWidget(self.xLabel, 0, 0, 1, 1)

        self.yLabel = QLabel(self.frmmrkBox)
        self.yLabel.setObjectName(u"yLabel")
        self.yLabel.setEnabled(False)
        self.yLabel.setFont(font2)

        self.cordLayout.addWidget(self.yLabel, 0, 1, 1, 1)

        self.xValue = QSpinBox(self.frmmrkBox)
        self.xValue.setObjectName(u"xValue")
        self.xValue.setEnabled(False)
        self.xValue.setMinimumSize(QSize(100, 20))
        self.xValue.setMaximumSize(QSize(100, 20))
        self.xValue.setFont(font2)
        self.xValue.setMinimum(-1)
        self.xValue.setValue(3)

        self.cordLayout.addWidget(self.xValue, 1, 0, 1, 1)

        self.yValue = QSpinBox(self.frmmrkBox)
        self.yValue.setObjectName(u"yValue")
        self.yValue.setEnabled(False)
        self.yValue.setMinimumSize(QSize(100, 20))
        self.yValue.setMaximumSize(QSize(100, 20))
        self.yValue.setFont(font2)
        self.yValue.setMinimum(-1)
        self.yValue.setValue(3)

        self.cordLayout.addWidget(self.yValue, 1, 1, 1, 1)


        self.frmmrkLayout.addLayout(self.cordLayout)


        self.featuresLayout.addWidget(self.frmmrkBox)

        self.labelGroup = QGroupBox(self.frmctrlWidget)
        self.labelGroup.setObjectName(u"labelGroup")
        self.labelGroup.setMinimumSize(QSize(250, 150))
        self.labelGroup.setMaximumSize(QSize(250, 150))
        self.labelGroup.setFont(font1)
        self.labelLayout = QVBoxLayout(self.labelGroup)
        self.labelLayout.setSpacing(5)
        self.labelLayout.setObjectName(u"labelLayout")
        self.labelLayout.setContentsMargins(10, 0, 10, 10)
        self.modeLayout = QGridLayout()
        self.modeLayout.setObjectName(u"modeLayout")
        self.modeLayout.setHorizontalSpacing(5)
        self.modeLayout.setVerticalSpacing(0)
        self.modeLayout.setContentsMargins(8, -1, 0, -1)
        self.expLabel = QLabel(self.labelGroup)
        self.expLabel.setObjectName(u"expLabel")
        self.expLabel.setFont(font2)

        self.modeLayout.addWidget(self.expLabel, 0, 0, 1, 1)

        self.objButton = QRadioButton(self.labelGroup)
        self.modeGroup = QButtonGroup(ControlViewer)
        self.modeGroup.setObjectName(u"modeGroup")
        self.modeGroup.addButton(self.objButton)
        self.objButton.setObjectName(u"objButton")
        self.objButton.setFont(font2)
        self.objButton.setChecked(True)

        self.modeLayout.addWidget(self.objButton, 1, 0, 1, 1)

        self.juvButton = QRadioButton(self.labelGroup)
        self.modeGroup.addButton(self.juvButton)
        self.juvButton.setObjectName(u"juvButton")
        self.juvButton.setFont(font2)

        self.modeLayout.addWidget(self.juvButton, 1, 1, 1, 1)


        self.labelLayout.addLayout(self.modeLayout)

        self.lblselLayout = QGridLayout()
        self.lblselLayout.setObjectName(u"lblselLayout")
        self.lblselLayout.setHorizontalSpacing(10)
        self.lblselLayout.setVerticalSpacing(2)
        self.tgtLabel = QLabel(self.labelGroup)
        self.tgtLabel.setObjectName(u"tgtLabel")
        self.tgtLabel.setFont(font2)

        self.lblselLayout.addWidget(self.tgtLabel, 0, 0, 1, 1)

        self.juvLabel = QLabel(self.labelGroup)
        self.juvLabel.setObjectName(u"juvLabel")
        self.juvLabel.setEnabled(False)
        self.juvLabel.setFont(font2)

        self.lblselLayout.addWidget(self.juvLabel, 0, 1, 1, 1)

        self.tgtBox = QComboBox(self.labelGroup)
        self.tgtBox.addItem("")
        self.tgtBox.addItem("")
        self.tgtBox.addItem("")
        self.tgtBox.addItem("")
        self.tgtBox.addItem("")
        self.tgtBox.setObjectName(u"tgtBox")
        self.tgtBox.setMinimumSize(QSize(100, 20))
        self.tgtBox.setMaximumSize(QSize(100, 20))
        self.tgtBox.setFont(font2)

        self.lblselLayout.addWidget(self.tgtBox, 1, 0, 1, 1)

        self.juvBox = QComboBox(self.labelGroup)
        self.juvBox.addItem("")
        self.juvBox.addItem("")
        self.juvBox.addItem("")
        self.juvBox.addItem("")
        self.juvBox.setObjectName(u"juvBox")
        self.juvBox.setEnabled(False)
        self.juvBox.setMinimumSize(QSize(100, 20))
        self.juvBox.setMaximumSize(QSize(100, 20))
        self.juvBox.setFont(font2)

        self.lblselLayout.addWidget(self.juvBox, 1, 1, 1, 1)


        self.labelLayout.addLayout(self.lblselLayout)

        self.lblctrlLayout = QGridLayout()
        self.lblctrlLayout.setObjectName(u"lblctrlLayout")
        self.lblctrlLayout.setHorizontalSpacing(10)
        self.lblctrlLayout.setVerticalSpacing(2)
        self.lblctrlLayout.setContentsMargins(-1, 5, -1, -1)
        self.labelLine = QFrame(self.labelGroup)
        self.labelLine.setObjectName(u"labelLine")
        self.labelLine.setFrameShape(QFrame.Shape.HLine)
        self.labelLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.lblctrlLayout.addWidget(self.labelLine, 0, 0, 1, 2)

        self.hidButton = QPushButton(self.labelGroup)
        self.hidButton.setObjectName(u"hidButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hidButton.sizePolicy().hasHeightForWidth())
        self.hidButton.setSizePolicy(sizePolicy)
        self.hidButton.setMinimumSize(QSize(100, 23))
        self.hidButton.setMaximumSize(QSize(100, 23))
        self.hidButton.setFont(font2)

        self.lblctrlLayout.addWidget(self.hidButton, 1, 0, 1, 1)

        self.updButton = QPushButton(self.labelGroup)
        self.updButton.setObjectName(u"updButton")
        sizePolicy.setHeightForWidth(self.updButton.sizePolicy().hasHeightForWidth())
        self.updButton.setSizePolicy(sizePolicy)
        self.updButton.setMinimumSize(QSize(100, 23))
        self.updButton.setMaximumSize(QSize(100, 23))
        self.updButton.setFont(font2)

        self.lblctrlLayout.addWidget(self.updButton, 1, 1, 1, 1)


        self.labelLayout.addLayout(self.lblctrlLayout)


        self.featuresLayout.addWidget(self.labelGroup)


        self.settingsLayout.addLayout(self.featuresLayout)


        self.controlsLayout.addLayout(self.settingsLayout)

        self.nextButton = QPushButton(self.frmctrlWidget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setMinimumSize(QSize(0, 250))
        self.nextButton.setFont(font)

        self.controlsLayout.addWidget(self.nextButton)


        self.inputsLayout.addLayout(self.controlsLayout)

        self.progressBar = QProgressBar(self.frmctrlWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.inputsLayout.addWidget(self.progressBar)

        self.progctrlLayout = QHBoxLayout()
        self.progctrlLayout.setSpacing(10)
        self.progctrlLayout.setObjectName(u"progctrlLayout")
        self.startButton = QPushButton(self.frmctrlWidget)
        self.startButton.setObjectName(u"startButton")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.startButton.setFont(font3)

        self.progctrlLayout.addWidget(self.startButton)

        self.progctrltSpacer = QSpacerItem(40, 25, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.progctrlLayout.addItem(self.progctrltSpacer)

        self.exitButton = QPushButton(self.frmctrlWidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setFont(font3)

        self.progctrlLayout.addWidget(self.exitButton)


        self.inputsLayout.addLayout(self.progctrlLayout)


        self.mainLayout.addLayout(self.inputsLayout)

        self.frmoutBox = QGroupBox(self.frmctrlWidget)
        self.frmoutBox.setObjectName(u"frmoutBox")
        self.frmoutBox.setFont(font1)
        self.frmoutLayout = QVBoxLayout(self.frmoutBox)
        self.frmoutLayout.setSpacing(0)
        self.frmoutLayout.setObjectName(u"frmoutLayout")
        self.frmoutLayout.setContentsMargins(5, 5, 5, 5)
        self.frmoutTable = QTableWidget(self.frmoutBox)
        if (self.frmoutTable.columnCount() < 2):
            self.frmoutTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.frmoutTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.frmoutTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.frmoutTable.setObjectName(u"frmoutTable")
        self.frmoutTable.setEnabled(True)
        self.frmoutTable.setFont(font2)

        self.frmoutLayout.addWidget(self.frmoutTable)


        self.mainLayout.addWidget(self.frmoutBox)

        ControlViewer.setCentralWidget(self.frmctrlWidget)
        self.statusBar = QStatusBar(ControlViewer)
        self.statusBar.setObjectName(u"statusBar")
        ControlViewer.setStatusBar(self.statusBar)
        self.menuBar = QMenuBar(ControlViewer)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1060, 21))
        ControlViewer.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.frameSlider, self.sliderValue)
        QWidget.setTabOrder(self.sliderValue, self.brtSlider)
        QWidget.setTabOrder(self.brtSlider, self.brtValue)
        QWidget.setTabOrder(self.brtValue, self.conSlider)
        QWidget.setTabOrder(self.conSlider, self.conValue)
        QWidget.setTabOrder(self.conValue, self.totfrmBox)
        QWidget.setTabOrder(self.totfrmBox, self.cutaButton)
        QWidget.setTabOrder(self.cutaButton, self.cutbButton)
        QWidget.setTabOrder(self.cutbButton, self.mrkCheck)
        QWidget.setTabOrder(self.mrkCheck, self.mrkMode)
        QWidget.setTabOrder(self.mrkMode, self.sizeValue)
        QWidget.setTabOrder(self.sizeValue, self.xValue)
        QWidget.setTabOrder(self.xValue, self.yValue)
        QWidget.setTabOrder(self.yValue, self.objButton)
        QWidget.setTabOrder(self.objButton, self.juvButton)
        QWidget.setTabOrder(self.juvButton, self.tgtBox)
        QWidget.setTabOrder(self.tgtBox, self.juvBox)
        QWidget.setTabOrder(self.juvBox, self.hidButton)
        QWidget.setTabOrder(self.hidButton, self.updButton)
        QWidget.setTabOrder(self.updButton, self.startButton)
        QWidget.setTabOrder(self.startButton, self.exitButton)
        QWidget.setTabOrder(self.exitButton, self.prevButton)
        QWidget.setTabOrder(self.prevButton, self.nextButton)
        QWidget.setTabOrder(self.nextButton, self.frmoutTable)

        self.retranslateUi(ControlViewer)
        self.frameSlider.valueChanged.connect(self.sliderValue.setValue)
        self.sliderValue.valueChanged.connect(self.frameSlider.setValue)
        self.prevButton.clicked.connect(self.sliderValue.stepDown)
        self.nextButton.clicked.connect(self.sliderValue.stepUp)
        self.brtSlider.valueChanged.connect(self.brtValue.setValue)
        self.brtValue.valueChanged.connect(self.brtSlider.setValue)
        self.conSlider.valueChanged.connect(self.conValue.setValue)
        self.conValue.valueChanged.connect(self.conSlider.setValue)
        self.juvButton.toggled.connect(self.juvBox.setEnabled)
        self.juvButton.toggled.connect(self.juvLabel.setEnabled)
        self.mrkCheck.clicked["bool"].connect(self.colourLabel.setEnabled)
        self.mrkCheck.clicked["bool"].connect(self.mrkMode.setEnabled)
        self.mrkCheck.clicked["bool"].connect(self.sizeLabel.setEnabled)
        self.mrkCheck.clicked["bool"].connect(self.sizeValue.setEnabled)
        self.mrkCheck.clicked["bool"].connect(self.xLabel.setEnabled)
        self.mrkCheck.clicked["bool"].connect(self.xValue.setEnabled)
        self.mrkCheck.clicked["bool"].connect(self.yLabel.setEnabled)
        self.mrkCheck.clicked["bool"].connect(self.yValue.setEnabled)

        self.mrkMode.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(ControlViewer)


    def retranslateUi(self, ControlViewer):
        ControlViewer.setWindowTitle(QCoreApplication.translate("ControlViewer", u"MEGIT Pre-Processing Control", None))
        self.prevButton.setText(QCoreApplication.translate("ControlViewer", u"\u25c0", None))
        self.imgadjBox.setTitle(QCoreApplication.translate("ControlViewer", u"Image Adjustments", None))
        self.brtLabel.setText(QCoreApplication.translate("ControlViewer", u"Brightness", None))
        self.conLabel.setText(QCoreApplication.translate("ControlViewer", u"Contrast", None))
        self.frameGroup.setTitle(QCoreApplication.translate("ControlViewer", u"Frame Setup", None))
        self.totfrmLabel.setText(QCoreApplication.translate("ControlViewer", u"Total Frames", None))
        self.cutfrmBox.setTitle(QCoreApplication.translate("ControlViewer", u"Cut-out Frames", None))
        self.cutaButton.setText(QCoreApplication.translate("ControlViewer", u"Set A", None))
        self.cutbButton.setText(QCoreApplication.translate("ControlViewer", u"Set B", None))
        self.frmmrkBox.setTitle(QCoreApplication.translate("ControlViewer", u"Frame Marking", None))
        self.mrkCheck.setText(QCoreApplication.translate("ControlViewer", u"Enable Marking", None))
        self.colourLabel.setText(QCoreApplication.translate("ControlViewer", u"Mark Style", None))
        self.sizeLabel.setText(QCoreApplication.translate("ControlViewer", u"Text Size", None))
        self.mrkMode.setItemText(0, QCoreApplication.translate("ControlViewer", u"Black", None))
        self.mrkMode.setItemText(1, QCoreApplication.translate("ControlViewer", u"White", None))
        self.mrkMode.setItemText(2, QCoreApplication.translate("ControlViewer", u"Black on White", None))
        self.mrkMode.setItemText(3, QCoreApplication.translate("ControlViewer", u"White on Black", None))

        self.xLabel.setText(QCoreApplication.translate("ControlViewer", u"X Value", None))
        self.yLabel.setText(QCoreApplication.translate("ControlViewer", u"Y Value", None))
        self.labelGroup.setTitle(QCoreApplication.translate("ControlViewer", u"Label", None))
        self.expLabel.setText(QCoreApplication.translate("ControlViewer", u"Experiment Type", None))
        self.objButton.setText(QCoreApplication.translate("ControlViewer", u"Object", None))
        self.juvButton.setText(QCoreApplication.translate("ControlViewer", u"Juvenile", None))
        self.tgtLabel.setText(QCoreApplication.translate("ControlViewer", u"Test Regions", None))
        self.juvLabel.setText(QCoreApplication.translate("ControlViewer", u"Juvenile Regions", None))
        self.tgtBox.setItemText(0, QCoreApplication.translate("ControlViewer", u"[NONE]", None))
        self.tgtBox.setItemText(1, QCoreApplication.translate("ControlViewer", u"Gap", None))
        self.tgtBox.setItemText(2, QCoreApplication.translate("ControlViewer", u"Top", None))
        self.tgtBox.setItemText(3, QCoreApplication.translate("ControlViewer", u"Bottom", None))
        self.tgtBox.setItemText(4, QCoreApplication.translate("ControlViewer", u"Wall", None))

        self.juvBox.setItemText(0, QCoreApplication.translate("ControlViewer", u"[NONE]", None))
        self.juvBox.setItemText(1, QCoreApplication.translate("ControlViewer", u"Gap", None))
        self.juvBox.setItemText(2, QCoreApplication.translate("ControlViewer", u"Top", None))
        self.juvBox.setItemText(3, QCoreApplication.translate("ControlViewer", u"Bottom", None))

        self.hidButton.setText(QCoreApplication.translate("ControlViewer", u"Hide", None))
        self.updButton.setText(QCoreApplication.translate("ControlViewer", u"Update", None))
        self.nextButton.setText(QCoreApplication.translate("ControlViewer", u"\u25b6", None))
        self.startButton.setText(QCoreApplication.translate("ControlViewer", u"Start", None))
        self.exitButton.setText(QCoreApplication.translate("ControlViewer", u"Exit", None))
        self.frmoutBox.setTitle(QCoreApplication.translate("ControlViewer", u"Removed Frames", None))
        ___qtablewidgetitem = self.frmoutTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ControlViewer", u"From", None))
        ___qtablewidgetitem1 = self.frmoutTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ControlViewer", u"To", None))
