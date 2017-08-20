# coding=utf-8
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_id("su").click()
sleep(300)
driver.quit()
