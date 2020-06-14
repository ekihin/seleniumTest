# -*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-04-12 19:30
# software: PyCharm

import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("有人来谈话了 |")
        while True:
            client_data = self.request.recv(1024).decode("utf8")
            print(client_data)

            if client_data == "罗恩：exit":
                break
            message = input(">>>")
            self.request.sendall(message.encode("utf8"))


sk = socketserver.ThreadingTCPServer(("127.0.0.1",13003),MyServer)
print("赫敏上线了...")
sk.serve_forever()