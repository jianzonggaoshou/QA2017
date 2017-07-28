# coding=utf-8

# 建站测试全流程

from selenium import webdriver
from time import sleep

# 检测站自增
c = 0

for i in range(1, 50):

    # ************************* 项目建立***************************************************

    #browser = webdriver.Chrome()
    browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
    browser.maximize_window()

    browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
    browser.find_element_by_id("userId").clear()
    browser.find_element_by_id("userId").send_keys("admin")
    browser.find_element_by_id("password").clear()
    browser.find_element_by_id("password").send_keys("123456")
    browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div[3]/button").click()

    sleep(3)
    browser.find_element_by_link_text("创建工程").click()
    sleep(1)
    browser.switch_to.frame("mainFrame")
    browser.switch_to.frame("/sito2000/action/sd/wf/contractProject/add")
    browser.find_element_by_id("contractName").send_keys(u"自动化测试合同全流程%s" % i)
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

    browser.find_element_by_xpath('//*[@id="substation"]/div[%s]/input' % c).click()
    browser.find_element_by_link_text("下一步").click()
    sleep(1)
    browser.switch_to.alert.accept()
    sleep(3)

    browser.quit()

    # ************************* 变电站建立***************************************************

    sleep(2)
    # browser = webdriver.Chrome()
    browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
    browser.maximize_window()

    browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
    browser.find_element_by_id("userId").clear()
    browser.find_element_by_id("userId").send_keys("admin")
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

    browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[1]/div/span[1]/img').click()
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
    # sleep(1)
    # browser.find_element_by_xpath('//*[@id="ext-gen294"]/div/table/thead/tr/td[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen296"]/div[1]/table/tbody/tr/td[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen296"]/div[2]/table/tbody/tr/td[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen296"]/div[3]/table/tbody/tr/td[2]/div/div').click()

    # 检测仪器
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen317"]/div[1]/table/tbody/tr/td[2]/div').click()

    # 人员列表
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen337"]/div/table/thead/tr/td[2]/div').click()

    # 选择台账2
    sleep(3)
    browser.find_element_by_link_text('SF6气体成分检测').click()

    # 设备列表
    # sleep(1)
    # browser.find_element_by_xpath('//*[@id="ext-gen294"]/div/table/thead/tr/td[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen382"]/div[1]/table/tbody/tr/td[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen382"]/div[2]/table/tbody/tr/td[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen382"]/div[3]/table/tbody/tr/td[2]/div/div').click()

    # 检测仪器
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen403"]/div[1]/table/tbody/tr/td[2]/div').click()

    # 人员列表
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen423"]/div/table/thead/tr/td[2]/div').click()

    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen65"]').click()
    sleep(10)

    print 'test项目test'

    # 项目循环，为下次
    # a = a + 1
    # user_build_csv = user_build_csv + 1
    sleep(1)
    browser.quit()

    # *************************手机app运行***************************************************
    from appium import webdriver
    import random

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.0.2'
    desired_caps['deviceName'] = 'Android Emulator'
    #desired_caps['udid'] = 'UW9555Q899999999'
    desired_caps['appPackage'] = 'com.sito.edetection'
    desired_caps['appActivity'] = '.view.login.LoginActivity'
    desired_caps['noReset'] = True
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # sleep(5)
    # driver.find_element_by_id('edit_username').set_value('caishoujun')
    # driver.find_element_by_id('edit_password').set_value('123456')
    # driver.find_element_by_id('btn_signin').click()
    # sleep(5)


    # 开始项目
    sleep(5)
    driver.find_element_by_id('menu').click()
    sleep(1)
    driver.find_element_by_id('downloadTaskIv').click()
    sleep(1)
    driver.find_element_by_id('md_buttonDefaultPositive').click()
    sleep(1)

    # sleep(1)
    sleep(3)
    el = driver.find_elements_by_id('text_pro_name')[0]
    el.click()
    #driver.find_element_by_id('downloadTaskIv').click()

    # 红外精确测温
    sleep(1)
    driver.find_element_by_id('text_name').click()

    # 检测记时开始按钮
    sleep(1)
    driver.find_element_by_id('off_report_tv').click()
    sleep(1)
    driver.find_element_by_id('md_buttonDefaultPositive').click()
    sleep(1)

    # 图片编号原始值
    # noinspection PyRedeclaration
    f = 1

    for o in range(1, 6, 2):
        # ******************************************************************************************
        # 1* 设备数据输入
        sleep(1)
        el = driver.find_elements_by_id('layout_item')[o]
        el.click()

        # 第一条数据-本体
        sleep(1)
        el = driver.find_elements_by_id('editBtn')[0]
        el.click()

        # 红外图片编号
        sleep(1)
        el = driver.find_elements_by_id('edit')[1]
        el.set_value(f)

        # 正常图片编号
        sleep(1)
        el = driver.find_elements_by_id('edit')[2]
        el.set_value(f + 1)

        # 最高温度
        sleep(1)
        el = driver.find_elements_by_id('edit')[3]
        el.set_value(random.randrange(26, 38))

        sleep(1)
        driver.find_element_by_id('saveTv').click()
        sleep(1)

        # (x,y, x,y, time)
        driver.swipe(500, 1500, 500, 500, 1000)
        sleep(3)

        # 第二条数据-冷却器
        sleep(1)
        el = driver.find_elements_by_id('editBtn')[1]
        el.click()

        # 红外图片编号
        sleep(1)
        el = driver.find_elements_by_id('edit')[1]
        el.set_value(f + 2)

        # 正常图片编号
        sleep(1)
        el = driver.find_elements_by_id('edit')[2]
        el.set_value(f + 3)

        # 最高温度
        sleep(1)
        el = driver.find_elements_by_id('edit')[3]
        el.set_value(random.randrange(26, 38))

        sleep(1)
        driver.find_element_by_id('saveTv').click()
        sleep(1)

        # 返回按键
        driver.find_element_by_class_name('android.widget.ImageButton').click()
        sleep(1)

        # 图片编号自增
        f = f + 4

    # 检测记时结束按钮
    sleep(1)
    driver.find_element_by_id('off_report_tv').click()
    sleep(1)
    driver.find_element_by_id('md_buttonDefaultPositive').click()
    sleep(1)

    # 上传数据
    sleep(1)
    driver.find_element_by_id('menu').click()
    sleep(1)
    driver.find_element_by_id('md_buttonDefaultPositive').click()
    sleep(5)

    sleep(1)
    driver.quit()

    # *************************BS上传图片***************************************************
    # from selenium import webdriver
    # import os
    # import random
	#
    # #browser = webdriver.Chrome()
    # browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
    # browser.maximize_window()
	#
    # browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
    # browser.find_element_by_id("userId").send_keys("admin")
    # browser.find_element_by_id("password").send_keys("123456")
    # browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div[3]/button").click()
	#
    # sleep(3)
    # browser.find_element_by_xpath('//*[@id="ext-gen29"]/user_build_csv').click()
    # sleep(1)
    # browser.find_element_by_link_text('数据上传').click()
    # sleep(1)
	#
    # # 框架转换
    # sleep(1)
    # browser.switch_to.frame("mainFrame")
    # browser.switch_to.frame("/sito2000/workflow/task_data_upload_list.jsp")
	#
    # sleep(1)
    # browser.find_element_by_xpath('//*[@id="ext-gen15"]/div[1]/table/tbody/tr/td[6]/div/a').click()
	#
    # # 框架转换
    # sleep(1)
    # browser.switch_to.parent_frame()
    # el = browser.find_element_by_xpath('//*[@id="ext-gen34"]/iframe')
    # browser.switch_to.frame(el)
	#
    # # 上传图谱
    # sleep(1)
    # browser.find_element_by_xpath('//*[@id="ext-gen17"]').click()
	#
    # # 添加
    # sleep(2)
    # browser.find_element_by_id('SWFUpload_0').click()
    # sleep(1)
	#
    # # 调用upflie.exe上传程序
    # os.system("D:\\upfile515.exe")
	#
    # sleep(3)
    # # 上传
    # browser.find_element_by_xpath('//*[@id="ext-gen124"]').click()
    # # 等待
    # sleep(10)
    # browser.find_element_by_xpath('//*[@id="ext-gen96"]').click()
	#
    # sleep(3)
    # browser.quit()

    # *************************BS认证***************************************************
    from selenium import webdriver

    #browser = webdriver.Chrome()
    browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
    browser.maximize_window()

    browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
    browser.find_element_by_id("userId").send_keys("admin")
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

    # # *************************发送邮件***************************************************
    # # coding=utf-8
    # import smtplib
    # import string
    # from email.mime.text import MIMEText
    # from email.header import Header
	#
    # # 发送邮箱服务器
    # smtpserver = 'smtp.si-top.com'
	#
    # # 发送邮箱用户/密码
    # user = 'xuzhen@si-top.com'
    # password = '123Li456'
	#
    # # 发送邮箱
    # sender = 'xuzhen@si-top.com'
    # # 接收邮箱
    # receiver = 'gongyupeng@si-top.com, wangyanjun@si-top.com, yanfabu@si-top.com'
    # receiver = string.splitfields(receiver, ',')
	#
    # # 发送邮件主题
    # subject = 'Python email test'
	#
    # # 编写HTML类型的邮件正文
    # msg = MIMEText('<html><h1>自动化测试合同全流程%s成功并成功运行</h1><html>' % i, 'html', 'utf-8')
    # msg['Subject'] = Header(subject, 'utf-8')
	#
    # # 连接发送邮件
    # smtp = smtplib.SMTP()
    # smtp.connect(smtpserver)
    # smtp.login(user, password)
    # smtp.sendmail(sender, receiver, msg.as_string())
    # smtp.quit()
