#!/usr/bin/python
#-*-coding:utf-8-*-


#类和对象
'''
#定义一个动物园的类
class dwuyuan(object):#(括号里写继承与哪一个类)
#object：所有类的基类
    #属性
    dongwu='老虎'
    #方法
    def biaoyan(self):  #self必须写，等于对象本身
        print(f'有一个动物在表演，{self.dongwu}在表演')  #self必须写
#类的使用
#第一步，创建对象
a=dwuyuan()
#第二步，使用对象操作类的属性方法
print(a.dongwu)
print(a.biaoyan())
'''


#################################################################################
#定义一个学生类
'''
class xuesheng(object):
    #类的属性
    mingzi='渣男'
    banji='1903'
    xingbie=True # 男true  女false
    #方法
    def dayinmz(self):
        print(f'有个学生的名字叫做{self.mingzi}')
    def dayinbj(self):
        print(f'学生叫{self.mingzi},在{self.banji}')
    def dayinxb(self):
        if self.xingbie:
            print('哇，靓仔')
        else:
            print('哇，靓女')
a=xuesheng()
print(a.dayinxb())
print(a.dayinbj())
print(a.dayinmz())
'''



#################################################################################
#定义一个学生类
'''
class xuesheng(object):
    #类的属性
    book=['言情','武侠','都市','玄幻']
    # 初始化方法
    def __init__(self, mingzi, banji, xingbie):
        #对象的属性
        self.mingzi = mingzi
        self.banji=banji
        self.xingbie=xingbie

    def dayinmz(self):
            print(f'有个学生的名字叫做{self.mingzi}')

    def dayinbj(self):
            print(f'学生叫{self.mingzi},在{self.banji}')

    def dayinxb(self):
        if self.xingbie:
                print('哇，靓仔')
        else:
                print('哇，靓女')
    def dayinbook(self):
        for i in self.book:
            print(f'图书有：{i}')
a = xuesheng('张三','12',True)
a.dayinmz()
a.dayinxb()
a.dayinbj()
a.dayinbook()

b=xuesheng('李四','13',False)
b.dayinbj()
b.dayinxb()
b.dayinmz()
b.dayinbook()

# 1.类不能使用对象的属性
# 2.类可以使用类的属性

# 1.对象可以访问对象的属性
# 2.对象可以访问类的属性
'''


#################################################################################
#老师类
class laoshi(object):
    #类属性:公有的，私有的
    #公有属性
    ke=['语文','数学','外语','生物']
    #私有属性，双下划线开头
    __banji=('1903')
    #初始化方法/魔法方法
    def  __init__(self,a,b):
        #对象属性
        #公有的对象属性
        self.a=a
        #私有的对象属性
        self.__b=b

        self.c='hello'

    def kl(self):
        print(f'方法访问类的公有属性，{self.ke}')
        print(f'方法访问类的私有属性，{self.__banji}')
    def g(self):
        print(f'方法访问对象的公有属性，{self.a}')
        print(f'方法访问对象的私有属性，{self.__b}')

'''
print(laoshi.ke)  #访问公有属性
print(laoshi.__banji)   #类的外部 类和对象都不能访问类的私有属性
ti=laoshi()
ti.kl()  #在类的内部访问私有属性
print(t1.__banji)  #不能
'''
#################################################################################

'''
t2=laoshi('pp','dd')
print(t2__b)  #私有的对象属性不能在对象和类的外部使用
#对象可以访问对象的私有属性，对象的公有属性，在类的内部
t2.g()
'''

#################################################################################
#更改属性对象的值
laoshi.ke=(1,2,3)
print(laoshi.ke)

#更改对象属性只能通过对象来修改
t3=laoshi(1,2)
t3.c='wordl'
print(t3.c)

t4=laoshi(2,3)
print(t4.c)



#################################################################################
#方法：静态、类方法，实例方法、魔法方法、私有方法
#私有方法

class tt(object):
    tt1=[1,2,3]
    #私有方法
    def __w(self):
        print('这是私有方法')
    #在类的外部通过对象.方法名访问方法、在类的内部要用self.方法名来访问方法
    #self>>>对象   访问方法和属性通过对象来操作的
    
    #实例方法
    def h(self):
        self.__w()

    # @符号在python里被称为语法糖
    @classmethod  #装饰器：将一个实例方法变成类方法
    def hello(cls):
        print('这是一个类方法')
    @staticmethod #装饰器：将一个实例方法变成静态方法
    def nihao(): #像一个没有参数的函数
        print('这是一个静态方法')

tt2=tt()
#tt2.__w   #私有方法不能在外部用

tt.hello()
#类方法的参数是cls
#cls    self  都指向对象本身
# cls作为参数的方法都可以通过 类名.方法访问

tt.nihao()
tt2.nihao()
#静态方法可以通过  类名.静态方法名  和  对象.静态方法名  来访问

#################################################################################
#继承

#创建A类
class A(object):
    #类属性
    name='abc'
    age=18
    def __init__(self,a):
        self.a=a
    def c(self):
        print('这是A类的实例方法a')
#创建B类
class B(A):
    def d(self):
        print(f'父类的类属性有name{self.name},age{self.age}')
        #在B类里直接使用A类的方法
        self.c()
#子类拥有父类的全部属性以及方法
#创建一个对象
b=B('hello')
print(b.name)
print(b.a)
b.c()
b.d()

#匿名函数
def a(x):
    print(x+1)
a(2)
f=lambda x:x+1
print(f(2))


d=lambda  a,b:a-b
print(d(5,3))

print('-----------------------------分割---------------------------')
#多态

class c(object):
    def foo(self):
        print('c的实例方法')
class d(c):
    def foo(self):
        print('d的实例方法')

    # super ()类
    def k(self):
        super().foo()
d1=d()
d1.foo()

d2=d()
d2.k()
    #super ()类

##  狗类
class aa(object):
    goutui = '有4条腿'
    t=True
    def __init__(self,maose,pinzhong,shengao,tizhong):
        self.maose=maose
        self.pinzhong=pinzhong
        self.shengao=shengao
        self.tizhong=tizhong
    def a1(self):
        print(f'狗的种类是：{self.pinzhong} \n{self.pinzhong}它{self.goutui}  '
              f'{self.pinzhong}颜色为{self.maose}  \n{self.pinzhong}身高有{self.shengao}  '
              f'{self.pinzhong}体重有{self.tizhong}')
    def a2(self):
        if self.t:
            print(f'如果{self.pinzhong}它饿了会吃')
    def a3(self):

        if self.t:
            print(f'如果{self.pinzhong}遇到了生人会叫')
    def a4(self):
        if self.t:
            print(f'{self.pinzhong}渴了会喝水水')
    def a5(self):
        if self.t:
            print(f'{self.pinzhong}挨打了会逃跑')
bb=aa('黑色','藏獒','120cm','60kg')
bb.a1()
bb.a2()
bb.a3()
bb.a4()
bb.a5()








































































































































































