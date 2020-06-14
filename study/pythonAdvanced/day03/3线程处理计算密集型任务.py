#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-03-23 22:52
# software: PyCharm

import threading
import time


def foo():
    num = 0
    for i in range(10000000):
        num = num + 1


b_time = time.time()
#串行成绩：2.6s
# foo()
# foo()
t1 = threading.Thread(target=foo)
t2 = threading.Thread(target=foo)
t1.start()
t2.start()
t1.join()
t2.join()
e_time = time.time()

s_time = e_time-b_time
print(s_time)