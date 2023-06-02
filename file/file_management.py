# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_management.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from lib import libcrypto
import sys,os
from lib import libconvertio
from lib import libsql
from file import file_delete
sys.path.insert(1,os.path.abspath("./fhipe/"))
from fhipe import ipe;

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.dialog = file_delete.Ui_Dialog()

        libsql.create_table_all()
        self.res = ""
        (self.pp,self.msk) = ipe.setup(10)
        (self.detB, self.B, self.Bstar, self.group, self.g1, self.g2) = self.msk
        self.aes_key = ""
        self.aes_iv = ""
        self.cryptor = libcrypto.AesCrypto(key = self.aes_key,IV = self.aes_iv)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inforEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.inforEdit.setGeometry(QtCore.QRect(10, 10, 501, 421))
        self.inforEdit.setObjectName("inforEdit")
        self.connectEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.connectEdit.setGeometry(QtCore.QRect(10, 440, 381, 70))
        self.connectEdit.setObjectName("connectEdit")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(420, 440, 82, 70))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uploadBtn = QtWidgets.QPushButton(self.widget)
        self.uploadBtn.setObjectName("uploadBtn")
        self.verticalLayout.addWidget(self.uploadBtn)
        self.deleteBtn = QtWidgets.QPushButton(self.widget)
        self.deleteBtn.setObjectName("deleteBtn")
        self.verticalLayout.addWidget(self.deleteBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 524, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.inforEdit.setPlainText(str(self.msk))
        print(self.aes_key,self.aes_iv)
        libsql.delete_FILE_CIPHER()
        libsql.delete_IPE_CIPHER()

        self.retranslateUi(MainWindow)
        self.uploadBtn.clicked.connect(self.openfile)
        self.deleteBtn.clicked.connect(self.deletefile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文件管理"))
        self.uploadBtn.setText(_translate("MainWindow", "文件上传"))
        self.deleteBtn.setText(_translate("MainWindow", "文件删除"))

    def openfile(self):
        self.cryptor = libcrypto.AesCrypto(key = self.aes_key,IV = self.aes_iv)
        filename,filetype = QFileDialog.getOpenFileName(None,'选择文件','',"*.txt;;*_vec.txt")
        self.res += "您选择的文件为:\t" + filename +"\n"
        print("您选择的文件为:\t" , filename , "\n")
        filedata = ""
        if filename:
            with open(filename, 'r',encoding='utf-8',errors='ignore') as f:
                filedata = f.read()
                print("文件内容: ",filedata)
        vector_name = filename[:-4] + "_vec.txt"

        aes_cipher = self.cryptor.encrypt(filedata.encode())

        self.res += "\n 文件特征向量为：\n"
        file_vector = []

        with open(vector_name, 'r',encoding='utf-8',errors='ignore') as f:
            data = f.read()
            self.res += data
            print("\n原向量:\n",data)
            file_vector = eval(data)

        extension_vector = libcrypto.y_extension(file_vector)
        self.res += "\n扩展向量为:\n"
        self.res += str(extension_vector)
        print("\n扩展向量\n",str(extension_vector))

        skx = ipe.encrypt(self.msk,extension_vector)
        strskx = libconvertio.element2str4cipher(skx,self.group)

        libsql.upload_file(filename,aes_cipher,str(strskx))
        # libsql.insert_ipe(filename,str(strskx))
        self.res += "\n序列化之后的IPE密文:\n"
        self.res += str(strskx)  
        self.res += "\nAES密文:\n"
        self.res += str(aes_cipher)
        print("\n序列化之后的IPE密文:\n",strskx)
        print("\n序列化之后的AES密文:\n",aes_cipher)

        self.inforEdit.setPlainText(str(self.B))
        self.inforEdit.setPlainText(self.res)
        # print(strskx)
        # print(aes_cipher)
        # print(self.res)
    def deletefile(self):
        data = libsql.show_file()
        self.dialog.textEdit.setPlainText(data)
        self.dialog.show()

        

