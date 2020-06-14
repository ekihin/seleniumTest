#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-03-23 22:37
# software: PyCharm
import time
import threading


def foo(something):
    print(something)
    time.sleep(2)

begin_time = time.time()

t1 = threading.Thread(target=foo,args=['磁盘写入数据'])
t2 = threading.Thread(target=foo,args=['cpu执行其他事情'])
t1.start()
t2.start()
#阻塞主线程
t1.join() #在线程t1运行结束之前，组织主线程继续运行
t2.join()

# foo('磁盘写入数据')
# foo('cpu执行其他事情')

end_time = time.time()

sum_time = end_time-begin_time
print(sum_time)