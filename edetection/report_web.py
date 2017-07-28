# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import time

# browser = webdriver.Chrome()
browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
browser.maximize_window()

browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
# browser.get("http://114.215.94.141:8081/SITO2000/login.jsp")
browser.find_element_by_id("userId").send_keys("15609100803")
browser.find_element_by_id("password").send_keys("123456")
browser.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[3]/button').click()

sleep(3)
browser.find_element_by_xpath('//*[@id="ext-gen35"]/user_build_csv').click()
sleep(1)
browser.find_element_by_link_text("未生成报告").click()
sleep(1)

# 跳入框架
browser.switch_to.frame("mainFrame")
browser.switch_to.frame("/sito2000/workflow/no_generated_report_list.jsp")

# 选择对应报告并生成报告
sleep(1)
browser.find_element_by_xpath('//*[@id="ext-gen25"]/div[1]/table/tbody/tr/td[6]/div/a').click()
# 生成确定
sleep(1)
browser.find_element_by_xpath('//*[@id="ext-gen94"]').click()

sleep(3)
browser.quit()
