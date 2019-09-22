#/usr/bin/python
#-*-coding:utf-8-*-
#print('内容')：代码有优先执行内容，然后在执行打印
#print('helo 中午吃啥 world')
#input('提示语')：输入的都是字符
#a=input ('tishiyu')
#print(a)
#单行注释
#多行注释：ctrl+？或者 单引号注释，首尾加三个单引号  或者 双引号注释，首尾加三个双引号
#a=input ('tishiyu')
#print(a)

#去重
'''
a=[1,1,2,3,3,5,7,7]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
'''

#99乘法表
'''
for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s' %(i,j,i*j),end=' ')
    print()
'''

# text = "Early in the day it was whispered that we should sail in a boat, only thou and I, and never a soul in the world would know of this our pilgrimage to no country and to no end"
# #将首字母大写的单词提取出来
'''
e=[]
a=text.split()
for i in a:
    if i.istitle():
        e.append(i)
print(e)
'''

# #将所有首字母大写
'''
print(text.title())
'''

# #将text中所有的包含a的字符替换成博文两个字
'''
print(text.replace('a','博文',))
'''

# #删除包含小t字符的单词后，组成一个新的字符串
'''
for i in  a:
    if 't' in i:
         a.remove(i)
print(a)
print(' '.join(a))
'''

#判断回文
'''
b=input('输入')
a =reversed(list(b))
if list(b) == list(a):
    print('shi')
else:
    print('no')
'''

#判断是否回文
'''
a=input('***')
b=str(a)
c=b[::1]
d=b[::-1]
if c==b:
    print('shi')
else:
    print('no')
'''

#冒泡排序

a=[10,30,20,40,50,70,60]
b=len(a)
for i in range(b):
    for j in range(b-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)


#选择排序

# c=input('***')
# a=c.split(' ')
# a=[1,2,3,4,5,6]
# b=len(a)
# for i in range(b):
#      for j in range(b):
#          if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)



#收银机1
'''
a=['香蕉','菠萝','提子','胡萝']
b=[100,80,50,30]
while True:
    print(f'商品编号\t\t\t商品名\t\t\t\t价格')
    for i,j in enumerate(a):
        print(i,'\t\t\t\t\t',j,'\t\t\t\t',b[i])
    c=int(input("编号0-3"))
    d=int(input('数量'))
    e=int(input('会员输入1，非会员输入0'))
    if e==1:
        z=input('输入账号')
        if z=='123456':
                print('会员你好，您享受95折优惠')
                for i1,j1 in enumerate(a):
                    if c==i1:
                        v=b[i1]*d*0.95
                        print('支付',v,end=' 元')
    else:
        for i2, j2 in enumerate(a):
            if c==i2:
                v1=b[i2]*d
                print('支付',v1,end=' 元     ')
    m=input('继续x，退出z')
    if m=='x':
        print('      继续购买  ！！！！！')
    elif m=='z':
        break
'''

#收银机2
'''
a=['水果','饮料','零食','香烟']
b=[100,200,300,400]
print("商品号\t\t\t商品名称\t\t\t商品单价")
for i,j in enumerate(a):
    print(f"\t{i}\t\t\t{j}\t\t\t{b[i]}")
while 1:
    c=input('购买输入y，退出输入q')
    if c=='y':
        a1=int(input('编号'))
        a2=int(input('数量'))
        if a1>3:
            print('输入错误')
        else:
            v=b[a1]*a2
            print('你购买了',a[a1],'购买数量',a2,'个','消费了',v,end=('  元'))
        break
    elif a==q:
        print('下次再来')
        break
    else:
        print('输入错误')
'''

#1234组成不同的三位数
'''
c=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j)and(i!=k)and(k!=j):
                print(i,j,k)
                c.append([i,j,k])
print(len(c))
'''
