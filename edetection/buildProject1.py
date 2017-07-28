#coding=utf-8
from selenium import webdriver
from time import sleep
import time

#browser = webdriver.Chrome()
browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
browser.maximize_window()

# browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
browser.get("http://192.168.8.66:8080/sito2000/login.jsp")
browser.find_element_by_id("userId").send_keys("15609100803")
browser.find_element_by_id("password").send_keys("123456")
browser.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[3]/button').click()

sleep(3)
browser.find_element_by_link_text("创建工程").click()
sleep(1)
browser.switch_to.frame("mainFrame")
browser.switch_to.frame("/sito2000/action/sd/wf/contractProject/add")

# 获取时间字符串
timeFF = time.strftime("%Y_%m_%d %H:%M:%S")
browser.find_element_by_id("contractName").send_keys(u"合同项目测试%s" % timeFF)
browser.find_element_by_id("contractNoA").send_keys(u"CQ100000001")
browser.find_element_by_id("contractNoB").send_keys(u"CQ100000002")
browser.find_element_by_id("signedTime").click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[2]/div[1]/table/tbody/tr[5]/td[2]').click()

sleep(1)
browser.find_element_by_xpath('//*[@id="enterpriseId"]/option[7]').click()
browser.find_element_by_id("contacts").send_keys(u"许臻")
browser.find_element_by_id("contactMobile").send_keys(u"15609100803")
browser.find_element_by_id("contactEamil").send_keys(u"xuzhen@si-top.com")
browser.find_element_by_name("companyId").click()
sleep(1)
browser.find_element_by_xpath('//*[@name="companyId"]/option[12]').click()
browser.find_element_by_xpath('//*[@id="substation"]/div[1]/input').click()
browser.find_element_by_xpath('//*[@id="substation"]/div[2]/input').click()
browser.find_element_by_xpath('//*[@id="substation"]/div[3]/input').click()
browser.find_element_by_xpath('//*[@id="substation"]/div[4]/input').click()
browser.find_element_by_xpath('//*[@id="substation"]/div[5]/input').click()
browser.find_element_by_link_text("下一步").click()
sleep(3)
browser.switch_to.alert.accept()
sleep(10)
browser.quit()

