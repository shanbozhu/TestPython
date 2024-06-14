#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## String

s1 = 'I\'m a great coder!'
print(s1)

s2 = 'It took me six months to write this Python tutorial. \
Please give me more support. \
I will keep it updated.'
print(s2)

s2 = '''It took me six months to write this Python tutorial.
Please give me more support.
I will keep it updated.'''
print(s2)

rstr = r'D:\Program Files\Python 3.8\python.exe'
print(rstr)
rstr = r'D:\Program Files\Python 3.8\python.exe' '\\'
print(rstr)

## print()

user_name = 'Charlie'
user_age = 8
print("读者名:", user_name, "年龄:", user_age)
print("读者名:", user_name, "年龄:", user_age, sep='|')

print(40, end="")
print(50, end="")
print(60)

f = open("print.txt", "w")
print('沧海月明珠有泪', file=f)
print('蓝田日暖玉生烟', file=f)
f.close()

age = 8
print("C语言中文网已经%d岁了!", age)
print("C语言中文网已经%d岁了!" % age)

name = "C语言中文网"
age = 8
url = "http://c.biancheng.net/"
print("%s已经%d岁了，它的网址是%s。" % (name, age, url))

str1 = "Oct: \061\062\063"
str2 = "Hex: \x31\x32\x33\x78\x79\x7A"
print(str1)
print(str2)

## 类型转换

height = 70.0
print("您的身高" + str(height))

## 运算符

# 整数不能除尽
print("23/5 =", 23/5)
print("23//5 =", 23//5) # 整除
print("23.0//5 =", 23.0//5)

# 整数能除尽
print("25/5 =", 25/5)
print("25//5 =", 25//5)
print("25.0//5 =", 25.0//5)

# 次方（乘方）运算
print('----次方运算----')
print('3**4 =', 3**4)
print('2**5 =', 2**5)
print('----开方运算----')
print('81**(1/4) =', 81**(1/4))
print('32**(1/5) =', 32**(1/5))

import time # 引入time模块
t1 = time.gmtime() # gmtime()用来获取当前时间
t2 =  time.gmtime()
print(t1 == t2) # 输出True
print(t1 is t2) # 输出False
print(t1 is not t2) # 输出True