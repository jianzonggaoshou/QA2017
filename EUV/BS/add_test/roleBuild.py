# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class RoleBuild(unittest.TestCase):

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

	def test_roleBuild(self):
		# 系统管理
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[1]/div[1]/div/div[1]/i').click()
		sleep(1)
		self.browser.find_element_by_link_text('角色权限').click()
		# 新增
		sleep(2)
		self.browser.find_element_by_id('buttonToAdd').click()
		# 表单
		sleep(1)
		self.browser.find_element_by_id('name').send_keys(u'角色test94444444')
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav3-content/div[2]/div/div/form/div[2]/textarea').send_keys(
			u'test	')
		# 确定
		self.browser.find_element_by_xpath('//*[@id="new-save"]').click()


if __name__ == "__main__":
	unittest.main()
