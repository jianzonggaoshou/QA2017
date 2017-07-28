# -*- coding: UTF-8 -*-

from time import sleep
from appium import webdriver
import random
import os

desired_caps = {}

desired_caps['automationName'] = 'XCUITest'

desired_caps['platformName'] = 'iOS'

desired_caps['platformVersion'] = '10.3'

desired_caps['bundleId'] = 'com.sitop.edetection'

desired_caps['app'] = os.path.abspath('/Users/xuzhen/edetection/edetection2.0.1.app')

desired_caps['noReset'] = True

desired_caps['unicodeKeyboard'] = True

desired_caps['resetKeyboard'] = True

desired_caps['deviceName'] = 'iphone Simulator'

# desired_caps['deviceName'] = 'iPhone 6'

# desired_caps['udid'] = '64a226e1f1e8b3548688ebeee60fc51730ad4d54'

dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

sleep(5)

# 首页-检测任务
el = dr.find_element_by_name('检测任务')
el.click()

# # 开始按钮
# sleep(1)
# el = dr.find_element_by_id('nav start normal')
# el.click()
#
# # 开始项目
# sleep(3)
# el = dr.find_elements_by_id('开始')[0]
# el.click()
# sleep(3)
# el = dr.find_element_by_id('确定')
# el.click()
# sleep(3)

# 第一个工程
sleep(1)
el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[1]')
el.click()

sleep(3)
# 测试项-红外精确测温
el = dr.find_element_by_id('1.红外精确测温')
el.click()


# # 点击开始检测
# sleep(3)
# el = dr.find_element_by_id('点击开始检测')
# el.click()
# sleep(1)
# el = dr.find_element_by_id('确定')
# el.click()

# 图片编号原始值
a = 1

for i in range(2, 9, 3):

	sleep(3)
	# 间隔检测
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[3]//*[%s]' % i)

	el.click()

	sleep(1)

	# 添加数据
	# 本体
	el = dr.find_elements_by_id('editor icon normal')[0]
	el.click()
	sleep(3)

	# 红外图片编号
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[1]//*[3]')
	el.set_value(str(a))

	# 正常图片编号
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[1]//*[4]')
	el.set_value(str(a + 1))

	# # 最高温度
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[2]//*[2]')

	sleep(3)
	dr.tap([(1151, 513)])
	el.click()
	#el.set_value(str(random.randrange(28, 38)))
	sleep(3)
	# 保存
	el = dr.find_element_by_id('保存')
	el.click()

	# noinspection PyBroadException
	try:
		sleep(3)
		el = dr.find_element_by_id('确定')
		el.click()

	except:
		print '温度异常'

	sleep(3)
	# 冷却器
	el = dr.find_elements_by_id('editor icon normal')[1]
	el.click()
	sleep(3)

	# 红外图片编号
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[1]//*[3]')
	el.set_value(str(a + 2))

	# 正常图片编号
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[1]//*[4]')
	el.set_value(str(a + 3))

	# 最高温度
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[2]//*[2]')
	el.set_value(str(random.randrange(28, 38)))

	sleep(3)
	# 保存
	el = dr.find_element_by_id('保存')
	el.click()

	# noinspection PyBroadException
	try:
		sleep(3)
		el = dr.find_element_by_id('确定')
		el.click()

	except:
		print '温度异常'

	# 返回上一界面
	sleep(3)
	el = dr.find_element_by_id('back icon normal')
	el.click()

	# 自增+4
	sleep(3)
	a = a + 4
	sleep(1)

sleep(3)
# 点击完成检测
el = dr.find_element_by_id('点击完成检测')
el.click()
sleep(1)
el = dr.find_element_by_id('确定')
el.click()

# # 现场环境
# sleep(3)
# el = dr.tap([(301, 205)], 500)
# el.click()
# sleep(1)
# # 温度
# el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[3]//*[2]')
# el.set_value(str(random.randrange(10, 40)))
# # 湿度
# el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[4]//*[2]')
# el.set_value(str(random.randrange(10, 40)))
# # 保存
# el = dr.find_element_by_id('保存')
# el.click()

sleep(3)
# 上传数据
el = dr.find_element_by_id('上传')
el.click()

# 完成
sleep(1)
el = dr.find_element_by_id('完成')
el.click()

# 返回
sleep(1)
el = dr.find_element_by_id('back icon normal')
el.click()

# *******************************************************************************************

sleep(3)
# 测试项-SF6气体成分检测
el = dr.find_element_by_id('2.SF6气体成分检测')
el.click()

sleep(3)
# 点击开始检测
el = dr.find_element_by_id('点击开始检测')
el.click()
sleep(1)
el = dr.find_element_by_id('确定')
el.click()

for i in range(2, 9, 3):

	print i
	sleep(3)
	# 间隔检测
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[3]//*[%s]' % i)
	el.click()

	# 编辑数据
	sleep(1)
	el = dr.find_element_by_id('editor icon normal')
	el.click()

	# SO2
	sleep(1)
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[1]//*[3]')
	el.set_value(str(random.uniform(0, 2)))
	# H2S
	sleep(1)
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[1]//*[4]')
	el.set_value(str(random.uniform(0, 2)))
	# CO
	sleep(1)
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[2]//*[3]')
	el.set_value(str(random.uniform(0, 2)))
	# HF
	sleep(1)
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[2]//*[4]')
	el.set_value(str(random.uniform(0, 2)))
	# 露点
	sleep(1)
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[3]//*[3]')
	el.set_value(str(random.uniform(0, 2)))
	# 纯度
	sleep(1)
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[3]//*[4]')
	el.set_value(str(random.uniform(95, 99)))
	# 湿度
	sleep(1)
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[4]//*[3]')
	el.set_value(str(random.uniform(0, 2)))
	# CF4
	sleep(1)
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[4]//*[4]')
	el.set_value(str(random.uniform(0, 2)))
	# 保存
	sleep(1)
	el = dr.find_element_by_id('保存')
	el.click()

	# noinspection PyBroadException
	try:
		sleep(3)
		el = dr.find_element_by_id('确定')
		el.click()

	except:
		print 'SF6数据异常'

	# 返回
	sleep(1)
	el = dr.find_element_by_id('back icon normal')
	el.click()

sleep(3)
# 点击完成检测
el = dr.find_element_by_id('点击完成检测')
el.click()
sleep(1)
el = dr.find_element_by_id('确定')
el.click()

# # 现场环境
# sleep(1)
# el = dr.find_element_by_id('环境')
# el.click()
# sleep(1)
# # 温度
# el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[3]//*[2]')
# el.set_value(str(random.randrange(10, 40)))
# # 湿度
# el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[4]//*[2]')
# el.set_value(str(random.randrange(10, 40)))
# # 保存
# el = dr.find_element_by_id('保存')
# el.click()

sleep(3)
# 上传数据
el = dr.find_element_by_id('上传')
el.click()

# 完成
sleep(1)
el = dr.find_element_by_id('完成')
el.click()

# 返回
sleep(1)
el = dr.find_element_by_id('back icon normal')
el.click()

sleep(8)
dr.quit()
