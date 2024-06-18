#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## 加判断

# 对于其它类型，当对象为空或者为 None 时，Python 会把它们当做“假”，其它情况当做真。比如，下面的表达式都是不成立的：
# ""   # 空字符串
# []   # 空列表
# ()   # 空元组
# {}   # 空字典
# None # 空值

# Python 是以缩进来标记代码块的，代码块一定要有缩进，没有缩进的不是代码块。另外，同一个代码块的缩进量要相同，缩进量不同的不属于同一个代码块。

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

# input函数表示命令行输入
proof = int( input("输入驾驶员每 100ml 血液酒精的含量：") )
if proof < 20:
    print("驾驶员不构成酒驾")
else:
    if proof < 80:
        print("驾驶员已构成酒驾")
    else:
        print("驾驶员已构成醉驾")

# Python assert 语句，又称断言语句，可以看做是功能缩小版的 if 语句，它用于判断某个表达式的值，如果值为真，则程序可以继续往下执行；反之，Python 解释器会报 AssertionError 错误。
# 有读者可能会问，明明 assert 会令程序崩溃，为什么还要使用它呢？这是因为，与其让程序在晚些时候崩溃，不如在错误条件出现时，就直接让程序崩溃，这有利于我们对程序排错，提高程序的健壮性。
mathmark = int( input() )
# 断言数学考试分数是否位于正常范围内
# assert 0 <= mathmark <= 100 # 允许这个写法
assert mathmark >= 0 and mathmark <= 100
# 只有当 mathmark 位于 [0, 100] 范围内，程序才会继续执行
print("数学考试分数为：", mathmark)

########## 加循环

# 一定要保证循环条件有变成假的时候，否则这个循环将成为一个死循环。所谓死循环，指的是无法结束循环的循环结构，

# 循环的初始化条件
num = 0
# 当 num 小于100时，会一直执行循环体
while num < 100 :
    print("num =", num)
    # 迭代语句
    num += 1
print("循环结束!")

my_char = "http://c.biancheng.net/python/"
i = 0;
while i < len(my_char):
    print(my_char[i], end = "+")
    i = i + 1
print()

add = "http://c.biancheng.net/python/"
# for循环，遍历 add 字符串
for ch in add:
    print(ch, end = "+")
print()

print("计算 1+2+...+100 的结果为：")
# 保存累加结果的变量
result = 0
# 逐个获取从 1 到 100 这些值，并做累加操作
for i in range(101): # range(101) 等价与 range(0, 101)
    result += i
print(result)
print(range(0, 101)) # range(0, 101)
# 上面代码中，使用了 range() 函数，此函数是 Python 内置函数，用于生成一系列连续整数，多用于 for 循环中。

my_list = [1, 2, 3, 4, 5]
for ele in my_list:
    print('ele =', ele)

my_dic = {'python教程': "http://c.biancheng.net/python/", # 表达式中有不必要的反斜杠
          'shell教程': "http://c.biancheng.net/shell/",
          'java教程': "http://c.biancheng.net/java/"}
for ele in my_dic: # 因此，直接遍历字典，和遍历字典 keys() 方法的返回值是相同的。
    print('ele =', ele)
for ele in my_dic.keys():
    print('ele =', ele)
for ele in my_dic.items():
    print('ele =', ele)
for ele in my_dic.values():
    print('ele =', ele)
