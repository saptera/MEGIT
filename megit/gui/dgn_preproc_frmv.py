# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dgn_preproc_frmv.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import QGraphicsView, QGridLayout, QStatusBar, QWidget


class Ui_FrameViewer(object):
    def setupUi(self, FrameViewer):
        if not FrameViewer.objectName():
            FrameViewer.setObjectName(u"FrameViewer")
        FrameViewer.resize(100, 120)
        self.frameWidget = QWidget(FrameViewer)
        self.frameWidget.setObjectName(u"frameWidget")
        self.frameLayout = QGridLayout(self.frameWidget)
        self.frameLayout.setSpacing(0)
        self.frameLayout.setObjectName(u"frameLayout")
        self.frameLayout.setContentsMargins(0, 0, 0, 0)
        self.frameDisplay = QGraphicsView(self.frameWidget)
        self.frameDisplay.setObjectName(u"frameDisplay")

        self.frameLayout.addWidget(self.frameDisplay, 0, 0, 1, 1)

        FrameViewer.setCentralWidget(self.frameWidget)
        self.statusBar = QStatusBar(FrameViewer)
        self.statusBar.setObjectName(u"statusBar")
        FrameViewer.setStatusBar(self.statusBar)

        self.retranslateUi(FrameViewer)

        QMetaObject.connectSlotsByName(FrameViewer)


    def retranslateUi(self, FrameViewer):
        FrameViewer.setWindowTitle(QCoreApplication.translate("FrameViewer", u"Frame View", None))
