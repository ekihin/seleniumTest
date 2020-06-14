#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-04-06 22:15
# software: PyCharm
import threading
import time

localA = threading.Lock()
localB = threading.Lock()

def foo1 ():
    localA.acquire()
    print("请解释什么是死锁")
    time.sleep(1)

    localB.acquire()
    print("发offer")
    time.sleep(1)

    localB.release()
    localA.release()

def foo2():
    localB.acquire()
    print('请给我offer')
    time.sleep(1)

    localA.acquire()
    print('解释了什么是死锁')
    time.sleep(1)

    localA.release()
    localB.release()

t1 = threading.Thread(target=foo1)
t2 = threading.Thread(target=foo2)

t1.start()
t2.start()