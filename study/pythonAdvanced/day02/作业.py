#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-03-22 22:42
# software: PyCharm

user_dict = {
    'user1':'123',
    'user2':'123'
}
token = ''

def isLogin(func):
    def inner(*args):
        global token
        #判断token是否为空：
        if token == '':
            flag = False
            while flag==False:
                user = input("请输入用户名：")
                passwd = input("请输入密码：")
                if user in user_dict.keys() and passwd == user_dict[user]:
                    #用户密码正确
                    token = 32131231
                    flag = True
                else:
                    print("密码错误！")
        else:
            pass
        func(*args)
    return inner

@isLogin
def my_log():
    print('my_log')

@isLogin
def my_name(name):
    print(name)

@isLogin
def my_shopping_mall():
    print("商城购物")

while True:
    choose_num = input('\n\n1.查看日志\n2.我的信息\n3.我的商城\n请输入操作选项(输入q退出)》》》')
    if choose_num == 'q' or choose_num == "Q":
        break
    elif choose_num == '1':
        my_log()
    elif choose_num == '2':
        my_name('张三')
    elif choose_num == '3':
        my_shopping_mall()