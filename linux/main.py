from PyQt5.QtGui import QMovie, QPixmap, QIcon
from PyQt5.QtCore import Qt, QTimer, QSize
from PyQt5.QtWidgets import (QMainWindow, QApplication, QFileDialog,
                             QInputDialog, QMessageBox, QLineEdit,
                             QCheckBox, QWidget, QProgressBar, QLabel,
                             QDialog, QGridLayout, QPushButton, QAction,
                             QHBoxLayout)
from subprocess import Popen, PIPE
from pathlib import Path
import design
import redesign
import decrypt
import encrypt
import logging
import os
import subprocess
import sys
import threading


if os.name == 'posix':
    #  linux os
    default_open_loc = os.path.expanduser('~/')
    default_output_dir = os.path.expanduser('~/Downloads')
    program = 'qpdf'
elif os.name == 'nt':
    # windows os
    default_open_loc = os.path.expandvars(r'%USERPROFILE%')
    default_output_dir = os.path.expandvars(r'%USERPROFILE%\Downloads')
    program = 'qpdf.exe'


# subprocess.call and check_call are blocking
# (waits for the child process to return)
# so we need to use threading

class DecryptScreen(QDialog, decrypt.Ui_decryptUI):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        self.resize(520, 280)
        self.outputDir.setText(default_output_dir)
        self.changeDir.clicked.connect(self.change_outputdir)
        self.btnPassword.setEchoMode(QLineEdit.Password)
        self.buttonOK.clicked.connect(self.disable_btns)
        self.buttonClose.clicked.connect(self.close)
        self.setWindowTitle("Decrypt")

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
        default_output_dir = QFileDialog.getExistingDirectory(self,
                                                              "Pick a folder")
        if default_output_dir:
            self.outputDir.setText(default_output_dir)

    def disable_btns(self):
        self.buttonOK.setEnabled(False)
        self.btnPassword.setEnabled(False)
        self.parent.decrypt(self.btnPassword, self.buttonOK, self.logEdit)


class EncryptScreen(QDialog, encrypt.Ui_encryptUI):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        self.resize(520, 280)
        self.outputDir.setText(default_output_dir)
        self.changeDir.clicked.connect(self.change_outputdir)
        self.btnPassword.setEchoMode(QLineEdit.Password)
        self.btnPassword2.setEchoMode(QLineEdit.Password)
        self.buttonOK.clicked.connect(self.disable_btns)
        self.buttonClose.clicked.connect(self.close)
        # self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Encrypt")
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

        self.show()

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
        default_output_dir = QFileDialog.getExistingDirectory(self,
                                                              "Pick a folder")
        if default_output_dir:
            self.outputDir.setText(default_output_dir)

    def disable_btns(self):
        self.buttonOK.setEnabled(False)
        self.btnPassword.setEnabled(False)
        self.btnPassword2.setEnabled(False)
        self.parent.encrypt(self.btnPassword, self.btnPassword2, self.buttonOK, self.logEdit)



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
        self.setupUi(self)
        self.actionExit.triggered.connect(self.exit)
        self.btnOpenFolder.triggered.connect(self.open_folder)
        self.btnOpenFile.triggered.connect(self.add_file)
        self.btnRemoveFile.triggered.connect(self.remove_file)
        # self.btnClearAll.triggered.connect(self.clear_all)
        self.btnEncrypt.triggered.connect(self.encrypt_screen)
        self.btnDecrypt.triggered.connect(self.decrypt_screen)
        # self.AESOption.activated[int]

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
        directory = QFileDialog.getExistingDirectory(self, "Pick a folder",
                                                     default_open_loc)
        if directory:
            for file in os.listdir(directory):
                if file.endswith(".pdf"):
                    filter = os.path.join(directory, file)
                    self.listWidget.addItem(filter)

    def add_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Pick a file",
                                              default_open_loc, filter='*.pdf')
        if file:
            self.listWidget.addItem(file)

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
                         text="QPDF Not found. Please install",
                         window_title="Error")

    def encrypt_screen(self):
        new_encrypt_screen = EncryptScreen(self)

    def encrypt(self, passwd, passwd2, okbtn, logEdit):
        destination = default_output_dir
        identifier = '(encry)'
        logging.basicConfig(filename="output.log", filemode='w', level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%H:%M:%S')
        # aes_choice = self.AESOption.activated[int]
        # aes_choice = str(self.AESOption.currentText()).strip('AES-')
        itemsTextList = [str(self.listWidget.item(i).text()) for i in range(self.listWidget.count())]
        if passwd.text() != passwd2.text():
            # self.write_to_log("Passwords do not match")
            logging.info("Passwords do not match")
            """
            self.show_dialog(icon=QMessageBox.Warning,
                             text="Passwords do not match. Try again",
                             window_title="Encrypt")
            """
        elif passwd.text() == passwd2.text():
            for item in itemsTextList:
                new_file_path = Path(item)
                suffix = new_file_path.suffix
                new_filename = new_file_path.stem+identifier+suffix
                try:
                    subprocess.check_output([program, '--encrypt', passwd.text(), passwd2.text(), '256', '--', item, os.path.join(destination, new_filename)],
                                            stderr=subprocess.STDOUT).decode()
                    okbtn.setEnabled(True)
                    passwd.setEnabled(True)
                    passwd2.setEnabled(True)
                except subprocess.CalledProcessError as e:
                    if e.returncode == 1 or e.returncode == 2:
                        self.write_to_log(e.output.decode())
                except FileNotFoundError:
                    # if qpdf binary cannot be found
                    self.not_found()
                else:
                    self.write_to_log("{}: Success".format(os.path.join(destination, new_filename)))
        open_log = open('output.log', 'r')
        logEdit.setPlainText(open_log.read())
        open_log.close()

    def write_to_log(self, text):
        logging.basicConfig(filename="output.log", filemode='w', level=logging.INFO,
                format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%H:%M:%S')
        logging.info(text)
        """
        with open('log.txt', 'w') as f:
            f.write(text)
        """
    def decrypt_screen(self):
        new_decrypt_screen = DecryptScreen(self)

    def decrypt(self, passwd, okbtn, logEdit):
        destination = default_output_dir
        identifier = '(decry)'
        itemsTextList = [str(self.listWidget.item(i).text()) for i in range(self.listWidget.count())]
        if len(itemsTextList) == 0:
            self.write_to_log("No files to decrypt")
        else:
            self.write_to_log("Decrypting...")
            for item in itemsTextList:
                new_file_path = Path(item)
                suffix = new_file_path.suffix
                new_filename = new_file_path.stem+identifier+suffix
                try:
                    subprocess.check_output([program, "--decrypt", "--password={}".format(passwd.text()), item, os.path.join(destination, new_filename)], stderr=subprocess.STDOUT).decode()
                    okbtn.setEnabled(True)
                    passwd.setEnabled(True)
                except subprocess.CalledProcessError as e:
                    if e.returncode == 1 or e.returncode == 2:
                        # unsuccessful.append(item)
                        # logEdit.setPlainText("Bad Password ({}) for:\n{}".format(p.returncode, "\n".join(unsuccessful)))
                        # self.write_to_log("Bad Password ({}): {}".format(e.returncode, item))
                        self.write_to_log(e.output.decode())
                except FileNotFoundError:
                    # if qpdf binary cannot be found
                    self.not_found()
                else:
                    # success.append(destination+new_filename)
                    self.write_to_log("{}: Success".format(os.path.join(destination, new_filename)))
        # put reading log file into a new func that uses threads
        # so that we can use both decrypt and encrypt whilst displaying log file
        open_log = open('output.log', 'r')
        logEdit.setPlainText(open_log.read())
        open_log.close()
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


def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
