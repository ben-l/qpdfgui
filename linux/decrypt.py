# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decrypt.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_decryptUI(object):
    def setupUi(self, decryptUI):
        decryptUI.setObjectName("decryptUI")
        decryptUI.resize(716, 539)
        decryptUI.setStyleSheet("QWidget {\n"
"padding: 5px;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(decryptUI)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.outputDir = QtWidgets.QLineEdit(decryptUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputDir.sizePolicy().hasHeightForWidth())
        self.outputDir.setSizePolicy(sizePolicy)
        self.outputDir.setReadOnly(True)
        self.outputDir.setObjectName("outputDir")
        self.horizontalLayout.addWidget(self.outputDir)
        self.changeDir = QtWidgets.QPushButton(decryptUI)
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
        self.btnPassword = QtWidgets.QLineEdit(decryptUI)
        self.btnPassword.setObjectName("btnPassword")
        self.verticalLayout.addWidget(self.btnPassword)
        self.logEdit = QtWidgets.QPlainTextEdit(decryptUI)
        self.logEdit.setReadOnly(True)
        self.logEdit.setObjectName("logEdit")
        self.verticalLayout.addWidget(self.logEdit)
        self.buttonOK = QtWidgets.QPushButton(decryptUI)
        self.buttonOK.setObjectName("buttonOK")
        self.verticalLayout.addWidget(self.buttonOK)
        self.buttonClose = QtWidgets.QPushButton(decryptUI)
        self.buttonClose.setObjectName("buttonClose")
        self.verticalLayout.addWidget(self.buttonClose)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(decryptUI)
        QtCore.QMetaObject.connectSlotsByName(decryptUI)

    def retranslateUi(self, decryptUI):
        _translate = QtCore.QCoreApplication.translate
        decryptUI.setWindowTitle(_translate("decryptUI", "Form"))
        self.changeDir.setText(_translate("decryptUI", "..."))
        self.btnPassword.setPlaceholderText(_translate("decryptUI", "Password"))
        self.buttonOK.setText(_translate("decryptUI", "Decrypt"))
        self.buttonClose.setText(_translate("decryptUI", "Close"))

