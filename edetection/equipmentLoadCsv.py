#coding=utf-8

from selenium import webdriver
from time import sleep

for i in range(1, 50):


    browser = webdriver.Chrome()
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
    browser.find_element_by_link_text('10kV测试变电站%s' %i).click()
    sleep(1)

    # 按模板新增
    browser.find_element_by_xpath('//*[@id="ext-gen149"]/span').click()

    sleep(1)
    browser.find_element_by_name('file').send_keys('D:\\EquipTemplate.xls')
    sleep(1)

    browser.find_element_by_xpath('//*[@id="ext-comp-1082"]/tbody/tr[2]/td[2]').click()
    sleep(3)

    browser.quit()