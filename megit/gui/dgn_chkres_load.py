# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dgn_chkres_load.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget


class Ui_MainLoader(object):
    def setupUi(self, MainLoader):
        if not MainLoader.objectName():
            MainLoader.setObjectName(u"MainLoader")
        MainLoader.resize(850, 335)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainLoader.sizePolicy().hasHeightForWidth())
        MainLoader.setSizePolicy(sizePolicy)
        MainLoader.setMinimumSize(QSize(850, 335))
        MainLoader.setMaximumSize(QSize(16777215, 335))
        self.loaderWidget = QWidget(MainLoader)
        self.loaderWidget.setObjectName(u"loaderWidget")
        self.loaderLayout = QVBoxLayout(self.loaderWidget)
        self.loaderLayout.setSpacing(10)
        self.loaderLayout.setObjectName(u"loaderLayout")
        self.loaderLayout.setContentsMargins(10, 10, 10, 10)
        self.reqGroup = QGroupBox(self.loaderWidget)
        self.reqGroup.setObjectName(u"reqGroup")
        font = QFont()
        font.setBold(True)
        self.reqGroup.setFont(font)
        self.reqLayout = QVBoxLayout(self.reqGroup)
        self.reqLayout.setObjectName(u"reqLayout")
        self.frmLayout = QHBoxLayout()
        self.frmLayout.setObjectName(u"frmLayout")
        self.frmPath = QLineEdit(self.reqGroup)
        self.frmPath.setObjectName(u"frmPath")
        font1 = QFont()
        font1.setBold(False)
        self.frmPath.setFont(font1)

        self.frmLayout.addWidget(self.frmPath)

        self.frmButton = QPushButton(self.reqGroup)
        self.frmButton.setObjectName(u"frmButton")
        self.frmButton.setMinimumSize(QSize(200, 0))
        self.frmButton.setFont(font1)

        self.frmLayout.addWidget(self.frmButton)


        self.reqLayout.addLayout(self.frmLayout)

        self.crsLayout = QHBoxLayout()
        self.crsLayout.setObjectName(u"crsLayout")
        self.crsPath = QLineEdit(self.reqGroup)
        self.crsPath.setObjectName(u"crsPath")
        self.crsPath.setFont(font1)

        self.crsLayout.addWidget(self.crsPath)

        self.crsButton = QPushButton(self.reqGroup)
        self.crsButton.setObjectName(u"crsButton")
        self.crsButton.setMinimumSize(QSize(200, 0))
        self.crsButton.setFont(font1)

        self.crsLayout.addWidget(self.crsButton)


        self.reqLayout.addLayout(self.crsLayout)

        self.roiLayout = QHBoxLayout()
        self.roiLayout.setObjectName(u"roiLayout")
        self.roiPath = QLineEdit(self.reqGroup)
        self.roiPath.setObjectName(u"roiPath")
        self.roiPath.setFont(font1)

        self.roiLayout.addWidget(self.roiPath)

        self.roiButton = QPushButton(self.reqGroup)
        self.roiButton.setObjectName(u"roiButton")
        self.roiButton.setMinimumSize(QSize(200, 0))
        self.roiButton.setFont(font1)

        self.roiLayout.addWidget(self.roiButton)


        self.reqLayout.addLayout(self.roiLayout)


        self.loaderLayout.addWidget(self.reqGroup)

        self.upperLine = QFrame(self.loaderWidget)
        self.upperLine.setObjectName(u"upperLine")
        self.upperLine.setFrameShape(QFrame.Shape.HLine)
        self.upperLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.loaderLayout.addWidget(self.upperLine)

        self.optGroup = QGroupBox(self.loaderWidget)
        self.optGroup.setObjectName(u"optGroup")
        self.optGroup.setFont(font)
        self.optLayout = QVBoxLayout(self.optGroup)
        self.optLayout.setObjectName(u"optLayout")
        self.aitLayout = QHBoxLayout()
        self.aitLayout.setObjectName(u"aitLayout")
        self.aitPath = QLineEdit(self.optGroup)
        self.aitPath.setObjectName(u"aitPath")
        self.aitPath.setFont(font1)

        self.aitLayout.addWidget(self.aitPath)

        self.aitButton = QPushButton(self.optGroup)
        self.aitButton.setObjectName(u"aitButton")
        self.aitButton.setMinimumSize(QSize(200, 0))
        self.aitButton.setFont(font1)

        self.aitLayout.addWidget(self.aitButton)


        self.optLayout.addLayout(self.aitLayout)

        self.hmlLayout = QHBoxLayout()
        self.hmlLayout.setObjectName(u"hmlLayout")
        self.hmlPath = QLineEdit(self.optGroup)
        self.hmlPath.setObjectName(u"hmlPath")
        self.hmlPath.setFont(font1)

        self.hmlLayout.addWidget(self.hmlPath)

        self.hmlButton = QPushButton(self.optGroup)
        self.hmlButton.setObjectName(u"hmlButton")
        self.hmlButton.setMinimumSize(QSize(200, 0))
        self.hmlButton.setFont(font1)

        self.hmlLayout.addWidget(self.hmlButton)


        self.optLayout.addLayout(self.hmlLayout)

        self.jslLayout = QHBoxLayout()
        self.jslLayout.setObjectName(u"jslLayout")
        self.jslPath = QLineEdit(self.optGroup)
        self.jslPath.setObjectName(u"jslPath")
        self.jslPath.setFont(font1)

        self.jslLayout.addWidget(self.jslPath)

        self.jslButton = QPushButton(self.optGroup)
        self.jslButton.setObjectName(u"jslButton")
        self.jslButton.setMinimumSize(QSize(200, 0))
        self.jslButton.setFont(font1)

        self.jslLayout.addWidget(self.jslButton)


        self.optLayout.addLayout(self.jslLayout)


        self.loaderLayout.addWidget(self.optGroup)

        self.lowerLine = QFrame(self.loaderWidget)
        self.lowerLine.setObjectName(u"lowerLine")
        self.lowerLine.setFrameShape(QFrame.Shape.HLine)
        self.lowerLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.loaderLayout.addWidget(self.lowerLine)

        self.controlLayout = QHBoxLayout()
        self.controlLayout.setSpacing(50)
        self.controlLayout.setObjectName(u"controlLayout")
        self.controlLayout.setContentsMargins(0, 0, 0, 0)
        self.loadButton = QPushButton(self.loaderWidget)
        self.loadButton.setObjectName(u"loadButton")
        self.loadButton.setFont(font)

        self.controlLayout.addWidget(self.loadButton)

        self.exitButton = QPushButton(self.loaderWidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setFont(font)

        self.controlLayout.addWidget(self.exitButton)


        self.loaderLayout.addLayout(self.controlLayout)

        MainLoader.setCentralWidget(self.loaderWidget)

        self.retranslateUi(MainLoader)

        QMetaObject.connectSlotsByName(MainLoader)


    def retranslateUi(self, MainLoader):
        MainLoader.setWindowTitle(QCoreApplication.translate("MainLoader", u"MEGIT Cross Verification Loader", None))
        self.reqGroup.setTitle(QCoreApplication.translate("MainLoader", u"Required Files", None))
        self.frmButton.setText(QCoreApplication.translate("MainLoader", u"Choose Frame File", None))
        self.crsButton.setText(QCoreApplication.translate("MainLoader", u"Choose Cross CSV File", None))
        self.roiButton.setText(QCoreApplication.translate("MainLoader", u"Choose ROI File", None))
        self.optGroup.setTitle(QCoreApplication.translate("MainLoader", u"Optional Files", None))
        self.aitPath.setToolTip(QCoreApplication.translate("MainLoader", u"This file is required to activate"
                                                                         u"[Intelligent Mode]", None))
        self.aitButton.setToolTip(QCoreApplication.translate("MainLoader", u"This file is required to activate"
                                                                           u"[Intelligent Mode]", None))
        self.aitButton.setText(QCoreApplication.translate("MainLoader", u"Choose Average Intensity File", None))
        self.hmlPath.setToolTip(QCoreApplication.translate("MainLoader", u"This file is required to activate"
                                                                         u"[Show HeatMap Label]", None))
        self.hmlButton.setToolTip(QCoreApplication.translate("MainLoader", u"This file is required to activate"
                                                                           u"[Show HeatMap Label]", None))
        self.hmlButton.setText(QCoreApplication.translate("MainLoader", u"Choose HeatMap Prediction File", None))
        self.jslPath.setToolTip(QCoreApplication.translate("MainLoader", u"This file is required to activate"
                                                                         u"[Show JSON Label]", None))
        self.jslButton.setToolTip(QCoreApplication.translate("MainLoader", u"This file is required to activate"
                                                                           u"[Show JSON Label]", None))
        self.jslButton.setText(QCoreApplication.translate("MainLoader", u"Choose JSON Prediction File", None))
        self.loadButton.setText(QCoreApplication.translate("MainLoader", u"Load", None))
        self.exitButton.setText(QCoreApplication.translate("MainLoader", u"Exit", None))
