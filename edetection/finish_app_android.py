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

# 进入【检测任务】
sleep(3)
el = driver.find_element_by_id('com.sito.edetection:id/ll_check_project')
el.click()

# 长按项目
sleep(3)
driver.tap([(500, 300)], 2000)
# 确定是否删除
sleep(1)
el = driver.find_element_by_id('com.sito.edetection:id/md_buttonDefaultPositive')
el.click()

sleep(3)
driver.quit()




