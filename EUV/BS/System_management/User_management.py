# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class UserManagement(unittest.TestCase):

	def setUp(self):
		print("test case start")
		# self.browser = webdriver.Chrome()
		self.browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
		self.browser.maximize_window()
		self.browser.get("http://192.168.8.88:8888/sitopeuv")
		# self.browser.get("http://192.168.8.250:8088/sitopeuv/")
		sleep(3)
		# 登录密码
		self.browser.find_element_by_id('userName').clear()
		self.browser.find_element_by_id('userName').send_keys('biandongfeng')
		self.browser.find_element_by_id('userPwd').clear()
		self.browser.find_element_by_id('userPwd').send_keys('12345678')
		# 登录
		self.browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/p[3]/input').click()
		# 等待
		sleep(5)

	def tearDown(self):
		print("test case end")
		sleep(10)
		self.browser.quit()

	# @unittest.skip("直接跳过测试test_build_user")
	def test_build_user(self):
		# 系统管理
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[1]/div[1]/div/div[1]/i').click()
		sleep(1)
		self.browser.find_element_by_link_text('用户管理').click()
		# 新增
		sleep(1)
		self.browser.find_element_by_id('button2').click()
		# 表单
		self.browser.find_elements_by_xpath('//*[@id="name"]')[0].send_keys('xuzhenaaa')
		self.browser.find_elements_by_xpath('//*[@id="name"]')[1].send_keys(u'许臻')
		self.browser.find_elements_by_xpath('//*[@id="name"]')[2].send_keys('123456')
		self.browser.find_elements_by_xpath('//*[@id="name"]')[3].send_keys('123456')
		self.browser.find_elements_by_id('tel')[0].send_keys('15609100803')
		self.browser.find_elements_by_id('tel')[1].send_keys('029-123456')

		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/div[2]/div/div/form/div[7]/span/div/div/button').click()
		self.browser.find_element_by_link_text('企业管理员').click()
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/div[2]/div/div/form/div[7]/span/div/div/button').click()
		self.browser.find_element_by_id('new-save').click()

	# @unittest.skip("直接跳过测试test_cancel_user")
	def test_cancel_user(self):
		# 系统管理
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[1]/div[1]/div/div[1]/i').click()
		sleep(1)
		self.browser.find_element_by_link_text('用户管理').click()
		# 删除第一个用户
		sleep(1)
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/table/tbody/tr[1]/td[7]/button[2]').click()
		sleep(1)
		self.browser.find_element_by_id('ensure').click()


if __name__ == "__main__":
	unittest.main()
