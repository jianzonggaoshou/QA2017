#coding=utf-8

from selenium import webdriver
from time import sleep

a = 258
b = 229

for i in range(3, 50):

    #browser = webdriver.Chrome()
    browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
    browser.maximize_window()

    browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
    browser.find_element_by_id("userId").clear()
    browser.find_element_by_id("userId").send_keys("admin")
    browser.find_element_by_id("password").clear()
    browser.find_element_by_id("password").send_keys("123456")
    browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/button").click()

    sleep(3)
    browser.find_element_by_xpath('//*[@id="ext-gen41"]/user_build_csv').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="4"]/li/a').click()

    sleep(1)
    browser.switch_to.frame("mainFrame")
    browser.switch_to.frame("/sito2000/admin/dept_list.jsp ")

    sleep(1)
    browser.find_element_by_link_text('国网新疆电力公司').click()
    sleep(1)
    browser.find_element_by_link_text('分公司').click()
    sleep(1)
    browser.find_element_by_link_text('乌鲁木齐电业局').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen97"]/span').click()

    sleep(1)
    browser.find_element_by_id('substationName').send_keys(u'10kV测试变电站%s' %i)
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-comp-1078"]').click()
    sleep(1)

    a = a + 1
    browser.find_element_by_xpath('//*[@id="ext-gen%s"]/div[3]' %a).click()
    sleep(1)
    b = b + 1
    browser.find_element_by_xpath('//*[@id="ext-gen%s"]' %b).click()
    sleep(1)


    browser.quit()