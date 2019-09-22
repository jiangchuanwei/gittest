#!/usr/bin/python
#-*-coding:utf-8-*-


import re
import requests

class xiaoshuo(object):

    def neirong(self):
        b = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
        r = requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/', headers=b)
        r1 = re.compile(r'<dd><a href="(.*?)">(.*?)</a></dd>')
        d = r.content.decode(encoding='gbk')
        cc = re.findall(r1,d)
        for i in cc:
            r2 = requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/'+i[0], headers=b)
            d1 = r2.content.decode(encoding='gbk')
            r3 = re.compile(r'<h2>(.*?)</h2>')
            cc2 = re.findall(r3, d1)
            r4 = re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />')
            cc1 = re.findall(r4, d1)
            for j in cc2:
                cc1.insert(0,f'============{j}============')
            f = open(file='b.txt', mode='a', encoding='utf-8')
            for h in cc1:
                f.write(f'{h}\n')
                print('完成！！！')
xiazai=xiaoshuo()
xiazai.neirong()