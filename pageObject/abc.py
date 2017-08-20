# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# test821
class Page(object):

	#  基础类，用于页面对象的继承

	login_url = 'http://192.168.8.88:8080/sito2000/login.jsp'

	def __init__(self, selenium_driver, base_url=login_url):
		self.base_url = base_url
		self.driver = selenium_driver
		self.timeout = 30

	def on_page(self):
		return self.driver.current_url == (self.base_url + self.url)

	def _open(self, url):
		url = self.base_url + url
		self.driver.get(url)
		assert self.on_page(), 'Did not land on %s' % url

	def open(self):
		self._open(self.url)

	def find_element(self, *loc):
		return self.driver.find_element(*loc)


class LoginPage(Page):

	# 智能带电检测登录页面模型
	url = '/'

	# 定位器
	username_loc = (By.ID, "userId")
	password_loc = (By.ID, "password")
	submit_loc = (By.PARTIAL_LINK_TEXT, "登录")

	# Action
	def type_username(self, username):
		self.find_element(*self.username_loc).send_keys(username)

	def type_password(self, password):
		self.find_element(*self.password_loc).send_keys(password)

	def submit(self):
		self.find_element(*self.submit_loc).click()


def test_user_login(driver, username, password):
	# 测试获取的用户名/密码是否可以登录
	login_page = LoginPage(driver)
	login_page.open()
	login_page.type_username(username)
	login_page.type_password(password)
	login_page.submit()


def main():
	try:
		driver = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
		username = '15609100803'
		password = '123456'
		test_user_login(driver, username, password)
	finally:
		# 关闭浏览器窗口
		driver.close()

print 'hello world821'

if __name__ == '__main__':
	main()
