#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-06-07 16:04
# software: PyCharm

from selenium import webdriver
#如果需要鼠标操作，必须引入ActionChains
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("E:\\driver\\chromedriver.exe")
driver.get("http://www.baidu.com")
setting  = driver.find_element_by_class_name("s-top-right-text.c-font-normal.c-color-t")
ActionChains(driver).move_to_element(setting).perform()
moreSetting = driver.find_element_by_class_name("setpref").click()


