#!/usr/bin/python
#-*-coding:utf-8-*-

class BOOK(object):
    books=[['三国','罗贯中','1','A区'],
           ['西游记','吴承恩','1','B区'],
           ['水浒传','施耐庵','1','C区']]
    def __init__(self,name,zuozhe,zhuangtai,weizhi):
        self.name=name
        self.zuozhe=zuozhe
        self.zhuangtai=zhuangtai
        self.weizhi=weizhi
    #展示图书
    def zhanshi(self):
        for i,j in enumerate(self.books):
            print(f'{i}{j[0]}{j[1]}{j[2]}{j[3]}')
    def add(self):
        print('dsaasd')
        self.books.append([self.name,self.zuozhe,self.zhuangtai,self.weizhi])
        self.zhanshi()
        print('dsfsfg')
    def jiechu(self):
        bianhao=int(input('输入编号'))
        if bianhao in range(len(self.books)):
            if self.books[bianhao][2]=='1':
                print('书可以借出')
                self.books[bianhao][2]='0'
            else:
                print('书已被借出')
        else:
            print('不存在此书')
    def huanshu(self):
        shuming=input('输入书名')
        for i in self.books:
            for shuming  in i[0]:
                i[2]='1'
                print('归还成功')
    def pao(self):
        while True:
            self.zhanshi()
            print('选择功能')
            print('1:添加')
            print('2:借出')
            print('3:归还')
            print('4:退出')
            shuzi=int(input("数字"))
            if shuzi==1:
                print('sasd')
                self.add()
                print('fadfa')
            elif shuzi==2:
                self.jiechu()
            elif shuzi==3:
                self.huanshu()
            elif shuzi==4:
                print('下次')
                break
            else:
                print('输入正确')

b1=BOOK('红楼梦','罗贯中','1','A区')
b1.pao()
































'''
        def xiugai(x):
            id = int(input("输入id："))
            name = str(input("输入name:"))
            for i in range(0, len(shuku)):
                if shuku[i].name == x:
                    shuku[i].id = id
                    shuku[i].name = name
'''



