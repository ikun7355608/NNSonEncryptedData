# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_delete.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QMessageBox
from lib import libsql
class Ui_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 311)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(0, 20, 391, 211))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 260, 80, 31))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 240, 167, 56))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.on_click)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "文件删除"))
        self.pushButton.setText(_translate("Dialog", "删除文件"))
        self.label.setText(_translate("Dialog", "请输入要删除的文件编号"))

    def on_click(self):
        fileid = self.lineEdit.text()
        libsql.delete_file(fileid)
        libsql.delete_ipe(fileid)
        QMessageBox.about(self,"通知","删除文件成功")
        data = libsql.show_file()
        self.textEdit.setPlainText(data)
        print(fileid,type(fileid))



