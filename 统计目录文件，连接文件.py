#!/usr/bin/python
#-*-coding:utf-8-*-
import os
w=[]
w1=[]
w2=[]
a=os.listdir(r'D:\PycharmProjects\untitled\DAR')
for i in a:
    c=os.path.join(r'D:\PycharmProjects\untitled\DAR', i)
    c1=os.path.isdir(c)
    c2=os.path.islink(c)
    c3=os.path.isfile(c)
    if c1==True:
        w.append(c1)
    if c2 ==True:
        w1.append(c2)
    if c3==True:
        w2.append(c3)
print(f'目录有{len(w)}个')
print(f'链接文件有{len(w1)}个')
print(f'普通文件有{len(w2)-len(w1)}个')
