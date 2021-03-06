# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class DetectionManagement(unittest.TestCase):
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

	# @unittest.skip("test_build_Detection")
	def test_build_Detection(self):
		# *******************创建设备***********************
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
		self.browser.find_element_by_id('name').send_keys(u'设备test1')
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/div[2]/div/div/form/div[2]/textarea').send_keys(u'test')
		# 确定
		self.browser.find_element_by_xpath('//*[@id="new-save"]').click()

		# ********************巡检项管理新增******************
		# 资源管理
		sleep(2)
		self.browser.find_element_by_link_text('检测项管理').click()
		# 新增
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="box"]/div[1]/div/div/div/p/button').click()
		# 表单
		# ***********************定性*************************
		sleep(2)
		self.browser.find_element_by_xpath(
			'//html/body/div/index-header/div[3]/nav5-content/div[2]/div/p[2]/input').send_keys(u'检测项定性test1')
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="one"]/span').click()
		self.browser.find_element_by_xpath('//*[@id="one"]/span').click()
		self.browser.find_element_by_xpath('//*[@id="one"]/span').click()
		# 输入
		self.browser.find_element_by_xpath('//*[@id="one"]/p[1]/input').clear()
		self.browser.find_element_by_xpath('//*[@id="one"]/p[1]/input').send_keys(u'是')
		self.browser.find_element_by_xpath('//*[@id="one"]/p[2]/input').clear()
		self.browser.find_element_by_xpath('//*[@id="one"]/p[2]/input').send_keys(u'否')
		self.browser.find_element_by_xpath('//*[@id="one"]/p[3]/input').clear()
		self.browser.find_element_by_xpath('//*[@id="one"]/p[3]/input').send_keys(u'是否')
		# 保存
		sleep(1)
		self.browser.find_element_by_id('all-sava1').click()
		# ***********************定量*************************
		# 新增
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="box"]/div[1]/div/div/div/p/button').click()
		sleep(2)
		self.browser.find_element_by_xpath(
			'//html/body/div/index-header/div[3]/nav5-content/div[2]/div/p[2]/input').send_keys(u'检测项定量test1')
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="elect"]/input[2]').click()
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav5-content/div[2]/div/div[2]/p[1]/input').send_keys(
			'kV')  # ********************巡检项管理新增******************
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav5-content/div[2]/div/div[2]/p[2]/input').send_keys(
			'1')  # ********************巡检项管理新增******************
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav5-content/div[2]/div/div[2]/p[3]/input').send_keys('10')
		# 保存
		sleep(1)
		self.browser.find_element_by_id('all-sava1').click()

		# ********************拍照******************
		# 新增
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="box"]/div[1]/div/div/div/p/button').click()
		sleep(2)
		self.browser.find_element_by_xpath(
			'//html/body/div/index-header/div[3]/nav5-content/div[2]/div/p[2]/input').send_keys(u'检测项拍照test1')
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="elect"]/input[3]').click()
		# 保存
		sleep(1)
		self.browser.find_element_by_id('all-sava1').click()

		# ********************模板管理新增******************
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="box"]/span[2]').click()
		# 新增
		sleep(1)
		self.browser.find_element_by_id('sten-new').click()
		# 表单
		self.browser.find_element_by_id('name').send_keys(u'设备test模板1')
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav5-content/div[4]/div/div[1]/form/div[2]/textarea').send_keys(u'test')
		# 确定
		self.browser.find_element_by_id('sten-save').click()

		# 配置
		sleep(2)
		self.browser.find_element_by_id('sten-amend').click()
		# 选择检测项
		sleep(1)
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav5-content/div[5]/div/div[1]/input').click()
		sleep(1)
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav5-content/div[5]/div/div[2]/input').click()
		sleep(1)
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav5-content/div[5]/div/div[3]/input').click()
		# 确定
		sleep(2)
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav5-content/div[5]/div/p[4]/button[1]').click()

	# @unittest.skip("直接跳过测试test_cancel_Detection")
	def test_cancel_Detection(self):
		# 资源管理
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="accordion"]/li[2]/div/i').click()
		sleep(1)
		self.browser.find_element_by_link_text('检测项管理').click()
		# 巡检项管理删除
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="box"]/div[1]/div/div/div/table/tbody/tr/td[3]/button[2]').click()
		# 模板管理删除
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="box"]/span[2]').click()
		sleep(1)
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav5-content/div[1]/div[2]/table/tbody/tr/td[3]/button[2]').click()
		# 设备类型删除
		sleep(1)
		self.browser.find_element_by_link_text('设备类型管理').click()
		# 删除
		sleep(1)
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/table/tbody/tr[1]/td[3]/button[2]').click()


if __name__ == "__main__":
	unittest.main()
