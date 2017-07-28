# coding=utf-8

from selenium import webdriver
from time import sleep
import csv

data = csv.reader(open('user.csv', 'r'))

for user in data:
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
    browser.find_element_by_id("userId").send_keys("admin")
    browser.find_element_by_id("password").send_keys("123456")
    browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/button").click()

    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen59"]/user_build_csv').click()
    sleep(1)
    browser.find_element_by_link_text("用户管理").click()
    sleep(1)

    browser.switch_to.frame("mainFrame")
    browser.switch_to.frame("/sito2000/admin/user_list1.jsp")

    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen52"]/span').click()
    sleep(1)

    # 回到最外层frame
    browser.switch_to.default_content()
    # 用户名
    browser.find_element_by_name('userId').send_keys(user[0])
    sleep(1)
    # 姓名
    browser.find_element_by_name('realName').send_keys(user[1].decode('gb2312'))
    # 密码
    browser.find_element_by_name('passWord').send_keys(user[2])
    # 确认密码
    browser.find_element_by_name('passWord2').send_keys(user[3])
    # 电话
    browser.find_element_by_name('phoneNumber').send_keys(user[4])
    # 邮箱
    browser.find_element_by_name('email').send_keys(user[5])
    # 备注
    browser.find_element_by_name('userMemo').send_keys(user[6].decode('gb2312'))

    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen95"]').click()
    sleep(1)
    browser.quit()
