# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_management.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QMainWindow
from lib import libsql
from user import user_update

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        self.window = user_update.Ui_MainWindow()
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.userEdit.setGeometry(QtCore.QRect(0, 0, 791, 411))
        self.userEdit.setObjectName("userEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 480, 67, 17))
        self.label.setText("")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(490, 470, 100, 70))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.updateBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.updateBtn.setObjectName("updateBtn")
        self.verticalLayout.addWidget(self.updateBtn)
        self.deleteBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.deleteBtn.setObjectName("deleteBtn")
        self.verticalLayout.addWidget(self.deleteBtn)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 490, 195, 23))
        self.label_2.setObjectName("label_2")
        self.idEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.idEdit.setGeometry(QtCore.QRect(270, 490, 142, 25))
        self.idEdit.setObjectName("idEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        data = "(工号，姓名，性别，电话，年龄，部门，职位)\n"
        data += libsql.show_user()
        self.userEdit.setPlainText(data)
        self.retranslateUi(MainWindow)
        self.updateBtn.clicked.connect(self.update_click)
        self.deleteBtn.clicked.connect(self.delete_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "用户信息管理"))
        self.updateBtn.setText(_translate("MainWindow", "更改用户信息"))
        self.deleteBtn.setText(_translate("MainWindow", "删除用户信息"))
        self.label_2.setText(_translate("MainWindow", "请输入要修改信息的员工工号"))

    def delete_click(self):
        user_id = self.idEdit.text()
        libsql.delete_by_id(user_id)
        QMessageBox.about(self,"通知","删除用户信息成功")
        data = "(工号，姓名，性别，电话，年龄，部门，职位)\n"
        data += libsql.show_user()
        self.idEdit.clear()
        self.userEdit.setPlainText(data)
        # print(user_id,type(user_id))

    def update_click(self):
        user_id = self.idEdit.text()
        self.window.userid = user_id
        data = libsql.select_user(user_id)
        # print(data)
        (user_id,name,gender,phone,age,department,title) = data
        self.window.nameEdit.setPlainText(name)
        self.window.phoneEdit.setPlainText(phone)
        self.window.departmentEdit.setPlainText(department)
        self.window.titleEdit.setPlainText(title)
        # print(gender,type(gender))
        self.window.show()




