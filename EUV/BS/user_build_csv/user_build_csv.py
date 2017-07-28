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
browser.find_element_by_link_text('用户管理').click()

# 读取csv文件
data = csv.reader(open('userDataModel.csv', 'r'))

for userData in data:

	print ('用户名:'),
	print (userData[0]),
	print ('真实姓名:'),
	print (userData[1].decode('gb2312')),
	print ('密码:'),
	print (userData[2]),
	print ('确认密码:'),
	print (userData[3]),
	print ('手机号码:'),
	print (userData[4]),
	print ('办公电话:'),
	print (userData[5])
	# 新增
	sleep(1)
	browser.find_element_by_id('button2').click()
	# 表单
	browser.find_elements_by_xpath('//*[@id="name"]')[0].send_keys(userData[0])
	browser.find_elements_by_xpath('//*[@id="name"]')[1].send_keys(userData[1].decode('gb2312'))
	browser.find_elements_by_xpath('//*[@id="name"]')[2].send_keys(userData[2])
	browser.find_elements_by_xpath('//*[@id="name"]')[3].send_keys(userData[3])
	browser.find_elements_by_id('tel')[0].send_keys(userData[4])
	browser.find_elements_by_id('tel')[1].send_keys(userData[5])

	browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div[2]/div/div/form/div[7]/span/div/div/button').click()
	browser.find_element_by_link_text('企业管理员').click()
	browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div[2]/div/div/form/div[7]/span/div/div/button').click()
	browser.find_element_by_id('new-save').click()

sleep(3)
browser.quit()