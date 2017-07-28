# coding=utf-8

from selenium import webdriver
from time import sleep

# ************************* 变电站建立***************************************************
# 单页变电站数目
a = 1

for i in range(1, 6):

	sleep(2)
	# browser = webdriver.Chrome()
	browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
	browser.maximize_window()

	browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
	# browser.get("http://192.168.8.66:8080/sito2000/login.jsp")
	browser.find_element_by_id("userId").clear()
	browser.find_element_by_id("userId").send_keys("xuzhen0913")
	browser.find_element_by_id("password").clear()
	browser.find_element_by_id("password").send_keys("123456")
	browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div[3]/button").click()

	sleep(3)
	browser.find_element_by_link_text("工程管理").click()
	sleep(1)
	browser.switch_to.frame("mainFrame")
	browser.switch_to.frame("/sito2000/action/sd/wf/contractProject/list")
	browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/span[1]/img').click()
	sleep(1)

	sleep(3)
	browser.switch_to.parent_frame()
	el = browser.find_element_by_xpath('//*[@id="ext-gen34"]/iframe')
	browser.switch_to.frame(el)

	# browser.switch_to.frame("/sito2000/action/sd/wf/contractProject/getContract?contractId=%s" %a)
	browser.find_element_by_link_text("站点信息").click()
	sleep(3)

	print a
	# 选择站点
	sleep(3)
	browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[%s]/div[1]/div/span[1]/img' % a).click()
	sleep(3)

	browser.switch_to.parent_frame()
	el = browser.find_element_by_xpath('//*[@id="ext-gen39"]/iframe')
	browser.switch_to.frame(el)
	# browser.switch_to.frame('/sito2000//workflow/project_add.jsp?contractId={}&projectId={}&projectState=1' .format(a, user_build_csv))
	browser.find_element_by_id('manageruser').click()
	sleep(1)
	browser.find_element_by_xpath('//*[@id="ext-gen121"]/div[1]/div').click()
	sleep(1)
	browser.find_element_by_xpath('//*[@id="deviceuser"]').click()
	sleep(3)
	browser.find_element_by_xpath('//*[@id="ext-gen124"]/div[2]/div').click()
	sleep(1)
	browser.find_element_by_xpath('//*[@id="safesuser"]').click()
	sleep(1)
	browser.find_element_by_xpath('//*[@id="ext-gen132"]/div[3]/div').click()
	sleep(1)
	browser.find_element_by_xpath('//*[@id="ext-gen63"]').click()
	sleep(1)
	browser.find_element_by_xpath('//*[@id="deviceType"]').click()
	sleep(1)
	# 红外精确测温
	browser.find_element_by_xpath('//*[@id="ext-gen184"]/div[2]/div').click()
	# SF6气体成分检测
	browser.find_element_by_xpath('//*[@id="ext-gen184"]/div[5]/div').click()

	sleep(1)
	browser.find_element_by_xpath('//*[@id="deviceType"]').click()
	sleep(1)
	browser.find_element_by_xpath('//*[@id="ext-gen157"]').click()

	# 选择台账1
	sleep(3)
	browser.find_element_by_link_text('红外精确测温').click()

	# 设备列表
	# sleep(1)
	# browser.find_element_by_xpath('//*[@id="ext-gen294"]/div/table/thead/tr/td[2]/div/div').click()
	browser.find_element_by_xpath('//*[@id="ext-gen240"]/div[1]/table/tbody/tr/td[2]/div/div').click()
	browser.find_element_by_xpath('//*[@id="ext-gen240"]/div[2]/table/tbody/tr/td[2]/div/div').click()
	browser.find_element_by_xpath('//*[@id="ext-gen240"]/div[3]/table/tbody/tr/td[2]/div/div').click()

	# 检测仪器
	sleep(1)
	browser.find_element_by_xpath('//*[@id="ext-gen261"]/div[1]/table/tbody/tr/td[2]/div').click()

	# 人员列表
	sleep(1)
	browser.find_element_by_xpath('//*[@id="ext-gen281"]/div/table/thead/tr/td[2]/div').click()

	# ****************************************************************************
	# 选择台账2
	sleep(3)
	browser.find_element_by_link_text('SF6气体成分检测').click()

	# 设备列表
	# sleep(1)
	# browser.find_element_by_xpath('//*[@id="ext-gen294"]/div/table/thead/tr/td[2]/div/div').click()
	browser.find_element_by_xpath('//*[@id="ext-gen326"]/div[1]/table/tbody/tr/td[2]/div/div').click()
	browser.find_element_by_xpath('//*[@id="ext-gen326"]/div[2]/table/tbody/tr/td[2]/div/div').click()
	browser.find_element_by_xpath('//*[@id="ext-gen326"]/div[3]/table/tbody/tr/td[2]/div/div').click()

	# 检测仪器
	sleep(1)
	browser.find_element_by_xpath('//*[@id="ext-gen347"]/div[1]/table/tbody/tr/td[2]/div').click()

	# 人员列表
	sleep(1)
	browser.find_element_by_xpath('//*[@id="ext-gen367"]/div/table/thead/tr/td[2]/div').click()

	# 保存
	sleep(1)
	browser.find_element_by_xpath('//*[@id="ext-gen65"]').click()
	sleep(10)

	a = a + 1

	print 'test项目test'

	sleep(1)
	browser.quit()


