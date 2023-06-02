import pymysql
from lib import libcrypto
 # 建表

def create_table_all():

	create_user_table = """ CREATE TABLE IF NOT EXISTS USER (
		user_id int  primary key auto_increment,
		name varchar(20),
	    gender tinyint,
	    phone varchar(20),
	    age smallint,
		department varchar(255),
		title varchar(20)
		)AUTO_INCREMENT = 10000;
		"""
	create_user_login_table = """ CREATE TABLE IF NOT EXISTS USER_LOGIN(
		account int primary key,
		passwd varchar(255),
	    uname varchar(20)
		)AUTO_INCREMENT = 10000;
		"""

	create_ipe_cipher_table = """ CREATE TABLE IF NOT EXISTS IPE_CIPHER (
		id int primary key auto_increment,
		file_name varchar(255),
		cipher text
		);
		"""

	create_aes_cipher_table = """ CREATE TABLE IF NOT EXISTS FILE_CIPHER (
		`id` int primary key auto_increment,
		`file_name` varchar(255),
	    `owner` varchar(20),
	    `upload_time` datetime,
		`aes_cipher` blob
		);
		"""

	table_set = []
	table_set.append(create_user_table)
	table_set.append(create_user_login_table)
	table_set.append(create_ipe_cipher_table)
	table_set.append(create_aes_cipher_table)
	for i in range(len(table_set)):
		create_table(table_set[i])

def create_table(tablename):
	db = pymysql.connect(host = 'localhost',
	                 user = 'root',
	                 password = 'joker7355608',
	                 database = 'IPE')
	cursor = db.cursor()
	try:
		cursor.execute(tablename)
		db.commmit()
	except:
		print("exists")
		db.rollback()
	db.close()



# 删表

def delete_IPE_CIPHER():
	"""
		清空IPE密文存储表
	"""
	db = pymysql.connect(host='localhost',
                 user='root',
                 password='joker7355608',
                 database='IPE')
	cursor = db.cursor()
	cursor.execute("DELETE FROM IPE_CIPHER")
	db.commit()
	db.close()

# 删除AES密文
def delete_FILE_CIPHER():
	db = pymysql.connect(host='localhost',
	    user='root',
	    password='joker7355608',
	    database='IPE')
	cursor = db.cursor()
	cursor.execute("DELETE FROM FILE_CIPHER")
	db.commit()
	db.close()


# 数据库 增


def insert_user(name,gender,phone,age,department,title):

	db = pymysql.connect(host='localhost',
             user='root',
             password='joker7355608',
             database='IPE')
	cursor = db.cursor()
	insert_sql = " INSERT INTO USER( \
					name,gender,phone,age,department,title) \
					VALUES('%s','%s','%s','%s','%s','%s') " \
					% (name,gender,phone,age,department,title)
	cursor.execute(insert_sql)
	db.commit()
	db.close()


def insert_login(account,passwd,username):
	db = pymysql.connect(host='localhost',
         user='root',
         password='joker7355608',
         database='IPE')
	cursor = db.cursor()
	passwd = libcrypto.hash_passwd(passwd)
	insert_sql = " INSERT INTO USER_LOGIN( \
				account,passwd,uname) \
				VALUES('%s','%s','%s') " \
				% (account,passwd,username)
	try:
		cursor.execute(insert_sql)
		db.commit()
	except:
		db.rollback()
	db.close()


def insert_ipe(filename,ciphertext):
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	insert_sql = """ INSERT INTO IPE_CIPHER
					(file_name, cipher)  VALUES(%s,%s)
				"""
	cursor.execute(insert_sql,(filename,ciphertext))
	db.commit()
	db.close()

def insert_file(filename,ciphertext,owner = "admin"):
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	insert_sql = """ INSERT INTO FILE_CIPHER
					(file_name,owner,upload_time,aes_cipher) 
					VALUES(%s,%s, NOW(),_binary %s)
				"""
	cursor.execute(insert_sql,(filename,owner,ciphertext))
	db.commit()
	db.close()

# 删除

def delete_user(id):
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	delete_sql = """ DELETE FROM USER 
					WHERE user_id = %s
				"""
	cursor.execute(delete_sql,(id))
	db.commit()
	db.close()


def delete_login(id):
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	delete_sql = """ DELETE FROM USER_LOGIN 
					WHERE account = %s
				"""
	cursor.execute(delete_sql,(id))
	db.commit()
	db.close()


def delete_ipe(id):
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	delete_sql = """ DELETE FROM IPE_CIPHER 
					WHERE id = %s
				"""
	cursor.execute(delete_sql,(id))
	db.commit()
	db.close()

def delete_file(id):
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	delete_sql = """ DELETE FROM FILE_CIPHER 
					WHERE id = %s
				"""
	cursor.execute(delete_sql,(id))
	db.commit()
	db.close()


def update_passwd(id,passwd):
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	passwd = libcrypto.hash_passwd(passwd)
	update_sql = """ UPDATE  USER_LOGIN  SET passwd = %s
					WHERE account = %s
				"""
	cursor.execute(update_sql,(passwd,id))
	db.commit()
	db.close()

def update_ipe(id,ciphertext):
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	update_sql = """ UPDATE  IPE_CIPHER  SET cipher = %s
					WHERE id = %s
				"""
	cursor.execute(update_sql,(ciphertext,id))
	db.commit()
	db.close()

def update_user(id,name,phone,department,title):
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	update_sql = """ UPDATE  USER  SET name = %s,
						phone = %s,
						department = %s,
						title = %s
					WHERE user_id = %s
				"""
	cursor.execute(update_sql,(name,phone,department,title,id))
	db.commit()
	db.close()


def update_file(id,ciphertext):
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	update_sql = """ UPDATE  FILE_CIPHER  SET aes_cipher = _binary %s,
						upload_time = NOW()
					WHERE id = %s
				"""
	try:
		cursor.execute(update_sql,(ciphertext,id))
		db.commit()
	except:
		print("xxxxx")
	db.close()	


def select_user(id):
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	select_sql = """ SELECT * FROM  USER
					WHERE user_id = %s
				"""
	cursor.execute(select_sql,id)
	db.commit()
	data = cursor.fetchone()
	db.close()	
	return data


def select_passwd(id):
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	select_sql = """ SELECT * FROM  USER_LOGIN
					WHERE account = %s
				"""
	cursor.execute(select_sql,id)
	db.commit()
	data = cursor.fetchone()
	return data

def select_ipe(id):
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	select_sql = """ SELECT * FROM  IPE_CIPHER
					WHERE id = %s
				"""
	cursor.execute(select_sql,id)
	db.commit()
	data = cursor.fetchone()
	db.close()
	return data

def select_aes(id):
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	select_sql = """ SELECT * FROM  FILE_CIPHER
					WHERE id = %s
				"""
	cursor.execute(select_sql,id)
	db.commit()
	data = cursor.fetchone()
	db.close()
	return data

def insert_user_infor(name,gender,phone,age,department,title,passwd):
	insert_user(name,gender,phone,age,department,title)
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	select_sql = "SELECT * FROM  USER "
	cursor.execute(select_sql)
	db.commit()
	data = cursor.fetchall()
	db.close()
	id = data[-1][0]
	print(id)
	# passwd = libcrypto.hash_passwd(passwd)
	insert_login(id,passwd,name)
	return id

def show_user():
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	select_sql = "SELECT * FROM  USER "
	cursor.execute(select_sql)
	data = cursor.fetchall()
	res = ""
	for i in range(len(data)):
		(user_id,name,gender,phone,age,department,title) = data[i]
		str_gender = ""
		if gender == 1:
			str_gender = "男"
		elif gender == 2:
			str_gender = "女"
		else:
			str_gender = "不详"
		str_data = str((user_id,name,str_gender,phone,age,department,title))
		res+= str_data
		res+="\n"
	db.commit()
	db.close()
	return res

def delete_by_id(id):
	delete_user(id)
	delete_login(id)
	res = "删除工号为" + id +"的用户信息成功!\n"
	return res

def upload_file(filename,aes,ipe):
	userid = 0
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	select_sql = "SELECT * FROM  IPE_CIPHER "
	cursor.execute(select_sql)
	data = cursor.fetchall()
	for row in data:
		if row[1] == filename:
			print("yes")
			userid = row[0]
			break
	db.close()
	if userid != 0:
		# delete_file(userid)
		# delete_ipe(userid)

		update_file(userid,aes)
		update_ipe(userid,ipe)
	else:
		insert_ipe(filename,ipe)
		insert_file(filename,aes)

def show_file():
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	select_sql = "SELECT * FROM  FILE_CIPHER "
	cursor.execute(select_sql)
	data = cursor.fetchall()
	db.close()
	res = "(文件编号，文件名，拥有者，上传时间)\n"
	for row in data:
		(fileid,filename,owner,upload_time,cipher) = row
		res += str((fileid,filename,owner,upload_time))
		res += "\n"
	return res


def show_ipe():
	db = pymysql.connect(host='localhost',
     user='root',
     password='joker7355608',
     database='IPE')
	cursor = db.cursor()
	select_sql = "SELECT id,cipher FROM  IPE_CIPHER "
	cursor.execute(select_sql)
	data = cursor.fetchall()
	db.close()
	return data



