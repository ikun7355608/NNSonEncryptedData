# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_register.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(70, 70, 251, 121))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.passwdEdit = QtWidgets.QTextEdit(self.widget)
        self.passwdEdit.setObjectName("passwdEdit")
        self.gridLayout.addWidget(self.passwdEdit, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.nameEdit = QtWidgets.QTextEdit(self.widget)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.user_name = "000"
        self.user_passwd = "000"
        self.nameEdit.setPlainText(self.user_name)
        self.passwdEdit.setPlainText(self.user_passwd)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "用户身份信息"))
        self.label_3.setText(_translate("Dialog", "帐号"))
        self.label_4.setText(_translate("Dialog", "密码"))
        self.label_2.setText(_translate("Dialog", "请妥善保管您的身份信息"))
        self.label.setText(_translate("Dialog", "帐号注册完成"))


