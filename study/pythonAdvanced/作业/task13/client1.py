#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-04-13 22:01
# software: PyCharm
import sys
from socket import socket,AF_INET,SOCK_STREAM


HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


class CloseSocketError(Exception):
    pass


class ConnectionHandler:
    NAME = 'roen'
    TYPE = 1
    BUFSIZ = 1024
    LEN_MSG_LEN_TYPE_FIELD = 7
    LEN_MSG_LEN_FIELD =  4
    _readbuffer = b''

    def __init__(self,sock):
        self.sock = sock
        self.sendMsg(1,self.NAME)

    @staticmethod
    def encode(msgType,msgBody):
        rawMsgBody = msgBody.encode('utf8')

        msgLenth = '{:04}'.format(len(rawMsgBody)+ConnectionHandler.LEN_MSG_LEN_TYPE_FIELD).encode()

        msgType = f'{msgType}'.encode()
        return b'|'.join([msgLenth,msgType,rawMsgBody])

    @staticmethod
    def decode(rawmsg):
        msgType = int(rawmsg[5:6])  # 这样写rawmsg[5] 返回的是字节对应的数字
        msgbody = rawmsg[ConnectionHandler.LEN_MSG_LEN_TYPE_FIELD:].decode('utf8')
        return [msgType,msgbody]

    def readMsg(self):
        bytes = self.sock.recv(self.BUFSIZ)

        # ** 用不同的返回值表示不同的含义

        # 当对方关闭连接的时候，抛出异常
        if not bytes:
            self.sock.close()
            raise CloseSocketError()

        # 应用程序的读取缓冲，和前面讲的系统的读取缓冲是两个不同的缓冲
        self._readbuffer += bytes

        buffLen = len(self._readbuffer)

        # 如果已经获取了消息头部 (包括 消息长度，消息类型)
        if buffLen >= self.LEN_MSG_LEN_TYPE_FIELD:
            msgLen = int(self._readbuffer[:self.LEN_MSG_LEN_FIELD])
            # 缓存区消息 已经包含了一个整体的消息(包括 消息长度，消息类型，消息体)
            if buffLen >= msgLen:
                # 从缓存区，截取整个消息
                msg = self._readbuffer[0:msgLen]
                # 缓存区变成剩余的消息部分
                self._readbuffer = self._readbuffer[msgLen:]

                return self.decode(msg)

        # 如果已经获取的消息还不包括一个完整的消息头部, 不做处理等待下面继续接受消息
        else:
            return None

        print('get:%s' % bytes)

    # msgBody 是 unicode
    def sendMsg(self,msgType,msgBody):
        self.sock.sendall(self.encode(msgType,msgBody))

    def handleMsg(self,msgType,msgBody):
        print(msgBody)
        print('---------------')
        # 回复客服消息
        msgSend = input('>>')
        self.sendMsg(2,msgSend)

    # 主循环，不断的接受消息发送消息
    def mainloop(self):
        while True:
            try:
                msg = self.readMsg()
                # msg 里面包含了 type 和body
                if msg:
                    msgType,msgBody= msg
                    self.handleMsg(msgType,msgBody)
            except CloseSocketError:
                print('成功断开连接')
                break
            except IOError:
                print('成功断开连接')
                break


#创建socket，指明协议
tcpSerSock = socket(AF_INET, SOCK_STREAM)

#绑定地址和端口
tcpSerSock.connect(ADDR)
handler = ConnectionHandler(tcpSerSock)


msg = input(">>>>")
handler.sendMsg(2,msg)
#阻塞式等待连接请求
handler.mainloop()

tcpSerSock.close()