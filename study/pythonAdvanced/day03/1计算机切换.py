# -*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-03-22 23:51
# software: PyCharm

import threading
import time


def foo(something, num):
    for i in range(num):
        print("cpu正在：" + something)
        time.sleep(1)


t1 = threading.Thread(target=foo, args=["听音乐",5])
t2 = threading.Thread(target=foo, args=["看电影",5])
t1.start()
t2.start()
