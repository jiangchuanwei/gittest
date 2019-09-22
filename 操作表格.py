#!/usr/bin/python
#-*-coding:utf-8-*-

'''
import xlrd
#操作Excel的xlrd读取Excel文件   xlwt写入数据到Excel文件
#打开Excel
d=xlrd.open_workbook(filename='清晨.xlsx')
#选中一个字表
#第1种
t=d.sheets()[0]#下标
print(t)
#第2种
t1=d.sheet_by_index(0)
print(t1)
#第三步，获取数据
a=t.row_values(0)#获取整行数据
print(a)
#获取某个单元格
#row（）  获取一行
#再通过列表的索引值获取元素         .value 获取到具体的值
print(t.row(0)[0].value)
#获取一列col()   返回一个列表
print(t.col(0)[0].value)
#通过行列索引获取具体单元格的值
print(t.cell(0,2).value)

#获取行数列数
#nrows获取行数  ncols获取列数
print(t.nrows)
print(t.ncols)

#如何获取所有行数据
for i in range(t.nrows):
    a1=t.row_values(i)
    print(a1)

#找出所有表格的名字
print(d.sheet_names())

import xlwt
a = [["序号", "名字", "年龄", "性别"],[1, "张三", 20, "男"],[2, "李四", 19, "男"],[3, "王五", 18, "女"],[4, "赵信", 16, "女"]]
#新建excel文件
v=xlwt.Workbook()

#新建Excel表
biao1=v.add_sheet('表一')

#写入数据到表中   一次写入一个单元格
#write(行号，列号，数据)
for i in range(len(a)):
    for j in range(len(a[i])):
        biao1.write(i,j,a[i][j])

#保存Excel文件
#save（文件名）
v.save('aaa.xls')
'''

'''
#定义类 1.打开不同的文件  2.读取任一行数据 3.按照读取指定单元格的数据，
# 4.按照列读取任一行数据    5.指定读取某个表的数据
class excel(object):
    def __init__(self,name,n):
        self.name=name#文件名
        self.n=n#表格
        self.d=xlrd.open_workbook(filename=self.name)
        #打开表
        self.d1=self.d.sheets()[self.n]
    def duqu(self):
        a=int(input('hanghao1'))
        # b=int(input('hanghao2'))
        if a>self.d1.nrows:
            print('cuo')
            return  None
        for i in range(a):
            print(self.d1.row_values(i))

    def duqu1(self):
        a = int(input('xanghao'))
        # b=int(input(''))
        if a > self.d1.ncols:
            print('cuo')
            return None
        for i in range(a):
            print(self.d1.col_values(i))
    def duqu2(self):
        a=int(input('hanghao'))
        b=int(input('lie'))
        print(self.d1.cell(a,b).value)

    def pao(self):
        while True:
            print(f'输入1打开文件\n输入2\n 输入3\n 4\n 5')
            rr = int(input('输入数字'))
            if rr == 1:
                self.duqu()
            if rr == 2:
                self.duqu1()
            if rr == 3:
                self.duqu2()
e=excel('清晨.xlsx',0)
e.pao()
'''





