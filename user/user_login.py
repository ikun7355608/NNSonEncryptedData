# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_login.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from lib import libcrypto
import os,sys
sys.path.insert(1,os.path.abspath("./fhipe/"))
from fhipe import ipe;
import socket
from lib import libconvertio
from user.user_select import *

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.dialog = Ui_Dialog()
        (self.pp,self.msk) = ipe.setup(10)
        (self.detB, self.B, self.Bstar, self.group, self.g1, self.g2) = self.msk
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(325, 212)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 130, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 40, 241, 71))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.idEdit = QtWidgets.QLineEdit(self.widget)
        self.idEdit.setObjectName("idEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.idEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.passwdEdit = QtWidgets.QLineEdit(self.widget)
        self.passwdEdit.setObjectName("passwdEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwdEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 325, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.on_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "用户登录界面"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.label.setText(_translate("MainWindow", "帐号"))
        self.label_2.setText(_translate("MainWindow", "密码"))

    def on_click(self):
        username = self.idEdit.text()
        passwd = self.passwdEdit.text()
        passwd = libcrypto.hash_passwd(passwd)
        temp = (username,passwd)
        soc = socket.socket()
        host = socket.gethostname()
        port = 12345
        soc.connect((host,port))
        soc.send(str(temp).encode())
        data = soc.recv(102400).decode()
        (self.detB,self.B,self.Bstar,self.g1,self.g2) = libconvertio.str2element4msk(data,self.group)
        # print(data)
        print(self.B)
        soc.close()
        self.dialog.detB = self.detB
        self.dialog.B = self.B
        self.dialog.Bstar = self.Bstar
        self.dialog.g1 = self.g1
        self.dialog.g2 = self.g2
        self.dialog.show()



