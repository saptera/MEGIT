# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dgn_preproc_load.ui'
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
        MainLoader.resize(600, 210)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainLoader.sizePolicy().hasHeightForWidth())
        MainLoader.setSizePolicy(sizePolicy)
        MainLoader.setMinimumSize(QSize(600, 210))
        MainLoader.setMaximumSize(QSize(16777215, 210))
        self.loaderWidget = QWidget(MainLoader)
        self.loaderWidget.setObjectName(u"loaderWidget")
        self.loaderLayout = QVBoxLayout(self.loaderWidget)
        self.loaderLayout.setSpacing(10)
        self.loaderLayout.setObjectName(u"loaderLayout")
        self.loaderLayout.setContentsMargins(10, 10, 10, 10)
        self.videoGroup = QGroupBox(self.loaderWidget)
        self.videoGroup.setObjectName(u"videoGroup")
        font = QFont()
        font.setBold(True)
        self.videoGroup.setFont(font)
        self.videoLayout = QHBoxLayout(self.videoGroup)
        self.videoLayout.setSpacing(5)
        self.videoLayout.setObjectName(u"videoLayout")
        self.videoLayout.setContentsMargins(10, 10, 10, 10)
        self.videoPath = QLineEdit(self.videoGroup)
        self.videoPath.setObjectName(u"videoPath")
        font1 = QFont()
        font1.setBold(False)
        self.videoPath.setFont(font1)

        self.videoLayout.addWidget(self.videoPath)

        self.videoButton = QPushButton(self.videoGroup)
        self.videoButton.setObjectName(u"videoButton")
        self.videoButton.setMinimumSize(QSize(100, 0))
        self.videoButton.setFont(font1)

        self.videoLayout.addWidget(self.videoButton)


        self.loaderLayout.addWidget(self.videoGroup)

        self.upperLine = QFrame(self.loaderWidget)
        self.upperLine.setObjectName(u"upperLine")
        self.upperLine.setFrameShape(QFrame.Shape.HLine)
        self.upperLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.loaderLayout.addWidget(self.upperLine)

        self.outputGroup = QGroupBox(self.loaderWidget)
        self.outputGroup.setObjectName(u"outputGroup")
        self.outputGroup.setFont(font)
        self.outputLayout = QHBoxLayout(self.outputGroup)
        self.outputLayout.setSpacing(5)
        self.outputLayout.setObjectName(u"outputLayout")
        self.outputLayout.setContentsMargins(10, 10, 10, 10)
        self.outputPath = QLineEdit(self.outputGroup)
        self.outputPath.setObjectName(u"outputPath")
        self.outputPath.setFont(font1)

        self.outputLayout.addWidget(self.outputPath)

        self.outputButton = QPushButton(self.outputGroup)
        self.outputButton.setObjectName(u"outputButton")
        self.outputButton.setMinimumSize(QSize(100, 0))
        self.outputButton.setFont(font1)

        self.outputLayout.addWidget(self.outputButton)


        self.loaderLayout.addWidget(self.outputGroup)

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
        MainLoader.setWindowTitle(QCoreApplication.translate("MainLoader", u"MEGIT Pre-Processing Loader", None))
        self.videoGroup.setTitle(QCoreApplication.translate("MainLoader", u"Select Video", None))
        self.videoButton.setText(QCoreApplication.translate("MainLoader", u"Choose Video", None))
        self.outputGroup.setTitle(QCoreApplication.translate("MainLoader", u"Output Directory", None))
        self.outputButton.setText(QCoreApplication.translate("MainLoader", u"Choose Directory", None))
        self.loadButton.setText(QCoreApplication.translate("MainLoader", u"Load", None))
        self.exitButton.setText(QCoreApplication.translate("MainLoader", u"Exit", None))
