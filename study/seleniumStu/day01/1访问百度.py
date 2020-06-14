#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-03-27 23:11
# software: PyCharm
from selenium import webdriver
import time

driver = webdriver.Chrome()
url = 'G:/pycharm_workspace/script/study/seleniumStu/day01/test.html'
driver.get(url)