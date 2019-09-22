#!/usr/bin/python
#-*-coding:utf-8-*-

#爬虫：通过python代码获取网络中存放的数据资源【文件，图片等等】
#反爬虫：防止资源被爬虫代码获取
#最常见的反爬虫机制 1.封ip地址 2.封Mac地址 3.验证码反爬
# 4.服务器传输给浏览器的数据通过异步加载

#re模块
#requests模块 python发送http https请求，接受响应数据的一个第三方库
import re
import requests
'''
#User-Agent:代表浏览器
b={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
#get 请求获取资源
#第一步发送请求
r=requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/17125664.html',headers=b)
#第二步获取响应的结果 content（）获取请求之后的响应数据
d=r.content.decode(encoding='gbk')
print(d)
#想要<h2> 第一章 雪鹰领</h2> 里的字
r1=re.compile(r'<h2>(.*?)</h2>')
cc=re.findall(r1,d)
# print(cc)

#想要内容
r2=re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />')
cc1=re.findall(r2,d)
print(cc1)

#写入文件
f=open(file='b.txt',mode='w',encoding='utf-8')
for i in cc1:
    f.write(f'{i}\n')
'''
##爬取多章小说
## 1 爬取目录
#User-Agent:代表浏览器
b={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
#get 请求获取资源
#第一步发送请求
r=requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/',headers=b)
#第二步获取响应的结果 content（）获取请求之后的响应数据
d=r.content.decode(encoding='gbk')

# 2 过滤目录
r1=re.compile(r'<dd><a href="(.*?)">(.*?)</a></dd>')
cc=re.findall(r1,d)


for i in  cc:
    r2 = requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/'+i[0], headers=b)
    d1 = r2.content.decode(encoding='gbk')
    r3 = re.compile(r'<h2>(.*?)</h2>')
    cc2 = re.findall(r3, d1)
    r4 = re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />')
    cc1 = re.findall(r4, d1)
    for j in cc2:
        cc1.insert(0,j)
    f = open(file='b.txt', mode='a', encoding='utf-8')
    for h in cc1:
        f.write(f'{h}\n')








































































































