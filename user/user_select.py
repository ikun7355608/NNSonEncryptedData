# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_select.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QDialog,QMessageBox
import sys,os
sys.path.insert(1,os.path.abspath("./fhipe/"))
from fhipe import ipe;
from lib import libcrypto
from lib import libconvertio
import socket

class Ui_Dialog(QDialog):
    def __init__(self):
        (self.pp,self.msk) = ipe.setup(10)
        (self.detB, self.B, self.Bstar, self.group, self.g1, self.g2) = self.msk
        self.res = ""
        self.data = ""
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 381, 231))
        self.textEdit.setObjectName("textEdit")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(120, 260, 168, 33))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uploadBtn = QtWidgets.QPushButton(self.widget)
        self.uploadBtn.setObjectName("uploadBtn")
        self.horizontalLayout.addWidget(self.uploadBtn)
        self.selectBtn = QtWidgets.QPushButton(self.widget)
        self.selectBtn.setObjectName("selectBtn")
        self.horizontalLayout.addWidget(self.selectBtn)


        self.textEdit.setPlainText(str(self.B))
        self.retranslateUi(Dialog)
        self.uploadBtn.clicked.connect(self.uploadfile)
        self.selectBtn.clicked.connect(self.selectfile)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "相似文件查找"))
        self.uploadBtn.setText(_translate("Dialog", "文件选择"))
        self.selectBtn.setText(_translate("Dialog", "文件查找"))

    def uploadfile(self):
        # 选择文件
        filename,filetype = QFileDialog.getOpenFileName(None,'选择文件','',"*.txt;;*_vec.txt")
        self.res += "您选择的文件为:\t" + filename +"\n"
        print("您选择的文件为:\t" , filename , "\n")
        filedata = ""
        if filename:
            with open(filename, 'r',encoding='utf-8',errors='ignore') as f:
                filedata = f.read()
                print("文件内容: ",filedata)
        vector_name = filename[:-4] + "_vec.txt"

        # 文本向量化
        self.res += "\n 文件特征向量为：\n"
        file_vector = []

        with open(vector_name, 'r',encoding='utf-8',errors='ignore') as f:
            data = f.read()
            self.res += data
            print("\n原向量:\n",data)
            file_vector = eval(data)

        # 扩展向量序列化 
        extension_vector = libcrypto.x_extension(file_vector)
        self.res += "\n扩展向量为:\n"
        self.res += str(extension_vector)
        print("\n扩展向量\n",str(extension_vector))
        cty = ipe.keygen(self.msk,extension_vector)
        strcty = libconvertio.element2str4cipher(cty,self.group)
        print(strcty,type(strcty))
        self.data = str(strcty)
        self.res += "\n内积加密密文\n"
        self.res += self.data
        self.textEdit.setPlainText(self.res)

    def selectfile(self):
        # 建立连接发送数据
        soc = socket.socket()
        host = socket.gethostname()
        port = 13579
        soc.connect((host,port))
        soc.send(self.data.encode())
        data = soc.recv(102400).decode()
        (filename,plaintext) = eval(data)
        most_str = "最相似的文件名为：" + filename +"\n 文件内容:" + plaintext +"\n"
        print(most_str)
        # self.res = most_str + self.res
        # self.textEdit.setPlainText(self.res)
        QMessageBox.about(self,"查找完成",most_str)
        soc.close()


