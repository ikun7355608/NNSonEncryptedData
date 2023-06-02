import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject
from user.user_regist import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 实例化用户注册界面对象
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    w = QMainWindow()
    window.setupUi(w)
    w.show()
    sys.exit(app.exec_())

