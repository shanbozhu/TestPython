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
f = open("my_file.txt", encoding ="utf-8")
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

f = open("my_file.txt", 'r')
print(f.tell())
print(f.read(3))
print(f.tell())
# 可以看到，当使用 open() 函数打开文件时，文件指针的起始位置为 0，表示位于文件的开头处，当使用 read() 函数从文件中读取 3 个字符之后，文件指针同时向后移动了 3 个字符的位置。这就表明，当程序使用文件对象读写数据时，文件指针会自动向后移动：读写了多少个数据，文件指针就自动向后移动多少个位置。

# with 表达式 [as target]：
#     代码块
# 此格式中，用 [] 括起来的部分可以使用，也可以省略。其中，target 参数用于指定一个变量，该语句会将 expression 指定的结果 保存 到该变量中。with as 语句中的代码块如果不想执行任何语句，可以直接使用 pass 语句代替。
with open('a.txt', 'a') as f:
    f.write("\nPython教程")

# Python pickle模块：实现Python对象的持久化存储
# Python 中有个序列化过程叫作 pickle，它能够实现 任意对象 与 文本 之间的相互转化，也可以实现 任意对象 与 二进制 之间的相互转化。也就是说，pickle 可以实现 Python 对象的存储及恢复。
# 值得一提的是，pickle 是 python 语言的一个标准模块，安装 python 的同时就已经安装了 pickle 库，因此它不需要再单独安装，使用 import 将其导入到程序中，就可以直接使用。

# pickle 模块提供了以下 4 个函数供我们使用：
# dumps()：将 Python 中的对象序列化成二进制对象，并返回；
# loads()：读取给定的二进制对象数据，并将其转换为 Python 对象；
# dump()：将 Python 中的对象序列化成二进制对象，并写入文件；
# load()：读取指定的序列化数据文件，并返回对象。
# 以上这 4 个函数可以分成两类，其中 dumps 和 loads 实现基于内存的 Python 对象与二进制互转；dump 和 load 实现基于文件的 Python 对象与二进制互转。

# pickle.dumps()函数
import pickle
tup1 = ('I love Python', {1,2,3}, None)
# 使用 dumps() 函数将 tup1 转成 p1
p1 = pickle.dumps(tup1)
print(p1)

# pickle.loads()函数
import pickle
tup1 = ('I love Python', {1, 2, 3}, None)
p1 = pickle.dumps(tup1)
# 使用 loads() 函数将 p1 转成 Python 对象
t2 = pickle.loads(p1)
print(t2)

# pickle.dump()函数
import pickle
tup1 = ('I love Python', {1, 2, 3}, None)
# 使用 dumps() 函数将 tup1 转成 p1
with open ("dump.txt", 'wb') as f: # 打开文件
    pickle.dump(tup1, f) # 用 dump 函数将 Python 对象 转成 二进制文件


with open ("dump.txt", 'rb') as f: # 打开文件
    t3 = pickle.load(f) # 将二进制文件 转换成 Python 对象
    print(t3)
# 看似强大的 pickle 模块，其实也有它的短板，即 pickle 不支持并发地访问持久性对象，在复杂的系统环境下，尤其是读取海量数据时，使用 pickle 会使整个系统的I/O读取性能成为瓶颈。这种情况下，可以使用 ZODB。

# ZODB 是一个健壮的、多用户的和面向对象的数据库系统，专门用于存储 Python 语言中的对象数据，它能够存储和管理任意复杂的 Python 对象，并支持事务操作和并发控制。并且，ZODB 也是在 Python 的序列化操作基础之上实现的，因此要想有效地使用 ZODB，必须先学好 pickle。

from os import path
# 获取绝对路径
print(path.abspath("my_file.txt"))
# 获取共同前缀
print(path.commonprefix(['C://my_file.txt', 'C://a.txt']))
# 获取共同路径
print(path.commonpath(['http://c.biancheng.net/python/', 'http://c.biancheng.net/shell/']))
# 获取目录
print(path.dirname('/usr/my_file.txt'))
# 判断指定目录是否存在
print(path.exists('my_file.txt'))

# Python tempfile模块：生成 临时文件 和 临时目录
import tempfile
# 创建临时文件
fp = tempfile.TemporaryFile()
print(fp.name)
fp.write('两情若是久长时，'.encode('utf-8'))
fp.write('又岂在朝朝暮暮。'.encode('utf-8'))
# 将文件指针移到开始处，准备读取文件
fp.seek(0)
print(fp.read().decode('utf-8')) # 输出刚才写入的内容
# 关闭文件，该文件将会被自动删除
fp.close()

# 通过with语句创建临时文件，with会自动关闭临时文件
with tempfile.TemporaryFile() as fp:
    # 写入内容
    fp.write(b'I Love Python!')
    # 将文件指针移到开始处，准备读取文件
    fp.seek(0)
    # 读取文件内容
    print(fp.read()) # b'I Love Python!'
# 通过with语句创建临时目录
with tempfile.TemporaryDirectory() as tmpdirname:
    print('创建临时目录', tmpdirname)
# 上面程序以两种方式来创建临时文件：
# 第一种方式是手动创建临时文件，读写临时文件后需要主动关闭它，当程序关闭该临时文件时，该文件会被自动删除。
# 第二种方式则是使用 with 语句创建临时文件，这样 with 语句会自动关闭临时文件。

# 第一行输出结果就是程序生成的临时文件的文件名，最后一行输出结果就是程序生成的临时目录的目录名。需要注意的是，不要去找临时文件或临时文件夹，因为程序退出时该临时文件和临时文件夹都会被删除。

# Python pathlib模块用法详解
from pathlib import *
# 创建PurePath，实际上使用PureWindowsPath
path = PurePath('my_file.txt')
print(type(path))

from pathlib import *
# 创建PurePath，实际上使用PureWindowsPath
path = PurePath('http:', 'c.biancheng.net', 'python')
print(path)

with open('my_file.txt', "r", encoding="utf-8") as f1:
    print(f1)
    for line in f1:
        print(line)

with open('my_file.txt', "r", encoding="utf-8") as f2:
    for line in f2.readlines(): # readlines 如连续调用两次readlines，后面一次返回空列表，因为第一次调用时文件指针已经移至文件内容的末尾，再次读取将从末尾开始，所以第二次读取空。
        print(line)

import os

# 指定目录
path = "/Users/wsc/Desktop/Test/TestPython/TestPython/example"
print(os.walk(path)) # 生成器，生成器属于迭代器
print(type(os.walk(path)))
# 遍历目录
for root, dirs, files in os.walk(path):
    print('root =', root, 'dirs =', dirs, 'files =', files)
    for name in files:
        print(os.path.join(root, name))  # 输出文件路径
    for name in dirs:
        print(os.path.join(root, name))  # 输出子目录路径