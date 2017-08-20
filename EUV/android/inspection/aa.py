# -*- coding: utf-8 -*-

from appium import webdriver
from time import sleep
import unittest


class Login(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.2'
        # desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Android Emulator'
        # desired_caps['udid'] = 'UW9555Q899999999'
        desired_caps['appPackage'] = 'com.sito.evpro.inspection'
        desired_caps['appActivity'] = '.view.login.LoginActivity'
        desired_caps['noReset'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        sleep(10)
        self.driver.quit()

    # def test_login(self):
