# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_design_test.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QInputDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.btnOpenFolder = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemoveFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnClearAll = QtWidgets.QPushButton(self.centralwidget)
        self.btnEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.btnPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnPassword.show()
        self.AESOption = QtWidgets.QComboBox(self.centralwidget)
        self.ShowPassword = QtWidgets.QCheckBox("Show Password", self.centralwidget)
        self.btnPassword2 = QtWidgets.QInputDialog(self.centralwidget)
        self.btnOpenFolder.setObjectName("btnOpenFolder")
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.btnRemoveFile.setObjectName("btnRemoveFile")
        self.btnClearAll.setObjectName("btnClearAll")
        self.btnPassword.setObjectName("btnPassword")
        self.btnPassword.setPlaceholderText("Password")
        self.btnPassword2.setObjectName("btnPassword2")
        self.AESOption.setObjectName("AESOption")
        self.btnEncrypt.setObjectName("btnEncrypt")
        self.btnDecrypt.setObjectName("btnDecrypt")
        self.verticalLayout.addWidget(self.btnOpenFolder)
        self.verticalLayout.addWidget(self.btnOpenFile)
        self.verticalLayout.addWidget(self.btnRemoveFile)
        self.verticalLayout.addWidget(self.btnClearAll)
        self.verticalLayout.addWidget(self.btnPassword)
        self.verticalLayout.addWidget(self.ShowPassword)
        self.verticalLayout.addWidget(self.btnPassword2)
        self.verticalLayout.addWidget(self.AESOption)
        self.verticalLayout.addWidget(self.btnEncrypt)
        self.verticalLayout.addWidget(self.btnDecrypt)
        self.listWidget.raise_()
        self.btnOpenFolder.raise_()
        self.btnOpenFile.raise_()
        self.btnRemoveFile.raise_()
        self.btnClearAll.raise_()
        self.btnPassword.raise_()
        self.ShowPassword.raise_()
        self.btnPassword2.raise_()
        self.AESOption.raise_()
        self.btnEncrypt.raise_()
        self.btnDecrypt.raise_()
        self.AESOption.addItem("AES-40")
        self.AESOption.addItem("AES-128")
        self.AESOption.addItem("AES-256")
        self.AESOption.setCurrentIndex(2) #set AES-256 as the default option in the dropdown
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QPDF"))
        self.btnOpenFolder.setText(_translate("MainWindow", "Import Folder"))
        self.btnOpenFile.setText(_translate("MainWindow", "Import File"))
        self.btnRemoveFile.setText(_translate("MainWindow", "Remove File From List"))
        self.btnClearAll.setText(_translate("MainWindow", "Clear All From List"))
        self.btnEncrypt.setText(_translate("MainWindow", "Encrypt to ..."))
        self.btnDecrypt.setText(_translate("MainWindow", "Decrypt to ..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())