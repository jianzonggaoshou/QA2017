#coding=utf-8

# 建站测试全流程

from selenium import webdriver
from time import sleep
import os

a = 191
b = a + 349
c = 0
# user_build_csv = a + 348

for i in range(191, 192):

    print a
    print b
    #************************* 项目建立***************************************************

    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
    browser.find_element_by_id("userId").clear()
    browser.find_element_by_id("userId").send_keys("admin")
    browser.find_element_by_id("password").clear()
    browser.find_element_by_id("password").send_keys("123456")
    browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/button").click()

    sleep(3)
    browser.find_element_by_link_text("创建工程").click()
    sleep(1)
    browser.switch_to.frame("mainFrame")
    browser.switch_to.frame("/sito2000/action/sd/wf/contractProject/add")
    browser.find_element_by_id("contractName").send_keys(u"自动化测试合同全流程%s" %i)
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
    browser.find_element_by_xpath('//*[@name="companyId"]/option[3]').click()

    sleep(1)

    c = c + 1

    browser.find_element_by_xpath('//*[@id="substation"]/div[%s]/input' %c).click()
    browser.find_element_by_link_text("下一步").click()
    sleep(1)
    browser.switch_to.alert.accept()
    sleep(3)

    browser.quit()

    # ************************* 变电站建立***************************************************

    sleep(2)
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
    browser.find_element_by_id("userId").clear()
    browser.find_element_by_id("userId").send_keys("admin")
    browser.find_element_by_id("password").clear()
    browser.find_element_by_id("password").send_keys("123456")
    browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/button").click()

    sleep(3)
    browser.find_element_by_link_text("工程管理").click()
    sleep(1)
    browser.switch_to.frame("mainFrame")
    browser.switch_to.frame("/sito2000/action/sd/wf/contractProject/list")
    browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/span[1]/img').click()
    sleep(1)

    browser.switch_to.parent_frame()
    browser.switch_to.frame("/sito2000/action/sd/wf/contractProject/getContract?contractId=%s" %a)
    browser.find_element_by_link_text("站点信息").click()
    sleep(3)

    browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[1]/div/span[1]/img').click()
    sleep(3)

    browser.switch_to.parent_frame()
    browser.switch_to.frame('/sito2000//workflow/project_add.jsp?contractId={}&projectId={}&projectState=1' .format(a, b))
    browser.find_element_by_id('manageruser').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen121"]/div[1]/div').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="deviceuser"]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen124"]/div[2]/div').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="safesuser"]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen146"]/div[3]/img').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen63"]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="deviceType"]').click()
    sleep(1)
    # 红外精确测温
    browser.find_element_by_xpath('//*[@id="ext-gen240"]/div[2]/img').click()

    sleep(1)
    browser.find_element_by_xpath('//*[@id="deviceType"]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen192"]').click()

    # 选择台账1
    sleep(3)
    browser.find_element_by_link_text('红外精确测温').click()

    # 设备列表
    # sleep(1)
    #browser.find_element_by_xpath('//*[@id="ext-gen294"]/div/table/thead/tr/td[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen295"]/div[1]/table/tbody/tr/td[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen295"]/div[2]/table/tbody/tr/td[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen295"]/div[3]/table/tbody/tr/td[2]/div/div').click()

    # 检测仪器
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen316"]/div[1]/table/tbody/tr/td[2]/div').click()

    # 人员列表
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen336"]/div/table/thead/tr/td[2]/div').click()


    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen65"]').click()
    sleep(10)

    print '项目'
    print a

    # 项目循环，为下次
    a = a + 1
    b = b + 1
    sleep(1)
    browser.quit()