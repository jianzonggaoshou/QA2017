# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class EquipmentTypeManagement(unittest.TestCase):

	def setUp(self):
		print("test case start")
		# self.browser = webdriver.Chrome()
		self.browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
		self.browser.maximize_window()
		# self.browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
		self.browser.get("http://192.168.8.250:8088/sitopeuv/")
		sleep(3)
		# 登录密码
		self.browser.find_element_by_id('userName').send_keys('biandongfeng')
		self.browser.find_element_by_id('userPwd').send_keys('12345678')
		# 登录
		self.browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/p[3]/input').click()
		# 等待
		sleep(5)

	def tearDown(self):
		print("test case end")
		sleep(10)
		self.browser.quit()

	# @unittest.skip("直接跳过测试test_build_EquipmentType")
	def test_build_EquipmentType(self):
		# 资源管理
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="accordion"]/li[2]/div/i').click()
		sleep(1)
		self.browser.find_element_by_link_text('设备类型管理').click()
		# 新增
		sleep(2)
		self.browser.find_element_by_id('news').click()
		# 表单
		sleep(1)
		self.browser.find_element_by_id('name').send_keys(u'设备test2')
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/div[2]/div/div/form/div[2]/textarea').send_keys(u'test')
		# 确定
		self.browser.find_element_by_xpath('//*[@id="new-save"]').click()

	# @unittest.skip("直接跳过测试test_cancel_EquipmentType")
	def test_cancel_EquipmentType(self):
		# 资源管理
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="accordion"]/li[2]/div/i').click()
		sleep(1)
		self.browser.find_element_by_link_text('设备类型管理').click()
		# 删除
		sleep(1)
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/table/tbody/tr[1]/td[3]/button[2]').click()


if __name__ == "__main__":
	unittest.main()
