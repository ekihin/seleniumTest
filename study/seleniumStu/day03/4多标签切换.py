#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-06-07 20:55
# software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("E:\\driver\\chromedriver.exe")
driver.get("http://www.baidu.com")
driver.find_element_by_link_text('新闻').click()
print("百度首页的句柄",driver.current_window_handle)
current = driver.current_window_handle
handles = driver.window_handles
for i in handles:
    if i != current:
        driver.switch_to.window(i)
        if '百度新闻' in driver.title:
            driver.find_element_by_class_name('word').send_keys('hah')
            break
driver.close()
driver.switch_to.window(current)
print(driver.title)
