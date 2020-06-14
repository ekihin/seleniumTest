#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-04-12 19:43
# software: PyCharm

#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-04-12 19:38
# software: PyCharm

import socket

sk = socket.socket()
sk.connect(("127.0.0.1",13003))
print("客户端启动了")

while True:
    message = "哈里：" + input(">>>")
    sk.sendall(message.encode("utf8"))

    if message == "exit":
        break

    sever_data = sk.recv(1024).decode("utf8")
    print(sever_data)
