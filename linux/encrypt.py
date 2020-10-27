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
        encryptUI.setStyleSheet("QPlainTextEdit{\n"
"line-height: 1.6;\n"
"}\n"
"QScrollBar:vertical {\n"
"        border: 1px solid #ffffff;\n"
"        background:1e1e1e;\n"
"        width:10px;\n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"QScrollBar::handle:vertical {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
"        min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"    QScrollBar::sub-line:vertical {\n"
"       height: 0 px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"")
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
        self.logEdit.setPlainText("")
        self.logEdit.setObjectName("logEdit")
        self.verticalLayout.addWidget(self.logEdit)
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

