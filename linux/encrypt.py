# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encrypt.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_encryptUI(object):
    def setupUi(self, encryptUI):
        encryptUI.setObjectName("encryptUI")
        encryptUI.resize(772, 588)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(encryptUI)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.outputDir = QtWidgets.QLineEdit(encryptUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputDir.sizePolicy().hasHeightForWidth())
        self.outputDir.setSizePolicy(sizePolicy)
        self.outputDir.setReadOnly(True)
        self.outputDir.setObjectName("outputDir")
        self.horizontalLayout.addWidget(self.outputDir)
        self.changeDir = QtWidgets.QPushButton(encryptUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changeDir.sizePolicy().hasHeightForWidth())
        self.changeDir.setSizePolicy(sizePolicy)
        self.changeDir.setMaximumSize(QtCore.QSize(40, 23))
        self.changeDir.setObjectName("changeDir")
        self.horizontalLayout.addWidget(self.changeDir)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnPassword = QtWidgets.QLineEdit(encryptUI)
        self.btnPassword.setObjectName("btnPassword")
        self.verticalLayout.addWidget(self.btnPassword)
        self.btnPassword2 = QtWidgets.QLineEdit(encryptUI)
        self.btnPassword2.setObjectName("btnPassword2")
        self.verticalLayout.addWidget(self.btnPassword2)
        self.logEdit = QtWidgets.QPlainTextEdit(encryptUI)
        self.logEdit.setReadOnly(True)
        self.logEdit.setObjectName("logEdit")
        self.verticalLayout.addWidget(self.logEdit)
        self.progressBar = QtWidgets.QProgressBar(encryptUI)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("color {\n"
"#000000\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.buttonOK = QtWidgets.QPushButton(encryptUI)
        self.buttonOK.setObjectName("buttonOK")
        self.verticalLayout.addWidget(self.buttonOK)
        self.buttonClose = QtWidgets.QPushButton(encryptUI)
        self.buttonClose.setObjectName("buttonClose")
        self.verticalLayout.addWidget(self.buttonClose)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(encryptUI)
        QtCore.QMetaObject.connectSlotsByName(encryptUI)

    def retranslateUi(self, encryptUI):
        _translate = QtCore.QCoreApplication.translate
        encryptUI.setWindowTitle(_translate("encryptUI", "Form"))
        self.changeDir.setText(_translate("encryptUI", "..."))
        self.btnPassword.setPlaceholderText(_translate("encryptUI", "Password"))
        self.btnPassword2.setPlaceholderText(_translate("encryptUI", "Confirm Password"))
        self.buttonOK.setText(_translate("encryptUI", "Encrypt"))
        self.buttonClose.setText(_translate("encryptUI", "Close"))

