from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QMainWindow, QApplication, QFileDialog,
                             QInputDialog, QMessageBox, QLineEdit,
                             QCheckBox, QWidget, QProgressBar, QLabel,
                             QDialog, QGridLayout, QPushButton)
from subprocess import Popen, PIPE
from pathlib import Path
import design
import os
import subprocess
import sys
import threading


if os.name == 'posix':
    #  linux os
    default_output_dir = os.path.expanduser('~/Downloads')
    program = 'qpdf'
elif os.name == 'nt':
    # windows os
    default_output_dir = os.path.expandvars(r'%USERPROFILE%\Downloads')
    program = 'qpdf.exe'



# subprocess.call and check_call are blocking (waits for the child process to return)
# so we need to use threading
class RepeatingTimer(threading.__Timer):
    def run(self):
        while True:
            self.finished.wait(self.interval)
            if self.finished.is_set():
                return
            else:
                self.function(*self.args, **self.kwargs)


class DecryptScreen(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.parent = parent
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Decrypt")
        layout = QGridLayout(self)

        # self.progress = QProgressBar(self)
        # self.progress.setGeometry(100, 80, 150, 20)
        self.resize(320, 180)
        self.passwordLabel = QLabel("Password")
        self.btnPassword = QLineEdit(self)
        self.btnPassword.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.passwordLabel, 0, 0)
        layout.addWidget(self.btnPassword, 0, 1)


        self.ShowPassword = QCheckBox("Show Password")
        layout.addWidget(self.ShowPassword, 1, 1, 1, 1)

        self.progress = QProgressBar(self)
        layout.addWidget(self.progress, 2, 1, 1, 1)

        self.buttonOK = QPushButton('Ok', self)
        layout.addWidget(self.buttonOK)
        self.buttonOK.clicked.connect(self.disable_btns)
        self.show()
        self.ShowPassword.clicked.connect(self.show_password)

    def show_password(self):
        if self.ShowPassword.isChecked():
            self.btnPassword.setEchoMode(QLineEdit.Normal)
        else:
            self.btnPassword.setEchoMode(QLineEdit.Password)

    def disable_btns(self):
        self.buttonOK.setEnabled(False)
        self.btnPassword.setEnabled(False)
        self.parent.decrypt(self.btnPassword, self.progress, self.buttonOK)

class EncryptScreen(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.parent = parent
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Encrypt")
        layout = QGridLayout(self)

        # self.progress = QProgressBar(self)
        # self.progress.setGeometry(100, 80, 150, 20)
        self.resize(320, 180)
        self.passwordLabel = QLabel("Password")
        self.btnPassword = QLineEdit(self)
        self.btnPassword.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.passwordLabel, 0, 0)
        layout.addWidget(self.btnPassword, 0, 1)

        self.password2Label = QLabel("Confirm")
        self.btnPassword2 = QLineEdit(self)
        self.btnPassword2.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password2Label, 1, 0)
        layout.addWidget(self.btnPassword2, 1, 1)

        self.ShowPassword = QCheckBox("Show Password")
        layout.addWidget(self.ShowPassword, 2, 1, 1, 1)

        self.progress = QProgressBar(self)
        layout.addWidget(self.progress, 3, 1, 1, 1)

        self.buttonOK = QPushButton('Ok', self)
        layout.addWidget(self.buttonOK)
        #self.buttonOK.clicked.connect(self.parent.encrypt)
        self.buttonOK.clicked.connect(self.disable_test)
        self.show()
        self.ShowPassword.clicked.connect(self.show_password)

    def show_password(self):
        if self.ShowPassword.isChecked():
            self.btnPassword.setEchoMode(QLineEdit.Normal)
            self.btnPassword2.setEchoMode(QLineEdit.Normal)
        else:
            self.btnPassword.setEchoMode(QLineEdit.Password)
            self.btnPassword2.setEchoMode(QLineEdit.Password)

    def disable_test(self):
        self.buttonOK.setEnabled(False)
        self.btnPassword.setEnabled(False)
        self.btnPassword2.setEnabled(False)
        self.parent.decrypt


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


class ExampleApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.btnOpenFolder.clicked.connect(self.open_folder)
        self.btnOpenFile.clicked.connect(self.add_file)
        self.btnRemoveFile.clicked.connect(self.remove_file)
        self.btnClearAll.clicked.connect(self.clear_all)
        self.ShowPassword.clicked.connect(self.show_password)
        self.btnEncrypt.clicked.connect(self.encrypt)
        self.btnDecrypt.clicked.connect(self.decrypt_screen)
        # self.AESOption.activated[int]

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
        directory = QFileDialog.getExistingDirectory(self, "Pick a folder")
        if directory:
            for file in os.listdir(directory):
                if file.endswith(".pdf"):
                    filter = os.path.join(directory, file)
                    self.listWidget.addItem(filter)

    def add_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Pick a file", filter='*.pdf')
        if file:
            self.listWidget.addItem(file)

    def remove_file(self):
        for SelectedItem in self.listWidget.selectedItems():
            self.listWidget.takeItem(self.listWidget.row(SelectedItem))

    def clear_all(self):
        self.listWidget.clear()
        # self.new_progress_screen = EncryptScreen(self)
        #self.new_progress_screen = DecryptScreen(self)

    def show_password(self):
        # self.show_progress_bar()
        if self.ShowPassword.isChecked():
            self.btnPassword.setEchoMode(QLineEdit.Normal)
        else:
            self.btnPassword.setEchoMode(QLineEdit.Password)

    def aes_choice(self):
        pass

    def not_found(self):
        self.show_dialog(icon=QMessageBox.Warning,
        text="QPDF Not found. Please install",
        window_title="Error")



    def encrypt(self):
        identifier = '(en)'
        passwd = QLineEdit.text(self.btnPassword)
        # aes_choice = self.AESOption.activated[int]
        aes_choice = str(self.AESOption.currentText()).strip('AES-')
        itemsTextList = [str(self.listWidget.item(i).text()) for i in range(self.listWidget.count())]
        text, ok = QInputDialog.getText(self, "Encrypt", "Confirm Password", QLineEdit.Password)
        try:
            if ok:
                # if ok is clicked as opposed to cancel, then check if both passwords match
                if text != passwd:
                    self.show_dialog(icon=QMessageBox.Warning,
                                     text="Passwords do not match. Try again",
                                     window_title="Encrypt")
                elif text == passwd:
                    destination = QFileDialog.getExistingDirectory(self, "Pick a folder")
                    for item in itemsTextList:
                        new_file_path = Path(item)
                        suffix = new_file_path.suffix
                        process = subprocess.call([program, '--encrypt', passwd, passwd, aes_choice,
                        '--', item, os.path.join(destination, new_file_path.stem+identifier+suffix)])
                    self.show_dialog(icon=QMessageBox.Information,
                                    text="{} pdf(s) successfully encrypted".format(len(itemsTextList)),
                                    window_title="Encrypt")
        except FileNotFoundError:
            self.not_found()

    def decrypt_screen(self):
        new_decrypt_screen = DecryptScreen(self)


    def decrypt(self, passwd, progress, okbtn):
        destination = default_output_dir
        identifier = '(de)'
        success = []
        unsuccessful = []
        #passwd = QLineEdit.text(self.btnPassword)
        itemsTextList = [str(self.listWidget.item(i).text()) for i in range(self.listWidget.count())]
        for item in itemsTextList:
            new_file_path = Path(item)
            suffix = new_file_path.suffix
            new_filename = new_file_path.stem+identifier+suffix
            try:
                #self.loading_screen = LoadingScreen()
                self.completed = 0
                while(subprocess.check_output([program, '--decrypt', '--password={}'.format(passwd.text()),
                    item, os.path.join(destination, new_filename)]) != 0):
                    self.completed += 1
                    progress.setValue(self.completed)
                #self.loading_screen.stopAnimation()
                """self.show_dialog(icon=QMessageBox.Information,
                                text="{} pdf(s) successfully decrypted".format(len(itemsTextList)),
                                window_title="decrypt")"""
            except FileNotFoundError:
                self.not_found()

            except subprocess.CalledProcessError as e:
                if e.returncode == 2:
                    #append to list
                    unsuccessful.append(item)
                    """self.show_dialog(icon=QMessageBox.Warning,
                                    text="({}) Bad Password for file {}".format(e.returncode, item),
                                    window_title="decrypt")"""
            else:
                success.append(destination+new_filename)
                """self.show_dialog(icon=QMessageBox.Information,
                                    text="{} pdf(s) successfully decrypted".format(len(success),
                                    window_title="decrypt")"""
        if len(unsuccessful) > 0:
                    self.show_dialog(icon=QMessageBox.Warning,
                                            text="Bad Password for {} file(s):\n {} (returncode)".format(len(unsuccessful), "\n".join(unsuccessful)),
                                            window_title="decrypt")
                    okbtn.setEnabled(True)
                    passwd.setEnabled(True)
        if len(success) > 0:
                self.show_dialog(icon=QMessageBox.Information,
                                        text="{} pdf(s) successfully decrypted:\n{}".format(len(success), "\n".join(success)),
                                        window_title="decrypt")

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
