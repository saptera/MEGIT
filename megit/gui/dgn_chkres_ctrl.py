# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dgn_chkres_ctrl.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QCheckBox, QComboBox, QDoubleSpinBox, QFormLayout, QFrame, QGraphicsView, QGridLayout,
                               QGroupBox, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSlider, QSpacerItem, QSpinBox,
                               QStatusBar, QVBoxLayout, QWidget)


class Ui_CrossVerifier(object):
    def setupUi(self, CrossVerifier):
        if not CrossVerifier.objectName():
            CrossVerifier.setObjectName(u"CrossVerifier")
        CrossVerifier.resize(1202, 756)
        CrossVerifier.setMinimumSize(QSize(1202, 756))
        CrossVerifier.setMaximumSize(QSize(1202, 756))
        self.centralWidget = QWidget(CrossVerifier)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralLayout = QVBoxLayout(self.centralWidget)
        self.centralLayout.setSpacing(10)
        self.centralLayout.setObjectName(u"centralLayout")
        self.frameLayout = QHBoxLayout()
        self.frameLayout.setSpacing(10)
        self.frameLayout.setObjectName(u"frameLayout")
        self.frameDisplay = QGraphicsView(self.centralWidget)
        self.frameDisplay.setObjectName(u"frameDisplay")
        self.frameDisplay.setMinimumSize(QSize(630, 630))
        self.frameDisplay.setMaximumSize(QSize(630, 630))
        self.frameDisplay.setFocusPolicy(Qt.NoFocus)

        self.frameLayout.addWidget(self.frameDisplay)

        self.setupLayout = QVBoxLayout()
        self.setupLayout.setSpacing(10)
        self.setupLayout.setObjectName(u"setupLayout")
        self.mrkFrame = QFrame(self.centralWidget)
        self.mrkFrame.setObjectName(u"mrkFrame")
        self.mrkFrame.setMinimumSize(QSize(540, 530))
        self.mrkFrame.setMaximumSize(QSize(540, 530))
        self.mrkFrame.setFocusPolicy(Qt.NoFocus)
        self.mrkFrame.setFrameShape(QFrame.Box)
        self.mrkFrame.setFrameShadow(QFrame.Sunken)
        self.mrkLayout = QVBoxLayout(self.mrkFrame)
        self.mrkLayout.setObjectName(u"mrkLayout")
        self.mrkLayout.setContentsMargins(-1, -1, -1, 0)
        self.manModeFrame = QFrame(self.mrkFrame)
        self.manModeFrame.setObjectName(u"manModeFrame")
        self.manModeFrame.setMinimumSize(QSize(518, 450))
        self.manModeFrame.setMaximumSize(QSize(518, 450))
        self.manModeFrame.setFocusPolicy(Qt.NoFocus)
        self.manModeFrame.setFrameShape(QFrame.StyledPanel)
        self.manModeFrame.setFrameShadow(QFrame.Raised)
        self.manModeLayout = QGridLayout(self.manModeFrame)
        self.manModeLayout.setObjectName(u"manModeLayout")
        self.manModeLayout.setContentsMargins(0, 0, 0, 0)
        self.btmRgn = QGroupBox(self.manModeFrame)
        self.btmRgn.setObjectName(u"btmRgn")
        self.btmRgn.setMinimumSize(QSize(246, 213))
        self.btmRgn.setMaximumSize(QSize(246, 213))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btmRgn.setFont(font)
        self.btmRgn.setFocusPolicy(Qt.NoFocus)
        self.btmRgnLayout = QVBoxLayout(self.btmRgn)
        self.btmRgnLayout.setObjectName(u"btmRgnLayout")
        self.btmMrkSgn = QGroupBox(self.btmRgn)
        self.btmMrkSgn.setObjectName(u"btmMrkSgn")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.btmMrkSgn.setFont(font1)
        self.btmMrkSgn.setFocusPolicy(Qt.NoFocus)
        self.btmMrkSgnLayout = QHBoxLayout(self.btmMrkSgn)
        self.btmMrkSgnLayout.setObjectName(u"btmMrkSgnLayout")
        self.btmBtnSgnT = QPushButton(self.btmMrkSgn)
        self.btmBtnSgnT.setObjectName(u"btmBtnSgnT")
        self.btmBtnSgnT.setMinimumSize(QSize(100, 25))
        self.btmBtnSgnT.setMaximumSize(QSize(100, 25))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.btmBtnSgnT.setFont(font2)
        self.btmBtnSgnT.setFocusPolicy(Qt.NoFocus)

        self.btmMrkSgnLayout.addWidget(self.btmBtnSgnT)

        self.btmBtnSgnF = QPushButton(self.btmMrkSgn)
        self.btmBtnSgnF.setObjectName(u"btmBtnSgnF")
        self.btmBtnSgnF.setMinimumSize(QSize(100, 25))
        self.btmBtnSgnF.setMaximumSize(QSize(100, 25))
        self.btmBtnSgnF.setFont(font2)
        self.btmBtnSgnF.setFocusPolicy(Qt.NoFocus)

        self.btmMrkSgnLayout.addWidget(self.btmBtnSgnF)


        self.btmRgnLayout.addWidget(self.btmMrkSgn)

        self.btmMrkRng = QGroupBox(self.btmRgn)
        self.btmMrkRng.setObjectName(u"btmMrkRng")
        self.btmMrkRng.setFont(font1)
        self.btmMrkRng.setFocusPolicy(Qt.NoFocus)
        self.btmMrkRgnLayout = QFormLayout(self.btmMrkRng)
        self.btmMrkRgnLayout.setObjectName(u"btmMrkRgnLayout")
        self.btmBtnRgnTS = QPushButton(self.btmMrkRng)
        self.btmBtnRgnTS.setObjectName(u"btmBtnRgnTS")
        self.btmBtnRgnTS.setMinimumSize(QSize(100, 25))
        self.btmBtnRgnTS.setMaximumSize(QSize(100, 25))
        self.btmBtnRgnTS.setFont(font2)
        self.btmBtnRgnTS.setFocusPolicy(Qt.NoFocus)
        self.btmBtnRgnTS.setCheckable(True)

        self.btmMrkRgnLayout.setWidget(0, QFormLayout.LabelRole, self.btmBtnRgnTS)

        self.btmBtnRgnTE = QPushButton(self.btmMrkRng)
        self.btmBtnRgnTE.setObjectName(u"btmBtnRgnTE")
        self.btmBtnRgnTE.setEnabled(False)
        self.btmBtnRgnTE.setMinimumSize(QSize(100, 25))
        self.btmBtnRgnTE.setMaximumSize(QSize(100, 25))
        self.btmBtnRgnTE.setFont(font2)
        self.btmBtnRgnTE.setFocusPolicy(Qt.NoFocus)

        self.btmMrkRgnLayout.setWidget(0, QFormLayout.FieldRole, self.btmBtnRgnTE)

        self.btmRgnLine = QFrame(self.btmMrkRng)
        self.btmRgnLine.setObjectName(u"btmRgnLine")
        self.btmRgnLine.setFocusPolicy(Qt.NoFocus)
        self.btmRgnLine.setFrameShape(QFrame.Shape.HLine)
        self.btmRgnLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.btmMrkRgnLayout.setWidget(1, QFormLayout.SpanningRole, self.btmRgnLine)

        self.btmBtnRgnFS = QPushButton(self.btmMrkRng)
        self.btmBtnRgnFS.setObjectName(u"btmBtnRgnFS")
        self.btmBtnRgnFS.setMinimumSize(QSize(100, 25))
        self.btmBtnRgnFS.setMaximumSize(QSize(100, 25))
        self.btmBtnRgnFS.setFont(font2)
        self.btmBtnRgnFS.setFocusPolicy(Qt.NoFocus)
        self.btmBtnRgnFS.setCheckable(True)

        self.btmMrkRgnLayout.setWidget(2, QFormLayout.LabelRole, self.btmBtnRgnFS)

        self.btmBtnRgnFE = QPushButton(self.btmMrkRng)
        self.btmBtnRgnFE.setObjectName(u"btmBtnRgnFE")
        self.btmBtnRgnFE.setEnabled(False)
        self.btmBtnRgnFE.setMinimumSize(QSize(100, 25))
        self.btmBtnRgnFE.setMaximumSize(QSize(100, 25))
        self.btmBtnRgnFE.setFont(font2)
        self.btmBtnRgnFE.setFocusPolicy(Qt.NoFocus)

        self.btmMrkRgnLayout.setWidget(2, QFormLayout.FieldRole, self.btmBtnRgnFE)


        self.btmRgnLayout.addWidget(self.btmMrkRng)


        self.manModeLayout.addWidget(self.btmRgn, 2, 1, 1, 1)

        self.gapRgn = QGroupBox(self.manModeFrame)
        self.gapRgn.setObjectName(u"gapRgn")
        self.gapRgn.setMinimumSize(QSize(246, 213))
        self.gapRgn.setMaximumSize(QSize(246, 213))
        self.gapRgn.setFont(font)
        self.gapRgn.setFocusPolicy(Qt.NoFocus)
        self.gapRgnLayout = QVBoxLayout(self.gapRgn)
        self.gapRgnLayout.setObjectName(u"gapRgnLayout")
        self.gapMrkSgn = QGroupBox(self.gapRgn)
        self.gapMrkSgn.setObjectName(u"gapMrkSgn")
        self.gapMrkSgn.setFont(font1)
        self.gapMrkSgn.setFocusPolicy(Qt.NoFocus)
        self.gapMrkSgnLayout = QHBoxLayout(self.gapMrkSgn)
        self.gapMrkSgnLayout.setObjectName(u"gapMrkSgnLayout")
        self.gapBtnSgnT = QPushButton(self.gapMrkSgn)
        self.gapBtnSgnT.setObjectName(u"gapBtnSgnT")
        self.gapBtnSgnT.setMinimumSize(QSize(100, 25))
        self.gapBtnSgnT.setMaximumSize(QSize(100, 25))
        self.gapBtnSgnT.setFont(font2)
        self.gapBtnSgnT.setFocusPolicy(Qt.NoFocus)

        self.gapMrkSgnLayout.addWidget(self.gapBtnSgnT)

        self.gapBtnSgnF = QPushButton(self.gapMrkSgn)
        self.gapBtnSgnF.setObjectName(u"gapBtnSgnF")
        self.gapBtnSgnF.setMinimumSize(QSize(100, 25))
        self.gapBtnSgnF.setMaximumSize(QSize(100, 25))
        self.gapBtnSgnF.setFont(font2)
        self.gapBtnSgnF.setFocusPolicy(Qt.NoFocus)

        self.gapMrkSgnLayout.addWidget(self.gapBtnSgnF)


        self.gapRgnLayout.addWidget(self.gapMrkSgn)

        self.gapMrkRng = QGroupBox(self.gapRgn)
        self.gapMrkRng.setObjectName(u"gapMrkRng")
        self.gapMrkRng.setFont(font1)
        self.gapMrkRng.setFocusPolicy(Qt.NoFocus)
        self.gapMrkRgnLayout = QFormLayout(self.gapMrkRng)
        self.gapMrkRgnLayout.setObjectName(u"gapMrkRgnLayout")
        self.gapBtnRgnTS = QPushButton(self.gapMrkRng)
        self.gapBtnRgnTS.setObjectName(u"gapBtnRgnTS")
        self.gapBtnRgnTS.setMinimumSize(QSize(100, 25))
        self.gapBtnRgnTS.setMaximumSize(QSize(100, 25))
        self.gapBtnRgnTS.setFont(font2)
        self.gapBtnRgnTS.setFocusPolicy(Qt.NoFocus)
        self.gapBtnRgnTS.setCheckable(True)

        self.gapMrkRgnLayout.setWidget(0, QFormLayout.LabelRole, self.gapBtnRgnTS)

        self.gapBtnRgnTE = QPushButton(self.gapMrkRng)
        self.gapBtnRgnTE.setObjectName(u"gapBtnRgnTE")
        self.gapBtnRgnTE.setEnabled(False)
        self.gapBtnRgnTE.setMinimumSize(QSize(100, 25))
        self.gapBtnRgnTE.setMaximumSize(QSize(100, 25))
        self.gapBtnRgnTE.setFont(font2)
        self.gapBtnRgnTE.setFocusPolicy(Qt.NoFocus)

        self.gapMrkRgnLayout.setWidget(0, QFormLayout.FieldRole, self.gapBtnRgnTE)

        self.gapRgnLine = QFrame(self.gapMrkRng)
        self.gapRgnLine.setObjectName(u"gapRgnLine")
        self.gapRgnLine.setFocusPolicy(Qt.NoFocus)
        self.gapRgnLine.setFrameShape(QFrame.Shape.HLine)
        self.gapRgnLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.gapMrkRgnLayout.setWidget(1, QFormLayout.SpanningRole, self.gapRgnLine)

        self.gapBtnRgnFS = QPushButton(self.gapMrkRng)
        self.gapBtnRgnFS.setObjectName(u"gapBtnRgnFS")
        self.gapBtnRgnFS.setMinimumSize(QSize(100, 25))
        self.gapBtnRgnFS.setMaximumSize(QSize(100, 25))
        self.gapBtnRgnFS.setFont(font2)
        self.gapBtnRgnFS.setFocusPolicy(Qt.NoFocus)
        self.gapBtnRgnFS.setCheckable(True)

        self.gapMrkRgnLayout.setWidget(2, QFormLayout.LabelRole, self.gapBtnRgnFS)

        self.gapBtnRgnFE = QPushButton(self.gapMrkRng)
        self.gapBtnRgnFE.setObjectName(u"gapBtnRgnFE")
        self.gapBtnRgnFE.setEnabled(False)
        self.gapBtnRgnFE.setMinimumSize(QSize(100, 25))
        self.gapBtnRgnFE.setMaximumSize(QSize(100, 25))
        self.gapBtnRgnFE.setFont(font2)
        self.gapBtnRgnFE.setFocusPolicy(Qt.NoFocus)

        self.gapMrkRgnLayout.setWidget(2, QFormLayout.FieldRole, self.gapBtnRgnFE)


        self.gapRgnLayout.addWidget(self.gapMrkRng)


        self.manModeLayout.addWidget(self.gapRgn, 0, 0, 3, 1)

        self.topRgn = QGroupBox(self.manModeFrame)
        self.topRgn.setObjectName(u"topRgn")
        self.topRgn.setMinimumSize(QSize(246, 213))
        self.topRgn.setMaximumSize(QSize(246, 213))
        self.topRgn.setFont(font)
        self.topRgn.setFocusPolicy(Qt.NoFocus)
        self.topRgnLayout = QVBoxLayout(self.topRgn)
        self.topRgnLayout.setObjectName(u"topRgnLayout")
        self.topMrkSgn = QGroupBox(self.topRgn)
        self.topMrkSgn.setObjectName(u"topMrkSgn")
        self.topMrkSgn.setFont(font1)
        self.topMrkSgn.setFocusPolicy(Qt.NoFocus)
        self.topMrkSgnLayout = QHBoxLayout(self.topMrkSgn)
        self.topMrkSgnLayout.setObjectName(u"topMrkSgnLayout")
        self.topBtnSgnT = QPushButton(self.topMrkSgn)
        self.topBtnSgnT.setObjectName(u"topBtnSgnT")
        self.topBtnSgnT.setMinimumSize(QSize(100, 25))
        self.topBtnSgnT.setMaximumSize(QSize(100, 25))
        self.topBtnSgnT.setFont(font2)
        self.topBtnSgnT.setFocusPolicy(Qt.NoFocus)

        self.topMrkSgnLayout.addWidget(self.topBtnSgnT)

        self.topBtnSgnF = QPushButton(self.topMrkSgn)
        self.topBtnSgnF.setObjectName(u"topBtnSgnF")
        self.topBtnSgnF.setMinimumSize(QSize(100, 25))
        self.topBtnSgnF.setMaximumSize(QSize(100, 25))
        self.topBtnSgnF.setFont(font2)
        self.topBtnSgnF.setFocusPolicy(Qt.NoFocus)

        self.topMrkSgnLayout.addWidget(self.topBtnSgnF)


        self.topRgnLayout.addWidget(self.topMrkSgn)

        self.topMrkRng = QGroupBox(self.topRgn)
        self.topMrkRng.setObjectName(u"topMrkRng")
        self.topMrkRng.setFont(font1)
        self.topMrkRng.setFocusPolicy(Qt.NoFocus)
        self.topMrkRgnLayout = QFormLayout(self.topMrkRng)
        self.topMrkRgnLayout.setObjectName(u"topMrkRgnLayout")
        self.topBtnRgnTS = QPushButton(self.topMrkRng)
        self.topBtnRgnTS.setObjectName(u"topBtnRgnTS")
        self.topBtnRgnTS.setMinimumSize(QSize(100, 25))
        self.topBtnRgnTS.setMaximumSize(QSize(100, 25))
        self.topBtnRgnTS.setFont(font2)
        self.topBtnRgnTS.setFocusPolicy(Qt.NoFocus)
        self.topBtnRgnTS.setCheckable(True)

        self.topMrkRgnLayout.setWidget(0, QFormLayout.LabelRole, self.topBtnRgnTS)

        self.topBtnRgnTE = QPushButton(self.topMrkRng)
        self.topBtnRgnTE.setObjectName(u"topBtnRgnTE")
        self.topBtnRgnTE.setEnabled(False)
        self.topBtnRgnTE.setMinimumSize(QSize(100, 25))
        self.topBtnRgnTE.setMaximumSize(QSize(100, 25))
        self.topBtnRgnTE.setFont(font2)
        self.topBtnRgnTE.setFocusPolicy(Qt.NoFocus)

        self.topMrkRgnLayout.setWidget(0, QFormLayout.FieldRole, self.topBtnRgnTE)

        self.topRgnLine = QFrame(self.topMrkRng)
        self.topRgnLine.setObjectName(u"topRgnLine")
        self.topRgnLine.setFocusPolicy(Qt.NoFocus)
        self.topRgnLine.setFrameShape(QFrame.Shape.HLine)
        self.topRgnLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.topMrkRgnLayout.setWidget(1, QFormLayout.SpanningRole, self.topRgnLine)

        self.topBtnRgnFS = QPushButton(self.topMrkRng)
        self.topBtnRgnFS.setObjectName(u"topBtnRgnFS")
        self.topBtnRgnFS.setMinimumSize(QSize(100, 25))
        self.topBtnRgnFS.setMaximumSize(QSize(100, 25))
        self.topBtnRgnFS.setFont(font2)
        self.topBtnRgnFS.setFocusPolicy(Qt.NoFocus)
        self.topBtnRgnFS.setCheckable(True)

        self.topMrkRgnLayout.setWidget(2, QFormLayout.LabelRole, self.topBtnRgnFS)

        self.topBtnRgnFE = QPushButton(self.topMrkRng)
        self.topBtnRgnFE.setObjectName(u"topBtnRgnFE")
        self.topBtnRgnFE.setEnabled(False)
        self.topBtnRgnFE.setMinimumSize(QSize(100, 25))
        self.topBtnRgnFE.setMaximumSize(QSize(100, 25))
        self.topBtnRgnFE.setFont(font2)
        self.topBtnRgnFE.setFocusPolicy(Qt.NoFocus)

        self.topMrkRgnLayout.setWidget(2, QFormLayout.FieldRole, self.topBtnRgnFE)


        self.topRgnLayout.addWidget(self.topMrkRng)


        self.manModeLayout.addWidget(self.topRgn, 0, 1, 1, 1)

        self.mrkSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.manModeLayout.addItem(self.mrkSpacer, 1, 1, 1, 1)


        self.mrkLayout.addWidget(self.manModeFrame)

        self.mrkLine = QFrame(self.mrkFrame)
        self.mrkLine.setObjectName(u"mrkLine")
        self.mrkLine.setFocusPolicy(Qt.NoFocus)
        self.mrkLine.setFrameShape(QFrame.Shape.HLine)
        self.mrkLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.mrkLayout.addWidget(self.mrkLine)

        self.intModeFrame = QFrame(self.mrkFrame)
        self.intModeFrame.setObjectName(u"intModeFrame")
        self.intModeFrame.setFrameShape(QFrame.StyledPanel)
        self.intModeFrame.setFrameShadow(QFrame.Raised)
        self.intModeLayout = QHBoxLayout(self.intModeFrame)
        self.intModeLayout.setObjectName(u"intModeLayout")
        self.intModeCheckBox = QCheckBox(self.intModeFrame)
        self.intModeCheckBox.setObjectName(u"intModeCheckBox")
        font3 = QFont()
        font3.setPointSize(12)
        self.intModeCheckBox.setFont(font3)

        self.intModeLayout.addWidget(self.intModeCheckBox)

        self.intModeSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.intModeLayout.addItem(self.intModeSpacer)

        self.intThsLayout = QHBoxLayout()
        self.intThsLayout.setSpacing(5)
        self.intThsLayout.setObjectName(u"intThsLayout")
        self.intThsSpinBox = QDoubleSpinBox(self.intModeFrame)
        self.intThsSpinBox.setObjectName(u"intThsSpinBox")
        self.intThsSpinBox.setEnabled(False)
        self.intThsSpinBox.setMinimumSize(QSize(70, 30))
        self.intThsSpinBox.setMaximumSize(QSize(70, 30))
        self.intThsSpinBox.setFont(font3)
        self.intThsSpinBox.setFocusPolicy(Qt.NoFocus)
        self.intThsSpinBox.setDecimals(1)
        self.intThsSpinBox.setMinimum(1.000000000000000)
        self.intThsSpinBox.setMaximum(20.000000000000000)
        self.intThsSpinBox.setSingleStep(0.500000000000000)
        self.intThsSpinBox.setValue(5.000000000000000)

        self.intThsLayout.addWidget(self.intThsSpinBox)

        self.intThsLabel = QLabel(self.intModeFrame)
        self.intThsLabel.setObjectName(u"intThsLabel")
        self.intThsLabel.setMinimumSize(QSize(75, 30))
        self.intThsLabel.setMaximumSize(QSize(75, 30))
        self.intThsLabel.setFont(font3)

        self.intThsLayout.addWidget(self.intThsLabel)


        self.intModeLayout.addLayout(self.intThsLayout)


        self.mrkLayout.addWidget(self.intModeFrame)


        self.setupLayout.addWidget(self.mrkFrame)

        self.dispFrame = QFrame(self.centralWidget)
        self.dispFrame.setObjectName(u"dispFrame")
        self.dispFrame.setMinimumSize(QSize(540, 90))
        self.dispFrame.setMaximumSize(QSize(540, 90))
        self.dispFrame.setFrameShape(QFrame.Box)
        self.dispFrame.setFrameShadow(QFrame.Sunken)
        self.dispLayout = QVBoxLayout(self.dispFrame)
        self.dispLayout.setSpacing(0)
        self.dispLayout.setObjectName(u"dispLayout")
        self.dispLayout.setContentsMargins(-1, 0, -1, 0)
        self.dispRoiFrame = QFrame(self.dispFrame)
        self.dispRoiFrame.setObjectName(u"dispRoiFrame")
        self.dispRoiFrame.setFrameShape(QFrame.StyledPanel)
        self.dispRoiFrame.setFrameShadow(QFrame.Raised)
        self.dispRoiLayout = QHBoxLayout(self.dispRoiFrame)
        self.dispRoiLayout.setObjectName(u"dispRoiLayout")
        self.dispRoiCheckBox = QCheckBox(self.dispRoiFrame)
        self.dispRoiCheckBox.setObjectName(u"dispRoiCheckBox")
        self.dispRoiCheckBox.setFont(font3)

        self.dispRoiLayout.addWidget(self.dispRoiCheckBox)

        self.dispRoiBox = QComboBox(self.dispRoiFrame)
        self.dispRoiBox.addItem("")
        self.dispRoiBox.addItem("")
        self.dispRoiBox.addItem("")
        self.dispRoiBox.addItem("")
        self.dispRoiBox.setObjectName(u"dispRoiBox")
        self.dispRoiBox.setEnabled(False)
        self.dispRoiBox.setFont(font3)
        self.dispRoiBox.setFocusPolicy(Qt.NoFocus)

        self.dispRoiLayout.addWidget(self.dispRoiBox)


        self.dispLayout.addWidget(self.dispRoiFrame)

        self.dispLblFrame = QFrame(self.dispFrame)
        self.dispLblFrame.setObjectName(u"dispLblFrame")
        self.dispLblFrame.setFrameShape(QFrame.StyledPanel)
        self.dispLblFrame.setFrameShadow(QFrame.Raised)
        self.dispLblLayout = QHBoxLayout(self.dispLblFrame)
        self.dispLblLayout.setObjectName(u"dispLblLayout")
        self.dispHmlCheckBox = QCheckBox(self.dispLblFrame)
        self.dispHmlCheckBox.setObjectName(u"dispHmlCheckBox")
        self.dispHmlCheckBox.setFont(font3)

        self.dispLblLayout.addWidget(self.dispHmlCheckBox)

        self.dispLblSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.dispLblLayout.addItem(self.dispLblSpacer)

        self.dispJslCheckBox = QCheckBox(self.dispLblFrame)
        self.dispJslCheckBox.setObjectName(u"dispJslCheckBox")
        self.dispJslCheckBox.setFont(font3)

        self.dispLblLayout.addWidget(self.dispJslCheckBox)


        self.dispLayout.addWidget(self.dispLblFrame)


        self.setupLayout.addWidget(self.dispFrame)


        self.frameLayout.addLayout(self.setupLayout)


        self.centralLayout.addLayout(self.frameLayout)

        self.frmsldrLayout = QHBoxLayout()
        self.frmsldrLayout.setSpacing(10)
        self.frmsldrLayout.setObjectName(u"frmsldrLayout")
        self.frmSlider = QSlider(self.centralWidget)
        self.frmSlider.setObjectName(u"frmSlider")
        self.frmSlider.setMinimumSize(QSize(0, 30))
        self.frmSlider.setMaximumSize(QSize(16777215, 30))
        self.frmSlider.setMaximum(35999)
        self.frmSlider.setOrientation(Qt.Horizontal)

        self.frmsldrLayout.addWidget(self.frmSlider)

        self.sldrValue = QSpinBox(self.centralWidget)
        self.sldrValue.setObjectName(u"sldrValue")
        self.sldrValue.setMinimumSize(QSize(75, 30))
        self.sldrValue.setMaximumSize(QSize(75, 30))
        self.sldrValue.setFont(font3)
        self.sldrValue.setFocusPolicy(Qt.ClickFocus)
        self.sldrValue.setMaximum(35999)

        self.frmsldrLayout.addWidget(self.sldrValue)


        self.centralLayout.addLayout(self.frmsldrLayout)

        self.ctrlLayout = QHBoxLayout()
        self.ctrlLayout.setObjectName(u"ctrlLayout")
        self.discardButton = QPushButton(self.centralWidget)
        self.discardButton.setObjectName(u"discardButton")
        self.discardButton.setMinimumSize(QSize(150, 30))
        self.discardButton.setMaximumSize(QSize(150, 30))
        self.discardButton.setFont(font)

        self.ctrlLayout.addWidget(self.discardButton)

        self.ctrlSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ctrlLayout.addItem(self.ctrlSpacer)

        self.saveButton = QPushButton(self.centralWidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(150, 30))
        self.saveButton.setMaximumSize(QSize(150, 30))
        self.saveButton.setFont(font)

        self.ctrlLayout.addWidget(self.saveButton)


        self.centralLayout.addLayout(self.ctrlLayout)

        CrossVerifier.setCentralWidget(self.centralWidget)
        self.statusbar = QStatusBar(CrossVerifier)
        self.statusbar.setObjectName(u"statusbar")
        CrossVerifier.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.frmSlider, self.sldrValue)
        QWidget.setTabOrder(self.sldrValue, self.intModeCheckBox)
        QWidget.setTabOrder(self.intModeCheckBox, self.intThsSpinBox)
        QWidget.setTabOrder(self.intThsSpinBox, self.dispRoiCheckBox)
        QWidget.setTabOrder(self.dispRoiCheckBox, self.dispRoiBox)
        QWidget.setTabOrder(self.dispRoiBox, self.dispHmlCheckBox)
        QWidget.setTabOrder(self.dispHmlCheckBox, self.dispJslCheckBox)
        QWidget.setTabOrder(self.dispJslCheckBox, self.discardButton)
        QWidget.setTabOrder(self.discardButton, self.saveButton)

        self.retranslateUi(CrossVerifier)
        self.frmSlider.valueChanged.connect(self.sldrValue.setValue)
        self.sldrValue.valueChanged.connect(self.frmSlider.setValue)
        self.gapBtnRgnTS.toggled.connect(self.gapBtnRgnTE.setEnabled)
        self.gapBtnRgnTE.clicked.connect(self.gapBtnRgnTS.toggle)
        self.gapBtnRgnFS.toggled.connect(self.gapBtnRgnFE.setEnabled)
        self.gapBtnRgnFE.clicked.connect(self.gapBtnRgnFS.toggle)
        self.topBtnRgnTS.toggled.connect(self.topBtnRgnTE.setEnabled)
        self.topBtnRgnTE.clicked.connect(self.topBtnRgnTS.toggle)
        self.topBtnRgnFS.toggled.connect(self.topBtnRgnFE.setEnabled)
        self.topBtnRgnFE.clicked.connect(self.topBtnRgnFS.toggle)
        self.btmBtnRgnTS.toggled.connect(self.btmBtnRgnTE.setEnabled)
        self.btmBtnRgnTE.clicked.connect(self.btmBtnRgnTS.toggle)
        self.btmBtnRgnFS.toggled.connect(self.btmBtnRgnFE.setEnabled)
        self.btmBtnRgnFE.clicked.connect(self.btmBtnRgnFS.toggle)
        self.gapBtnRgnTS.toggled.connect(self.gapBtnRgnFS.setDisabled)
        self.gapBtnRgnFS.toggled.connect(self.gapBtnRgnTS.setDisabled)
        self.topBtnRgnTS.toggled.connect(self.topBtnRgnFS.setDisabled)
        self.topBtnRgnFS.toggled.connect(self.topBtnRgnTS.setDisabled)
        self.btmBtnRgnTS.toggled.connect(self.btmBtnRgnFS.setDisabled)
        self.btmBtnRgnFS.toggled.connect(self.btmBtnRgnTS.setDisabled)
        self.gapBtnRgnTS.toggled.connect(self.gapMrkSgn.setDisabled)
        self.gapBtnRgnFS.toggled.connect(self.gapMrkSgn.setDisabled)
        self.gapBtnRgnTS.toggled.connect(self.topRgn.setDisabled)
        self.gapBtnRgnFS.toggled.connect(self.topRgn.setDisabled)
        self.gapBtnRgnFS.toggled.connect(self.btmRgn.setDisabled)
        self.gapBtnRgnTS.toggled.connect(self.btmRgn.setDisabled)
        self.topBtnRgnTS.toggled.connect(self.topMrkSgn.setDisabled)
        self.topBtnRgnFS.toggled.connect(self.topMrkSgn.setDisabled)
        self.topBtnRgnFS.toggled.connect(self.gapRgn.setDisabled)
        self.topBtnRgnTS.toggled.connect(self.gapRgn.setDisabled)
        self.topBtnRgnTS.toggled.connect(self.btmRgn.setDisabled)
        self.topBtnRgnFS.toggled.connect(self.btmRgn.setDisabled)
        self.btmBtnRgnTS.toggled.connect(self.btmMrkSgn.setDisabled)
        self.btmBtnRgnFS.toggled.connect(self.btmMrkSgn.setDisabled)
        self.btmBtnRgnTS.toggled.connect(self.gapRgn.setDisabled)
        self.btmBtnRgnFS.toggled.connect(self.gapRgn.setDisabled)
        self.btmBtnRgnTS.toggled.connect(self.topRgn.setDisabled)
        self.btmBtnRgnFS.toggled.connect(self.topRgn.setDisabled)
        self.intModeCheckBox.toggled.connect(self.manModeFrame.setDisabled)
        self.intModeCheckBox.toggled.connect(self.intThsSpinBox.setEnabled)
        self.dispRoiCheckBox.toggled.connect(self.dispRoiBox.setEnabled)

        QMetaObject.connectSlotsByName(CrossVerifier)


    def retranslateUi(self, CrossVerifier):
        CrossVerifier.setWindowTitle(QCoreApplication.translate("CrossVerifier", u"Cross Detection Verifier", None))
        self.btmRgn.setTitle(QCoreApplication.translate("CrossVerifier", u"Bottom Region", None))
        self.btmMrkSgn.setTitle(QCoreApplication.translate("CrossVerifier", u"Single Frame", None))
        self.btmBtnSgnT.setText(QCoreApplication.translate("CrossVerifier", u"Cross", None))
        self.btmBtnSgnF.setText(QCoreApplication.translate("CrossVerifier", u"Noncross", None))
        self.btmMrkRng.setTitle(QCoreApplication.translate("CrossVerifier", u"Frame Range", None))
        self.btmBtnRgnTS.setText(QCoreApplication.translate("CrossVerifier", u"Cross Start", None))
        self.btmBtnRgnTE.setText(QCoreApplication.translate("CrossVerifier", u"Cross End", None))
        self.btmBtnRgnFS.setText(QCoreApplication.translate("CrossVerifier", u"Noncross Start", None))
        self.btmBtnRgnFE.setText(QCoreApplication.translate("CrossVerifier", u"Noncross End", None))
        self.gapRgn.setTitle(QCoreApplication.translate("CrossVerifier", u"Gap Region", None))
        self.gapMrkSgn.setTitle(QCoreApplication.translate("CrossVerifier", u"Single Frame", None))
        self.gapBtnSgnT.setText(QCoreApplication.translate("CrossVerifier", u"Cross", None))
        self.gapBtnSgnF.setText(QCoreApplication.translate("CrossVerifier", u"Noncross", None))
        self.gapMrkRng.setTitle(QCoreApplication.translate("CrossVerifier", u"Frame Range", None))
        self.gapBtnRgnTS.setText(QCoreApplication.translate("CrossVerifier", u"Cross Start", None))
        self.gapBtnRgnTE.setText(QCoreApplication.translate("CrossVerifier", u"Cross End", None))
        self.gapBtnRgnFS.setText(QCoreApplication.translate("CrossVerifier", u"Noncross Start", None))
        self.gapBtnRgnFE.setText(QCoreApplication.translate("CrossVerifier", u"Noncross End", None))
        self.topRgn.setTitle(QCoreApplication.translate("CrossVerifier", u"Top Region", None))
        self.topMrkSgn.setTitle(QCoreApplication.translate("CrossVerifier", u"Single Frame", None))
        self.topBtnSgnT.setText(QCoreApplication.translate("CrossVerifier", u"Cross", None))
        self.topBtnSgnF.setText(QCoreApplication.translate("CrossVerifier", u"Noncross", None))
        self.topMrkRng.setTitle(QCoreApplication.translate("CrossVerifier", u"Frame Range", None))
        self.topBtnRgnTS.setText(QCoreApplication.translate("CrossVerifier", u"Cross Start", None))
        self.topBtnRgnTE.setText(QCoreApplication.translate("CrossVerifier", u"Cross End", None))
        self.topBtnRgnFS.setText(QCoreApplication.translate("CrossVerifier", u"Noncross Start", None))
        self.topBtnRgnFE.setText(QCoreApplication.translate("CrossVerifier", u"Noncross End", None))
        self.intModeCheckBox.setToolTip(QCoreApplication.translate("CrossVerifier", u"Use intelligent mode for manual"
                                                                                    u"correction, enable this to allow"
                                                                                    u"keyboard shortcuts", None))
        self.intModeCheckBox.setText(QCoreApplication.translate("CrossVerifier", u"Intelligent Mode", None))
        self.intThsLabel.setText(QCoreApplication.translate("CrossVerifier", u"Threshold", None))
        self.dispRoiCheckBox.setToolTip(QCoreApplication.translate("CrossVerifier", u"Use intelligent mode for manual"
                                                                                    u"correction, enable this to allow"
                                                                                    u"keyboard shortcuts", None))
        self.dispRoiCheckBox.setText(QCoreApplication.translate("CrossVerifier", u"Show ROI", None))
        self.dispRoiBox.setItemText(0, QCoreApplication.translate("CrossVerifier", u"AUTO", None))
        self.dispRoiBox.setItemText(1, QCoreApplication.translate("CrossVerifier", u"Gap", None))
        self.dispRoiBox.setItemText(2, QCoreApplication.translate("CrossVerifier", u"Top", None))
        self.dispRoiBox.setItemText(3, QCoreApplication.translate("CrossVerifier", u"Bottom", None))

        self.dispHmlCheckBox.setToolTip(QCoreApplication.translate("CrossVerifier", u"Use intelligent mode for manual"
                                                                                    u"correction, enable this to allow"
                                                                                    u"keyboard shortcuts", None))
        self.dispHmlCheckBox.setText(QCoreApplication.translate("CrossVerifier", u"Show HeatMap Label", None))
        self.dispJslCheckBox.setToolTip(QCoreApplication.translate("CrossVerifier", u"Use intelligent mode for manual"
                                                                                    u"correction, enable this to allow"
                                                                                    u"keyboard shortcuts", None))
        self.dispJslCheckBox.setText(QCoreApplication.translate("CrossVerifier", u"Show JSON Label", None))
        self.discardButton.setText(QCoreApplication.translate("CrossVerifier", u"Discard && Exit", None))
        self.saveButton.setText(QCoreApplication.translate("CrossVerifier", u"Save && Exit", None))
