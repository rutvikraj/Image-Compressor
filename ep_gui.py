from PyQt5 import QtCore, QtGui, QtWidgets
from win32 import win32gui
from win32.lib import win32con
from tkinter.filedialog import askopenfilename
import subprocess
from PyQt5.QtWidgets import QMessageBox
from PIL import Image

import tkinter as tk
from tkinter import PhotoImage
root = tk.Tk()
root.withdraw()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1370, 835)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 1371, 31))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(4, 0, 121, 31))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(1310, 0, 61, 31))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(214, 214, 214);\n"
"    border-style: outset;\n"
"    border-radius: 15px;\n"
"    padding: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font-color: beige;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 2px;\n"
"    border-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(1250, 0, 61, 31))
        self.pushButton_4.setMinimumSize(QtCore.QSize(51, 0))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background-color: rgb(214, 214, 214);\n"
"    border-style: outset;\n"
"    border-radius: 15px;\n"
"    padding: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font-color: beige;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 255, 255);\n"
"    border: 2px;\n"
"    border-color: rgb(0, 255, 255);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 30, 681, 41))
        self.pushButton.setMinimumSize(QtCore.QSize(51, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(214, 214, 214);\n"
"    border-style: outset;\n"
"    border-radius: 15px;\n"
"    padding: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font-color: beige;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 85, 255);\n"
"    border: 2px;\n"
"    border-color: rgb(0, 85, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 30, 691, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(214, 214, 214);\n"
"    border-style: outset;\n"
"    border-radius: 15px;\n"
"    padding: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font-color: beige;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 214, 0);\n"
"    border: 2px;\n"
"    border-color: rgb(0, 214, 0);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 75, 1371, 761))
        self.label_2.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../EndPresso-master/noImageSelected.png"))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.select_image)
        self.pushButton_2.clicked.connect(self.compress_image)
        self.pushButton_3.clicked.connect(self.closeWindow)
        self.pushButton_4.clicked.connect(self.minimizeWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">AI PROJECT</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "X"))
        self.pushButton_4.setText(_translate("MainWindow", "_"))
        self.pushButton.setText(_translate("MainWindow", "Click Here To Select Image!!!"))
        self.pushButton_2.setText(_translate("MainWindow", "Compress the Image!!!"))

    def closeWindow(self, mousePressEvent):
        sys.exit()

    def minimizeWindow(self, mousePressEvent):
        Minimize = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

    file = ""

    def select_image(self):
        global file
        file = askopenfilename(filetypes=[("Image File", '*.jpg ; *.png')])
        if not file:
            pass
        else:
            img=Image.open(file)
            imgWidth, imgHeight = img.size
            width = int(imgWidth/2)
            height = int(imgHeight/4)
            if imgWidth>imgHeight:
                pixmap = QtGui.QPixmap(file).scaled(1366, 768)
                self.label_2.setPixmap(QtGui.QPixmap(pixmap))
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)
            else:
                pixmap = QtGui.QPixmap(file).scaled(height, width)
                self.label_2.setPixmap(QtGui.QPixmap(pixmap))
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)

    def compress_image(self):
        if not file:
            pass
        else:
            subprocess.Popen("python detect.py --images "+file, shell=True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
    MainWindow.setWindowFlags(flags)
    MainWindow.show()
    sys.exit(app.exec_())
