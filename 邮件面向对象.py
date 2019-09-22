#!/usr/bin/python
#-*-coding:utf-8-*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
class youjian(object):
    mail_host = 'smtp.163.com'
    mail_port = 465
    def __init__(self,user,password):
        self.user=user
        self.password=password
        self.mail_user = self.user
        self.mail_pass = self.password
    def fasong(self):
        jieshou = [input('输入接收方的信息')]
        subject = input('输入主题')
        content = input('输入正文')
        message = MIMEText(content, 'plain', 'utf-8')
        message['from'] = Header(self.user)
        message['To'] = Header(str(';'.join(jieshou)))
        message['Subject'] = Header(subject)
        denglu = smtplib.SMTP_SSL(host=self.mail_host, port=self.mail_port)
        denglu.login(self.mail_user ,self.mail_pass)
        denglu.sendmail(self.user,jieshou,message.as_string())
        print('发送成功')
        denglu.close()
aa=youjian('17839210927@163.com','jcw214265532')
aa.fasong()












