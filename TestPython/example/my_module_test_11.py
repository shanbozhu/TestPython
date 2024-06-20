#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import my_module_demo_22
from my_module_demo_22 import *

# 可以看到，当执行 test.py 文件时，它同样会执行 demo.py 中用来测试的程序，这显然不是我们想要的效果。正常的效果应该是，只有直接运行模板文件时，测试代码才会被执行；反之，如果是其它程序以引入的方式执行模板文件，则测试代码不应该被执行。
# 要实现这个效果，可以借助 Python 内置的 __name__ 变量。当直接运行一个模块时，name 变量的值为 __main__；而将 模块 导入其他程序中并运行该程序时，处于 模块 中的 __name__ 变量的值就变成了 模块名。因此，如果希望测试函数只有在 直接运行模块文件 时才执行，则可在 调用 测试函数时增加判断，即只有当 __name__ == '__main__' 时才 调用 测试函数。

print(my_module_demo_22.__doc__)

# 事实上，当我们向文件导入某个模块时，导入的是该模块中那些名称不以 下划线（单下划线 “_” 或者双下划线 “__”）开头的变量、函数和类。因此，如果我们不想模块文件中的某个成员被引入到其它文件中使用，可以在其名称前添加 下划线。

say()
clangs = CLanguage("C语言中文网","http://c.biancheng.net")
# _disPython()
# __disPython()

print(dir(my_module_demo_22))
# 事实上，在前面章节的学习中，曾多次使用 dir() 函数。通过 dir() 函数，我们可以查看某指定模块包含的全部成员（包括变量、函数和类）。注意这里所指的全部成员，不仅包含可供我们调用的模块成员，还包含所有名称以双下划线“__”开头和结尾的成员，而这些“特殊”命名的成员，是为了在本模块中使用的，并不希望被其它文件调用。
# 可以看到，通过 dir() 函数获取到的模块成员，不仅包含供外部文件使用的成员，还包含很多“特殊”（名称以 2 个下划线开头和结束）的成员，列出这些成员，对我们并 没有 实际意义。
# 因此，这里给读者推荐一种可以 忽略 显示 dir() 函数输出的特殊成员的方法。
print([e for e in dir(my_module_demo_22) if not e.startswith('_')])
# 显然通过 列表 推导式，可在 dir() 函数输出结果的基础上，筛选出对我们有用的成员并显示出来。

print(my_module_demo_22.__all__)
# 不过需要注意的是，并非所有的模块都支持使用 __all__ 变量，因此对于获取有些 模块 的成员，就只能使用 dir() 函数。