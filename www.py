#!/usr/bin/python
#-*-coding:utf-8-*-

import pymysql
import xlrd

a=xlrd.open_workbook(filename='清晨.xlsx')
b=a.sheets()[0]
for i in range(a.nrow):
