#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## 加判断

# 对于其它类型，当对象为空或者为 None 时，Python 会把它们当做“假”，其它情况当做真。比如，下面的表达式都是不成立的：
# ""   # 空字符串
# []   # 空列表
# ()   # 空元组
# {}   # 空字典
# None # 空值

b = False
if b:
    print('b是True')
else:
    print('b是False')

n = 0
if n:
    print('n不是零值')
else:
    print('n是零值')

s = ""
if s:
    print('s不是空字符串')
else:
    print('s是空字符串')

l = []
if l:
    print('l不是空列表')
else:
    print('l是空列表')

d = {}
if d:
    print('d不是空字典')
else:
    print('d是空字典')

def func():
    print("函数被调用")

if func():
    print('func()返回值不是空')
else:
    print('func()返回值为空')
