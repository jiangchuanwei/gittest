#/usr/bin/python
#-*-coding:utf-8-*-
#账号密码放入字典
'''
a=['123','487798745','478962','145568']
b=['44785','47866','47856','4879']
c=len(a)
d=[]
e=[]
for i in range(c):
    if len(a[i])>=6 and len(a[i])<=8 and len(b[i])>=5 and len(b[i])<=6:
        print(a[i])
        print(b[i])
        d.append(a[i])
        e.append(b[i])
if len(e)>=1:
    # d1=''.join(d)
    # e1=''.join(e)
# d2=int(d1)
# e2=int(e1)
    print(len(e))
    f = {}
    f['账号']=d
    f['密码']=e
    print(f)
else:
    print('没有符合')
'''

'''
d = {
    "data": {
        "msg":
        [
            {
                "s_1": ["Jim", "男",  19, "175cm"],
                "country": "美国"
            },
            {
                "s_2": ["Kity", "女",  17, "165cm"],
                "country": "法国"
            },
            {
                "s_3": ["Tom", "男",  19, "173cm"],
                "country": "美国"
            },
            {
                "s_4": ["拖拉斯基", "男",  18, "180cm"],
                "country": "俄罗斯"
            },
            {
                "s_5": ["阿卡丽", "女",  17, "175cm"],
                "country": "乌克兰"
            },
            {
                "s_6": ["牙买稻子", "女",  18, "161cm"],
                "country": "日本"
            },
            {
                "s_7": ["龟田一郎", "男",  19, "175cm"],
                "country": "日本"
            },
            {
                "s_8": ["张三", "男",  20, "180cm"],
                "country": "中国"
            },
            {
                "s_9": ["李秀琴", "女",  19, "175cm"],
                "country": "中国"
            },
            {
                "s_10": ["宋仲基", "女",  19, "175cm"],
                "country": "韩国"
            },
            {
                "s_11": ["金正鞋", "男",  19, "168cm"],
                "country": "朝鲜"
            },
            {
                "s_12": ["卡列夫斯基", "男",  21, "190cm"],
                "country": "俄罗斯"
            },
        ]
    },
}
# c=[]
# n=[]
# for i in d.values():
#     # print(i)
#     for j in i.values():
#         # print(j)
#         for k in j:
#             # print(k)
#             for z in k.values():
#                 # print(z)
#                 c.append(z)
# # print(c)
# t=(len(c))
# for g in range(t):
#     if g%2!=0:
#         # print(c[g])
#         n.append(c[g])
# # print(n)
# m=set(n)
# print(m)
# print(len(m))


# c=[]
# e=[]
# for i in d.values():
#     print(i)
#     for j in i.values():
#         print(j)
#         for g in j:
#             print(g)
#             for z in g.values():
#                 print(z)
#                 c.append(z)
# print(c)
# a=len(c)
# for q in range(a):
#     if q%2==0:
#         print(c[q])
#         e.append(c[q])
# print(e)
# w=[]
# for a1 in e:
#     c=a1[3]
#     print(c)
#     w.append(c)
# print(w)
# w1=''.join(w)
# print(w1)
# q1=w1.split('cm')
# print(q1)
# q2=' '.join(q1)
# print(q2)
# q3=str(q2)
# q4=max(q3)
# print(q4)
a1=d['data']['msg']
print(a1)
mz=[]
xb=[]
nl=[]
sg=[]
gj=[]
for i in a1:
    for j in i.values():
        if type(j)==list:
            mz.append(j[0])
            xb.append(j[1])
            nl.append(j[2])
            sg.append(j[3])

        else:
            gj.append(j)
print(f'国家的个数{len(set(gj))}')
print(f'最大身高{max(sg)},最小身高{min(sg)}')
print(f'男生{xb.count("男")},女士{xb.count("女")},比例{xb.count("男")/xb.count("女")}')
print(xb)

print(xb.count('男')/xb.count('女'))

#身高
sg1=0
for t in sg:
    sg1+=int(t.replace('cm',''))
print(f'平均身高{sg1/len(sg)}')

m=0
for i1 in sg:
    if '170cm' <=i1<='180cm':
        print(m)
        print(mz[m])
    m+=1
'''

###质数之和1
'''
a=2
for j in range(2,100):
    for i in range(2,j):
        if j%i==0:
            break
        if j==i+1:
            print(j)
            a=a+j
print(a)
'''

#质数之和2
'''
a=0
for j in range(2,100):
    for i in range(2,j+1):
        if j%i==0:
            break
    if i==j:
        print(j)
        a=a+j
print(a)
'''

#水仙花数
'''
for i in range(100,1000):
    b=i//100
    c=i//10%10
    d=i%10
    x=b*b*b
    y=c*c*c
    z=d*d*d
    n=x+y+z
    if i == n:
        print(n)
'''

#阶乘之和1
'''
c=input("shuru")
a=1
b=0
d=(int(c))
for i in range(1,d+1):
    a=a*i
    b=b+a
print(b)
'''

#阶乘之和2
'''
c=input('****')
if c.isdigit():
    if isinstance(c,float)==True:
        print('错误')
    elif int(c)>=1:
        n=1
        m=0
        d=int(c)
        for i in range(1,d+1):
            n=n*i
            m=m+n
        print(m)
    else:
        print('cuo')
else:
    print('cuo')
'''

'''
d=[]
a='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
c=len(a)
for i in range(6):
    import random
    e=random.randint(0,c-1)
    d.append(a[e])
d1=''.join(d)
print(d1)
while True:
    n=input('请输入验证码')
    if n==d1:
        print('正确')
        break
    elif n!=d1:
        print('你瞎嘛')
        m=input('结束输入按1，继续输入按2')
        m1=int(m)
        if m1==1:
            break
        elif m1==2:
            print()
'''

#左移
'''
a=list(input('***'))
a1=int(input('输入移动的次数'))
b=[]
for i in range(a1):
    b.append(a[0])
    a.pop(0)
a.extend(b)
print(a)
'''
#无参数 无返回值
# def aa():
#     n=0
#     for i in range(100):
#         n+=i
#     print(n)
# aa()

#有参数 无返回值
# def aa(x):#    x属于必填参数 使用函数的时候必须传入值
#     n=0
#     for i in range(x):
#         n+=i
#     print(n)
# aa(101)


'''
全局变量定义之后，在整个脚本的所有行都能用
'''
'''
def aa(x):
    n=0
    for i in range(x):
        n+=i
    print(n)
    return n  #函数没有
#print(aa(101))  #直接打印函数名print（aa）的话 结果是函数在内存中的位置
aa(3)
'''

#质数和函数
'''
def cc(x1):
    if x1>2:
        a=0
        for j in range(2,x1+1):
            for i in range(2,j+1):
                if j%i==0:
                    break
            if i==j:
                a=a+j
    return a
print(cc(100))
'''
#阶乘和
a=1
b=0
for i in range(1,5):
    a=a*i
    b=b+a
print(b)


#定义一个可以输入可变长参数的函数
# 如果输入参数个数为0提示

def a(*args):
    if len(args)==2:
        x,y=args
        if x<y:
            b=x
            c=0
            for i in range(x,y+1):
                b=b*i
                c=c+b
            return c
        else:
            print('请输入正确')
    elif len(args)==4:
        q1,q2,q3,q4=args
        d1 = []
        if type(q1)==int and type(q2)==int and type(q3)==int and type(q4)==int:#and q1!=0 and q1!=q2 and q1!=q3 and q1!=q4 and q2!=q3 and q2!=q4 and q3!=q4:
            for i in range(4):
                for i1 in range(4):
                    for i2 in range(4):
                        for i3 in range(4):
                            if args[i]!=0 and args[i] != args[i1] and args[i] != args[i2] and args[i] != args[i3] and args[i1] != args[i2] and args[i1] != args[i3] and \
                                args[i2] != args[i3]:
                                    d1.append(f'{args[i]}{args[i1]}{args[i2]}{args[i3]}')
            d2 = len(d1)
            return d2
        else:
            print('请输入数字')
    elif len(args)==0:
        print('请输入参数')
    else:
        print('该函数不执行')
print(a(2,8,9,5))