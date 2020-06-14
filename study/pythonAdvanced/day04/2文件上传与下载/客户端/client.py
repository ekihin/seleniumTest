#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-04-08 22:15
# software: PyCharm
import socket
import os

sk = socket.socket()
sk.connect(("127.0.0.1",13001))

def post_file(sk_obj,file_path):
    #发送文件大小
    file_size = int(os.stat(file_path).st_size)  #获取文件大小
    sk_obj.sendall(str(file_size).encode("utf-8"))
    #避免粘包
    sk_obj.recv(1024)

    #发送文件名称
    file_name = os.path.split(file_path)[1]
    sk_obj.sendall(file_name.encode("utf-8"))
    sk_obj.recv(1024)

    #发送文件内容
    with open(file_path,"rb")as f:
        while file_size >0:
            sk_obj.sendall(f.read(1024))
            file_size = file_size-1024


post_file(sk,"./a.jpg")
sk.close()