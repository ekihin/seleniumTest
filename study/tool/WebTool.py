#-*- coding:utf-8 -*-
# author:ekihin
# datetime:2020-06-07 19:57
# software: PyCharm
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def webWait(driver,waitTime,lTime,byEle,eleName):
    return WebDriverWait(driver,waitTime,lTime).until(
        ec.presence_of_element_located(
            byEle,eleName
        )
    )