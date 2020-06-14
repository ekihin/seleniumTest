# -*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-03-22 21:46
# software: PyCharm

def outer():
    x = 10

    def inner():
        print(x)

    return inner


a = outer()
a()
outer()()
