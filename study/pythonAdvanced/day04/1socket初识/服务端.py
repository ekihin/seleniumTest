#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-04-07 22:21
# software: PyCharm
import socket

ip = ('127.0.0.1',13000)

sk = socket.socket()
sk.bind(ip)
sk.listen()
print("服务端启动了")

conn,addr = sk.accept()
print("客户端的地址为：",addr)

client_data = conn.recv(1024).decode("utf-8")
print("客户端：",client_data)

send_data = input(">>>")
conn.sendall(send_data.encode("utf-8"))

conn.close()
sk.close()