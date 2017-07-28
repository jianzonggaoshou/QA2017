#coding=utf-8
from selenium import webdriver
from time import sleep

# browser = webdriver.Chrome()
browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
browser.maximize_window()

browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
browser.find_element_by_id("userId").send_keys("15609100803")
browser.find_element_by_id("password").send_keys("123456")
browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div[3]/button").click()

sleep(3)
browser.find_element_by_xpath('//*[@id="ext-gen29"]/user_build_csv').click()
sleep(1)

sleep(1)
browser.find_element_by_link_text('数据审核').click()
sleep(1)

sleep(1)
browser.switch_to.frame("mainFrame")
browser.switch_to.frame('/sito2000/workflow/task_data_check_list.jsp')

sleep(1)
browser.find_element_by_xpath('//*[@id="ext-gen17"]/div[1]/table/tbody/tr/td[6]/div/a').click()
sleep(1)

#
sleep(1)
browser.switch_to.parent_frame()
el = browser.find_element_by_xpath('//*[@id="ext-gen34"]/iframe')
browser.switch_to.frame(el)

sleep(1)
browser.find_element_by_xpath('//*[@id="ext-gen13"]').click()

sleep(3)
browser.quit()

