#coding:utf8
import requests
import MySQLdb

def get_courese_from_api():
    res = requests.get("http://127.0.0.1/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20")
    return res.json()['retlist']


def get_course_from_db():
    conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='plesson',charset='utf8')
    cu = conn.cursor()
    sql = 'select * from sq_course;'
    cu.execute(sql)
    data =cu.fetchall()
    cu.close()
    conn.close()
    return data

if __name__ == '__main__': 
    dbData = get_course_from_db()
    apiData = get_courese_from_api()
    for ele in dbData:
        print(ele)
    for ele in apiData:
        course_info = ['','','','']
        i = 0
        for value in ele.values():
            course_info[i] = value
            i +=1

