#coding:utf8
import requests
import MySQLdb
import unittest

class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        '''连接数据库，做初始化工作'''

    @classmethod
    def tearDownClass(cls) -> None:
        db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='plesson', charset='utf8')
        cu = db.cursor()
        sql = '''delete from sq_course where name like '课程%';'''
        cu.execute(sql)
        db.commit()
        cu.close()
        db.close()

    def testClassA(self):
        pass


if __name__ == '__main__':
    lo = unittest.TestLoader()
    suit = unittest.TestSuite()
    tests = lo.loadTestsFromTestCase(TestClass)
    suit.addTest(tests)
    unittest.TextTestRunner(verbosity=2).run(suit)
