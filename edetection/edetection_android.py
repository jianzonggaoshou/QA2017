# -*- coding: utf-8 -*-

from appium import webdriver
from time import sleep
import random

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0.2'
# desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'Android Emulator'
# desired_caps['udid'] = 'UW9555Q899999999'
desired_caps['appPackage'] = 'com.sito.edetection'
desired_caps['appActivity'] = '.view.login.LoginActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# sleep(5)
# driver.find_element_by_id('edit_username').set_value('caishoujun')
# driver.find_element_by_id('edit_password').set_value('123456')
# driver.find_element_by_id('btn_signin').click()

# 进入【检测任务】
sleep(3)
el = driver.find_element_by_id('com.sito.edetection:id/ll_check_project')
el.click()

# 开始项目
sleep(5)
driver.find_element_by_id('menu').click()
sleep(1)
driver.find_element_by_id('downloadTaskIv').click()
sleep(1)
driver.find_element_by_id('md_buttonDefaultPositive').click()
sleep(1)

# 进入工程
sleep(3)
el = driver.find_elements_by_id('text_pro_name')[0]
el.click()
sleep(1)

# 上传工程现场照片
# 项目照片
sleep(1)
el = driver.find_element_by_id('com.sito.edetection:id/tv_take_photo')
el.click()

# 选择
sleep(1)
el = driver.find_element_by_id('com.sito.edetection:id/imageIv')
el.click()

# 相册
sleep(1)
el = driver.find_elements_by_id('com.sito.edetection:id/md_title')[1]
el.click()

# 进入相册程序
sleep(1)
driver.wait_activity('com.android.documentsui', 2)

# 选择图片1
driver.implicitly_wait(10)
sleep(6)
el = driver.find_elements_by_id('com.android.documentsui:id/icon_thumb')[0]
el.click()

# 返回
sleep(1)
el = driver.find_element_by_class_name('android.widget.ImageButton')
el.click()

# 红外精确测温
sleep(1)
driver.find_elements_by_id('text_name')[0].click()

# 检测记时开始按钮
sleep(1)
driver.find_element_by_id('off_report_tv').click()
sleep(1)
driver.find_element_by_id('md_buttonDefaultPositive').click()
sleep(1)

# 图片编号原始值
ff = 1

for i in range(1, 6, 2):
	# ******************************************************************************************
	# 1* 设备数据输入
	sleep(1)
	el = driver.find_elements_by_id('layout_item')[i]
	el.click()

	# 第一条数据-本体
	driver.implicitly_wait(10)
	el = driver.find_elements_by_id('editBtn')[0]
	el.click()

	# 红外图片编号
	sleep(1)
	el = driver.find_elements_by_id('edit')[1]
	el.set_value(ff)

	# 正常图片编号
	sleep(1)
	el = driver.find_elements_by_id('edit')[2]
	el.set_value(ff + 1)

	# 最高温度
	sleep(1)
	el = driver.find_elements_by_id('edit')[3]
	el.set_value(random.randrange(10, 29))

	sleep(1)
	driver.find_element_by_id('saveTv').click()
	sleep(1)

	# (x,y, x,y, time)
	driver.swipe(500, 1500, 500, 500, 1000)
	sleep(3)

	# 第二条数据-冷却器
	sleep(1)
	el = driver.find_elements_by_id('editBtn')[1]
	el.click()

	# 红外图片编号
	sleep(1)
	el = driver.find_elements_by_id('edit')[1]
	el.set_value(ff + 2)

	# 正常图片编号
	sleep(1)
	el = driver.find_elements_by_id('edit')[2]
	el.set_value(ff + 3)

	# 最高温度
	sleep(1)
	el = driver.find_elements_by_id('edit')[3]
	el.set_value(random.randrange(30, 60))

	sleep(1)
	driver.find_element_by_id('saveTv').click()
	sleep(1)

	# 返回按键
	driver.find_element_by_class_name('android.widget.ImageButton').click()
	sleep(1)

	# 图片编号自增
	ff = ff + 4

# 检测记时结束按钮
sleep(1)
driver.find_element_by_id('off_report_tv').click()
sleep(1)
driver.find_element_by_id('md_buttonDefaultPositive').click()
sleep(1)

# 添加环境数据
sleep(1)
driver.find_element_by_id('com.sito.edetection:id/envTv').click()
# 湿度
sleep(1)
el = driver.find_elements_by_id('com.sito.edetection:id/enter')[0]
el.set_value(random.randrange(20, 30))
# 温度
sleep(1)
el = driver.find_elements_by_id('com.sito.edetection:id/enter')[1]
el.set_value(random.randrange(20, 30))
# 保存
sleep(1)
el = driver.find_element_by_id('com.sito.edetection:id/menu')
el.click()

# 上传红外现场照片
# 项目照片
sleep(1)
el = driver.find_element_by_id('com.sito.edetection:id/tv_take_photo')
el.click()

# 选择
sleep(1)
el = driver.find_element_by_id('com.sito.edetection:id/imageIv')
el.click()

# 相册
sleep(1)
el = driver.find_elements_by_id('com.sito.edetection:id/md_title')[1]
el.click()

# 进入相册程序
sleep(1)
driver.wait_activity('com.android.documentsui', 2)

# 选择图片2
sleep(1)
el = driver.find_elements_by_id('com.android.documentsui:id/icon_thumb')[1]
el.click()

# 返回
sleep(1)
el = driver.find_element_by_class_name('android.widget.ImageButton')
el.click()


# 上传数据
sleep(1)
driver.find_element_by_id('menu').click()
sleep(1)
driver.find_element_by_id('md_buttonDefaultPositive').click()
sleep(5)

# 完成上传
sleep(3)
driver.find_element_by_id('btn_finish').click()

# 返回按键
driver.find_element_by_class_name('android.widget.ImageButton').click()

# ******************************************************************

# SF6气体成分检测
sleep(1)
driver.find_elements_by_id('text_name')[1].click()

# 检测记时开始按钮
sleep(1)
driver.find_element_by_id('off_report_tv').click()
sleep(1)
driver.find_element_by_id('md_buttonDefaultPositive').click()
sleep(1)

for i in range(1, 6, 2):

	# 1#电抗器
	sleep(1)
	el = driver.find_elements_by_id('com.sito.edetection:id/layout_item')[i]
	el.click()

	# 数据录入
	driver.implicitly_wait(10)
	el = driver.find_elements_by_id('editBtn')[0]
	el.click()

	# SO2
	sleep(1)
	el = driver.find_elements_by_id('com.sito.edetection:id/edit')[1]
	el.set_value(random.uniform(0, 2))

	# H2S
	sleep(1)
	el = driver.find_elements_by_id('com.sito.edetection:id/edit')[2]
	el.set_value(random.uniform(0, 2))

	# CO
	sleep(1)
	el = driver.find_elements_by_id('com.sito.edetection:id/edit')[3]
	el.set_value(random.uniform(0, 2))

	# 纯度
	sleep(1)
	el = driver.find_elements_by_id('com.sito.edetection:id/edit')[4]
	el.set_value(random.randrange(95, 99))

	# 湿度
	sleep(1)
	el = driver.find_elements_by_id('com.sito.edetection:id/edit')[5]
	el.set_value(random.uniform(0, 2))

	# HF
	sleep(1)
	el = driver.find_elements_by_id('com.sito.edetection:id/edit')[6]
	el.set_value(random.uniform(0, 2))

	# 露点
	sleep(1)
	el = driver.find_elements_by_id('com.sito.edetection:id/edit')[7]
	el.set_value(random.uniform(0, 2))

	# CF4
	sleep(1)
	el = driver.find_elements_by_id('com.sito.edetection:id/edit')[8]
	el.set_value(random.uniform(0, 2))

	# 保存
	sleep(1)
	el = driver.find_element_by_id('com.sito.edetection:id/saveTv')
	el.click()

	# 返回按键
	driver.find_element_by_class_name('android.widget.ImageButton').click()
	sleep(1)

# 检测记时结束按钮
sleep(1)
driver.find_element_by_id('off_report_tv').click()
sleep(1)
driver.find_element_by_id('md_buttonDefaultPositive').click()
sleep(1)

# 添加环境数据
sleep(1)
driver.find_element_by_id('com.sito.edetection:id/envTv').click()
# 湿度
sleep(1)
el = driver.find_elements_by_id('com.sito.edetection:id/enter')[0]
el.set_value(random.randrange(20, 30))
# 温度
sleep(1)
el = driver.find_elements_by_id('com.sito.edetection:id/enter')[1]
el.set_value(random.randrange(20, 30))
# 保存
sleep(1)
el = driver.find_element_by_id('com.sito.edetection:id/menu')
el.click()

# 上传SF6现场图片
# 项目照片
sleep(1)
el = driver.find_element_by_id('com.sito.edetection:id/tv_take_photo')
el.click()

# 选择
sleep(1)
el = driver.find_element_by_id('com.sito.edetection:id/imageIv')
el.click()

# 相册
sleep(1)
el = driver.find_elements_by_id('com.sito.edetection:id/md_title')[1]
el.click()

# 进入相册程序
sleep(1)
driver.wait_activity('com.android.documentsui', 2)

# 选择图片1
driver.implicitly_wait(10)
sleep(6)
el = driver.find_elements_by_id('com.android.documentsui:id/icon_thumb')[0]
el.click()

# 返回
sleep(1)
el = driver.find_element_by_class_name('android.widget.ImageButton')
el.click()

# 上传数据
sleep(1)
driver.find_element_by_id('menu').click()
sleep(1)
driver.find_element_by_id('md_buttonDefaultPositive').click()
sleep(5)

# 完成上传
sleep(3)
driver.find_element_by_id('btn_finish').click()

# 返回按键
driver.find_element_by_class_name('android.widget.ImageButton').click()

sleep(3)
driver.quit()
