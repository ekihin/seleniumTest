#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-04-04 22:56
# software: PyCharm
import threading
import time
balance = 500
r = threading.Lock()

#操作账户余额
def foo(num):
    #申明全局变量
    global balance
    r.acquire()
    account_balance = balance
    time.sleep(1)
    account_balance = account_balance + num
    balance = account_balance
    r.release()


t1 = threading.Thread(target=foo,args=[-300])
t2 = threading.Thread(target=foo,args=[1000])

t1.start()
t2.start()
t1.join()
t2.join()

print(balance)