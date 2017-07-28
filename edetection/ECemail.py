#coding=utf-8
import smtplib
import string
from email.mime.text import MIMEText
from email.header import Header


# 发送邮箱服务器
smtpserver = 'smtp.si-top.com'

# 发送邮箱用户/密码
user = 'xuzhen@si-top.com'
password = '123Li456'

# 发送邮箱
sender = 'xuzhen@si-top.com'
# 接收邮箱
receiver = 'gongyupeng@si-top.com, guoshasha@si-top.com'
receiver = string.splitfields(receiver, ',')

# 发送邮件主题
subject = 'Python email test'

# 编写HTML类型的邮件正文
msg = MIMEText('<html><h1>Hello World!123</h1><html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()