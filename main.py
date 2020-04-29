import PyQt5.QtGui
from PyQt5.QtWidgets import (QMainWindow, QApplication, QFileDialog,
                             QInputDialog, QMessageBox, QLineEdit,
                             QCheckBox)
from subprocess import Popen, PIPE
from pathlib import Path
import subprocess
import sys
import os
import design

if os.name == 'posix':
    #  linux os
    program = 'qpdf'
elif os.name == 'nt':
    # windows os
    program = 'qpdf.exe'


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
        self.btnDecrypt.clicked.connect(self.decrypt)
        # self.AESOption.activated[int]

    def show_dialog(self, icon=None, text=None, window_title=None):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(text)
        msg.setWindowTitle(window_title)
        msg.exec_()


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

    def decrypt(self):
        destination = QFileDialog.getExistingDirectory(self, "Pick a folder")
        identifier = '(de)'
        success = []
        unsuccessful = []
        passwd = QLineEdit.text(self.btnPassword)
        itemsTextList = [str(self.listWidget.item(i).text()) for i in range(self.listWidget.count())]
        for item in itemsTextList:
            new_file_path = Path(item)
            suffix = new_file_path.suffix
            new_filename = new_file_path.stem+identifier+suffix
            try:
                subprocess.check_output([program, '--decrypt', '--password={}'.format(passwd),
                                            item, os.path.join(destination, new_filename)])
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
