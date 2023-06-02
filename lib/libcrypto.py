from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import random
import hashlib

def generate_rand(n):
    """
        随机字符串生成函数，用于生成AES加密所用的密钥及初始化向量
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    for i in range(n):
        random_str += base_str[random.randint(0,len(base_str) - 1)]
    return random_str.encode()

class AesCrypto():
    def __init__(self, key, IV):
        self.key = key
        self.iv = IV
        self.mode = AES.MODE_CBC
    
    # 加密函数，不是16的倍数会自动填充"\0"
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv) 
        length = 16
        count = len(text)
        if(count%length != 0):
            add = length-(count%length)
        else:
            add = 0

        text = text+("\0".encode()*add)  

        self.ciphertext = cryptor.encrypt(text)
        return (self.ciphertext)
    # 解密函数
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        plain_text = cryptor.decrypt((text)).decode()
        # return plain_text.rstrip("\0")  
        return plain_text

 
def  hash_passwd(text):
    cryptor = hashlib.sha256()    # Get the hash algorithm.
    cryptor.update(text.encode())    # Hash the data.
    hash_val = cryptor.hexdigest()       # Get he hash value.
    return hash_val


# y向量扩展
def y_extension(arr):
    list = [0.0] * (len(arr) + 2)
    sum  = 0
    for i in range(len(arr)):
      sum += arr[i] ** 2
      list[i + 1] = arr[i]
    list[0] = 1
    list[-1] = sum
    for i in range(len(list)):
      list[i] *= 10
      list[i] = int(list[i])
    return list

# x向量扩展
def x_extension(arr):
    list = [0.0] * (len(arr) + 2)
    sum  = 0
    for i in range(len(arr)):
      sum += arr[i] ** 2
      list[i + 1] = -2 * arr[i]
    list[-1] = 1
    list[0] = sum
    for i in range(len(list)):
      list[i] *= 10
      list[i] = int(list[i])
    return list


