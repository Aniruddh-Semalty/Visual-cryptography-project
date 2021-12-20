import hashlib
import os
from Crypto.Cipher import AES
from PIL import Image
import math
from random import randrange, seed

def aes_encrypt(u,key,f):
    fin = open(f,'rb') 
    image = fin.read() 
    fin.close() 
    key=hashlib.sha256((str(key)).encode("utf-8")).digest()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext,tag= cipher.encrypt_and_digest(image)

    path=os.path.join(u,"encrypt")
    file1=open(os.path.join(path,"aesout.jpg"),"wb")
    file2=open(os.path.join(path,"n.txt"),"wb")
    file2.write(nonce)
    file1.write(ciphertext)
    file1.close()
    file2.close()

def aes_decrypt(u,key,f):
    key=hashlib.sha256((str(key)).encode("utf-8")).digest()
    path=os.path.join(u,"encrypt")

    file1 = open(f,'rb') 
    file3=open(os.path.join(path,"n.txt"),"rb")
    image = file1.read() 
    nonce=file3.read()
    file1.close() 
    file3.close()

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(image)

    path=os.path.join(u,"decrypt")
    file1=open(os.path.join(path,"aesout.jpg"),"wb")
    file1.write(plaintext)
    file1.close()