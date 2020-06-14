#coding:utf8
# import os
# import subprocess
#
# # os.system('ipconfig')
#
#
# out = subprocess.check_output("ipconfig")
# #print(out.decode('gbk'))
# print('hhhh')
#

from subprocess import Popen,PIPE

# var = Popen("mspaint")
# print("dsdsd")
# var.wait()
# print(var)

# #输出重定向
# child = Popen(
#     "ipconfig",
#     stdout=PIPE,
#     encoding="gbk"
# )
# output,err = child.communicate()


#输入重定向
child = Popen(
    'python ioTest.py',
    stdout=PIPE,
    stdin=PIPE,
    stderr=PIPE,
    encoding='gbk'
)
output,err = child.communicate('\n'.join(['1','2']))
print('\n'.join(['1','2']))
print(output)