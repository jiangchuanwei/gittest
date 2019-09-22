#!/usr/bin/python
#-*-coding:utf-8-*-
#python正则表达式 re 正则模块 【只能操作字符串】
import re
# 1  【 .】 在python里表示除了换行符以外任意一个字符
s='11112333456'

# re.search(参数一，参数二):搜索
# 参数一：已经编辑好的正则表达式
# 参数二：要匹配的字符串
#写正则的步骤：
#第一步：编译正则表达式 r1=re.compile(r'.') 编译的过程， r1代表编译完成的正则表达式
# r1=re.compile(r'.')
#第二步：执行正则表达式
# print(re.search(r1,s))

# 2 【*】匹配*前面的字符0次或多次
# r2=re.compile(r'123*')
# print(re.search(r2,s))

# 3 【+】匹配+前面的字符一次或者多次
# r3=re.compile(r'1+')
# print(re.search(r3,s))

# 4 【?】匹配?前面的字符0次或者1次
r4=re.compile(r'23?')
print(re.search(r4,s))

# 5 【$】以某个字符结尾
# r5=re.compile(r'6$')
# print(re.search(r5,s))

# 6 【^】以某个字符开头
# r6=re.compile(r'^1')
# print(re.search(r6,s))

# 7 【{m}】匹配{}前面的字符m次
# r7=re.compile(r'1{3}')
# print(re.search(r7,s))

# 8 【{m,n}】匹配{}前面的字符m到n次  最少m次 最多n次
# r8=re.compile(r'1{3,5}')
# print(re.search(r8,s))

# 9 【[abc]】匹配[]里的任意一个字符
# r9=re.compile(r'1[235]')
# print(re.search(r9,s))


# \d 代表0-9
# \D 代表除了0-9以外的任意字符
# \s 代表空白字符  Unicode编码的空白字符 \t \n \r \v
# \S 代表除了空白字符以外任意一个字符

#贪婪模式：尽可能匹配多的字符 不存在?

#非贪婪模式：匹配到符合规则的就停止 存在?
#sub(参数1，参数2，参数3) 替换的意思
#参数1指的是正则 参数2指的是新的字符  参数3指的是被更改的字符串
#group() 组 ：作用将匹配到的内容拿出来
#groups() 多个分组
# url='http://www.baidu.com'
# r11=re.compile(r'\.(.*?)\.')
# cc=re.search(r11,url).group()
# cc1=re.sub(r'\.','',cc)
# print(cc1)

# re.findall(r11,url) 返回的列表 每个元素都是字符串  搜索符合规则的全部结果
# url='http://www.baidu.comhttp://www.jd.com'
# r11=re.compile(r'\.(.*?)\.')
# cc=re.findall(r11,url)
# print(cc)




#过滤手机号
# a='1783921092717939210928'
# b1=re.compile('(178)[0-9]{8}|(179)][0-9]{8}')
#match和search的区别  match 一旦匹配不到，立即结束匹配
# search 匹配不到继续匹配，直到匹配成功第一次或者字符串结束为止
# 共同点：匹配成功第一次之后就停止 如果后面还有符合的不输出
# print(re.search(b1,a))
# print(re.match(b1,a))

# \d 代表0-9
# \D 代表除了0-9以外的任意字符


























