# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import csv

print("test case start")
# self.browser = webdriver.Chrome()
browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
browser.maximize_window()
browser.get("http://192.168.8.88:8888/sitopeuv")
# self.browser.get("http://192.168.8.250:8088/sitopeuv/")
sleep(3)
# 登录密码
browser.find_element_by_id('userName').clear()
browser.find_element_by_id('userName').send_keys('biandongfeng')
browser.find_element_by_id('userPwd').clear()
browser.find_element_by_id('userPwd').send_keys('12345678')
# 登录
browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/p[3]/input').click()
# 等待
sleep(5)

# 系统管理
browser.find_element_by_xpath('/html/body/div/index-header/div[1]/div[1]/div/div[1]/i').click()
sleep(1)
browser.find_element_by_link_text('角色权限').click()

# 读取csv文件
data = csv.reader(open('userDataModel.csv', 'r'))

for userData in data:

	print ('角色名称:'),
	print (userData[0].decode('gb2312')),
	print ('备注:'),
	print (userData[1].decode('gb2312'))
	# 新增
	sleep(2)
	browser.find_element_by_id('buttonToAdd').click()
	# 表单
	sleep(1)
	browser.find_element_by_id('name').clear()
	browser.find_element_by_id('name').send_keys(userData[0].decode('gb2312'))
	browser.find_element_by_xpath(
		'/html/body/div/index-header/div[3]/nav3-content/div[2]/div/div/form/div[2]/textarea').clear()
	browser.find_element_by_xpath(
		'/html/body/div/index-header/div[3]/nav3-content/div[2]/div/div/form/div[2]/textarea').send_keys(
		userData[1].decode('gb2312'))
	# 确定
	browser.find_element_by_xpath('//*[@id="new-save"]').click()

sleep(3)
browser.quit()