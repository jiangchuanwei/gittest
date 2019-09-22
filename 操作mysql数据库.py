#!/usr/bin/python
#-*-coding:utf-8-*-

#连接mysql
#导入pymysql模块
import  pymysql
#第一步 与Navicat建立连接
d= pymysql.connect(host='192.168.10.52',port=3306,user='root',password='123456',charset='utf8')
#第二步 创建一个游标  类似于mysql进入命令行模式
e=d.cursor()
#第三步  写语句
sql='show databases'
#第四步 执行语句   放入需要执行的sql语句
# 执行多条sql语句 e.executemany()
date=e.execute(sql)
print(date)
#第五步 查询具体结果
# print(e.fetchall())  #获取执行sql后的所有结果
# print(e.fetchone())  #获取执行sql后的第一个结果
# print(e.fetchmany(3)) #获取执行sql后的指定条结果

#创建库
#  sql1='create database zhisheng'
#  e.execute(sql1)

#进入库
sql2='use zhisheng'
e.execute(sql2)

#创建表
# sql3='create table biao2(id int,name char(20))'
# e.execute(sql3)

#数据插入
# sql4="insert into biao2 values(4,'yisi'),(5,'asda'),(8,'fdsf')"
# e.execute(sql4)
#保存   找到链接d 使用commit保存
# d.commit()

#更新操作
# sql5="update biao2 set id=5 where name='lisi'"
# e.execute(sql5)
#保存
# d.commit()

