#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 序列

########## str

# 在 Python 中，序列类型包括字符串、列表、元组、集合和字典，这些序列支持以下几种通用的操作，但比较特殊的是，集合和字典不支持索引、切片、相加和相乘操作。
s = "C语言中文网"
print(s[0], "==", s[-6])
print(s[5], "==", s[-1])

# sname[start : end : step]
s = "C语言中文网"
# 取索引区间为 [0, 2) 之间的字符串
print(s[:2])
# 隔1个字符取一个字符，区间是整个字符串
print(s[::2])
# 取整个字符串，此时 [] 中只需一个冒号即可
print(s[:])

s = "c.biancheng.net"
print("C语言" + "中文网:" + s)

s = "C语言中文网"
print(s * 3)

s = "c.biancheng.net"
print('c' in s)
print('c' not in s)
# 找出最大的字符
print(max(s))
# 找出最小的字符
print(min(s))
# 对字符串中的元素进行排序
print(sorted(s))

########## list

num = [1, 2, 3, 4, 5, 6, 7]
name = ["C语言中文网", "http://c.biancheng.net"]
program = ["C语言", "Python", "Java"]
print(num, name, program)

# 将字符串转换成列表
list1 = list("hello")
print(list1)

# 将元组转换成列表
tuple1 = ('Python', 'Java', 'C++', 'JavaScript')
list2 = list(tuple1)
print(list2)

# 将字典转换成列表
dict1 = {'a' : 100, 'b' : 42, 'c' : 9}
list3 = list(dict1)
print(list3) # ['a', 'b', 'c']

# 将区间转换成列表
range1 = range(1, 6)
list4 = list(range1)
print(list4) # [1, 2, 3, 4, 5]
print(list4[3])
print(list4[-4])

intlist = [1, 45, 8, 34]
print(intlist)
del intlist

language = ["Python", "C++", "Java"]
birthday = [1991, 1998, 1995]
info = language + birthday
print("language =", language)
print("birthday =", birthday)
print("info =", info)

l = ['Python', 'C++', 'Java']
# 追加元素
l.append('PHP')
print(l)
# 追加元组，整个元组被当成一个元素
t = ('JavaScript', 'C#', 'Go')
l.append(t)
print(l)

l = ['Python', 'C++', 'Java']
# 追加元素
l.extend('C')
print(l)

# 追加元组，元祖被拆分成多个元素
t = ('JavaScript', 'C#', 'Go')
l.extend(t)
print(l)

l = ['Python', 'C++', 'Java']
# 插入元素
l.insert(1, 'C')
print(l)

# 插入元组，整个元祖被当成一个元素
t = ('C#', 'Go')
l.insert(2, t)
print(l)

lang = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
# 使用正数索引
del lang[2]
print(lang)
lang = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
del lang[1 : 4]
print(lang)

nums = [40, 36, 89, 2, 36, 100, 7]
nums.pop(3)
print(nums)
nums.pop()
print(nums)

nums = [40, 36, 89, 2, 36, 100, 7]
# 第一次删除36
nums.remove(36)
print(nums)
# 第二次删除36
nums.remove(36)
print(nums)

url = list("http://c.biancheng.net/python/")
print(url)
url.clear()
print(url)

nums = [40, 36, 89, 2, 36, 100, 7]
nums[2] = -26  # 使用正数索引
nums[-3] = -66.2  # 使用负数索引
print(nums)

# Python 支持通过切片语法给一组元素赋值。在进行这种操作时，如果不指定步长（step 参数），Python 就不要求新赋值的元素个数与原来的元素个数相同；这意味，该操作既可以为列表添加元素，也可以为列表删除元素。
nums = [40, 36, 89, 2, 36, 100, 7]
# 修改第 1~4 个元素的值（不包括第4个元素）
nums[1: 4] = [45.25, -77, -52.5]
print(nums)

# 如果对空切片（slice）赋值，就相当于插入一组新的元素：
nums = [40, 36, 89, 2, 36, 100, 7]
# 在4个位置插入元素; 4 =< x < 4
nums[4: 4] = [-77, -52.5, 999]
print(nums) # [40, 36, 89, 2, -77, -52.5, 999, 36, 100, 7]

s = list("Hello")
s[2: 4] = "XYZ"
print(s)

nums = [40, 36, 89, 2, 36, 100, 7]
# 步长为2，为第1、3、5个元素赋值
nums[1: 6: 2] = [0.025, -99, 20.5]
print(nums)

nums = [40, 36, 89, 2, 36, 100, 7, -20.5, -999]
# 检索列表中的所有元素
print( nums.index(2) )
# 检索3~7之间的元素
print( nums.index(7, 3, 7) )

nums = [40, 36, 89, 2, 36, 100, 7, -20.5, 36]
# 统计元素出现的次数
print("36出现了%d次" % nums.count(36))
# 判断一个元素是否存在
if nums.count(100):
    print("列表中存在100这个元素")
else:
    print("列表中不存在100这个元素")