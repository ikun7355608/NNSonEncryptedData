import socket
import os,sys
import random
import time
from lib import libconvertio
import multiprocessing
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject
sys.path.insert(1,os.path.abspath("./fhipe/"))
from fhipe import ipe;
from file.file_management import *
from lib import libsql
from lib import libcrypto


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 实例化界面对象
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def most_similarity(pp, dict, cty, max_innerprod = 50000):
	"""
		相似文件查找
		输入：
			公共参数pp
			key:id+value:IPE的字典（模拟hashmap）
			收到的功能私钥
			max_innerprod : 离散对数求解 最大值的限制
		输出：
			最相似文件id
	"""
	res = {}
	for key in dict.keys():
		res[key] = ipe.decrypt(pp,dict[key],cty,max_innerprod)
	res = sorted(res.items(), key=lambda d:d[1])
	print(res)
	for key in res:
		if key[1] != -1 :
			return key[0]

        
# 进程1 绘制界面
def draw(aes_key,aes_iv):
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.aes_key = aes_key
    window.aes_iv = aes_iv
    w = QMainWindow()
    window.setupUi(w)
    w.show()
    sys.exit(app.exec_())

# 进程2 监听连接请求
def listenlogin(msk):
	# (pp, sk) = ipe.setup(10)
	(detB, B, Bstar, group, g1, g2) = msk
	sk_temp = libconvertio.element2str4msk(msk)
	soc = socket.socket()
	host = socket.gethostname()
	port = 12345
	soc.bind((host,port))
	soc.listen(5)
	while (True):
		conn,addr = soc.accept()
		login_infor = conn.recv(1024).decode()
		(account,passwd) = eval(login_infor)
		temp = libsql.select_passwd(account)
		# print(B)
		data = ""
		if temp[1] == passwd:
			print("true")
			data = str(sk_temp)
		conn.send(data.encode())
		conn.close()

# 进程3 监听查询请求
def listenselect(msk,aes_key,aes_iv):
	pp = ()
	(detB, B, Bstar, group, g1, g2) = sk
	soc = socket.socket()
	host = socket.gethostname()
	port = 13579
	soc.bind((host,port))
	soc.listen(5)
	while (True):
		conn,addr = soc.accept()
		strcty = conn.recv(1024).decode()
		# print(strcty)
		cty = libconvertio.str2element4cipher(strcty,group)
		strskxs = libsql.show_ipe()
		# print(strskxs)
		dict_skx = {}
		for row in strskxs:
			# print(row,type(row))
			(fileid,strskx) = row
			print(type(strskx))
			data = libconvertio.str2element4cipher(strskx,group)
			dict_skx[fileid] = data
		fileid = most_similarity(pp,dict_skx,cty)
		data = libsql.select_aes(fileid)
		cryptor = libcrypto.AesCrypto(key = aes_key,IV = aes_iv)
		plaintext = cryptor.decrypt(data[4])
		conn.send(str((data[1],plaintext)).encode())
		conn.close()
		print(data[1],plaintext)




if __name__ == '__main__':
	aes_key = libcrypto.generate_rand(16)
	aes_iv = libcrypto.generate_rand(16)
	print(aes_key)
	print(aes_iv)
	(pp, sk) = ipe.setup(10)
	p1 = multiprocessing.Process(name='p1', target = draw,args=(aes_key,aes_iv))
	p = multiprocessing.Process(name='p', target = listenlogin,args=(sk,))
	p2 = multiprocessing.Process(name='p2', target = listenselect,args=(sk,aes_key,aes_iv))
	p1.start()
	p.start()
	p2.start()



# soc = socket.socket()
# host = socket.gethostname()
# port = 12345
# soc.bind((host,port))
# soc.listen(5)
# (pp, sk) = ipe.setup(10)
# (detB, B, Bstar, group, g1, g2) = sk
# sk_temp = convertio.element2str4msk(sk)
# (detB, B, Bstar, g1, g2) = convertio.str2element4msk(str(sk_temp),group)
# sk_new = (detB, B, Bstar, group, g1, g2)
# x = [0,1,2,3,4,0,0,2,0,0]
# skx = ipe.encrypt(sk,x)
# strskx = convertio.element2str4cipher(skx,group)
# # print(skx ==skx2)
# (detB, B, Bstar, group, g1, g2) = sk
# while True:
# 	conn,addr = soc.accept()
# 	conn.send(str(sk_temp).encode())
# 	sss = conn.recv(102400).decode()
# 	cty = convertio.str2element4cipher(sss,group)
# 	# print(convertio.element2str4cipher(cty,group))
# 	print(skx)
# 	# res = ipe.decrypt(pp,skx,cty,200)
# 	pp = ()
# 	print(ipe.decrypt(pp, skx, cty, 1000))
# 	print(ipe.decrypt(pp, cty, skx, 1000))

# 	conn.close()

