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

# 进入工程
sleep(3)
el = driver.find_elements_by_id('text_pro_name')[0]
el.click()
sleep(1)

# 红外精确测温
sleep(1)
driver.find_elements_by_id('text_name')[1].click()

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
sleep(1)
el = driver.find_elements_by_id('com.android.documentsui:id/icon_mime')[2]
el.click()

# 返回
sleep(1)
el = driver.find_element_by_class_name('android.widget.ImageButton')
el.click()

sleep(3)
driver.quit()
