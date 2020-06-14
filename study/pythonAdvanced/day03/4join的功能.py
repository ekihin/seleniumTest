#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-03-23 23:40
# software: PyCharm
import time
import threading

def foo():
    time.sleep(3)
    print('阳光明媚')

t1 = threading.Thread(target=foo)
t1.start()
t1.join()
print("主线程的最后一行代码")