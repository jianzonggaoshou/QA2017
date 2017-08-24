# coding=utf-8
from selenium import webdriver
from time import sleep
import unittest


class BaiduAppium2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    def tearDown(self):
        sleep(5)
        self.driver.quit()

    def test_appium(self):
        self.driver.find_element_by_id("kw").send_keys("appium")
        self.driver.find_element_by_id("su").click()