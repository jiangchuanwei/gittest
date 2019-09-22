#!/usr/bin/python
#-*-coding:utf-8-*-

import re
import requests
class tupian(object):
    b = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    def __init__(self,yeshu):
        self.yeshu=yeshu

    def duoye(self):
        dd=[]
        urls2=[]
        for k in range(1,self.yeshu+1):
            h='https://www.qiushibaike.com/pic/page/'+str(k)+'/?s=5216045'
            r = requests.get(url=h, headers=self.b)
            d1 = r.content.decode(encoding='utf-8')
            r1 = re.compile(r'<img src="//pic.qiushibaike.com/system/pictures/(.*?).jpg" alt="')
            r2=re.findall(r1,d1)
            dd.append(r2)
        for k1 in dd:
            for k2 in k1:
                b2 = 'https://pic.qiushibaike.com/system/pictures/' + k2 + '.jpg'
                urls2.append(b2)
        return  urls2



    def pa1(self):
        n=0
        for j in self.duoye():
            r3=requests.get(url=j,headers=self.b)
            jiegou=r3.content  #接受图片 二进制
            #保存图片
            f=open(f'{n}.jpg',mode='wb')
            f.write(jiegou)
            n+=1


p1=tupian(35)

p1.pa1()



















