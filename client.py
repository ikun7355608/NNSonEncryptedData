import multiprocessing
import time
import socket
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject
from user.user_login import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 实例化用户登录界面对象 打开界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    w = QMainWindow()
    window.setupUi(w)
    w.show()
    sys.exit(app.exec_())

