#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
print(os.path.join('demo', 'exercise'))

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('/demo/exercise', filename))

print(os.getcwd())

print(os.path.relpath("/Users/wsc/Desktop/Test/TestPython/TestPython/example", ".."))

path = "/Users/wsc/Desktop/Test/TestPython/TestPython/example"
print(os.getcwd())
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))

print(os.path.exists(os.path.join(path, 'exists')))
print(os.path.isdir(path))

try:
    os.remove(os.path.join(path, 'print.txt'))
except:
    pass

# 文件的应用级操作可以分为以下 3 步，每一步都需要借助对应的函数实现：
# 1、打开文件：使用 open() 函数，该函数会返回一个文件对象；
# 2、对已打开文件做读/写操作：读取文件内容可使用 read()、readline() 以及 readlines() 函数；向文件中写入内容，可以使用 write() 函数。
# 3、关闭文件：完成对文件的读/写操作之后，最后需要关闭文件，可以使用 close() 函数。

# 当前程序文件同目录下没有 my_file.txt 文件
file = open("my_file.txt")
print(file)

file = open("my_file.txt", encoding="utf-8") # 注意，手动修改 encoding 参数的值，仅限于文件以文本的形式打开，也就是说，以二进制格式打开时，不能对 encoding 参数的值做任何修改，否则程序会抛出 ValueError 异常
print(file)
# 输出文件是否已经关闭
print(file.closed)
# 输出访问模式
print(file.mode)
#输出编码格式
print(file.encoding)
# 输出文件名
print(file.name)

# 注意，使用 open() 函数打开的文件对象，必须手动进行关闭（后续章节会详细讲解），Python 垃圾回收机制无法自动回收打开文件所占用的资源。

# 标识符（数字、符号、英文字母）：占 一个 字节
# 汉字：占 三个 字节

# Python 提供了如下 3 种函数，它们都可以帮我们实现读取文件中数据的操作：
# read() 函数：逐个字节或者字符读取文件中的内容；
# readline() 函数：逐行读取文件中的内容；
# readlines() 函数：一次性读取文件中多行内容。

# 如果文件是以文本模式（非二进制模式）打开的，则 read() 函数会逐个 字符 进行读取；反之，如果文件以二进制模式打开，则 read() 函数会逐个 字节 进行读取。

# 以 utf-8 的编码格式打开指定文件
f = open("my_file.txt", encoding = "utf-8")
# 输出读取到的数据
a = f.read(6)
print(a)
print(f.read()) # 跟着上次读取的位置 接着读
# 关闭文件
f.close()

# 以二进制形式打开指定文件
f = open("my_file.txt", 'rb+')
# 输出读取到的数据
a = f.read()
print(a)
# 关闭文件
f.close()