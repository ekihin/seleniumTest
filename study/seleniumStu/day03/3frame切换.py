#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-06-07 20:36
# software: PyCharm


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("E:\\driver\\chromedriver.exe")
driver.get("G:\pycharm_workspace\script\study\seleniumStu\day03\\test.html")
iframe = driver.find_element_by_id('abd')
#切换到嵌套iframe
driver.switch_to.frame(iframe)
driver.find_element_by_id('kw').send_keys("哈哈哈")
driver.switch_to.default_content()
driver.find_element_by_id('kw').send_keys("哈哈哈")