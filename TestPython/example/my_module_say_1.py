#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 通过 import 关键字，将 hello.py 模块引入此文件
import my_module_hello_2

print(my_module_hello_2)
print(my_module_hello_2.__doc__)
print(type(my_module_hello_2))

my_module_hello_2.say()

# 读者可能注意到，my_module_say_1.py 文件中使用了原本在 my_module_hello_2.py 文件中才有的 say() 函数，相对于 my_module_say_1.py 来说，my_module_hello_2.py 就是一个自定义的模块（有关自定义模块，后续章节会做详细讲解），我们只需要将 my_module_hellp.py 模块导入到 my_module_say_1.py 文件中，就可以直接在 my_module_say_1.py 文件中使用模块中的资源。

# 与此同时，当调用模块中的 say() 函数时，使用的语法格式为 “模块名.函数”，这是因为，相对于 my_module_say_1.py 文件，my_module_hello_2.py 文件中的代码自成一个 命名空间，因此在调用其他模块中的函数时，需要明确指明函数的 出处，否则 Python 解释器将会 报错。