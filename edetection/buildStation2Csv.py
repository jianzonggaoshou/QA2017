#coding=utf-8
from selenium import webdriver
from time import sleep
#import csv

#data = csv.reader(open('stationProject.csv', 'r'))
b = 361
a = 8

for i in range(75, 60, -1):

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
    #browser.switch_to.frame("/SITO2000_JC/action/sd/wf/contractProject/list")
    browser.switch_to.frame("/sito2000/action/sd/wf/contractProject/list")

    # js = "window.scrollTo(100,450)"
    # browser.execute_script(js)
    # sleep(6)

    sleep(1)
    a = a + 1
    s = browser.find_element_by_xpath('/html/body/div[2]/div[%s]/div[1]/div/span[1]/img' %a)

    sleep(3)

    s.click()
    sleep(3)
    browser.switch_to.parent_frame()
    browser.switch_to.frame("/sito2000/action/sd/wf/contractProject/getContract?contractId=%s" %i)
    browser.find_element_by_link_text("站点信息").click()
    sleep(3)

    browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/span[1]/img').click()
    sleep(3)
    browser.switch_to.parent_frame()

    b = b-2

    browser.switch_to.frame("/sito2000//workflow/project_add.jsp?contractId={}&projectId={}&projectState=1".format(i, b))
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
    # 铁芯接地电流检测
    browser.find_element_by_xpath('//*[@id="ext-gen240"]/div[4]/img').click()
    # SF6气体成分检测
    browser.find_element_by_xpath('//*[@id="ext-gen240"]/div[5]/img').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="deviceType"]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen192"]').click()

    # 选择台账1
    sleep(3)
    browser.find_element_by_link_text('红外精确测温').click()

    # 设备列表
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen297"]/div[2]/table/tbody/tr/td[2]/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen297"]/div[3]/table/tbody/tr/td[2]/div').click()

    # 检测仪器
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen318"]/div[1]/table/tbody/tr/td[2]/div').click()

    # 人员列表
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen338"]/div/table/thead/tr/td[2]/div').click()

    # 选择台账2
    browser.find_element_by_partial_link_text('铁芯').click()

    # 设备列表
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen383"]/div[2]/table/tbody/tr/td[2]/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen383"]/div[3]/table/tbody/tr/td[2]/div').click()

    # 检测仪器
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen404"]/div/table/tbody/tr/td[2]/div').click()

    # 人员列表
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen424"]/div/table/thead/tr/td[2]/div').click()

    # 选择台账3
    browser.find_element_by_partial_link_text('SF6').click()

    # 设备列表
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen469"]/div[4]/table/tbody/tr/td[2]/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen469"]/div[5]/table/tbody/tr/td[2]/div').click()
    # 检测仪器
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen490"]/div[1]/table/tbody/tr/td[2]/div').click()

    # 人员列表
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen510"]/div/table/thead/tr/td[2]/div').click()


    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen65"]').click()
    sleep(10)
    browser.quit()