#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-06-07 21:39
# software: PyCharm
from selenium import webdriver

import time

driver = webdriver.Chrome("E:\\driver\\chromedriver.exe")
driver.get("http://www.51job.com")
driver.implicitly_wait(5)
driver.find_element_by_link_text('杭州').click()
current = driver.current_window_handle
handles = driver.window_handles
for i in handles:
    if i != current:
        driver.switch_to.window(i)
        if '杭州招聘网' in driver.title:
            driver.find_element_by_id('kwdselectid').send_keys('python')
            driver.find_element_by_xpath('//*[@id="supp"]/div[1]/div/div[1]/button').click()
            eles = driver.find_elements_by_class_name('el')
            for ele in eles:
                pass
            break

