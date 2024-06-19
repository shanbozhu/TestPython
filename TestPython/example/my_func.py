#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 我们不妨设想一下，如果没有 len() 函数，要想获取一个字符串的长度，该如何实现呢？请看下面的代码：
n = 0
for c in "http://c.biancheng.net/python/":
    n = n + 1
print(n)

# 自定义 len() 函数
def my_len(str):
    length = 0
    for c in str:
        length = length + 1
    return length

# 调用自定义的 my_len() 函数
length = my_len("http://c.biancheng.net/python/")
print(length)
# 再次调用 my_len() 函数
length = my_len("http://c.biancheng.net/shell/")
print(length)

# 需要注意的是，创建函数有多少个形参，那么调用时就需要传入多少个值，且顺序必须和创建函数时一致。即便该函数没有参数，函数名后的小括号也不能省略。
# 定义个空函数，没有实际意义
def pass_dis():
    pass
# 定义一个比较字符串大小的函数
def str_max(str1, str2):
    """
    比较 2 个字符串的大小
    """
    return str1 if str1 > str2 else str2
pass_dis()
strmax = str_max("http://c.biancheng.net/python","http://c.biancheng.net/shell")
print(strmax)
help(str_max)
print(str_max.__doc__)

# Python 中，根据实际参数的类型不同，函数参数的传递方式可分为 2 种，分别为值传递和引用（地址）传递：
# 值传递：适用于实参类型为不可变类型（字符串、数字、元组）；
# 引用（地址）传递：适用于实参类型为可变类型（列表，字典）；

# 值传递和引用传递的区别是，函数参数进行值传递后，若形参的值发生改变，不会影响实参的值；而函数参数继续引用传递后，改变形参的值，实参的值也会一同改变。

def demo(obj) :
    obj += obj
    print("形参值为：", obj)

print("-------值传递-----")
a = "C语言中文网"
print("a的值为：", a)
demo(a)
print("实参值为：", a)

print("-----引用传递-----")
a = [1, 2, 3]
print("a的值为：", a)
demo(a)
print("实参值为：", a)

# 关键字参数是指使用形式参数的名字来确定输入的参数值。通过此方式指定函数实参时，不再需要与形参的位置完全一致，只要将参数名写正确即可。
# 可以看到，在调用有参函数时，既可以根据位置参数来调用，也可以使用关键字参数（程序中第 8 行）来调用。在使用关键字参数调用时，可以任意调换参数传参的位置。
# 使用位置参数和关键字参数混合传参的方式。但需要注意，混合传参时关键字参数必须位于所有的位置参数 之后。
def dis_str(str1, str2):
    print("str1:", str1)
    print("str2:", str2)
# 位置参数
dis_str("http://c.biancheng.net/python/","http://c.biancheng.net/shell/")
# 关键字参数; 位置参数必须放在关键字参数之前
dis_str("http://c.biancheng.net/python/", str2="http://c.biancheng.net/shell/")
dis_str(str2="http://c.biancheng.net/python/", str1="http://c.biancheng.net/shell/")

# 指定有默认值的形式参数必须在所有没默认值参数的最后，否则会产生语法错误。
# str1没有默认参数，str2有默认参数
def dis_str(str1, str2 = "http://c.biancheng.net/python/"):
    print("str1:", str1)
    print("str2:", str2)
dis_str("http://c.biancheng.net/shell/")
dis_str("http://c.biancheng.net/java/","http://c.biancheng.net/golang/")
dis_str(str1 = "http://c.biancheng.net/shell/")
dis_str("http://c.biancheng.net/java/", str2 = "http://c.biancheng.net/golang/")
dis_str(str1 = "http://c.biancheng.net/java/", str2 = "http://c.biancheng.net/golang/")
print(dis_str.__defaults__)

print(type(None))

def add(a, b):
    c = a + b
    return c
# 函数赋值给变量
c = add(3,4)
print(c)
# 函数返回值作为其他函数的实际参数
print(add(3,4))

# 定义全局变量的方式有以下 2 种：
# 在函数体外定义的变量，一定是全局变量
# 在函数体内定义全局变量。即使用 global 关键字对变量进行修饰后，该变量就会变为全局变量。
add = "http://c.biancheng.net/shell/"
def text():
    print("函数体内访问：", add)
text()
print('函数体外访问：', add)

def text():
    global add # 注意，在使用 global 关键字修饰变量名时，不能直接给变量赋初值，否则会引发语法错误。
    add = "http://c.biancheng.net/java/"
    print("函数体内访问：", add)
text()
print('函数体外访问：', add)

# 全局变量
Pyname = "Python教程"
Pyadd = "http://c.biancheng.net/python/"
def text():
    # 局部变量
    Shename = "shell教程"
    Sheadd= "http://c.biancheng.net/shell/"
print( globals() ) # globals() 函数为 Python 的内置函数，它可以返回一个包含全局范围内所有变量的字典，该字典中的每个键值对，键为变量名，值为该变量的值。注意，globals() 函数返回的字典中，会默认包含有很多变量，这些都是 Python 主程序内置的，读者暂时不用理会它们。

# 全局变量
Pyname = "Python教程"
Pyadd = "http://c.biancheng.net/python/"
def text():
    # 局部变量
    Shename = "shell教程"
    Sheadd= "http://c.biancheng.net/shell/"
    print("函数内部的 locals:")
    print(locals())
text()
print("函数外部的 locals:")
print(locals()) # locals() 函数也是 Python 内置函数之一，通过调用该函数，我们可以得到一个包含当前作用域内所有变量的字典。这里所谓的“当前作用域”指的是，在函数内部调用 locals() 函数，会获得包含所有局部变量的字典；而在全局范文内调用 locals() 函数，其功能和 globals() 函数相同。

# 全局变量
Pyname = "Python教程"
Pyadd = "http://c.biancheng.net/python/"
class Demo:
    name = "Python 教程"
    add = "http://c.biancheng.net/python/"
print("有 object：")
print( vars(Demo) ) # vars() 函数也是 Python 内置函数，其功能是返回一个指定 object 对象范围内所有变量组成的字典。如果不传入object 参数，vars() 和 locals() 的作用完全相同。
print("无 object：")
print( vars() )

# 首先，和局部变量一样，默认情况下局部函数只能在其所在函数的作用域内使用。举个例子：
# 全局函数
def outdef():
    # 局部函数
    def indef():
        print("http://c.biancheng.net/python/")
    # 调用局部函数
    indef()
# 调用全局函数
outdef()

# 就如同全局函数返回其局部变量，就可以扩大该变量的作用域一样，通过将局部函数作为所在函数的返回值，也可以扩大局部函数的使用范围。例如，修改上面程序为：
# 全局函数
def outdef ():
    # 局部函数
    def indef():
        print("调用局部函数")
    # 调用局部函数
    return indef
# 调用全局函数
new_indef = outdef()
# 调用全局函数中的局部函数
new_indef()
# 因此，对于局部函数的作用域，可以总结为：如果所在函数没有返回局部函数，则局部函数的可用范围仅限于所在函数内部；反之，如果所在函数将局部函数作为返回值，则局部函数的作用域就会扩大，既可以在所在函数内部使用，也可以在所在函数的作用域中使用。

# 全局函数
def outdef():
    name = "所在函数中定义的 name 变量"
    # 局部函数
    def indef():
        name = "局部函数中定义的 name 变量"
        print(name)
    indef()
# 调用全局函数
outdef()

# 全局函数
def outdef():
    name = "所在函数中定义的 name 变量"
    # 局部函数
    def indef():
        nonlocal name
        print(name)
        # 修改name变量的值
        name = "局部函数中定义的 name 变量"
        print(name)
    indef()
# 调用全局函数
outdef()

