# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\megit\gui\dgn_chkres_ctrl.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CrossVerifier(object):
    def setupUi(self, CrossVerifier):
        CrossVerifier.setObjectName("CrossVerifier")
        CrossVerifier.resize(1202, 756)
        CrossVerifier.setMinimumSize(QtCore.QSize(1202, 756))
        CrossVerifier.setMaximumSize(QtCore.QSize(1202, 756))
        self.centralWidget = QtWidgets.QWidget(CrossVerifier)
        self.centralWidget.setObjectName("centralWidget")
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.centralLayout.setSpacing(10)
        self.centralLayout.setObjectName("centralLayout")
        self.frameLayout = QtWidgets.QHBoxLayout()
        self.frameLayout.setSpacing(10)
        self.frameLayout.setObjectName("frameLayout")
        self.frameDisplay = QtWidgets.QGraphicsView(self.centralWidget)
        self.frameDisplay.setMinimumSize(QtCore.QSize(630, 630))
        self.frameDisplay.setMaximumSize(QtCore.QSize(630, 630))
        self.frameDisplay.setFocusPolicy(QtCore.Qt.NoFocus)
        self.frameDisplay.setObjectName("frameDisplay")
        self.frameLayout.addWidget(self.frameDisplay)
        self.setupLayout = QtWidgets.QVBoxLayout()
        self.setupLayout.setSpacing(10)
        self.setupLayout.setObjectName("setupLayout")
        self.mrkFrame = QtWidgets.QFrame(self.centralWidget)
        self.mrkFrame.setMinimumSize(QtCore.QSize(540, 530))
        self.mrkFrame.setMaximumSize(QtCore.QSize(540, 530))
        self.mrkFrame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mrkFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.mrkFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mrkFrame.setObjectName("mrkFrame")
        self.mrkLayout = QtWidgets.QVBoxLayout(self.mrkFrame)
        self.mrkLayout.setContentsMargins(-1, -1, -1, 0)
        self.mrkLayout.setObjectName("mrkLayout")
        self.manModeFrame = QtWidgets.QFrame(self.mrkFrame)
        self.manModeFrame.setMinimumSize(QtCore.QSize(518, 450))
        self.manModeFrame.setMaximumSize(QtCore.QSize(518, 450))
        self.manModeFrame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.manModeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.manModeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.manModeFrame.setObjectName("manModeFrame")
        self.manModeLayout = QtWidgets.QGridLayout(self.manModeFrame)
        self.manModeLayout.setContentsMargins(0, 0, 0, 0)
        self.manModeLayout.setObjectName("manModeLayout")
        self.btmRgn = QtWidgets.QGroupBox(self.manModeFrame)
        self.btmRgn.setMinimumSize(QtCore.QSize(246, 213))
        self.btmRgn.setMaximumSize(QtCore.QSize(246, 213))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btmRgn.setFont(font)
        self.btmRgn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btmRgn.setObjectName("btmRgn")
        self.btmRgnLayout = QtWidgets.QVBoxLayout(self.btmRgn)
        self.btmRgnLayout.setObjectName("btmRgnLayout")
        self.btmMrkSgn = QtWidgets.QGroupBox(self.btmRgn)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btmMrkSgn.setFont(font)
        self.btmMrkSgn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btmMrkSgn.setObjectName("btmMrkSgn")
        self.btmMrkSgnLayout = QtWidgets.QHBoxLayout(self.btmMrkSgn)
        self.btmMrkSgnLayout.setObjectName("btmMrkSgnLayout")
        self.btmBtnSgnT = QtWidgets.QPushButton(self.btmMrkSgn)
        self.btmBtnSgnT.setMinimumSize(QtCore.QSize(100, 25))
        self.btmBtnSgnT.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btmBtnSgnT.setFont(font)
        self.btmBtnSgnT.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btmBtnSgnT.setObjectName("btmBtnSgnT")
        self.btmMrkSgnLayout.addWidget(self.btmBtnSgnT)
        self.btmBtnSgnF = QtWidgets.QPushButton(self.btmMrkSgn)
        self.btmBtnSgnF.setMinimumSize(QtCore.QSize(100, 25))
        self.btmBtnSgnF.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btmBtnSgnF.setFont(font)
        self.btmBtnSgnF.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btmBtnSgnF.setObjectName("btmBtnSgnF")
        self.btmMrkSgnLayout.addWidget(self.btmBtnSgnF)
        self.btmRgnLayout.addWidget(self.btmMrkSgn)
        self.btmMrkRng = QtWidgets.QGroupBox(self.btmRgn)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btmMrkRng.setFont(font)
        self.btmMrkRng.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btmMrkRng.setObjectName("btmMrkRng")
        self.btmMrkRgnLayout = QtWidgets.QFormLayout(self.btmMrkRng)
        self.btmMrkRgnLayout.setObjectName("btmMrkRgnLayout")
        self.btmBtnRgnTS = QtWidgets.QPushButton(self.btmMrkRng)
        self.btmBtnRgnTS.setMinimumSize(QtCore.QSize(100, 25))
        self.btmBtnRgnTS.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btmBtnRgnTS.setFont(font)
        self.btmBtnRgnTS.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btmBtnRgnTS.setCheckable(True)
        self.btmBtnRgnTS.setObjectName("btmBtnRgnTS")
        self.btmMrkRgnLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btmBtnRgnTS)
        self.btmBtnRgnTE = QtWidgets.QPushButton(self.btmMrkRng)
        self.btmBtnRgnTE.setEnabled(False)
        self.btmBtnRgnTE.setMinimumSize(QtCore.QSize(100, 25))
        self.btmBtnRgnTE.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btmBtnRgnTE.setFont(font)
        self.btmBtnRgnTE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btmBtnRgnTE.setObjectName("btmBtnRgnTE")
        self.btmMrkRgnLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.btmBtnRgnTE)
        self.btmRgnLine = QtWidgets.QFrame(self.btmMrkRng)
        self.btmRgnLine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btmRgnLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.btmRgnLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.btmRgnLine.setObjectName("btmRgnLine")
        self.btmMrkRgnLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.btmRgnLine)
        self.btmBtnRgnFS = QtWidgets.QPushButton(self.btmMrkRng)
        self.btmBtnRgnFS.setMinimumSize(QtCore.QSize(100, 25))
        self.btmBtnRgnFS.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btmBtnRgnFS.setFont(font)
        self.btmBtnRgnFS.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btmBtnRgnFS.setCheckable(True)
        self.btmBtnRgnFS.setObjectName("btmBtnRgnFS")
        self.btmMrkRgnLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.btmBtnRgnFS)
        self.btmBtnRgnFE = QtWidgets.QPushButton(self.btmMrkRng)
        self.btmBtnRgnFE.setEnabled(False)
        self.btmBtnRgnFE.setMinimumSize(QtCore.QSize(100, 25))
        self.btmBtnRgnFE.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btmBtnRgnFE.setFont(font)
        self.btmBtnRgnFE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btmBtnRgnFE.setObjectName("btmBtnRgnFE")
        self.btmMrkRgnLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btmBtnRgnFE)
        self.btmRgnLayout.addWidget(self.btmMrkRng)
        self.manModeLayout.addWidget(self.btmRgn, 2, 1, 1, 1)
        self.gapRgn = QtWidgets.QGroupBox(self.manModeFrame)
        self.gapRgn.setMinimumSize(QtCore.QSize(246, 213))
        self.gapRgn.setMaximumSize(QtCore.QSize(246, 213))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gapRgn.setFont(font)
        self.gapRgn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gapRgn.setObjectName("gapRgn")
        self.gapRgnLayout = QtWidgets.QVBoxLayout(self.gapRgn)
        self.gapRgnLayout.setObjectName("gapRgnLayout")
        self.gapMrkSgn = QtWidgets.QGroupBox(self.gapRgn)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.gapMrkSgn.setFont(font)
        self.gapMrkSgn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gapMrkSgn.setObjectName("gapMrkSgn")
        self.gapMrkSgnLayout = QtWidgets.QHBoxLayout(self.gapMrkSgn)
        self.gapMrkSgnLayout.setObjectName("gapMrkSgnLayout")
        self.gapBtnSgnT = QtWidgets.QPushButton(self.gapMrkSgn)
        self.gapBtnSgnT.setMinimumSize(QtCore.QSize(100, 25))
        self.gapBtnSgnT.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.gapBtnSgnT.setFont(font)
        self.gapBtnSgnT.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gapBtnSgnT.setObjectName("gapBtnSgnT")
        self.gapMrkSgnLayout.addWidget(self.gapBtnSgnT)
        self.gapBtnSgnF = QtWidgets.QPushButton(self.gapMrkSgn)
        self.gapBtnSgnF.setMinimumSize(QtCore.QSize(100, 25))
        self.gapBtnSgnF.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.gapBtnSgnF.setFont(font)
        self.gapBtnSgnF.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gapBtnSgnF.setObjectName("gapBtnSgnF")
        self.gapMrkSgnLayout.addWidget(self.gapBtnSgnF)
        self.gapRgnLayout.addWidget(self.gapMrkSgn)
        self.gapMrkRng = QtWidgets.QGroupBox(self.gapRgn)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.gapMrkRng.setFont(font)
        self.gapMrkRng.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gapMrkRng.setObjectName("gapMrkRng")
        self.gapMrkRgnLayout = QtWidgets.QFormLayout(self.gapMrkRng)
        self.gapMrkRgnLayout.setObjectName("gapMrkRgnLayout")
        self.gapBtnRgnTS = QtWidgets.QPushButton(self.gapMrkRng)
        self.gapBtnRgnTS.setMinimumSize(QtCore.QSize(100, 25))
        self.gapBtnRgnTS.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.gapBtnRgnTS.setFont(font)
        self.gapBtnRgnTS.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gapBtnRgnTS.setCheckable(True)
        self.gapBtnRgnTS.setObjectName("gapBtnRgnTS")
        self.gapMrkRgnLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.gapBtnRgnTS)
        self.gapBtnRgnTE = QtWidgets.QPushButton(self.gapMrkRng)
        self.gapBtnRgnTE.setEnabled(False)
        self.gapBtnRgnTE.setMinimumSize(QtCore.QSize(100, 25))
        self.gapBtnRgnTE.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.gapBtnRgnTE.setFont(font)
        self.gapBtnRgnTE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gapBtnRgnTE.setObjectName("gapBtnRgnTE")
        self.gapMrkRgnLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.gapBtnRgnTE)
        self.gapRgnLine = QtWidgets.QFrame(self.gapMrkRng)
        self.gapRgnLine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gapRgnLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.gapRgnLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gapRgnLine.setObjectName("gapRgnLine")
        self.gapMrkRgnLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.gapRgnLine)
        self.gapBtnRgnFS = QtWidgets.QPushButton(self.gapMrkRng)
        self.gapBtnRgnFS.setMinimumSize(QtCore.QSize(100, 25))
        self.gapBtnRgnFS.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.gapBtnRgnFS.setFont(font)
        self.gapBtnRgnFS.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gapBtnRgnFS.setCheckable(True)
        self.gapBtnRgnFS.setObjectName("gapBtnRgnFS")
        self.gapMrkRgnLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.gapBtnRgnFS)
        self.gapBtnRgnFE = QtWidgets.QPushButton(self.gapMrkRng)
        self.gapBtnRgnFE.setEnabled(False)
        self.gapBtnRgnFE.setMinimumSize(QtCore.QSize(100, 25))
        self.gapBtnRgnFE.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.gapBtnRgnFE.setFont(font)
        self.gapBtnRgnFE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gapBtnRgnFE.setObjectName("gapBtnRgnFE")
        self.gapMrkRgnLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.gapBtnRgnFE)
        self.gapRgnLayout.addWidget(self.gapMrkRng)
        self.manModeLayout.addWidget(self.gapRgn, 0, 0, 3, 1)
        self.topRgn = QtWidgets.QGroupBox(self.manModeFrame)
        self.topRgn.setMinimumSize(QtCore.QSize(246, 213))
        self.topRgn.setMaximumSize(QtCore.QSize(246, 213))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.topRgn.setFont(font)
        self.topRgn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.topRgn.setObjectName("topRgn")
        self.topRgnLayout = QtWidgets.QVBoxLayout(self.topRgn)
        self.topRgnLayout.setObjectName("topRgnLayout")
        self.topMrkSgn = QtWidgets.QGroupBox(self.topRgn)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.topMrkSgn.setFont(font)
        self.topMrkSgn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.topMrkSgn.setObjectName("topMrkSgn")
        self.topMrkSgnLayout = QtWidgets.QHBoxLayout(self.topMrkSgn)
        self.topMrkSgnLayout.setObjectName("topMrkSgnLayout")
        self.topBtnSgnT = QtWidgets.QPushButton(self.topMrkSgn)
        self.topBtnSgnT.setMinimumSize(QtCore.QSize(100, 25))
        self.topBtnSgnT.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.topBtnSgnT.setFont(font)
        self.topBtnSgnT.setFocusPolicy(QtCore.Qt.NoFocus)
        self.topBtnSgnT.setObjectName("topBtnSgnT")
        self.topMrkSgnLayout.addWidget(self.topBtnSgnT)
        self.topBtnSgnF = QtWidgets.QPushButton(self.topMrkSgn)
        self.topBtnSgnF.setMinimumSize(QtCore.QSize(100, 25))
        self.topBtnSgnF.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.topBtnSgnF.setFont(font)
        self.topBtnSgnF.setFocusPolicy(QtCore.Qt.NoFocus)
        self.topBtnSgnF.setObjectName("topBtnSgnF")
        self.topMrkSgnLayout.addWidget(self.topBtnSgnF)
        self.topRgnLayout.addWidget(self.topMrkSgn)
        self.topMrkRng = QtWidgets.QGroupBox(self.topRgn)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.topMrkRng.setFont(font)
        self.topMrkRng.setFocusPolicy(QtCore.Qt.NoFocus)
        self.topMrkRng.setObjectName("topMrkRng")
        self.topMrkRgnLayout = QtWidgets.QFormLayout(self.topMrkRng)
        self.topMrkRgnLayout.setObjectName("topMrkRgnLayout")
        self.topBtnRgnTS = QtWidgets.QPushButton(self.topMrkRng)
        self.topBtnRgnTS.setMinimumSize(QtCore.QSize(100, 25))
        self.topBtnRgnTS.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.topBtnRgnTS.setFont(font)
        self.topBtnRgnTS.setFocusPolicy(QtCore.Qt.NoFocus)
        self.topBtnRgnTS.setCheckable(True)
        self.topBtnRgnTS.setObjectName("topBtnRgnTS")
        self.topMrkRgnLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.topBtnRgnTS)
        self.topBtnRgnTE = QtWidgets.QPushButton(self.topMrkRng)
        self.topBtnRgnTE.setEnabled(False)
        self.topBtnRgnTE.setMinimumSize(QtCore.QSize(100, 25))
        self.topBtnRgnTE.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.topBtnRgnTE.setFont(font)
        self.topBtnRgnTE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.topBtnRgnTE.setObjectName("topBtnRgnTE")
        self.topMrkRgnLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.topBtnRgnTE)
        self.topRgnLine = QtWidgets.QFrame(self.topMrkRng)
        self.topRgnLine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.topRgnLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.topRgnLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topRgnLine.setObjectName("topRgnLine")
        self.topMrkRgnLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.topRgnLine)
        self.topBtnRgnFS = QtWidgets.QPushButton(self.topMrkRng)
        self.topBtnRgnFS.setMinimumSize(QtCore.QSize(100, 25))
        self.topBtnRgnFS.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.topBtnRgnFS.setFont(font)
        self.topBtnRgnFS.setFocusPolicy(QtCore.Qt.NoFocus)
        self.topBtnRgnFS.setCheckable(True)
        self.topBtnRgnFS.setObjectName("topBtnRgnFS")
        self.topMrkRgnLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.topBtnRgnFS)
        self.topBtnRgnFE = QtWidgets.QPushButton(self.topMrkRng)
        self.topBtnRgnFE.setEnabled(False)
        self.topBtnRgnFE.setMinimumSize(QtCore.QSize(100, 25))
        self.topBtnRgnFE.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.topBtnRgnFE.setFont(font)
        self.topBtnRgnFE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.topBtnRgnFE.setObjectName("topBtnRgnFE")
        self.topMrkRgnLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.topBtnRgnFE)
        self.topRgnLayout.addWidget(self.topMrkRng)
        self.manModeLayout.addWidget(self.topRgn, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.manModeLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.mrkLayout.addWidget(self.manModeFrame)
        self.mrkLine = QtWidgets.QFrame(self.mrkFrame)
        self.mrkLine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mrkLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.mrkLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mrkLine.setObjectName("mrkLine")
        self.mrkLayout.addWidget(self.mrkLine)
        self.intModeFrame = QtWidgets.QFrame(self.mrkFrame)
        self.intModeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.intModeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.intModeFrame.setObjectName("intModeFrame")
        self.intModeLayout = QtWidgets.QHBoxLayout(self.intModeFrame)
        self.intModeLayout.setObjectName("intModeLayout")
        self.intModeCheckBox = QtWidgets.QCheckBox(self.intModeFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.intModeCheckBox.setFont(font)
        self.intModeCheckBox.setObjectName("intModeCheckBox")
        self.intModeLayout.addWidget(self.intModeCheckBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.intModeLayout.addItem(spacerItem1)
        self.intThsLayout = QtWidgets.QHBoxLayout()
        self.intThsLayout.setSpacing(5)
        self.intThsLayout.setObjectName("intThsLayout")
        self.intThsSpinBox = QtWidgets.QDoubleSpinBox(self.intModeFrame)
        self.intThsSpinBox.setEnabled(False)
        self.intThsSpinBox.setMinimumSize(QtCore.QSize(70, 30))
        self.intThsSpinBox.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.intThsSpinBox.setFont(font)
        self.intThsSpinBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.intThsSpinBox.setDecimals(1)
        self.intThsSpinBox.setMinimum(1.0)
        self.intThsSpinBox.setMaximum(20.0)
        self.intThsSpinBox.setSingleStep(0.5)
        self.intThsSpinBox.setProperty("value", 5.0)
        self.intThsSpinBox.setObjectName("intThsSpinBox")
        self.intThsLayout.addWidget(self.intThsSpinBox)
        self.intThsLabel = QtWidgets.QLabel(self.intModeFrame)
        self.intThsLabel.setMinimumSize(QtCore.QSize(75, 30))
        self.intThsLabel.setMaximumSize(QtCore.QSize(75, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.intThsLabel.setFont(font)
        self.intThsLabel.setObjectName("intThsLabel")
        self.intThsLayout.addWidget(self.intThsLabel)
        self.intModeLayout.addLayout(self.intThsLayout)
        self.mrkLayout.addWidget(self.intModeFrame)
        self.setupLayout.addWidget(self.mrkFrame)
        self.dispFrame = QtWidgets.QFrame(self.centralWidget)
        self.dispFrame.setMinimumSize(QtCore.QSize(540, 90))
        self.dispFrame.setMaximumSize(QtCore.QSize(540, 90))
        self.dispFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.dispFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dispFrame.setObjectName("dispFrame")
        self.dispLayout = QtWidgets.QVBoxLayout(self.dispFrame)
        self.dispLayout.setContentsMargins(-1, 0, -1, 0)
        self.dispLayout.setSpacing(0)
        self.dispLayout.setObjectName("dispLayout")
        self.dispRoiFrame = QtWidgets.QFrame(self.dispFrame)
        self.dispRoiFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dispRoiFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dispRoiFrame.setObjectName("dispRoiFrame")
        self.dispRoiLayout = QtWidgets.QHBoxLayout(self.dispRoiFrame)
        self.dispRoiLayout.setObjectName("dispRoiLayout")
        self.dispRoiCheckBox = QtWidgets.QCheckBox(self.dispRoiFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dispRoiCheckBox.setFont(font)
        self.dispRoiCheckBox.setObjectName("dispRoiCheckBox")
        self.dispRoiLayout.addWidget(self.dispRoiCheckBox)
        self.dispRoiBox = QtWidgets.QComboBox(self.dispRoiFrame)
        self.dispRoiBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dispRoiBox.setFont(font)
        self.dispRoiBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dispRoiBox.setObjectName("dispRoiBox")
        self.dispRoiBox.addItem("")
        self.dispRoiBox.addItem("")
        self.dispRoiBox.addItem("")
        self.dispRoiBox.addItem("")
        self.dispRoiLayout.addWidget(self.dispRoiBox)
        self.dispLayout.addWidget(self.dispRoiFrame)
        self.dispLblFrame = QtWidgets.QFrame(self.dispFrame)
        self.dispLblFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dispLblFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dispLblFrame.setObjectName("dispLblFrame")
        self.dispLblLayout = QtWidgets.QHBoxLayout(self.dispLblFrame)
        self.dispLblLayout.setObjectName("dispLblLayout")
        self.dispHmlCheckBox = QtWidgets.QCheckBox(self.dispLblFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dispHmlCheckBox.setFont(font)
        self.dispHmlCheckBox.setObjectName("dispHmlCheckBox")
        self.dispLblLayout.addWidget(self.dispHmlCheckBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.dispLblLayout.addItem(spacerItem2)
        self.dispJslCheckBox = QtWidgets.QCheckBox(self.dispLblFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dispJslCheckBox.setFont(font)
        self.dispJslCheckBox.setObjectName("dispJslCheckBox")
        self.dispLblLayout.addWidget(self.dispJslCheckBox)
        self.dispLayout.addWidget(self.dispLblFrame)
        self.setupLayout.addWidget(self.dispFrame)
        self.frameLayout.addLayout(self.setupLayout)
        self.centralLayout.addLayout(self.frameLayout)
        self.frmsldrLayout = QtWidgets.QHBoxLayout()
        self.frmsldrLayout.setSpacing(10)
        self.frmsldrLayout.setObjectName("frmsldrLayout")
        self.frmSlider = QtWidgets.QSlider(self.centralWidget)
        self.frmSlider.setMinimumSize(QtCore.QSize(0, 30))
        self.frmSlider.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frmSlider.setMaximum(35999)
        self.frmSlider.setOrientation(QtCore.Qt.Horizontal)
        self.frmSlider.setObjectName("frmSlider")
        self.frmsldrLayout.addWidget(self.frmSlider)
        self.sldrValue = QtWidgets.QSpinBox(self.centralWidget)
        self.sldrValue.setMinimumSize(QtCore.QSize(75, 30))
        self.sldrValue.setMaximumSize(QtCore.QSize(75, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sldrValue.setFont(font)
        self.sldrValue.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sldrValue.setMaximum(35999)
        self.sldrValue.setObjectName("sldrValue")
        self.frmsldrLayout.addWidget(self.sldrValue)
        self.centralLayout.addLayout(self.frmsldrLayout)
        self.ctrlLayout = QtWidgets.QHBoxLayout()
        self.ctrlLayout.setObjectName("ctrlLayout")
        self.discardButton = QtWidgets.QPushButton(self.centralWidget)
        self.discardButton.setMinimumSize(QtCore.QSize(150, 30))
        self.discardButton.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.discardButton.setFont(font)
        self.discardButton.setObjectName("discardButton")
        self.ctrlLayout.addWidget(self.discardButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ctrlLayout.addItem(spacerItem3)
        self.saveButton = QtWidgets.QPushButton(self.centralWidget)
        self.saveButton.setMinimumSize(QtCore.QSize(150, 30))
        self.saveButton.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.ctrlLayout.addWidget(self.saveButton)
        self.centralLayout.addLayout(self.ctrlLayout)
        CrossVerifier.setCentralWidget(self.centralWidget)
        self.statusbar = QtWidgets.QStatusBar(CrossVerifier)
        self.statusbar.setObjectName("statusbar")
        CrossVerifier.setStatusBar(self.statusbar)

        self.retranslateUi(CrossVerifier)
        self.frmSlider.valueChanged['int'].connect(self.sldrValue.setValue)
        self.sldrValue.valueChanged['int'].connect(self.frmSlider.setValue)
        self.gapBtnRgnTS.toggled['bool'].connect(self.gapBtnRgnTE.setEnabled)
        self.gapBtnRgnTE.clicked.connect(self.gapBtnRgnTS.toggle)
        self.gapBtnRgnFS.toggled['bool'].connect(self.gapBtnRgnFE.setEnabled)
        self.gapBtnRgnFE.clicked.connect(self.gapBtnRgnFS.toggle)
        self.topBtnRgnTS.toggled['bool'].connect(self.topBtnRgnTE.setEnabled)
        self.topBtnRgnTE.clicked.connect(self.topBtnRgnTS.toggle)
        self.topBtnRgnFS.toggled['bool'].connect(self.topBtnRgnFE.setEnabled)
        self.topBtnRgnFE.clicked.connect(self.topBtnRgnFS.toggle)
        self.btmBtnRgnTS.toggled['bool'].connect(self.btmBtnRgnTE.setEnabled)
        self.btmBtnRgnTE.clicked.connect(self.btmBtnRgnTS.toggle)
        self.btmBtnRgnFS.toggled['bool'].connect(self.btmBtnRgnFE.setEnabled)
        self.btmBtnRgnFE.clicked.connect(self.btmBtnRgnFS.toggle)
        self.gapBtnRgnTS.toggled['bool'].connect(self.gapBtnRgnFS.setDisabled)
        self.gapBtnRgnFS.toggled['bool'].connect(self.gapBtnRgnTS.setDisabled)
        self.topBtnRgnTS.toggled['bool'].connect(self.topBtnRgnFS.setDisabled)
        self.topBtnRgnFS.toggled['bool'].connect(self.topBtnRgnTS.setDisabled)
        self.btmBtnRgnTS.toggled['bool'].connect(self.btmBtnRgnFS.setDisabled)
        self.btmBtnRgnFS.toggled['bool'].connect(self.btmBtnRgnTS.setDisabled)
        self.gapBtnRgnTS.toggled['bool'].connect(self.gapMrkSgn.setDisabled)
        self.gapBtnRgnFS.toggled['bool'].connect(self.gapMrkSgn.setDisabled)
        self.gapBtnRgnTS.toggled['bool'].connect(self.topRgn.setDisabled)
        self.gapBtnRgnFS.toggled['bool'].connect(self.topRgn.setDisabled)
        self.gapBtnRgnFS.toggled['bool'].connect(self.btmRgn.setDisabled)
        self.gapBtnRgnTS.toggled['bool'].connect(self.btmRgn.setDisabled)
        self.topBtnRgnTS.toggled['bool'].connect(self.topMrkSgn.setDisabled)
        self.topBtnRgnFS.toggled['bool'].connect(self.topMrkSgn.setDisabled)
        self.topBtnRgnFS.toggled['bool'].connect(self.gapRgn.setDisabled)
        self.topBtnRgnTS.toggled['bool'].connect(self.gapRgn.setDisabled)
        self.topBtnRgnTS.toggled['bool'].connect(self.btmRgn.setDisabled)
        self.topBtnRgnFS.toggled['bool'].connect(self.btmRgn.setDisabled)
        self.btmBtnRgnTS.toggled['bool'].connect(self.btmMrkSgn.setDisabled)
        self.btmBtnRgnFS.toggled['bool'].connect(self.btmMrkSgn.setDisabled)
        self.btmBtnRgnTS.toggled['bool'].connect(self.gapRgn.setDisabled)
        self.btmBtnRgnFS.toggled['bool'].connect(self.gapRgn.setDisabled)
        self.btmBtnRgnTS.toggled['bool'].connect(self.topRgn.setDisabled)
        self.btmBtnRgnFS.toggled['bool'].connect(self.topRgn.setDisabled)
        self.intModeCheckBox.toggled['bool'].connect(self.manModeFrame.setDisabled)
        self.intModeCheckBox.toggled['bool'].connect(self.intThsSpinBox.setEnabled)
        self.dispRoiCheckBox.toggled['bool'].connect(self.dispRoiBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(CrossVerifier)
        CrossVerifier.setTabOrder(self.frmSlider, self.sldrValue)
        CrossVerifier.setTabOrder(self.sldrValue, self.intModeCheckBox)
        CrossVerifier.setTabOrder(self.intModeCheckBox, self.intThsSpinBox)
        CrossVerifier.setTabOrder(self.intThsSpinBox, self.dispRoiCheckBox)
        CrossVerifier.setTabOrder(self.dispRoiCheckBox, self.dispRoiBox)
        CrossVerifier.setTabOrder(self.dispRoiBox, self.dispHmlCheckBox)
        CrossVerifier.setTabOrder(self.dispHmlCheckBox, self.dispJslCheckBox)
        CrossVerifier.setTabOrder(self.dispJslCheckBox, self.discardButton)
        CrossVerifier.setTabOrder(self.discardButton, self.saveButton)

    def retranslateUi(self, CrossVerifier):
        _translate = QtCore.QCoreApplication.translate
        CrossVerifier.setWindowTitle(_translate("CrossVerifier", "Cross Detection Verifier"))
        self.btmRgn.setTitle(_translate("CrossVerifier", "Bottom Region"))
        self.btmMrkSgn.setTitle(_translate("CrossVerifier", "Single Frame"))
        self.btmBtnSgnT.setText(_translate("CrossVerifier", "Cross"))
        self.btmBtnSgnF.setText(_translate("CrossVerifier", "Noncross"))
        self.btmMrkRng.setTitle(_translate("CrossVerifier", "Frame Range"))
        self.btmBtnRgnTS.setText(_translate("CrossVerifier", "Cross Start"))
        self.btmBtnRgnTE.setText(_translate("CrossVerifier", "Cross End"))
        self.btmBtnRgnFS.setText(_translate("CrossVerifier", "Noncross Start"))
        self.btmBtnRgnFE.setText(_translate("CrossVerifier", "Noncross End"))
        self.gapRgn.setTitle(_translate("CrossVerifier", "Gap Region"))
        self.gapMrkSgn.setTitle(_translate("CrossVerifier", "Single Frame"))
        self.gapBtnSgnT.setText(_translate("CrossVerifier", "Cross"))
        self.gapBtnSgnF.setText(_translate("CrossVerifier", "Noncross"))
        self.gapMrkRng.setTitle(_translate("CrossVerifier", "Frame Range"))
        self.gapBtnRgnTS.setText(_translate("CrossVerifier", "Cross Start"))
        self.gapBtnRgnTE.setText(_translate("CrossVerifier", "Cross End"))
        self.gapBtnRgnFS.setText(_translate("CrossVerifier", "Noncross Start"))
        self.gapBtnRgnFE.setText(_translate("CrossVerifier", "Noncross End"))
        self.topRgn.setTitle(_translate("CrossVerifier", "Top Region"))
        self.topMrkSgn.setTitle(_translate("CrossVerifier", "Single Frame"))
        self.topBtnSgnT.setText(_translate("CrossVerifier", "Cross"))
        self.topBtnSgnF.setText(_translate("CrossVerifier", "Noncross"))
        self.topMrkRng.setTitle(_translate("CrossVerifier", "Frame Range"))
        self.topBtnRgnTS.setText(_translate("CrossVerifier", "Cross Start"))
        self.topBtnRgnTE.setText(_translate("CrossVerifier", "Cross End"))
        self.topBtnRgnFS.setText(_translate("CrossVerifier", "Noncross Start"))
        self.topBtnRgnFE.setText(_translate("CrossVerifier", "Noncross End"))
        self.intModeCheckBox.setToolTip(_translate("CrossVerifier", "Use intelligent mode for manual correction, "
                                                                    "enable this to allow keyboard shortcuts"))
        self.intModeCheckBox.setText(_translate("CrossVerifier", "Intelligent Mode"))
        self.intThsLabel.setText(_translate("CrossVerifier", "Threshold"))
        self.dispRoiCheckBox.setToolTip(_translate("CrossVerifier", "Use intelligent mode for manual correction, "
                                                                    "enable this to allow keyboard shortcuts"))
        self.dispRoiCheckBox.setText(_translate("CrossVerifier", "Show ROI"))
        self.dispRoiBox.setItemText(0, _translate("CrossVerifier", "AUTO"))
        self.dispRoiBox.setItemText(1, _translate("CrossVerifier", "Gap"))
        self.dispRoiBox.setItemText(2, _translate("CrossVerifier", "Top"))
        self.dispRoiBox.setItemText(3, _translate("CrossVerifier", "Bottom"))
        self.dispHmlCheckBox.setToolTip(_translate("CrossVerifier", "Use intelligent mode for manual correction, "
                                                                    "enable this to allow keyboard shortcuts"))
        self.dispHmlCheckBox.setText(_translate("CrossVerifier", "Show HeatMap Label"))
        self.dispJslCheckBox.setToolTip(_translate("CrossVerifier", "Use intelligent mode for manual correction, "
                                                                    "enable this to allow keyboard shortcuts"))
        self.dispJslCheckBox.setText(_translate("CrossVerifier", "Show JSON Label"))
        self.discardButton.setText(_translate("CrossVerifier", "Discard && Exit"))
        self.saveButton.setText(_translate("CrossVerifier", "Save && Exit"))