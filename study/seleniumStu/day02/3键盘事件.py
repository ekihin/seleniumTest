#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-06-07 16:39
# software: PyCharm
from time import sleep

from selenium import webdriver
#如果需要鼠标操作，必须引入ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("E:\\driver\\chromedriver.exe")
driver.get("http://www.baidu.com")

kw = driver.find_element_by_id('kw')
driver.find_element_by_id('kw').send_keys("selenium")
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
kw.send_keys(Keys.SPACE)
kw.send_keys("教程")
kw.send_keys(Keys.CONTROL,'a')
kw.send_keys(Keys.CONTROL,'x')
sleep(3)
kw.send_keys(Keys.CONTROL,'v')
driver.find_element_by_id('kw').send_keys(Keys.ENTER)