# coding =utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

_user = "sigeken@qq.com"
_pwd = "***"
_to = "402363522@qq.com"

msg = MIMEMultipart()
msg["Subject"] = "don't panic"
msg["From"] = _user
msg["To"] = _to

part = MIMEText("乔装打扮，不择手段")
msg.attach(part)

part = MIMEApplication(open('foo.xlsx', 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename="foo.xlsx")
msg.attach(part)


s = smtplib.SMTP("smtp.qq.com")
s.login(_user, _pwd)
s.sendmail(_user, _to, msg.as_string())
s.close()