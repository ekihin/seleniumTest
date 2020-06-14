#coding:utf8
import MySQLdb

#打开数据库连接
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',port=3306,db='plesson')

#获取游标
cu = conn.cursor()

#通过excute方法执行sql语句
cu.execute("select version();")

#获取结果
#data  = cu.fetchone() #获取一条结果
datas = cu.fetchall()#获取所有
#datax = cu.fetchmany(5) #获取x条记录


#释放语句
cu.close()
conn.close()