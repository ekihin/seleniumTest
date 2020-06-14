#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-06-02 23:51
# software: PyCharm
from selenium import webdriver

#1 控制浏览器大小
driver = webdriver.Chrome("E:\\driver\\chromedriver.exe")
driver.get('http://www.baidu.com')
driver.maximize_window()

driver.set_window_size(900,900)
driver.back()
driver.forward()
driver.refresh()