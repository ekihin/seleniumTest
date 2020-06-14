#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-06-07 18:12
# software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("E:\\driver\\chromedriver.exe")
driver.get("http://www.toutiao.com")
driver.maximize_window()
#鼠标悬停在更多
ActionChains(driver).move_to_element(driver.find_element_by_class_name('channel-more')).perform()

urlList = driver.find_element_by_css_selector(
    'body > div > div.bui-box.container > div.bui-left.index-channel > div > div > ul')
spList  = urlList.find_elements_by_tag_name('span')
for i in spList:
    print(i.text)