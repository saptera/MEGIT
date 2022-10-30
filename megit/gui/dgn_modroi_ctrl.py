# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\megit\gui\dgn_modroi_ctrl.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ControlViewer(object):
    def setupUi(self, ControlViewer):
        ControlViewer.setObjectName("ControlViewer")
        ControlViewer.resize(428, 328)
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
        self.prevButton.setMinimumSize(QtCore.QSize(0, 205))
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
        self.modmodeBox = QtWidgets.QGroupBox(self.frmctrlWidget)
        self.modmodeBox.setMinimumSize(QtCore.QSize(250, 45))
        self.modmodeBox.setMaximumSize(QtCore.QSize(250, 45))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.modmodeBox.setFont(font)
        self.modmodeBox.setObjectName("modmodeBox")
        self.modmodeLayout = QtWidgets.QHBoxLayout(self.modmodeBox)
        self.modmodeLayout.setContentsMargins(18, 5, 18, 5)
        self.modmodeLayout.setSpacing(5)
        self.modmodeLayout.setObjectName("modmodeLayout")
        self.fullmodeButton = QtWidgets.QRadioButton(self.modmodeBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.fullmodeButton.setFont(font)
        self.fullmodeButton.setChecked(False)
        self.fullmodeButton.setObjectName("fullmodeButton")
        self.rangeGroup = QtWidgets.QButtonGroup(ControlViewer)
        self.rangeGroup.setObjectName("rangeGroup")
        self.rangeGroup.addButton(self.fullmodeButton)
        self.modmodeLayout.addWidget(self.fullmodeButton)
        self.selcmodeButton = QtWidgets.QRadioButton(self.modmodeBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.selcmodeButton.setFont(font)
        self.selcmodeButton.setChecked(True)
        self.selcmodeButton.setObjectName("selcmodeButton")
        self.rangeGroup.addButton(self.selcmodeButton)
        self.modmodeLayout.addWidget(self.selcmodeButton)
        self.settingsLayout.addWidget(self.modmodeBox)
        self.featuresLayout = QtWidgets.QHBoxLayout()
        self.featuresLayout.setSpacing(10)
        self.featuresLayout.setObjectName("featuresLayout")
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
        self.aniLabel = QtWidgets.QLabel(self.labelGroup)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.aniLabel.setFont(font)
        self.aniLabel.setObjectName("aniLabel")
        self.modeLayout.addWidget(self.aniLabel, 0, 0, 1, 1)
        self.tgtButton = QtWidgets.QRadioButton(self.labelGroup)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tgtButton.setFont(font)
        self.tgtButton.setChecked(True)
        self.tgtButton.setObjectName("tgtButton")
        self.modeGroup = QtWidgets.QButtonGroup(ControlViewer)
        self.modeGroup.setObjectName("modeGroup")
        self.modeGroup.addButton(self.tgtButton)
        self.modeLayout.addWidget(self.tgtButton, 1, 0, 1, 1)
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
        self.updButton.setEnabled(False)
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
        self.nextButton.setMinimumSize(QtCore.QSize(0, 205))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")
        self.controlsLayout.addWidget(self.nextButton)
        self.inputsLayout.addLayout(self.controlsLayout)
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
        ControlViewer.setCentralWidget(self.frmctrlWidget)
        self.statusBar = QtWidgets.QStatusBar(ControlViewer)
        self.statusBar.setObjectName("statusBar")
        ControlViewer.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(ControlViewer)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 428, 21))
        self.menuBar.setObjectName("menuBar")
        ControlViewer.setMenuBar(self.menuBar)

        self.retranslateUi(ControlViewer)
        self.frameSlider.valueChanged['int'].connect(self.sliderValue.setValue)
        self.sliderValue.valueChanged['int'].connect(self.frameSlider.setValue)
        self.prevButton.clicked.connect(self.sliderValue.stepDown)
        self.nextButton.clicked.connect(self.sliderValue.stepUp)
        self.juvButton.toggled['bool'].connect(self.juvBox.setEnabled)
        self.juvButton.toggled['bool'].connect(self.juvLabel.setEnabled)
        self.tgtButton.toggled['bool'].connect(self.tgtLabel.setEnabled)
        self.tgtButton.toggled['bool'].connect(self.tgtBox.setEnabled)
        self.fullmodeButton.toggled['bool'].connect(self.updButton.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ControlViewer)
        ControlViewer.setTabOrder(self.frameSlider, self.sliderValue)
        ControlViewer.setTabOrder(self.sliderValue, self.tgtButton)
        ControlViewer.setTabOrder(self.tgtButton, self.juvButton)
        ControlViewer.setTabOrder(self.juvButton, self.tgtBox)
        ControlViewer.setTabOrder(self.tgtBox, self.juvBox)
        ControlViewer.setTabOrder(self.juvBox, self.hidButton)
        ControlViewer.setTabOrder(self.hidButton, self.updButton)
        ControlViewer.setTabOrder(self.updButton, self.startButton)
        ControlViewer.setTabOrder(self.startButton, self.exitButton)
        ControlViewer.setTabOrder(self.exitButton, self.prevButton)
        ControlViewer.setTabOrder(self.prevButton, self.nextButton)

    def retranslateUi(self, ControlViewer):
        _translate = QtCore.QCoreApplication.translate
        ControlViewer.setWindowTitle(_translate("ControlViewer", "MEGIT Pre-Processing Control"))
        self.prevButton.setText(_translate("ControlViewer", "◀"))
        self.modmodeBox.setTitle(_translate("ControlViewer", "Modification Mode"))
        self.fullmodeButton.setText(_translate("ControlViewer", "Full-Frame"))
        self.selcmodeButton.setText(_translate("ControlViewer", "Pre-Defined"))
        self.labelGroup.setTitle(_translate("ControlViewer", "Label"))
        self.aniLabel.setText(_translate("ControlViewer", "Animal Type"))
        self.tgtButton.setText(_translate("ControlViewer", "Test"))
        self.juvButton.setText(_translate("ControlViewer", "Juvenile"))
        self.tgtLabel.setText(_translate("ControlViewer", "Test Regions"))
        self.juvLabel.setText(_translate("ControlViewer", "Juvenile Regions"))
        self.tgtBox.setItemText(0, _translate("ControlViewer", "[NONE]"))
        self.tgtBox.setItemText(1, _translate("ControlViewer", "Gap"))
        self.tgtBox.setItemText(2, _translate("ControlViewer", "Top"))
        self.tgtBox.setItemText(3, _translate("ControlViewer", "Bottom"))
        self.tgtBox.setItemText(4, _translate("ControlViewer", "Wall"))
        self.juvBox.setItemText(0, _translate("ControlViewer", "[NONE]"))
        self.juvBox.setItemText(1, _translate("ControlViewer", "Gap"))
        self.juvBox.setItemText(2, _translate("ControlViewer", "Top"))
        self.juvBox.setItemText(3, _translate("ControlViewer", "Bottom"))
        self.hidButton.setText(_translate("ControlViewer", "Hide"))
        self.updButton.setText(_translate("ControlViewer", "Update"))
        self.nextButton.setText(_translate("ControlViewer", "▶"))
        self.startButton.setText(_translate("ControlViewer", "Start"))
        self.exitButton.setText(_translate("ControlViewer", "Exit"))
