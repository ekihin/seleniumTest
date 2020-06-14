#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-06-07 19:16
# software: PyCharm
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome("E:\\driver\\chromedriver.exe")
driver.get("http://m.weibo.cn")

#隐式等待，在元素定位的时候，如果查找不到，轮询检查（每0.5s检查一次），直到元素出现，如果元素超时未出现则报错
# driver.implicitly_wait(5)
# driver.find_element_by_class_name('m-search').click()
# driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div/div[8]/div/div/h4').click()

#显示等待，使webdriver等待元素出现
driver.find_element_by_class_name('m-search').click()
#显示等待微博热搜榜
ele = WebDriverWait(driver,5,0.5).until(
    ec.presence_of_element_located(
        (By.XPATH,"//*[@id=\"app\"]/div[1]/div[1]/div[2]/div/div/div[8]/div/div/h4")
    )
)
ele.click()