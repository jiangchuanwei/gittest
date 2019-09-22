#!/usr/bin/python
#-*-coding:utf-8-*-
f = open(file='ccc.txt', encoding='utf-8')
a = f.read()

b = a.split('),')

cc = []
for i in range(len(b)):
    b1 = b[i].split('(')
    c = b1[1].replace(');', '').split(',')
    cc.append(c)
import xlwt

v = xlwt.Workbook()
biao1 = v.add_sheet('表2')
for i in range(len(cc)):
    for j in range(len(cc[i])):
        biao1.write(i, j, cc[i][j])
v.save('qqe.xls')
'''
'''


class shuju(object):
    f = open(file='ccc.txt', encoding='utf-8')
    a = f.read()

    b = []
    b.append(a)

    def lianjie(self):
        import pymysql
        d = pymysql.connect(host='192.168.10.52', port=3306, user='root', password='123456', charset='utf8')
        e = d.cursor()
        sql = 'use zhisheng'
        e.execute(sql)
        # sql2='create table biao8(id int,name text,zhiye text,wangzhi text,leixing text,zhuangtai text,renyuan text,diqu text,jingyan text,xueli text)'
        # e.execute(sql2)
        # sql3=f"insert into biao8 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s),self.a"
        e.executemany('insert into biao8 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', self.b)

        # e.execute(sql3)
        d.commit()
        # for i in range(len(self.a)):
        # print(i)
        # for j in range(len(self.a[i])):
        # print(j)
        # sql3=f"insert into biao8 values({self.a[i][j]},{self.a[i][j+1]},{self.a[i][j+2]},{self.a[i][j+3]},{self.a[i][j+4]},{self.a[i][j+5]},{self.a[i][j+6]},{self.a[i][j+7]},{self.a[i][j+8]},{self.a[i][j+9]})"
        # e.execute(sql3)
        # d.commit()


v = shuju()
v.lianjie()
'''



# f = open(file='ccc.txt', encoding='utf-8')
# c=[]
# a = f.read()
# for i in a:
#     b=i.replace(';','').replace(')','').replace('(','')
#     print(b)
# import pymysql
# d = pymysql.connect(host='192.168.10.52', port=3306, user='root', password='123456', charset='utf8')
# e = d.cursor()
# sql = 'use zhisheng'
# e.execute(sql)
# sql2 = 'create table biao8(id int,name text,zhiye text,wangzhi text,leixing text,zhuangtai text,renyuan text,diqu text,jingyan text,xueli text)'
# e.execute(sql2)
# for i in c:
#     sql3 = f"insert into biao8 value{i}"
#     e.execute(sql3)
# d.commit()

# e=[]
# a=open(file='ccc.txt',encoding='utf-8')
# b=a.readlines()
# for i in b:
#     c=i.replace('\n','').replace("'",'').replace('(','').replace("'",'').replace(';','')#.split('),')
#     d=c.split('),')
#     print(d)

f=open(file='ccc.txt',encoding='utf-8')
a=f.read()
b=a.split('),')
cc=[]
for i in range(len(b)):
        b1=b[i].split('(')
        c=b1[1].replace(');','').replace('\n','').replace("'",'').split(',')
        cc.append(tuple(c))
import pymysql
d = pymysql.connect(host='192.168.10.52', port=3306, user='root', password='123456', charset='utf8')
e = d.cursor()
sql = 'use zhisheng'
e.execute(sql)
sql2 = 'create table biao13(id varchar(30),mingzi varchar(30),zhiye varchar(30),wangzhi varchar(30),leixing varchar(30),zhuangtai varchar(30),renyuan varchar(30),diqu varchar(30),jingyan varchar(30),xueli varchar(30))'
e.execute(sql2)
for j in cc:
    sql3 = f"insert into biao13 value {j}"
    e.execute(sql3)
d.commit()