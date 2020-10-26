from PyQt5.QtGui import QMovie, QPixmap, QIcon
from PyQt5.QtCore import (Qt, QTimer, QSize, QThread, pyqtSignal,
                          QObject, QModelIndex)
from PyQt5.QtWidgets import (QMainWindow, QApplication, QFileDialog,
                             QInputDialog, QMessageBox, QLineEdit,
                             QCheckBox, QWidget, QProgressBar, QLabel,
                             QDialog, QGridLayout, QPushButton, QAction,
                             QHBoxLayout)
from pathlib import Path
from subprocess import Popen, PIPE
import datetime
import decrypt
import design
import encrypt
import logging
import os
import queue
import redesign
import shlex
import subprocess
import sys
import threading


class bcolors:
    FAIL = '\033[91m'
    OKGREEN = '\033[92m'


class DecryptScreen(QDialog, decrypt.Ui_decryptUI):
    appendSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        self.resize(800, 443)
        self.changeDir.clicked.connect(self.change_outputdir)
        self.btnPassword.setEchoMode(QLineEdit.Password)
        self.buttonOK.clicked.connect(self.disable_btns)
        self.buttonClose.clicked.connect(self.close)
        self.default_output_dir = self.parent.default_output_dir
        self.outputDir.setText(self.parent.default_output_dir)
        self.setWindowTitle("Decrypt")

        # Threads and Signals
        self.maxthreads = 1
        self.sema = threading.Semaphore(value=self.maxthreads)
        self.threads = []
        self.appendSignal.connect(self.reallyAppendToTextEdit)

        # final status
        self.startTime = 0
        self.successful = []
        self.warnings = []
        self.errors = []

        # show password
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/icons/resources/view_simple [#815].png"),
                        QIcon.Normal, QIcon.Off)
        self.reveal = self.btnPassword.addAction(icon1,
                                                 QLineEdit.TrailingPosition)
        self.reveal.triggered.connect(self.show_password)
        self.password_shown = False

        self.show()

    def show_password(self):
        if not self.password_shown:
            self.btnPassword.setEchoMode(QLineEdit.Normal)
            self.password_shown = True
        else:
            self.btnPassword.setEchoMode(QLineEdit.Password)
            self.password_shown = False

    def change_outputdir(self):
        # replace None with self to use non-native qfiledialog
        default_output_dir = \
                QFileDialog.getExistingDirectory(self,
                                                 "Choose Output Directory",
                                                 self.parent.default_open_loc)
        if default_output_dir:
            self.default_output_dir = default_output_dir
            self.outputDir.setText(self.default_output_dir)
        else:
            self.default_output_dir = self.parent.default_output_dir
            self.outputDir.setText(self.parent.default_output_dir)

    def disable_btns(self):
        self.buttonOK.setEnabled(False)
        self.btnPassword.setEnabled(False)
        self.decrypt()

    def renable_btns(self):
        self.buttonOK.setEnabled(True)
        self.btnPassword.setEnabled(True)
        self.btnPassword2.setEnabled(True)

    def reallyAppendToTextEdit(self, txt):
        self.logEdit.appendPlainText(txt)

    def runcmd(self, *cmd):
        self.sema.acquire()
        filename = cmd[3]
        print(filename)
        try:
            self.startTime = datetime.datetime.now()
        except TypeError:
            pass
        process = subprocess.Popen([*cmd], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8')
        while True:
            # the process will hang because output is a byte array
            # make sure to decode readline
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                self.appendToTextEdit = self.appendSignal.emit
                self.appendToTextEdit(output.strip())
                print(output.strip())
        self.sema.release()
        rc = process.poll()
        if rc == 1 or rc == 2:
            # these are errors
            self.errors.append(filename)
        elif rc == 3:
            # these are warnings, safe to ignore
            self.warnings.append(filename)
        else:
            self.successful.append(filename)

    def thread_status(self):
        print(threading.enumerate())
        while self.thread1.is_alive():
            if self.thread1.is_alive() is False:
                break
        time_completed = datetime.datetime.now() - self.startTime
        self.appendToTextEdit("\nTime Elapsed: {}".format(time_completed))
        if len(self.successful):
            self.appendToTextEdit("{} file(s) successful".format(len(self.successful)))
        if len(self.warnings):
            self.appendToTextEdit("{} file(s) successful with a warning".format(len(self.warnings)))
        if len(self.errors):
            self.appendToTextEdit("{} file(s) encountered an ERROR".format(len(self.errors)))
        self.renable_btns()

    def decrypt(self):
        self.logEdit.clear()
        successful = []
        warnings = []
        errors = []

        identifier = '(decry)'
        itemsTextList = [str(self.parent.listWidget.item(i).text())
                         for i in range(self.parent.listWidget.count())]
        for item in itemsTextList:
            new_file_path = Path(item)
            suffix = new_file_path.suffix
            new_filename = new_file_path.stem+identifier+suffix
            self.thread1 = threading.Thread(target=self.runcmd, args=(self.parent.program, "--decrypt", "--password={}".format(self.btnPassword.text()), item, os.path.join(self.default_output_dir, new_filename), "--progress",))
            self.thread1.daemon = True
            self.thread1.start()
        self.thread2 = threading.Thread(target=self.thread_status)
        self.thread2.daemon = True
        self.thread2.start()


class EncryptScreen(QDialog, encrypt.Ui_encryptUI):
    appendSignal = pyqtSignal(str)
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.parent = parent
        self.setupUi(self)
        # setWindowModality stops user from interacting with parent window
        # whilst the child window is open
        self.setWindowModality(Qt.ApplicationModal)
        # this gets sized in encrypt.py
        # and then resized here - need to change
        self.resize(800, 443)
        self.outputDir.setText(self.parent.default_output_dir)
        self.changeDir.clicked.connect(self.change_outputdir)
        self.btnPassword.setEchoMode(QLineEdit.Password)
        self.btnPassword2.setEchoMode(QLineEdit.Password)
        self.buttonOK.clicked.connect(self.disable_btns)
        self.buttonClose.clicked.connect(self.close)
        self.appendSignal.connect(self.reallyAppendToTextEdit)
        self.setWindowTitle("Encrypt")
        self.default_output_dir = self.parent.default_output_dir
        # show password
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/icons/resources/view_simple [#815].png"),
                        QIcon.Normal, QIcon.Off)
        self.reveal = self.btnPassword.addAction(icon1,
                                                 QLineEdit.TrailingPosition)
        self.reveal2 = self.btnPassword2.addAction(icon1,
                                                   QLineEdit.TrailingPosition)
        self.reveal.triggered.connect(self.show_password)
        self.reveal2.triggered.connect(self.show_password2)
        self.password_shown = False

        # Threads
        self.maxthreads = 1
        self.sema = threading.Semaphore(value=self.maxthreads)
        self.threads = []

        # final status
        self.startTime = 0
        self.successful = []
        self.warnings = []
        self.errors = []

        self.show()
        # create new instance of Logger
        # which is then destroyed when clicking encrypt
        # after which another instance is created
        # to ensure logs are refreshed everytime user clicks encrypt
        # and for everytime user closes and reopens encrypt screen

        # self.log_inst = Logger(self)

        # resize window for testing

    def resizeEvent(self, event):
        print("resize")
        print("Width: {}".format(event.size().width()))
        print("Height: {}".format(event.size().height()))


    def show_password(self):
        if not self.password_shown:
            self.btnPassword.setEchoMode(QLineEdit.Normal)
            self.password_shown = True
        else:
            self.btnPassword.setEchoMode(QLineEdit.Password)
            self.password_shown = False

    def show_password2(self):
        if not self.password_shown:
            self.btnPassword2.setEchoMode(QLineEdit.Normal)
            self.password_shown = True
        else:
            self.btnPassword2.setEchoMode(QLineEdit.Password)
            self.password_shown = False

    def change_outputdir(self):
        # replace None with self to use non-native qfiledialog
        default_output_dir = QFileDialog.getExistingDirectory(self,
                                                              "Choose Output Directory", self.parent.default_open_loc)
        if default_output_dir:
            self.default_output_dir = default_output_dir
            self.outputDir.setText(self.default_output_dir)
        else:
            self.default_output_dir = self.parent.default_output_dir
            self.outputDir.setText(self.parent.default_output_dir)

    def onButtonClick(self):
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.countChanged.connect(self.onCountChanged)
        self.worker.finished.connect(self.evt_worker_finished)
        return self.worker

    def evt_worker_finished(self):
        print("worker thread complete")

    def onCountChanged(self, value):
        self.progressBar.setValue(value)
        self.progressBar.setProperty("value", value)
        print(value)

    def disable_btns(self):
        self.buttonOK.setEnabled(False)
        self.btnPassword.setEnabled(False)
        self.btnPassword2.setEnabled(False)
        self.encrypt(self.btnPassword, self.btnPassword2)

    def renable_btns(self):
        self.buttonOK.setEnabled(True)
        self.btnPassword.setEnabled(True)
        self.btnPassword2.setEnabled(True)

    def reallyAppendToTextEdit(self, txt):
        self.logEdit.appendPlainText(txt)

    def runcmd(self, *cmd):
        self.sema.acquire()
        filename = cmd[6]
        try:
            self.startTime = datetime.datetime.now()
        except TypeError:
            pass
        process = subprocess.Popen([*cmd], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8')
        while True:
            # the process will hang because output is a byte array
            # make sure to decode readline
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                self.appendToTextEdit = self.appendSignal.emit
                self.appendToTextEdit(output.strip())
                print(output.strip())
        self.sema.release()
        rc = process.poll()
        if rc == 1 or rc == 2:
            # these are errors
            self.errors.append(filename)
        elif rc == 3:
            # these are warnings, safe to ignore
            self.warnings.append(filename)
        else:
            self.successful.append(filename)

    def thread_status(self):
        print(threading.enumerate())
        while self.thread1.is_alive():
            if self.thread1.is_alive() is False:
                break
        time_completed = datetime.datetime.now() - self.startTime
        self.appendToTextEdit("\nTime Elapsed: {}".format(time_completed))
        if len(self.successful):
            self.appendToTextEdit("{} file(s) successful".format(len(self.successful)))
        if len(self.warnings):
            self.appendToTextEdit("{} file(s) successful with a warning".format(len(self.warnings)))
        if len(self.errors):
            self.appendToTextEdit("{} file(s) encountered an ERROR".format(len(self.errors)))
        self.renable_btns()


    def encrypt(self, passwd, passwd2):
        self.logEdit.clear()

        # reset lists
        successful = []
        warnings = []
        errors = []

        identifier = '(encry)'
        # aes_choice = self.AESOption.activated[int]
        # aes_choice = str(self.AESOption.currentText()).strip('AES-')
        itemsTextList = [str(self.parent.listWidget.item(i).text()) for i in range(self.parent.listWidget.count())]
        if passwd.text() != passwd2.text():
            self.logEdit.insertPlainText("ERROR: Passwords do not match")
            self.renable_btns()
            successful.append(1)
        elif passwd.text() == passwd2.text():
            for item in itemsTextList:
                new_file_path = Path(item)
                suffix = new_file_path.suffix
                new_filename = new_file_path.stem+identifier+suffix
                self.thread1 = threading.Thread(target = self.runcmd, args = (self.parent.program, "--encrypt", self.btnPassword.text(), self.btnPassword2.text(), "256", "--", item, os.path.join(self.default_output_dir, new_filename), "--progress",))
                self.thread1.daemon = True
                self.thread1.start()
        self.thread2 = threading.Thread(target = self.thread_status)
        self.thread2.daemon = True
        self.thread2.start()


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        # setWindowModality stops user from interacting with parent window
        # whilst the child window is open
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(64, 64)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        self.label_animation = QLabel(self)

        self.movie = QMovie('loading.gif')

        self.label_animation.setMovie(self.movie)

        # timer = QTimer(self)

        self.startAnimation()
        # timer.singleShot(3000, self.stopAnimation)

        self.show()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()


class ExampleApp(QMainWindow, redesign.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        if os.name == 'posix':
            #  linux os
            self.default_open_loc = os.path.expanduser('~/')
            self.default_output_dir = os.path.expanduser('~/Downloads')
            self.program = 'qpdf'
        elif os.name == 'nt':
            # windows os
            self.default_open_loc = os.path.expandvars(r'%USERPROFILE%')
            self.default_output_dir = os.path.expandvars(r'%USERPROFILE%\Downloads')
            self.program = 'qpdf.exe'
        self.setupUi(self)
        self.actionExit.triggered.connect(self.exit)
        self.btnOpenFolder.triggered.connect(self.open_folder)
        self.btnOpenFile.triggered.connect(self.add_file)
        self.btnRemoveFile.triggered.connect(self.remove_file)
        # self.btnClearAll.triggered.connect(self.clear_all)
        self.btnEncrypt.triggered.connect(self.encrypt_screen)
        self.btnDecrypt.triggered.connect(self.decrypt_screen)
        # self.AESOption.activated[int]

        # remove initial dotted line/focus from qlistwidget item
        self.listWidget.setCurrentIndex(QModelIndex())
        """
        if len(unsuccessful) > 0:
            self.show_dialog(icon=QMessageBox.Warning,
                             text="Bad Password for {} file(s):\n{}".format(len(unsuccessful), "\n".join(unsuccessful)),
                             window_title="decrypt")
        if len(success) > 0:
            self.show_dialog(icon=QMessageBox.Information,
                             text="{} pdf(s) successfully decrypted:\n{}".format(len(success), "\n".join(success)),
                             window_title="decrypt")
        """

    def exit(self):
        sys.exit(0)

    def show_dialog(self, icon=None, text=None, window_title=None):
        msg = QMessageBox(self)
        msg.setIcon(icon)
        msg.setText(text)
        msg.setWindowTitle(window_title)
        msg.exec_()

    def show_progress_bar(self):
        w = QMessageBox(self)
        w.setText("test")
        self.progress = QProgressBar()
        self.progress.setGeometry(200, 80, 250, 20)
        # w.setFixedSize(100, 100)
        # w.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        w.exec_()

        # self.progress = QProgressBar(self)
        # self.progress.setGeometry(200, 80, 250, 20)

    def open_folder(self):
        # replace None with self to use non-native qfiledialog
        directory = QFileDialog.getExistingDirectory(self, "Import Folder",
                                                     self.default_open_loc)
        if directory:
            for file in os.listdir(directory):
                if file.endswith(".pdf"):
                    filter = os.path.join(directory, file)
                    self.listWidget.addItem(filter)

    def add_file(self):
        # replace None with self to use non-native qfiledialog
        file, _ = QFileDialog.getOpenFileNames(self, "Import Files",
                                               self.default_open_loc,
                                               filter='*.pdf')
        if file:
            for f in file:
                self.listWidget.addItem(f)

    def remove_file(self):
        for SelectedItem in self.listWidget.selectedItems():
            self.listWidget.takeItem(self.listWidget.row(SelectedItem))

    def clear_all(self):
        self.listWidget.clear()

    def show_password(self):
        if self.ShowPassword.isChecked():
            self.btnPassword.setEchoMode(QLineEdit.Normal)
        else:
            self.btnPassword.setEchoMode(QLineEdit.Password)

    def aes_choice(self):
        pass

    def not_found(self):
        self.show_dialog(icon=QMessageBox.Warning,
                         text="QPDF Not Found. Please Install",
                         window_title="Error")

    def encrypt_screen(self):
        self.new_encrypt_screen = EncryptScreen(self)

    def decrypt_screen(self):
        new_decrypt_screen = DecryptScreen(self)



def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
