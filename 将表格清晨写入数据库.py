#!/usr/bin/python
#-*-coding:utf-8-*-
import xlwt
import xlrd
import pymysql
d=xlrd.open_workbook('清晨.xlsx')
t=d.sheets()[0]
b=[]
for i in range(t.nrows):
    a1=t.row_values(i)
    b.append(tuple(a1))
print(b)
aa1=pymysql.connect(host='192.168.10.33',port=3306,user='root',password='123456',charset='utf8')
dd=aa1.cursor()

sql1='use zhisheng'
dd.execute(sql1)

sql2='create table biao778(bianhao float,xingming char(30),nianling float,xingbie char(20))'
dd.execute(sql2)
for i in b:
    sql3 = f"insert into biao778 value {i}"
    dd.execute(sql3)
aa1.commit()









































































