#!/usr/bin/python
#-*-coding:utf-8-*-

import re
import requests
class tupian(object):
    b = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    def __init__(self):
        #发送请求
        #局部变量
        r=requests.get(url='https://www.qiushibaike.com/pic/',headers=self.b)
        self.d=r.content.decode(encoding='utf-8')
    def fenxi(self):

        #正则
        r1=re.compile(r'<img src="//pic.qiushibaike.com/system/pictures/(.*?).jpg" alt="')
        #正则匹配
        r2=re.findall(r1,self.d)
        urls=[]
        for i in r2:
            b1 = 'https://pic.qiushibaike.com/system/pictures/'+ i +'.jpg'
            urls.append(b1)
        return urls
    def pa(self):
        n=0
        for j in self.fenxi():
            r3=requests.get(url=j,headers=self.b)
            jiegou=r3.content  #接受图片 二进制
            #保存图片
            f=open(f'{n}.jpg',mode='wb')
            f.write(jiegou)
            n+=1
p1=tupian()
p1.pa()






























