#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-04-08 22:15
# software: PyCharm

import socket

sk = socket.socket()
sk.bind(("127.0.0.1",13001))
sk.listen()

def get_file(sk_obj):
    file_size = int(sk_obj.recv(1024).decode("utf-8"))
    sk_obj.sendall(b'ok')
    file_name = sk_obj.recv(1024).decode("utf-8")
    sk_obj.sendall(b'ok')

    with open("./%s"%file_name,'wb') as f:
        while file_size >0 :
            f.write(sk_obj.recv(1024))
            file_size =  file_size-1024

conn,addr = sk.accept()
get_file(conn)
conn.close()
sk.close()