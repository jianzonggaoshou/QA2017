# coding=utf-8
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.oneplus.calculator'
desired_caps['appActivity'] = '.Calculator'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("com.oneplus.calculator:id/digit_1").click()

driver.find_element_by_id("com.oneplus.calculator:id/digit_5").click()

driver.find_element_by_id("com.oneplus.calculator:id/digit_9").click()

driver.find_element_by_id("com.oneplus.calculator:id/op_sub").click()

driver.find_element_by_id("com.oneplus.calculator:id/digit_9").click()

driver.find_element_by_id("com.oneplus.calculator:id/digit_5").click()

driver.find_element_by_id("com.oneplus.calculator:id/op_add").click()

driver.find_element_by_id("com.oneplus.calculator:id/digit_6").click()

driver.find_element_by_id("com.oneplus.calculator:id/eq").click()

driver.quit()
