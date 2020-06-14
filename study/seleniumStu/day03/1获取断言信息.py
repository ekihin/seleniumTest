#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-06-07 19:02
# software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("E:\\driver\\chromedriver.exe")
driver.get('http://www.toutiao.com')
link = driver.find_element_by_link_text('热点')
if '热点' == link.text:
    print('断言通过')

