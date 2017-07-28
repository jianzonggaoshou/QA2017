# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class SafeBagBuild(unittest.TestCase):

	def setUp(self):
		print("RoleBuild case start"),
		# self.browser = webdriver.Chrome()
		self.browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
		self.browser.maximize_window()
		self.browser.get("http://192.168.8.88:8888/sitopeuv/")
		# self.browser.get("http://192.168.8.250:8088/sitopeuv/")
		sleep(3)
		# 登录密码
		self.browser.find_element_by_id('userName').send_keys('biandongfeng')
		self.browser.find_element_by_id('userPwd').send_keys('12345678')
		# 登录
		self.browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/p[3]/input').click()
		# 等待
		sleep(5)

	def tearDown(self):
		print("RoleBuild case end")
		sleep(10)
		self.browser.quit()

	def test_safeBagBuild(self):
		# 安全包管理
		self.browser.find_element_by_xpath('/html/body/div[1]/index-header/div[1]/div[9]/div/div[1]/i').click()
		sleep(1)
		# 新建
		sleep(2)
		self.browser.find_element_by_xpath('/html/body/div[1]/index-header/div[3]/p/button').click()
		# 表单
		# 安全包详情
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div[1]/index-header/div[3]/div[2]/div/div[1]/input').send_keys(u'安全包test1')
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div[1]/index-header/div[3]/div[2]/div/div[2]/textarea').send_keys(u'安全包test')
		# 提交
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()
		# 页列表
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div[1]/index-header/div[3]/table/tbody/tr[1]/td[3]/button[2]').click()
		# 新建
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div[1]/index-header/div[3]/p/button').click()
		# 表单
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div[1]/index-header/div[3]/div[2]/div/div[1]/input').send_keys(u'第一页')
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div[1]/index-header/div[3]/div[2]/div/div[2]/input').send_keys('1')
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div[1]/index-header/div[3]/div[2]/div/div[3]/div/div/div[2]').send_keys('1111')
		# s

if __name__ == "__main__":
	unittest.main()
