# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class DepartBuild(unittest.TestCase):

	def setUp(self):
		print("departBuild case start"),
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
		print("departBuild case end")
		sleep(10)
		self.browser.quit()

	def test_departBuild(self):
		# 系统管理
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[1]/div[1]/div/div[1]/i').click()
		sleep(1)
		self.browser.find_element_by_link_text('组织部门管理').click()
		# 新增
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="box"]/div[2]/p/button').click()
		# 表单
		# 部门名称
		sleep(3)
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav2-content/div[2]/div/div/form/div[1]/input').send_keys(u'部门test2')
		# 部门类型
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav2-content/div[2]/div/div/form/div[2]/select').click()
		sleep(1)
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav2-content/div[2]/div/div/form/div[2]/select/option[2]').click()
		# 备注
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav2-content/div[2]/div/div/form/div[3]/textarea').send_keys(u'部门test')
		# 确定
		self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()
		# *******************************建立DOM树二级***********************************
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="box"]/div[1]/div/ol/li/ol/li[2]/div/span').click()
		# 新增
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="box"]/div[2]/p/button').click()
		# 表单
		# 部门名称
		sleep(3)
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav2-content/div[2]/div/div/form/div[1]/input').send_keys(
			u'班组test1')
		# 部门类型
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav2-content/div[2]/div/div/form/div[2]/select').click()
		sleep(1)
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav2-content/div[2]/div/div/form/div[2]/select/option[2]').click()
		# 备注
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav2-content/div[2]/div/div/form/div[3]/textarea').send_keys(
			u'班组test')
		# 确定
		self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()


if __name__ == "__main__":
	unittest.main()