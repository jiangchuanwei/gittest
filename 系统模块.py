#!/usr/bin/python
#-*-coding:utf-8-*-
#OS内模块，作用：python与计算机系统进行交互
import os
#获取当前目录路径
os.getcwd()
#chdir(路径的名字)：切换目录
# os.chdir(r'D:\PycharmProjects\untitled\DAR')

# . 代表当前目录==os.curdir
# print(os.curdir)

# .. 代表上一级目录==os.pardir
# print(os.pardir)

# os.name 获取操作系统的类型
# print(os.name)

#创建多及目录 os.makedirs（'多及目录'）a/b/c
# os.makedirs('a/b/c')

#创建一个目录 os.mkdir（‘目录名字’）
#os.mkdir('aaa')

#删除多个空目录  os.removedirs('目录名')
# os.removedirs('a/b/c')

#删除单个空目录   os.rmdir('目录名')
# os.rmdir('aaa')

#查看当前路径下所有的文件、目录 print(os.listdir(r'路径'))
# print(os.listdir(r'D:\PycharmProjects\untitled\DAR'))

#对文件 目录重命名 os.rename('老名字','新名字')
#os.rename(r'D:\PycharmProjects\untitled\DAY',r'D:\PycharmProjects\untitled\DAR')

#删除文件 os.remove(r'文件路径')
# os.remove(r'D:\PycharmProjects\untitled\DAR\rrr.txt')

#执行系统命令 os.popen('需要执行的命令')
# c=os.popen('dir')
# print(c.read())

#os.path 类 对文件的操作 返回文件的路径 例如绝对路径 相对路径、 判断文件，目录类型
#1 返回文件的绝对路径 os.path.abspath（'文件名'）
# print(os.path.abspath('b.txt'))

#2 返回文件的上一级目录 os.path.dirname('路径')
print(os.path.dirname(r'D:\PycharmProjects\untitled\DAR\998.py'))

#3 返回当前文件或目录 名字 os.path.basename('路径')
print(os.path.basename(r'D:\PycharmProjects\untitled\DAR\998.py'))

#4 判断文件或目录是否存在 返回True false   os.path.exists('文件名')
print(os.path.exists('a.txt'))

#5 判断是否是目录 返回True false   os.path.isdir('路径')
print(os.path.isdir(r'D:\PycharmProjects\untitled\DAR'))

#6 判断是否是文件 返回True false  os.path.isfile('路径')
print(os.path.isfile(r'D:\PycharmProjects\untitled\DAR'))

#7 判断是否是链接文件  返回True false   os.path.islink('路径')
print(os.path.islink(r'D:\PycharmProjects\untitled\DAR'))

#8 文件路径拼接 join（'路径1'，'路径2'）
print(os.path.join('/a/','b'))

#9 文件路径分离 split('路径名字')   将最后一个文件或目录分离
print(os.path.split(r'D:\PycharmProjects\untitled\DAR\998.py'))

#10 分割文件的后缀名  返回一个元组  os.path.splitext('文件名')
print(os.path.splitext('b.txt'))

print('------------------------------------------------------------------')



#统计顶级目录下有多少个目录，文件 个数
# a=os.listdir(r'D:\PycharmProjects\untitled')
# print(a)
# d=[]
# d1=[]
# d2=[]
# d3=[]
# d4=0
# for i in a:
#     c=os.path.join(r'D:\PycharmProjects\untitled', i)
#     c1=os.path.isfile(c)
#     if c1 ==True:
#         d.append(c1)
#     elif c1==False:
#         d1.append(c1)
#         c2=os.listdir(c)
#         d2.append(c2)
# for j in d2:
#     c2=len(j)
#     d3.append(c2)
# for g in range(len(d3)):
#     d4=d4+d3[g]
# dd=len(d)+len(d1)+d4
# print(dd)


#python时间模块  time datetime 操作的时间、日期
import time

#1 sleep(数值：浮点数/整数)
#  time.sleep(2)

#2 clock 计算的是执行代码是CPU花费的时间
print(time.clock())

#3 获取当前时间 ctime()   asctime（）
print(time.ctime())
print(time.asctime())

#4 输出时间 localtime（）  本地时区
print(time.localtime())

#5 格式化输出时间 strftime（’关于时间的字符串‘）
print(time.strftime('%A %B %H: %M: %S'))

#6 格式化解析字符串 strptime（’关于时间的字符串‘）
#  %d一个月的第几天 %b 表示的月份 %y 年份
print(time.strptime('30 Nov 00','%d %b %y'))

#7 计算机元年 time（） 表示计算机元年到现在多少秒的总和
print(time.time())


import datetime
#1 获取当前时间日期 datetime.now（）
print(datetime.datetime.now())

#2 获取指定的时间日期 datetime（整数）
print(datetime.datetime(2019,7,30,12,1,1))

#3 将时间字符串转成datetime里的日期  strptime（）
print(datetime.datetime.strptime('1937 7 7 12:00:00','%Y %m %d %H:%M:%S'))

#4 将日期转化为字符串 strftime（）
print(datetime.datetime.now().strftime("%H:%M:%S"))

#5 日期的加减法
#求当前时间
a=datetime.datetime.now()
#加三个小时
b=a + datetime.timedelta(hours=3)
print(b)

#6 获取当前日期 today（）
print(datetime.date.today())

#7 对日期的加减timedelta（days=xxx）
print(datetime.date.today()-datetime.timedelta(days=1))





























