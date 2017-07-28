# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import time


class UserManagement(unittest.TestCase):

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

	# @unittest.skip("直接跳过测试test_page_click")
	def test_page_click(self):

		# *****************************系统管理************************************
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="accordion"]/li[1]/div/i').click()
		# 用户管理
		sleep(1)
		self.browser.find_element_by_link_text('用户管理').click()
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/用户管理%s.jpg' % now)
		# 组织部门管理
		sleep(1)
		self.browser.find_element_by_link_text('组织部门管理').click()
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/组织部门管理%s.jpg' % now)

		sleep(1)
		self.browser.find_element_by_link_text('角色权限').click()
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/角色权限%s.jpg' % now)

		# *****************************资源管理********************************
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="accordion"]/li[2]/div/i').click()
		# 设备类型管理
		sleep(1)
		self.browser.find_element_by_link_text('设备类型管理').click()
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/设备类型管理%s.jpg' % now)
		# 检测项管理
		sleep(1)
		self.browser.find_element_by_link_text('检测项管理').click()
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/检测项管理%s.jpg' % now)
		# 台账管理
		sleep(1)
		self.browser.find_element_by_link_text('台账管理').click()
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/台账管理%s.jpg' % now)

		# ******************************故障中心************************************
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="accordion"]/li[3]/div/i').click()
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/故障中心%s.jpg' % now)

		# ******************************待办任务************************************
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="accordion"]/li[4]/div/i').click()
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/待办任务%s.jpg' % now)

		# ******************************设备状态列表************************************
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="accordion"]/li[5]/div/i').click()
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/设备状态列表%s.jpg' % now)

		# ******************************检修列表************************************
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="accordion"]/li[5]/div/i').click()
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/检修列表%s.jpg' % now)

		# ******************************设备状态列表************************************
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="accordion"]/li[5]/div/i').click()
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/设备状态列表%s.jpg' % now)





if __name__ == "__main__":
	unittest.main()
