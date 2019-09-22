#!/usr/bin/python
#-*-coding:utf-8-*-


# import random
#
# k = []
# v = []
#
#
# def func(x, y=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
#     print(f'x的值为：{x} , y的值为：{y}')
#     if x in y:
#         for j in range(x, len(y)):
#             v.append(y[j])
#         for q in range(1, x + 1):
#             v.append(q)
#         return f'x的值为：{x} , y的值为：{v}'
#     else:
#         for i in range(2):
#             a = random.choice(y)
#             k.append(a)
#         print(f'随机数为：{k}')
#         y.remove(k[0]),y.remove(k[1]),y.insert(5, x)
#         return f'x的值为：{x} , y的值为：{y}'
#
#
# print(func(2))
# print(func(0))

#定义一个函数，函数一有一个可变长参数: kwargs
#问题一:获取kwargs传入的所有的键、值
# 问题二:判断kwargs的每个值类型， 统计有多少个字符串、列表、元组、集合、数值、字典类型的个数
#问题三:如果有某个类型的值个数大于3，函数终止、并返回由这些类型的值组成的列表
'''
def cc(**kwargs):
    print(kwargs.keys())
    print(kwargs.values())
    yz=[]
    list_1=[]
    str_1=[]
    jih=[]
    dict_1=[]
    int_1=[]
    for i in kwargs.values():
        if type(i)==tuple:
            yz.append(i)
            if len(yz)>3:
                break
        elif type(i)==list:
            list_1.append(i)
            if len(list_1)>3:
                break
        elif  type(i)==str:
            str_1.append(i)
            if len(str_1)>3:
                break
        elif type==dict:
            dict_1.append(i)
            if len(dict_1)>3:
                break
        elif type(i)==int:
            int_1.append(i)
            if len(int_1)>3:
                break
        else:
            jih.append(i)
            if len(jih)>3:
                break
    print('字符串元素有', len(str_1), '个')
    print('元组元素有', len(yz), '个')
    print('数值元素有', len(int_1), '个')
    print('字典元素有', len(dict_1), '个')
    print('列表元素有', len(list_1), '个')
    print('集合元素有', len(jih), '个')
    print(str_1)
    print(yz)
    print(int_1)
    print(dict_1)
    print(list_1)
    print(jih)
cc(a=[1,0],c=[5,3],b='wadad',d=['jsd','fds'],f=[2,3],s=[2,3])
'''

# import random
# def kk(x,y=[1,2,3,4,5,6,7,8,9]):
#     if x in y:
#         z=y.index(x)
#         for i in range(z+1):
#             y.append(y[0])
#             y.pop(0)
#         print(y)
#     else:
#         for i in range(2):
#             a = random.randint(0, len(y) + 1)
#             y.remove(y[a-1])
#         y.insert(5,x)
#         print(y)
# kk(12)

# def cc(x,*args):
#     b=sum(args)
#     c=x+b
#     return c
#
# def aa(z):
#     i=cc(1,2,3)
#     a1=z
#     dd=dict.fromkeys(a1,i)
#     return dd
# print(aa([1,2,3]))

'''
def  qq(x,y):
    a=str(x)
    b=str(y)
    c=','.join(a)
    d=','.join(b)
    cc=c.split(',')
    dd=d.split(',')
    cc.extend(dd)
    print(cc)
    a1=len(cc)
    import random
    for i in range(6):
        a2=random.randint(0,a1-1)
        for i1 in  range(7):
            a3= random.randint(0, a1 - 1)
            for i2 in range(8):
                a4 = random.randint(0, a1 - 1)





qq(123458,5464547)
'''
#设计一个用户登录后生成session的函数，x为用户名，y为密码。
# 当用户密码都输入正确时，将用户名和密码组成一个新的字符串随机取6~ 8位字符作为用户登录后的session
# 当用户名和密码组成的字符串“A”长度小于8位时，自动添加0~ 9任意数字到“A"， 再随机生成6~ 8位字符作为用户登录后的session
'''
import random
d = {'admin':'12345','abc':'123','user':'54321'}
def session(x,y):
    A = ''
    for i,c in d.items():
        if x == i and d[i] == y:
            A = x + y
            while True:
                if len(A) >= 8:
                    a = random.randint(6,8)
                    b = ''
                    for j in range(a):
                        q = random.choice(A)
                        b += q
                    return f'这是session：{b}'
                else:
                    e = random.randint(0,9)
                    f = str(e)
                    A += f
    else:
        return '请重新输入用户名和密码'

print(session('admin','12345'))
print(session('abc','123'))
print(session('admin',2))
'''

















































































































































































