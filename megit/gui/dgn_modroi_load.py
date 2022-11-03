# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\megit\gui\dgn_modroi_load.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainLoader(object):
    def setupUi(self, MainLoader):
        MainLoader.setObjectName("MainLoader")
        MainLoader.resize(600, 130)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainLoader.sizePolicy().hasHeightForWidth())
        MainLoader.setSizePolicy(sizePolicy)
        MainLoader.setMinimumSize(QtCore.QSize(600, 130))
        MainLoader.setMaximumSize(QtCore.QSize(16777215, 210))
        self.loaderWidget = QtWidgets.QWidget(MainLoader)
        self.loaderWidget.setObjectName("loaderWidget")
        self.loaderLayout = QtWidgets.QVBoxLayout(self.loaderWidget)
        self.loaderLayout.setContentsMargins(10, 10, 10, 10)
        self.loaderLayout.setSpacing(10)
        self.loaderLayout.setObjectName("loaderLayout")
        self.inputGroup = QtWidgets.QGroupBox(self.loaderWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inputGroup.setFont(font)
        self.inputGroup.setObjectName("inputGroup")
        self.inputLayout = QtWidgets.QHBoxLayout(self.inputGroup)
        self.inputLayout.setContentsMargins(10, 10, 10, 10)
        self.inputLayout.setSpacing(5)
        self.inputLayout.setObjectName("inputLayout")
        self.inputPath = QtWidgets.QLineEdit(self.inputGroup)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.inputPath.setFont(font)
        self.inputPath.setObjectName("inputPath")
        self.inputLayout.addWidget(self.inputPath)
        self.inputButton = QtWidgets.QPushButton(self.inputGroup)
        self.inputButton.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.inputButton.setFont(font)
        self.inputButton.setObjectName("inputButton")
        self.inputLayout.addWidget(self.inputButton)
        self.loaderLayout.addWidget(self.inputGroup)
        self.sepLine = QtWidgets.QFrame(self.loaderWidget)
        self.sepLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.sepLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sepLine.setObjectName("sepLine")
        self.loaderLayout.addWidget(self.sepLine)
        self.controlLayout = QtWidgets.QHBoxLayout()
        self.controlLayout.setContentsMargins(0, 0, 0, 0)
        self.controlLayout.setSpacing(50)
        self.controlLayout.setObjectName("controlLayout")
        self.loadButton = QtWidgets.QPushButton(self.loaderWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loadButton.setFont(font)
        self.loadButton.setObjectName("loadButton")
        self.controlLayout.addWidget(self.loadButton)
        self.exitButton = QtWidgets.QPushButton(self.loaderWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.controlLayout.addWidget(self.exitButton)
        self.loaderLayout.addLayout(self.controlLayout)
        MainLoader.setCentralWidget(self.loaderWidget)

        self.retranslateUi(MainLoader)
        QtCore.QMetaObject.connectSlotsByName(MainLoader)

    def retranslateUi(self, MainLoader):
        _translate = QtCore.QCoreApplication.translate
        MainLoader.setWindowTitle(_translate("MainLoader", "MEGIT ROI Modification Loader"))
        self.inputGroup.setTitle(_translate("MainLoader", "Preprocessed Frame Directory"))
        self.inputButton.setText(_translate("MainLoader", "Choose Directory"))
        self.loadButton.setText(_translate("MainLoader", "Load"))
        self.exitButton.setText(_translate("MainLoader", "Exit"))