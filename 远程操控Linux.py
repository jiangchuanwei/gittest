#!/usr/bin/python
#-*-coding:utf-8-*-
import paramiko
# paramiko用于远程连接Linux系统

#面向过程  ssh协议进行连接  可以执行Linux里的命令

#创造一个ssh客户端
# c=paramiko.SSHClient()

#信任远程Linux主机
# c.set_missing_host_key_policy(paramiko.AutoAddPolicy)#自动添加信任密文

#通过客户端连接远程Linux主机
# c.connect(
#     hostname='192.168.10.78',
#     port=22,
#     username='root',
#     password='123456'
# )

#执行Linux命令 exec_command('命令')
#stdin 指的是输入的命令    stdout 输出的结果    stderr 错误信息
# stdin,stdout,stderr = c.exec_command('cat 123')
#read() 读取  decode()把xxx编译成xxx
# print(stdout.read().decode())


#文件下载与上传 Transport()类似于htp服务器    参数包含ip地址 端口号的元组
# f=paramiko.Transport(('192.168.10.78',22))

#建立与远程Linux的连接
# f.connect(username='root',password='123456')

#创建类似于ftp的客户端
# s = paramiko.SFTPClient.from_transport(f)

#下载远程文件 get(参数1，参数2)
#参数1代表远程文件  参数2代表本地文件
# x1='/opt/a.txt'
# x2=r'D:\PycharmProjects\untitled\DAR\38.txt'
# s.get(x1,x2)

#上传
# x1='/opt/997.txt'
# x2=r'D:\PycharmProjects\untitled\DAR\38.txt'
# s.put(x2,x1)

#断开连接
# f.close()



class lianjie(object):

    def __init__(self,wangzhi,duankou,yonghu,mima):
        self.wangzhi=wangzhi
        self.duankou=duankou
        self.yonghu=yonghu
        self.mima=mima
    def mingling(self):
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        c.connect(
            hostname=self.wangzhi,
            port=self.duankou,
            username=self.yonghu,
            password=self.mima
        )
        stdin, stdout, stderr = c.exec_command(input('输入命令'))
        print(stdout.read().decode())
    def wenjian(self):
        f = paramiko.Transport((self.wangzhi,self.duankou))
        f.connect(username=self.yonghu, password=self.mima)
        s = paramiko.SFTPClient.from_transport(f)
        c=int(input('下载输入1，上传输入2'))

        if c == 1:
            x1 = input('输入远程文件路径')
            x2 = input(r'输入本地路径')
            s.get(x1,x2)
            f.close()
        elif c == 2:
            x3 = input(r'输入本地路径')
            x4 = input('输入远程文件路径')
            s.put(x3,x4)
            f.close()
        else:
            print('错误')

    def pao(self):
        while 1:
            cc=input('***输入功能***\n  【操作命令输入x】\n  【上传下载输入y】\n  【退出输入t】')
            if cc=='x':
                self.mingling()
            elif cc=='y':
                self.wenjian()
            elif cc=='t':
                print('已退出')
                break
            else:
                print('请重新输入>>>>>>\n                  ')
r=lianjie('192.168.10.78',22,'root','123456')
r.pao()

























