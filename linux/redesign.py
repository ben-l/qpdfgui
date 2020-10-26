# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qpdf-redesign.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget{\n"
"background-color: #1E1E1E;\n"
"color: #ffffff;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QToolBar{ \n"
"font-weight: bold;\n"
"padding: 5px; \n"
"}\n"
"\n"
"QListWidget{ \n"
"color: #ffffff;\n"
"font-weight: bold;\n"
"padding: 5px;\n"
"outline: 0;\n"
"}\n"
"\n"
"QListWidget::item:hover{\n"
"    background-color: #18ff94;\n"
"    color: #1E1E1E;\n"
"}\n"
"\n"
"QListWidget::item::selected{\n"
"    background-color: #18ff94;\n"
"    color: #1E1E1E;\n"
"    outline:0;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #3E3E42;\n"
"font-weight: bold;\n"
"color: #ffffff\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #18ff94;\n"
"font-weight: bold;\n"
"color: #1E1E1E;\n"
"}\n"
"QScrollBar{\n"
"        border: 1px solid #ffffff;\n"
"}\n"
"QScrollBar:vertical {\n"
"        width:12px;\n"
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
"QScrollBar:horizontal {\n"
"            height: 12px;\n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"\n"
"        QScrollBar::handle:horizontal {\n"
"            /* background: lightgray;*/\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
"            min-height: 0px;\n"
"            min-width: 26px;\n"
"        }\n"
"\n"
"        QScrollBar::add-line:horizontal {\n"
"           width: 26px;\n"
"            subcontrol-position: right;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"  QScrollBar::sub-line:horizontal {\n"
"       height: 0 px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setAcceptDrops(False)
        self.listWidget.setToolTip("")
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.toolBar.setFont(font)
        self.toolBar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar.setIconSize(QtCore.QSize(27, 27))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.btnOpenFile = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/file_pdf [#1729].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOpenFile.setIcon(icon)
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.btnOpenFolder = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resources/folder__plus_fill [#1788].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOpenFolder.setIcon(icon1)
        self.btnOpenFolder.setObjectName("btnOpenFolder")
        self.btnRemoveFile = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/resources/delete [#1487].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRemoveFile.setIcon(icon2)
        self.btnRemoveFile.setObjectName("btnRemoveFile")
        self.btnEncrypt = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/resources/lock_close [#705].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEncrypt.setIcon(icon3)
        self.btnEncrypt.setObjectName("btnEncrypt")
        self.btnDecrypt = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/resources/lock_open [#706].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDecrypt.setIcon(icon4)
        self.btnDecrypt.setObjectName("btnDecrypt")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/resources/arrow_in_right [#385].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon5)
        self.actionExit.setObjectName("actionExit")
        self.ShowPassword = QtWidgets.QAction(MainWindow)
        self.ShowPassword.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/resources/view_simple [#815].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ShowPassword.setIcon(icon6)
        self.ShowPassword.setObjectName("ShowPassword")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/resources/edit [#1479].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit.setIcon(icon7)
        self.actionEdit.setObjectName("actionEdit")
        self.toolBar.addAction(self.btnOpenFile)
        self.toolBar.addAction(self.btnOpenFolder)
        self.toolBar.addAction(self.btnRemoveFile)
        self.toolBar.addAction(self.btnEncrypt)
        self.toolBar.addAction(self.btnDecrypt)
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.btnOpenFile.setText(_translate("MainWindow", "Import File"))
        self.btnOpenFile.setToolTip(_translate("MainWindow", "Import File"))
        self.btnOpenFolder.setText(_translate("MainWindow", "Import Folder"))
        self.btnOpenFolder.setToolTip(_translate("MainWindow", "Import Folder"))
        self.btnRemoveFile.setText(_translate("MainWindow", "Delete"))
        self.btnRemoveFile.setToolTip(_translate("MainWindow", "Delete Selected Files(s)"))
        self.btnEncrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btnEncrypt.setToolTip(_translate("MainWindow", "Encrypt"))
        self.btnDecrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btnDecrypt.setToolTip(_translate("MainWindow", "Decrypt"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit"))
        self.ShowPassword.setText(_translate("MainWindow", "Show Password"))
        self.ShowPassword.setToolTip(_translate("MainWindow", "Show Password"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
        self.actionEdit.setToolTip(_translate("MainWindow", "Edit"))

import resources_rc
