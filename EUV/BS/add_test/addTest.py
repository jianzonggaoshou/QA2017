# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import time


class AddTest(unittest.TestCase):

	# 变量赋值
	username = 'xuzhen9997'
	role = u'角色test9997'
	depart = u'部门test9997'
	group = u'班组test9997'
	equipment_type = u'设备类型test9997'
	room = u'配电室test9997'
	transformer = u'变压器test9997'
	plan = u'日计划测试test9997'
	task = u'特检任务test9997'

	def setUp(self):
		print("test case start"),
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

	# @unittest.skip("直接跳过测试test_userBuild")
	def test1_userBuild(self):
		# 系统管理
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[1]/div[1]/div/div[1]/i').click()
		sleep(1)
		self.browser.find_element_by_link_text('用户管理').click()
		# 新增
		sleep(1)
		self.browser.find_element_by_id('button2').click()
		# 表单
		self.browser.find_elements_by_xpath('//*[@id="name"]')[0].send_keys(AddTest.username)
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
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/用户管理%s.jpg' % now)

	# @unittest.skip("直接跳过测试test_roleBuild")
	def test2_roleBuild(self):
		# 系统管理
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[1]/div[1]/div/div[1]/i').click()
		sleep(1)
		self.browser.find_element_by_link_text('角色权限').click()
		# 新增
		sleep(2)
		self.browser.find_element_by_id('buttonToAdd').click()
		# 表单
		sleep(1)
		self.browser.find_element_by_id('name').send_keys(AddTest.role)
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav3-content/div[2]/div/div/form/div[2]/textarea').send_keys(
			u'test	')
		# 确定
		self.browser.find_element_by_xpath('//*[@id="new-save"]').click()
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/角色权限%s.jpg' % now)

	# @unittest.skip("直接跳过测试test_departBuild")
	def test3_departBuild(self):
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
			'/html/body/div/index-header/div[3]/nav2-content/div[2]/div/div/form/div[1]/input').send_keys(AddTest.depart)
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
		sleep(3)
		self.browser.find_element_by_xpath('//*[@id="box"]/div[1]/div/ol/li/ol/li[2]/div/span').click()
		# 新增
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="box"]/div[2]/p/button').click()
		# 表单
		# 部门名称
		sleep(3)
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/nav2-content/div[2]/div/div/form/div[1]/input').send_keys(AddTest.group)
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
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/组织部门管理%s.jpg' % now)

	# @unittest.skip("直接跳过测试test_equipmentTypeBuild")
	def test4_equipmentTypeBuild(self):
		# 资源管理
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[1]/div[2]/div/div[1]/i').click()
		sleep(1)
		self.browser.find_element_by_link_text('设备类型管理').click()
		# 新增
		sleep(2)
		self.browser.find_element_by_id('news').click()
		# 表单
		sleep(1)
		self.browser.find_element_by_id('name').send_keys(AddTest.equipment_type)
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/div[2]/div/div/form/div[2]/textarea').send_keys(u'设备类型test')
		# 确定
		self.browser.find_element_by_xpath('//*[@id="new-save"]').click()
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/设备类型管理%s.jpg' % now)

	# @unittest.skip("直接跳过测试test_detectionBuild")
	def test5_detectionBuild(self):
		# *******************创建设备***********************
		# 资源管理
		# ********************巡检项管理新增******************
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[1]/div[2]/div/div[1]/i').click()
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
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/检测项管理%s.jpg' % now)

	# @unittest.skip("直接跳过测试test_equipmentBuild")
	def test6_equipmentBuild(self):
		# *******************新增配电室***********************
		# 资源管理
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[1]/div[2]/div/div[1]/i').click()
		sleep(1)
		self.browser.find_element_by_link_text('台账管理').click()
		# 新增配电室
		sleep(2)
		self.browser.find_element_by_id('newRoom').click()
		sleep(1)
		self.browser.find_element_by_id('roomName').send_keys(AddTest.room)
		self.browser.find_element_by_id('roomRemark').send_keys(u'配电室test')
		# 确定
		self.browser.find_element_by_id('newR-save').click()

		# *******************新增设备***********************
		sleep(2)
		self.browser.find_element_by_id('newEquipment').click()
		# 表单
		# 设备名称
		sleep(1)
		self.browser.find_element_by_id('equipmentName').send_keys(AddTest.transformer)
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
		self.browser.find_element_by_id('equipmentSn').send_keys(u'生产编号number1')
		# 出厂编号
		sleep(1)
		self.browser.find_element_by_id('equipmentFsn').send_keys(u'出厂编号number1')
		# 生产厂商
		sleep(1)
		self.browser.find_element_by_id('manufacturer').send_keys(u'生产厂家number1')
		# 供应厂商
		sleep(1)
		self.browser.find_element_by_id('supplier').send_keys(u'供应厂商number1')
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
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/台账管理%s.jpg' % now)

	# @unittest.skip("直接跳过测试test_planBuild")
	def test7_planBuild(self):
		# 计划管理
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[1]/div[7]/div/div[1]/i').click()
		sleep(1)
		# 新增
		sleep(2)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/plan-table/p/button').click()
		# 表单
		sleep(1)
		# 计划名称
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[1]/input').send_keys(AddTest.plan)
		# 周期类型
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[2]/select').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[2]/select/option[2]').click()
		# 开始时间
		# 时
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[3]/select[1]').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[3]/select[1]/option[10]').click()
		# 分
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[3]/select[2]').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[3]/select[2]/option[2]').click()
		# 秒
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[3]/select[3]').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[3]/select[3]/option[2]').click()
		# 结束时间
		# 时
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[4]/select[1]').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[4]/select[1]/option[19]').click()
		# 分
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[4]/select[2]').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[4]/select[2]/option[2]').click()
		# 秒
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[4]/select[3]').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[4]/select[3]/option[2]').click()

		# 选择班组
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[5]/div/div/div/button').click()
		sleep(1)
		self.browser.find_element_by_link_text('运行一班').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[5]/div/div/div/button').click()
		# 是否激活
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[6]/input').click()

		# 选择安全包
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[7]/select').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[7]/select/option[2]').click()

		# 计划描述
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[8]/textarea').send_keys(u'日计划测试test')

		# 选择设备
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[1]/ol/li[1]/div/input').click()
		self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[1]/ol/li[2]/div/input').click()

		# 选择模板
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[1]/ol/li[1]/div/span').click()
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[9]/div[2]/span/select').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[9]/div[2]/span/select/option[2]').click()
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[1]/ol/li[2]/div/span').click()
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[3]/div/div/div[9]/div[2]/span/select').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div/div/div[9]/div[2]/span/select/option[2]').click()

		# 提交
		self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()

		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/计划管理%s.jpg' % now)

	# @unittest.skip("直接跳过测试test_taskBuild")
	def task_taskBuild(self):
		# 任务管理
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[1]/div[8]/div/div[1]/i').click()
		sleep(1)
		# 新增
		sleep(2)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/p/button').click()
		# 表单
		sleep(1)
		# 任务名称
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div[2]/div/div[1]/input').send_keys(AddTest.task)
		# 执行班组
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div[2]/div/div[2]/div[1]/div/div/div/button').click()
		sleep(1)
		self.browser.find_element_by_link_text('运行一班').click()
		# 选择安全包
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div[2]/div/div[2]/div[2]/select').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div[2]/div/div[2]/div[2]/select/option[2]').click()
		# 开始时间
		self.browser.find_element_by_id('startDateTime').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div[2]/div/div[3]/div[1]/div/ul/div/table/tbody/tr[5]/td[4]').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div[2]/div/div[3]/div[1]/div/ul/div/table/tbody/tr/td/span[10]').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div[2]/div/div[3]/div[1]/div/ul/div/table/tbody/tr/td/span[1]').click()

		# 结束时间
		sleep(1)
		self.browser.find_element_by_id('endDateTime').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div[2]/div/div[3]/div[2]/div/ul/div/table/tbody/tr[5]/td[4]').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div[2]/div/div[3]/div[2]/div/ul/div/table/tbody/tr/td/span[19]').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div[2]/div/div[3]/div[2]/div/ul/div/table/tbody/tr/td/span[1]').click()
		# 选择设备
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[1]/ol/li[1]/div/input').click()
		self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[1]/ol/li[2]/div/input').click()
		# 选择模板
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[1]/ol/li[1]/div/span').click()
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div[2]/div/div[4]/div[2]/span/select').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div[2]/div/div[4]/div[2]/span/select/option[2]').click()
		# 提交
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[1]/ol/li[2]/div/span').click()
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div[2]/div/div[4]/div[2]/span/select').click()
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div/index-header/div[3]/div[2]/div/div[4]/div[2]/span/select/option[2]').click()

		# 提交
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()
		# 截图
		sleep(3)
		now = time.strftime('%y-%m-%d-%H:%M:%S')
		self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/任务管理%s.jpg' % now)


if __name__ == "__main__":
	unittest.main()
