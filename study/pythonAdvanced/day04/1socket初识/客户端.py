#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-04-07 22:12
# software: PyCharm
import socket

sk = socket.socket()

ip = ('127.0.0.1',13000)
sk.connect(ip)

send_data = input(">>>")
sk.sendall(send_data.encode("utf-8"))


server_data = sk.recv(1024).decode("utf-8")
print("服务端：",server_data)

sk.close()