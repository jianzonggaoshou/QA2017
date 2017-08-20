# coding=utf-8
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = 'com.android.calculator2.Calculator'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("com.android.calculator2:id/digit_1").click()

driver.find_element_by_id("com.android.calculator2:id/digit_5").click()

driver.find_element_by_id("com.android.calculator2:id/digit_9").click()

driver.find_element_by_id("com.android.calculator2:id/del").click()

driver.find_element_by_id("com.android.calculator2:id/digit_9").click()

driver.find_element_by_id("com.android.calculator2:id/digit_5").click()

driver.find_element_by_id("com.android.calculator2:id/op_add").click()

driver.find_element_by_id("com.android.calculator2:id/digit_6").click()

driver.find_element_by_id("com.android.calculator2:id/eq").click()

driver.quit()
