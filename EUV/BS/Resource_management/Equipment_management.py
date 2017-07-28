# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class EquipmentManagement(unittest.TestCase):
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

	# @unittest.skip("直接跳过测试test_build_Equipment")
	def test_build_Equipment(self):
		# *******************新增配电室***********************
		# 资源管理
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="accordion"]/li[2]/div/i').click()
		sleep(1)
		self.browser.find_element_by_link_text('台账管理').click()
		# 新增配电室
		sleep(2)
		self.browser.find_element_by_id('newRoom').click()
		sleep(1)
		self.browser.find_element_by_id('roomName').send_keys(u'1#1配电室test')
		self.browser.find_element_by_id('roomRemark').send_keys(u'test')
		# 确定
		self.browser.find_element_by_id('newR-save').click()

		# *******************新增设备***********************
		sleep(2)
		self.browser.find_element_by_id('newEquipment').click()
		# 表单
		# 设备名称
		sleep(1)
		self.browser.find_element_by_id('equipmentName').send_keys(u'变压器test1')
		# 设备类型
		sleep(1)
		self.browser.find_element_by_id('equipmentTypeId').click()
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="equipmentTypeId"]/option[5]').click()
		# 配电室
		sleep(1)
		self.browser.find_element_by_id('roomId').click()
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="roomId"]/option[2]').click()
		# 设备编号
		sleep(1)
		self.browser.find_element_by_id('equipmentSn').send_keys('shebeibianhao1')
		# 出厂编号
		sleep(1)
		self.browser.find_element_by_id('equipmentFsn').send_keys('chuchangbianhao1')
		# 生产厂商
		sleep(1)
		self.browser.find_element_by_id('manufacturer').send_keys('shengchanchangshang1')
		# 供应厂商
		sleep(1)
		self.browser.find_element_by_id('supplier').send_keys('gongyingchangshang1')
		# 运行状态
		sleep(1)
		self.browser.find_element_by_id('workingState').click()
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="workingState"]/option[10]').click()
		# 设备状态
		sleep(1)
		self.browser.find_element_by_id('equipmentState').click()
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="equipmentState"]/option[2]').click()
		# 备注
		sleep(1)
		self.browser.find_element_by_id('equipmentRemark').send_keys(u'test备注')
		# 确定
		sleep(1)
		self.browser.find_element_by_id('newE-save').click()


if __name__ == "__main__":
	unittest.main()
