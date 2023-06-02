# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup

from user import user_infor
from lib import libsql

class Ui_MainWindow(object):

    def __init__(self):
        self.dialog = user_infor.Ui_Dialog()
        # self.sigl.connect(self.dialog.get_data)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(289, 656)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 215, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 215, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 215, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 215, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.register_btn = QtWidgets.QPushButton(self.centralwidget)
        self.register_btn.setGeometry(QtCore.QRect(100, 560, 80, 31))
        self.register_btn.setObjectName("register_btn")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 221, 505))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_name = QtWidgets.QLabel(self.layoutWidget)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_name)
        self.nameEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameEdit)
        self.label_gender = QtWidgets.QLabel(self.layoutWidget)
        self.label_gender.setObjectName("label_gender")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_gender)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radio_btn1 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radio_btn1.setObjectName("radio_btn1")
        self.horizontalLayout.addWidget(self.radio_btn1)
        self.radio_btn2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radio_btn2.setObjectName("radio_btn2")
        self.horizontalLayout.addWidget(self.radio_btn2)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_phone = QtWidgets.QLabel(self.layoutWidget)
        self.label_phone.setObjectName("label_phone")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_phone)
        self.phoneEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.phoneEdit.setObjectName("phoneEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.phoneEdit)
        self.label_age = QtWidgets.QLabel(self.layoutWidget)
        self.label_age.setObjectName("label_age")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_age)
        self.ageBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.ageBox.setMinimum(18)
        self.ageBox.setMaximum(60)
        self.ageBox.setObjectName("ageBox")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.ageBox)
        self.label_department = QtWidgets.QLabel(self.layoutWidget)
        self.label_department.setObjectName("label_department")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_department)
        self.departmentEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.departmentEdit.setObjectName("departmentEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.departmentEdit)
        self.label_title = QtWidgets.QLabel(self.layoutWidget)
        self.label_title.setObjectName("label_title")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_title)
        self.titleEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.titleEdit.setObjectName("titleEdit")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.titleEdit)
        self.label_passwd = QtWidgets.QLabel(self.layoutWidget)
        self.label_passwd.setObjectName("label_passwd")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_passwd)
        self.passwdEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.passwdEdit.setObjectName("passwdEdit")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.passwdEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 289, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btn_group = QButtonGroup()
        self.btn_group.addButton(self.radio_btn1,10)
        self.btn_group.addButton(self.radio_btn2,11)
        # self.btn_group.buttonClicked.connect(self.btn_click)

        self.retranslateUi(MainWindow)
        self.register_btn.clicked.connect(self.btn_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "用户注册"))
        self.register_btn.setText(_translate("MainWindow", "注册"))
        self.label_name.setText(_translate("MainWindow", "姓名"))
        self.label_gender.setText(_translate("MainWindow", "性别"))
        self.radio_btn1.setText(_translate("MainWindow", "男"))
        self.radio_btn2.setText(_translate("MainWindow", "女"))
        self.label_phone.setText(_translate("MainWindow", "电话"))
        self.label_age.setText(_translate("MainWindow", "年龄"))
        self.label_department.setText(_translate("MainWindow", "部门"))
        self.label_title.setText(_translate("MainWindow", "职位"))
        self.label_passwd.setText(_translate("MainWindow", "密码"))

    def btn_click(self):
        name = self.nameEdit.toPlainText()
        self.nameEdit.clear()
        gender = "0"

        if self.btn_group.checkedId() == 10:
            gender = "1"
        elif self.btn_group.checkedId() == 11:
            gender = "2"

        phone = self.phoneEdit.toPlainText()
        self.phoneEdit.clear()

        age = self.ageBox.value()

        department = self.departmentEdit.toPlainText()
        self.departmentEdit.clear()

        title = self.titleEdit.toPlainText()
        self.titleEdit.clear()

        passwd = self.passwdEdit.toPlainText()
        self.passwdEdit.clear()

        user_infor = (name,passwd)
        user_id = libsql.insert_user_infor(name,gender,phone,age,department,title,passwd)    
        print(user_infor)
        self.dialog.nameEdit.setPlainText(str(user_id))
        self.dialog.passwdEdit.setPlainText(passwd)
        self.dialog.show()        
