# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\MEGIT\megit\gui\dgn_preproc_frmv.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameViewer(object):
    def setupUi(self, FrameViewer):
        FrameViewer.setObjectName("FrameViewer")
        FrameViewer.resize(100, 120)
        self.frameWidget = QtWidgets.QWidget(FrameViewer)
        self.frameWidget.setObjectName("frameWidget")
        self.frameLayout = QtWidgets.QGridLayout(self.frameWidget)
        self.frameLayout.setContentsMargins(0, 0, 0, 0)
        self.frameLayout.setSpacing(0)
        self.frameLayout.setObjectName("frameLayout")
        self.frameDisplay = QtWidgets.QGraphicsView(self.frameWidget)
        self.frameDisplay.setObjectName("frameDisplay")
        self.frameLayout.addWidget(self.frameDisplay, 0, 0, 1, 1)
        FrameViewer.setCentralWidget(self.frameWidget)
        self.statusBar = QtWidgets.QStatusBar(FrameViewer)
        self.statusBar.setObjectName("statusBar")
        FrameViewer.setStatusBar(self.statusBar)

        self.retranslateUi(FrameViewer)
        QtCore.QMetaObject.connectSlotsByName(FrameViewer)

    def retranslateUi(self, FrameViewer):
        _translate = QtCore.QCoreApplication.translate
        FrameViewer.setWindowTitle(_translate("FrameViewer", "Frame View"))