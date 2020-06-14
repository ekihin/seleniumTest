#coding:utf8
import requests
import MySQLdb

def add_courese_from_api():
    res = requests.get("http://127.0.0.1/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20")
    return res.json()['retlist']


def add_course_from_db():
    db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='plesson',charset='utf8')
    cu = db.cursor()
    sql = '''insert into sq_course values (NULL,'课程2','这是课程2的描述',1) ;'''
    cu.execute(sql)
    db.commit()
    cu.close()
    db.close()

if __name__ == '__main__':
    add_course_from_db()