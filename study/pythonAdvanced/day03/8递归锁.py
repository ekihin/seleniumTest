#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-04-06 22:23
# software: PyCharm


import threading
import time

localR = threading.RLock()

def foo1 ():
    localR.acquire()
    print("请解释什么是死锁")
    time.sleep(1)

    localR.acquire()
    print("发offer")
    time.sleep(1)

    localR.release()
    localR.release()

def foo2():
    localR.acquire()
    print('请给我offer')
    time.sleep(1)

    localR.acquire()
    print('解释了什么是死锁')
    time.sleep(1)

    localR.release()
    localR.release()


t1 = threading.Thread(target=foo1)
t2 = threading.Thread(target=foo2)

t1.start()
t2.start()