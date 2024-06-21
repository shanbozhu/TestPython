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
print(a.decode())

# Python readline()和readlines()函数：按行读取文件
# 和 read() 函数不同，这 2 个函数都以“行”作为读取单位，即每次都读取目标文件中的一行。对于读取以文本格式打开的文件，读取一行很好理解；对于读取以二进制格式打开的文件，它们会以“\n”作为读取一行的标志。
# readline() 函数用于读取文件中的一行，包含 最后的换行符“\n”。
f = open("my_file.txt")
# 读取一行数据
byt = f.readline()
print(byt)

# 以二进制形式打开指定文件
f = open("my_file.txt", 'rb')
byt = f.readline(6)
print(byt) # 和上一个例子的输出结果相比，由于这里没有完整读取一行的数据，因此不会读取到换行符。

f = open("my_file.txt", 'rb')
byt = f.readlines()
print(byt)

# Python write()和writelines()：向文件中写入数据
f = open("a.txt", 'a')
f.write("写入一行新数据")
f.close()

# Python 的文件对象中，不仅提供了 write() 函数，还提供了 writelines() 函数，可以实现将 字符串列表 写入文件中。
f = open('a.txt', 'r')
n = open('b.txt', 'w+')
n.writelines(f.readlines())
n.close()
f.close()
# 需要注意的是，使用 writelines() 函数向文件中写入多行数据时，不会自动给各行添加换行符。上面例子中，之所以 b.txt 文件中会逐行显示数据，是因为 readlines() 函数在读取各行数据时，读入了行尾的换行符。

n = open('c.txt', 'w+')
n.writelines(["1111111", "2222222"])
n.close()
