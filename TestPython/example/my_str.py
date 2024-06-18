#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在 Python 中拼接（连接）字符串很简单，可以直接将两个字符串紧挨着写在一起，具体格式为：
strname = "str1" "str2"
print(strname)
strname = "str1"+"str2"
print(strname)

str1 = "Python教程" "http://c.biancheng.net/python/"
print(str1)
str2 = "Java" "Python" "C++" "PHP"
print(str2)

name = "C++教程"
url = "http://c.biancheng.net/cplus/"
info = name + "的网址是：" + url
print(info)

name = "C语言中文网"
age = 8
course = 30
info = name + "已经" + str(age) + "岁了，共发布了" + repr(course) + "套教程。"
print(info)

# str() 和 repr() 函数虽然都可以将数字转换成字符串，但它们之间是有区别的：
# str() 用于将数据转换成适合人类阅读的字符串形式。
# repr() 用于将数据转换成适合解释器阅读的字符串形式（Python 表达式的形式），适合在开发和调试阶段使用；如果没有等价的语法，则会发生 SyntaxError 异常。
s = "http://c.biancheng.net/shell/"
s_str = str(s)
s_repr = repr(s)
print( type(s_str) )
print(s_str)
print( type(s_repr) )
print(s_repr)

url = 'http://c.biancheng.net/python/'
# 获取索引为10的字符
print(url[10])
# 获取索引为 6 的字符
print(url[-6])

url = 'http://c.biancheng.net/java/'
# 获取索引从7处到22（不包含22）的子串
print(url[7: 22])
# 获取索引从7处到-6的子串
print(url[7: -6])
# 获取索引从-21到6的子串
print(url[-21: -6])
# 从索引3开始，每隔4个字符取出一个字符，直到索引22为止
print(url[3: 22: 4])

a = 'http://c.biancheng.net'
print(len(a))

# 在实际开发中，除了常常要获取字符串的长度外，有时还要获取字符串的字节数。
# 在 Python 中，不同的字符所占的字节数不同，数字、英文字母、小数点、下划线以及空格，各占一个字节，而一个汉字可能占 2~4 个字节，具体占多少个，取决于采用的编码方式。例如，汉字在 GBK/GB2312 编码中占用 2 个字节，而在 UTF-8 编码中一般占用 3 个字节。
# 我们可以通过使用 encode() 方法，将字符串进行编码后再获取它的字节数。例如，采用 UTF-8 编码方式，计算“人生苦短，我用Python”的字节数，可以执行如下代码：
str1 = "人生苦短，我用Python"
print(str1)
print(len(str1))
print(str1.encode())
print( len(str1.encode()) )

# 同理，如果要获取采用 GBK 编码的字符串的长度，可以执行如下代码：
str1 = "人生苦短，我用Python"
print( len(str1.encode('gbk')) )

str = "C语言中文网 >>> c.biancheng.net"
list1 = str.split() # 采用默认 空白字符 分隔符进行分割
print(list1)
list2 = str.split('>>>') # 采用多个字符进行分割
print(list2)
list3 = str.split('.')
print(list3)
list4 = str.split(' ',1) # 采用空格进行分割，并规定最多只能分割 1 次
print(list4) # ['C语言中文网', '>>> c.biancheng.net']
list5 = str.split('>') # 采用 > 字符进行分割
print(list5) # ['C语言中文网 ', '', '', ' c.biancheng.net']
str = "C语言中文网   >>>   c.biancheng.net"  # 包含 3 个连续的空格
list6 = str.split()
print(list6)