#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-03-25 20:06
# software: PyCharm

from selenium import webdriver
import time

driver = webdriver.Chrome("E:\\driver\\chromedriver.exe")
driver.get("https://m.weibo.cn/")
time.sleep(2)
el = driver.find_element_by_class_name("m-font.m-font-search").click()
time.sleep(2)
el1 = driver.find_elements_by_class_name("m-item-box")[7].click()
time.sleep(1)
eles = driver.find_elements_by_xpath("//span[@class='m-link-icon']/img")
time.sleep(2)
hot = []
fei = []
new = []
for ele in eles:
    textin = ele.find_element_by_xpath("../../span[@class='main-text m-text-cut']").text
    icontext = ele.get_attribute('src')
    if 'hot.png' in icontext:
        hot.append(textin)
    elif 'fei.png' in icontext:
        fei.append(textin)
    elif 'new.png' in icontext:
        new.append(textin)
print('热：',hot)
print('沸：',fei)
print('新：',new)

driver.quit()