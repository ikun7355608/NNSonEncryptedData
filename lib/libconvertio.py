import socket
import os,sys
sys.path.insert(1,os.path.abspath("./fhipe/"))
from fhipe import ipe;

"""
	内积加密相关函数中元素的序列化、反序列化操作
"""
def element2str4msk(sk):
	"""
	  msk中的group.element序列化为string 
	"""
	(detB,B,Bstar,group,g1,g2) = sk
	n = len(B)
	str_B = []
	str_Bstar = []
	for i in range(n):
		tmpB = []
		tmpBstar = []
		for j in range(n):
			tmpB.append(group.serialize(B[i][j]))
			tmpBstar.append(group.serialize(B[i][j]))

		str_B.append(tmpB)
		str_Bstar.append(tmpBstar)
	str_g1 = group.serialize(g1)
	str_g2 = group.serialize(g2)
	return (detB,str_B,str_Bstar,str_g1,str_g2)


def str2element4msk(str_sk,group):
	"""
		msk中的string反序列化为group.element
	"""
	(detB,str_B,str_Bstar,str_g1,str_g2) = eval(str_sk)
	B = []
	Bstar = []
	n = len(str_B)
	for i in range(n):
		tmp_B = []
		tmp_Bstar = []
		for j in range(n):
			tmp_B.append(group.deserialize(str_B[i][j]))
			tmp_Bstar.append(group.deserialize(str_Bstar[i][j]))
		B.append(tmp_B)
		Bstar.append(tmp_Bstar)
	g1 = group.deserialize(str_g1)
	g2 = group.deserialize(str_g2)
	return (detB,B,Bstar,g1,g2)


def element2str4cipher(cipher,group):
	(c1,c2) = cipher
	n = len(c1)
	str_c1 = []
	for i in range(n):
		str_c1.append(group.serialize(c1[i]))
	str_c2 = group.serialize(c2)
	return (str_c1,str_c2)


def str2element4cipher(str_cipher,group):
	(str_c1,str_c2) = eval(str_cipher)
	n = len(str_c1)
	c1 = []
	for i in range(n):
		c1.append(group.deserialize(str_c1[i]))
	c2 = group.deserialize(str_c2)
	return (c1,c2)
