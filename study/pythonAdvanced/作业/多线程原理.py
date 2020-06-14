#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-04-07 21:26
# software: PyCharm

import requests
import threading
import time
file  = "readme89.TXT"
r1 = "http://mirrors.163.com/centos/6/isos/x86_64/README.txt"
r2 = "http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt"
_text = ''
local = threading.Lock()

def getText(url):
    global _text
    global local
    local.acquire()
    _text += _text + requests.get(url).text
    local.release()


thread1 = threading.Thread(target=getText,args=[r1])
thread2 = threading.Thread(target=getText,args=[r2])

thread1.start()
thread2.start()
thread1.join()
thread2.join()
with open(file,'w+') as file1:
    file1.write(_text)


