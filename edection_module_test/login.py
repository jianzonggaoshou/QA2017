# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class Login(unittest.TestCase):
	def setUp(self):
		print "test start"

	def tearDown(self):
		print "test end"

	def login(self):
		browser = webdriver.Chrome()
		browser.maximize_window()

		browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
		browser.find_element_by_id("userId").send_keys("15609100803")
		browser.find_element_by_id("password").send_keys("123456")
		browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/button").click()

	if __name__ == '__main__':
		unittest.main()
