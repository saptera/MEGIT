# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dgn_preprocz_ctrl.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QCheckBox, QComboBox, QDoubleSpinBox, QGridLayout, QGroupBox, QHBoxLayout, QLabel,
                               QMenuBar, QProgressBar, QPushButton, QSizePolicy, QSlider, QSpacerItem, QSpinBox,
                               QStatusBar, QVBoxLayout, QWidget)


class Ui_ControlViewer(object):
    def setupUi(self, ControlViewer):
        if not ControlViewer.objectName():
            ControlViewer.setObjectName(u"ControlViewer")
        ControlViewer.resize(530, 410)
        ControlViewer.setMinimumSize(QSize(530, 410))
        ControlViewer.setMaximumSize(QSize(530, 410))
        self.frmctrlWidget = QWidget(ControlViewer)
        self.frmctrlWidget.setObjectName(u"frmctrlWidget")
        self.mainLayout = QVBoxLayout(self.frmctrlWidget)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(5, 5, 5, 5)
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


        self.mainLayout.addLayout(self.frmsldrLayout)

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
        self.frmmrkBox = QGroupBox(self.frmctrlWidget)
        self.frmmrkBox.setObjectName(u"frmmrkBox")
        self.frmmrkBox.setMinimumSize(QSize(230, 135))
        self.frmmrkBox.setMaximumSize(QSize(230, 135))
        self.frmmrkBox.setFont(font1)
        self.frmmrkLayout = QVBoxLayout(self.frmmrkBox)
        self.frmmrkLayout.setSpacing(6)
        self.frmmrkLayout.setObjectName(u"frmmrkLayout")
        self.frmmrkLayout.setContentsMargins(6, 6, 6, 6)
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

        self.frmflpBox = QGroupBox(self.frmctrlWidget)
        self.frmflpBox.setObjectName(u"frmflpBox")
        self.frmflpBox.setMinimumSize(QSize(110, 135))
        self.frmflpBox.setMaximumSize(QSize(110, 135))
        self.frmflpBox.setFont(font1)
        self.frmflpLayout = QVBoxLayout(self.frmflpBox)
        self.frmflpLayout.setSpacing(10)
        self.frmflpLayout.setObjectName(u"frmflpLayout")
        self.frmflpLayout.setContentsMargins(6, 6, 6, 6)
        self.hflpBox = QCheckBox(self.frmflpBox)
        self.hflpBox.setObjectName(u"hflpBox")
        self.hflpBox.setFont(font2)

        self.frmflpLayout.addWidget(self.hflpBox)

        self.vflpBox = QCheckBox(self.frmflpBox)
        self.vflpBox.setObjectName(u"vflpBox")
        self.vflpBox.setFont(font2)

        self.frmflpLayout.addWidget(self.vflpBox)


        self.featuresLayout.addWidget(self.frmflpBox)


        self.settingsLayout.addLayout(self.featuresLayout)


        self.controlsLayout.addLayout(self.settingsLayout)

        self.nextButton = QPushButton(self.frmctrlWidget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setMinimumSize(QSize(0, 250))
        self.nextButton.setFont(font)

        self.controlsLayout.addWidget(self.nextButton)


        self.mainLayout.addLayout(self.controlsLayout)

        self.progressBar = QProgressBar(self.frmctrlWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.mainLayout.addWidget(self.progressBar)

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


        self.mainLayout.addLayout(self.progctrlLayout)

        ControlViewer.setCentralWidget(self.frmctrlWidget)
        self.statusBar = QStatusBar(ControlViewer)
        self.statusBar.setObjectName(u"statusBar")
        ControlViewer.setStatusBar(self.statusBar)
        self.menuBar = QMenuBar(ControlViewer)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 530, 21))
        ControlViewer.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.frameSlider, self.sliderValue)
        QWidget.setTabOrder(self.sliderValue, self.brtSlider)
        QWidget.setTabOrder(self.brtSlider, self.brtValue)
        QWidget.setTabOrder(self.brtValue, self.conSlider)
        QWidget.setTabOrder(self.conSlider, self.conValue)
        QWidget.setTabOrder(self.conValue, self.mrkCheck)
        QWidget.setTabOrder(self.mrkCheck, self.mrkMode)
        QWidget.setTabOrder(self.mrkMode, self.sizeValue)
        QWidget.setTabOrder(self.sizeValue, self.xValue)
        QWidget.setTabOrder(self.xValue, self.yValue)
        QWidget.setTabOrder(self.yValue, self.startButton)
        QWidget.setTabOrder(self.startButton, self.exitButton)
        QWidget.setTabOrder(self.exitButton, self.prevButton)
        QWidget.setTabOrder(self.prevButton, self.nextButton)

        self.retranslateUi(ControlViewer)
        self.frameSlider.valueChanged.connect(self.sliderValue.setValue)
        self.sliderValue.valueChanged.connect(self.frameSlider.setValue)
        self.prevButton.clicked.connect(self.sliderValue.stepDown)
        self.nextButton.clicked.connect(self.sliderValue.stepUp)
        self.brtSlider.valueChanged.connect(self.brtValue.setValue)
        self.brtValue.valueChanged.connect(self.brtSlider.setValue)
        self.conSlider.valueChanged.connect(self.conValue.setValue)
        self.conValue.valueChanged.connect(self.conSlider.setValue)
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
        self.frmflpBox.setTitle(QCoreApplication.translate("ControlViewer", u"Frame Flipping", None))
        self.hflpBox.setText(QCoreApplication.translate("ControlViewer", u"Horizontal", None))
        self.vflpBox.setText(QCoreApplication.translate("ControlViewer", u"Vertical", None))
        self.nextButton.setText(QCoreApplication.translate("ControlViewer", u"\u25b6", None))
        self.startButton.setText(QCoreApplication.translate("ControlViewer", u"Start", None))
        self.exitButton.setText(QCoreApplication.translate("ControlViewer", u"Exit", None))
