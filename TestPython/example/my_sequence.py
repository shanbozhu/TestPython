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

########## tuple

# 从形式上看，元组的所有元素都放在一对小括号( )中，相邻元素之间用逗号,分隔
# 在 Python 中，元组通常都是使用一对小括号将所有元素包围起来的，但小括号可省略，只要将各元素用逗号隔开，Python 就会将其视为元组
# 元组也可以看做是不可变的列表，通常情况下，元组用于保存无需修改的内容。

num = 7, 14, 21, 28, 35
abc = ( "Python", 19, [1, 2], ('c', 2.0) )
print(num)
print(abc)

# 最后加上逗号
a = ("http://c.biancheng.net/cplus/",)
print(type(a))
print(a)

# 最后不加逗号
b = ("http://c.biancheng.net/socket/")
print(type(b))
print(b)

# 将字符串转换成元组
tup1 = tuple("hello")
print(tup1)

# 将列表转换成元组
list1 = ['Python', 'Java', 'C++', 'JavaScript']
tup2 = tuple(list1)
print(tup2)

#将字典转换成元组
dict1 = {'a':100, 'b':42, 'c':9}
tup3 = tuple(dict1)
print(tup3)

#将区间转换成元组
range1 = range(1, 6)
tup4 = tuple(range1)
print(tup4)

url = tuple("http://c.biancheng.net/shell/")
# 使用索引访问元组中的某个元素
print(url[3])  # 使用正数索引
print(url[-4])  # 使用负数索引
# 使用切片访问元组中的一组元素
print(url[9: 18])  # 使用正数切片
print(url[9: 18: 3])  # 指定步长
print(url[-6: -1])  # 使用负数切片

tup = (100, 0.5, -36, 73)
print(tup)
# 对元组进行重新赋值
tup = ('Shell脚本', "http://c.biancheng.net/shell/")
print(tup)

tup1 = (100, 0.5, -36, 73)
tup2 = (3+12j, -54.6, 99)
print(tup1 + tup2)
print(tup1) # 你看，使用+拼接元组以后，tup1 和 tup2 的内容没发生改变，这说明生成的是一个新的元组。
print(tup2)

tup = ('Java教程', "http://c.biancheng.net/java/")
print(tup)
del tup # Python 自带垃圾回收功能，会自动销毁不用的元组，所以一般不需要通过 del 来手动删除。

########## dict

a = {'one': 1, 'two': 2, 'three': 3}  # a是一个字典类型
print(type(a))

# 使用字符串作为key
scores = {'数学': 95, '英语': 92, '语文': 84}
print(scores)

# 使用元组和数字作为key
dict1 = {(20, 30): 'great', 30: [1,2,3]}
print(dict1)

knowledge = ['语文', '数学', '英语']
scores = dict.fromkeys(knowledge, 60)
print(scores)

# a = dict(str1=value1, str2=value2, str3=value3)
# str 表示字符串类型的键，value 表示键对应的值。使用此方式创建字典时，字符串不能带引号。
a = dict(two=2, one=1, three=3)
print(a)

# 方式1
demo = [('two',2), ('one',1), ('three',3)]
print(dict(demo))
#方式2
demo = [['two',2], ['one',1], ['three',3]]
print(dict(demo))
#方式3
demo = (('two',2), ('one',1), ('three',3))
print(dict(demo))
#方式4
demo = (['two',2], ['one',1], ['three',3])
print(dict(demo))

keys = ['one', 'two', 'three'] # 还可以是字符串或元组
values = [1, 2, 3] # 还可以是字符串或元组
print(dict( zip(keys, values) ))

tup = (['two',26], ['one',88], ['three',100], ['four',-59])
dic = dict(tup)
print(dic['one'])  # 键存在

a = dict(two=0.65, one=88, three=100, four=-59)
print( a.get('one') ) # 键存在
print( a.get('five') ) # 键不存在 return None

a = dict(two=0.65, one=88, three=100, four=-59)
print(a)
del a

a = {'数学': 95}
print(a)
# 添加新键值对
a['语文'] = 89
print(a)
# 再次添加新键值对
a['英语'] = 90
print(a)

a = {'数学': 95, '语文': 89, '英语': 90}
print(a)
a['语文'] = 100
print(a)

# 使用del语句删除键值对
a = {'数学': 95, '语文': 89, '英语': 90}
del a['语文']
del a['数学']
print(a)

a = {'数学': 95, '语文': 89, '英语': 90}
# 判断 a 中是否包含名为'数学'的key
print('数学' in a) # True
# 判断 a 是否包含名为'物理'的key
print('物理' in a) # False

# 我们知道，Python 字典的数据类型为 dict，我们可使用 dir(dict) 来查看该类型包含哪些方法，例如：
print(dir(dict))

scores = {'数学': 95, '语文': 89, '英语': 90}
print(scores.keys())
print(scores.values())
print(scores.items()) # 可以发现，keys()、values() 和 items() 返回值的类型分别为 dict_keys、dict_values 和 dict_items。但在 Python 3.x 中，它们的返回值并不是我们常见的列表或者元组类型，因为 Python 3.x 不希望用户直接操作这几个方法的返回值。

a = {'数学': 95, '语文': 89, '英语': 90}
b = list(a.keys())
print(b)

a = {'数学': 95, '语文': 89, '英语': 90}
for k in a.keys():
    print(k, end=' ')
print("\n---------------")
for v in a.values():
    print(v, end=' ')
print("\n---------------")
for k,v in a.items():
    print("key:", k, " value:", v)

# 深拷贝只会拷贝一层，与OC一样
a = {'one': 1, 'two': 2, 'three': [1,2,3]}
b = a.copy()
# 向 a 中添加新键值对，由于b已经提前将 a 所有键值对都深拷贝过来，因此 a 添加新键值对，不会影响 b。
a['four'] = 100
print(a)
print(b)
# 由于 b 和 a 共享[1,2,3]（浅拷贝），因此移除 a 中列表中的元素，也会影响 b。
a['three'].remove(1)
print(a)
print(b)
del b["one"]
print(a)
print(b)

a = {'one': 1, 'two': 2, 'three': 3}
a.update({'one':4.5, 'four': 9.3})
print(a)

# pop() 用来删除指定的键值对，而 popitem() 用来随机删除一个键值对
a = {'数学': 95, '语文': 89, '英语': 90, '化学': 83, '生物': 98, '物理': 89}
print(a)
a.pop('化学')
print(a)
a.popitem()
print(a)

a = {'数学': 95, '语文': 89, '英语': 90}
print(a)
# key不存在，指定默认值
a.setdefault('物理', 94)
print(a)
# key不存在，不指定默认值
a.setdefault('化学')
print(a)
# key存在，指定默认值
a.setdefault('数学', 100)
print(a)

########## set

# 从形式上看，和字典类似，Python 集合会将所有元素放在一对大括号 {} 中，相邻元素之间用“,”分隔
# 从内容上看，同一集合中，只能存储不可变的数据类型，包括整形、浮点型、字符串、元组，无法存储列表、字典、集合这些可变的数据类型，否则 Python 解释器会抛出 TypeError 错误

a = {1, 2, 1, (1, 2, 3), 'c', 'c'}
print(a) # 去重

set1 = set("c.biancheng.net")
set2 = set([1,2,3,4,5,5])
set3 = set((1,2,3,4,5))
print("set1:", set1)
print("set2:", set2)
print("set3:", set3)

a = {1, 'c', 1, (1, 2, 3), 'c'}
for ele in a:
    print(ele)

a = {1, 2, 3}
a.add((1, 2))
print(a)

a = {1,2,3}
a.remove(1)
print(a)

a = {1,2,3}
a.remove(1)
print(a)
a.discard(1)
print(a)

# 需要注意的是，set 集合本身的元素必须是不可变的， 所以 set 的元素不能是 set，只能是 frozenset。向 set 中添加 frozenset 是没问题的，因为 frozenset 是不可变的。
s = {'Python', 'C', 'C++'}
fs = frozenset(['Java', 'Shell'])
s_sub = {'PHP', 'C#'}
# 向set集合中添加frozenset
s.add(fs)
print('s =', s)