#!/usr/bin/python
#-*-coding:utf-8-*-

#smtplib email 作用 用于发送邮件

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# 服务器端信息
# 服务器地址
mail_host='smtp.163.com'

# 用户名
mail_user='17839210927@163.com'

# 用户授权码
mail_pass='jcw214265532'

# 邮件服务器端口号
mail_port=465

# 邮件发送方的信息
fasong='17839210927@163.com'

# 邮件接收方的地址
jieshou=['z13683789936@163.com']

# 邮件正文
# 设置主题
subject='垃圾'
'''
# 设置正文
content='小垃圾'

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# MIMEText()是一个类
message=MIMEText(content, 'plain', 'utf-8')

# 发送邮件的过程
# Header() 是一个类
# 第一步：添加邮件发送者头部
message['from']=Header(fasong)
# 第二步：添加接收者头部
message['To']=  Header(str(';'.join(jieshou)))
# 第三步：添加邮件主题
message['Subject']=Header(subject)

# 连接邮件服务器发送邮件
# 第一步：登录邮箱
denglu=smtplib.SMTP_SSL(host=mail_host,port=mail_port)
# 第二步：输入账号密码
denglu.login(mail_user ,mail_pass)
# 第三步：发送邮件
denglu.sendmail(fasong,jieshou,message.as_string())
print('成功')
# 第四步：退出登录
denglu.close()
'''

# 带附件的邮件发送
# 添加一个MIMEMultipart()类，将正文及附件添加到邮箱里，并发送出去
message=MIMEMultipart()
# # 第一步：添加邮件发送者头部
message['from']=Header(fasong)
# # 第二步：添加接收者头部
message['To']=  Header(str(';'.join(jieshou)))
# # 第三步：添加邮件主题
message['Subject']=Header(subject)

# 准备要发送的正文：以HTML网页的形式发送
with open(file='邮件.html',mode='r',encoding='utf-8') as  f:
    content=f.read()

# 设置html格式
p1 = MIMEText(content,'html','utf-8')

# 准备一个要发送的附件
with open(file='b.txt',mode='r',encoding='utf-8') as  f:
    d=f.read()

# 设置txt格式
p2=MIMEText(d,'plain','utf-8')
# 将文本转为二进制
p2['Content-Type'] = 'application/octet-stream'
# 对附件添加一个名字
p2['Content-Disposition'] = 'attachment;filename="b.txt"'

# 准备一个照片作为附件
with open(file='kkk.png',mode='rb') as f:
    # MIMEImage() 作用加载二进制图片
    p3=MIMEImage(f.read())
# 将图片转为二进制
p3['Content-Type'] = 'application/octet-stream'
# 对附件添加一个名字
p3['Content-Disposition'] = 'attachment;filename="kkk.png"'

# 将三部分添加到邮件里
message.attach(p1)
message.attach(p2)
message.attach(p3)

# 连接邮件服务器发送邮件
# 第一步：登录邮箱
denglu=smtplib.SMTP_SSL(host=mail_host,port=mail_port)
# 第二步：输入账号密码
denglu.login(mail_user ,mail_pass)
# 第三步：发送邮件
denglu.sendmail(fasong,jieshou,message.as_string())
print('成功')
# 第四步：退出登录
denglu.close()








