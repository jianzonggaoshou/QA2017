# -*- coding: utf-8 -*-

from time import sleep
from appium import webdriver
import os

desired_caps = {}

desired_caps['automationName'] = 'XCUITest'

desired_caps['platformName'] = 'iOS'

desired_caps['platformVersion'] = '10.3'

desired_caps['bundleId'] = 'com.sitop.edetection'

# desired_caps['app'] = os.path.abspath('/Users/xuzhen/edetection1.0.3.app')

desired_caps['noReset'] = True

desired_caps['deviceName'] = 'iphone Simulator'

# desired_caps['deviceName'] = 'iPhone 6'

# desired_caps['udid'] = '64a226e1f1e8b3548688ebeee60fc51730ad4d54'

dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

sleep(3)

# 第一个工程
sleep(1)
el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[1]')
el.click()

sleep(3)
# 项目拍照

