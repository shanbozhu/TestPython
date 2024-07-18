#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## str

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

# r原生字符串，自带转义
rs = r'D:\Program Files\Python 3.8\python.exe'
print(rs)
rs = r'D:\Program Files\Python 3.8\python.exe' '\\'
print(rs)

########## print()

user_name = 'Charlie'
user_age = 8
print("读者名:", user_name, "年龄:", user_age)
print("读者名:", user_name, "年龄:", user_age, sep = '|')

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

s1 = "Oct: \061\062\063"
s2 = "Hex: \x31\x32\x33\x78\x79\x7A"
print(s1)
print(s2)

# 1、使用 f-string（Python 3.6 及以上版本）：
count = 10  # 示例变量
print(f"被裁剪的描述表一共有：{count}个")

# 2、使用 format 方法：
count = 10  # 示例变量
print("被裁剪的描述表一共有：{}个".format(count))

# 3、使用字符串连接：
count = 10  # 示例变量
print("被裁剪的描述表一共有：" + str(count) + "个")

# 4、使用 % 操作符：
count = 10  # 示例变量
print("被裁剪的描述表一共有：%d个" % count)

# 5、直接输出
count = 10
print("被裁剪的描述表一共有：", count, "个", sep="")

########## 类型转换

height = 70.0
print("您的身高" + str(height))

########## 运算符

# 整数不能除尽
print("23 / 5 =", 23 / 5)
print("23 // 5 =", 23 // 5) # 整除
print("23.0 // 5 =", 23.0 // 5)

# 整数能除尽
print("25 / 5 =", 25 / 5)
print("25 // 5 =", 25 // 5)
print("25.0 // 5 =", 25.0 // 5)

# 次方（乘方）运算
print('----次方运算----')
print('3 ** 4 =', 3 ** 4)
print('2 ** 5 =', 2 ** 5)
print('----开方运算----')
print('81 ** (1/4) =', 81 ** (1/4))
print('32 ** (1/5) =', 32 ** (1/5))

import time # 引入time模块
t1 = time.gmtime() # gmtime()用来获取当前时间
t2 = time.gmtime()
print(t1 == t2) # 输出True
print(t1 is t2) # 输出False
print(t1 is not t2) # 输出True

age = 20
height = 175
if age >= 18 and age <= 30 and height >= 170 and height <= 185:
    print("恭喜，你符合报考飞行员的条件")
else:
    print("抱歉，你不符合报考飞行员的条件")

# 在 Python 中，and 和 or 不一定会计算右边表达式的值，有时候只计算左边表达式的值就能得到最终结果。
# 另外，and 和 or 运算符会将其中一个表达式的 值 作为最终结果，而不是将 True 或者 False 作为最终结果。
# 该"其中一个表达式"决定了逻辑运算的最终结果，遵守 逻辑运算短路特性
print(100 and 200) # 200
print(45 and 0) # 0
print("" or "http://c.biancheng.net/python/") # http://c.biancheng.net/python/
print(18.5 or "http://c.biancheng.net/python/") # 18.5

a = 10
b = 5
if a > b:
    max = a
else:
    max = b
print(max)

# 这是一种类似于其它编程语言中三目运算符 ?: 的写法。Python 是一种极简主义的编程语言，它没有引入 ?: 这个新的运算符，而是使用已有的 if else 关键字来实现相同的功能。
a = 20
b = 10
max = a if a > b else b
print(max)