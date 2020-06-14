#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-03-23 23:44
# software: PyCharm
import time
import threading

a = []

def foo():
    while True:
        a.append("1")
        print('生产了一个数据')
        time.sleep(1)
t1 = threading.Thread(target=foo)
t1.setDaemon(True)
t1.start()

for i in range(10):
    print("想要消费数据")
    if a:
        a.remove("1")
        print("消费了一个数据")
    time.sleep(0.5)
print("不需要再消费数据了")