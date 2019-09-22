#!/usr/bin/python
#-*-coding:utf-8-*-

# 异常
# 1.python 语法错误，缩进、缺少class
# 2.代码逻辑错误

# 处理异常 try...except  ：处理python代码中可能会出现的错误
# 格式
# try:
#     代码块1
# except：
#     代码块2
# 当try语句没有错误是不执行except语句，当try存在错误时执行except

# except 后面可以指定异常的类型
# except <名字>：          #发生异常时的操作。名字为对应错误的名称
#     <语句>



# try   except  finally
# try 语句存在错误  except finally 语句都被执行
# try 语句不管错误还是正确 finally语句都会被执行

# try:
#     a=1/10
# except:
#     print('try语句错误')
# finally:
#     print('hello')

# try except else
# try 存在错误时 except语句执行  else语句不执行

try:
    a=1/0
except:
    print('错误')
else:
    print('hello')








