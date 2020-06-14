#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-03-27 23:33
# software: PyCharm
from selenium import webdriver
import time

driver = webdriver.Chrome()
url = 'G:/pycharm_workspace/script/study/seleniumStu/day01/test.html'
driver.get(url)
driver.find_element_by_id("username").send_keys("张三")
driver.find_element_by_id("password").send_keys("123")

driver.find_element_by_class_name("uname").send_keys("李四")
driver.find_element_by_class_name("pwd").send_keys("456")

driver.find_element_by_name("pwd").clear()

text = driver.find_element_by_tag_name("p").text
print(text)

#driver.find_element_by_link_text("抗击肺炎").click()

driver.find_element_by_partial_link_text("肺炎").click()