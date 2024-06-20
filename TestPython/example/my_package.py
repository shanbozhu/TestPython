#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 通过前面的学习我们知道，包 其实本质上还是 模块，因此 导入模块的语法 同样也适用于 导入包。无论导入我们自定义的包，还是导入从他处下载的第三方包，导入方法可归结为以下 3 种：
# import 包名[.模块名 [as 别名]]
# from 包名 import 模块名 [as 别名]
# from 包名.模块名 import 成员名 [as 别名]

# 注意，导入包的同时，会在 包目录 下生成一个含有 __init__.cpython-36.pyc 文件的 __pycache__ 文件夹。
# 当导入指定包时，程序会自动执行该包所对应文件夹下的 __init__.py 文件中的代码。

import my_package # 直接导入包名，并不会将 包中 所有 模块 全部 导入到程序 中，它的作用仅仅是 导入并执行包下的 __init__.py 文件。因此，运行该程序，在执行 __init__.py 文件中代码的同时，还会抛出 AttributeError 异常（访问的对象不存在）
# my_package.my_package_module_1.display("http://c.biancheng.net/linux_tutorial/")

# 我们知道，包的本质就是模块，导入模块时，当前程序中会包含一个和 模块名 同名 且类型为 module 的变量，导入包也是如此：
print(my_package)
print(my_package.__doc__)
print(type(my_package))

import my_package.my_package_module_1
my_package.my_package_module_1.display("http://c.biancheng.net/java/")

# 可以看到，通过此语法格式导入包中的指定模块后，在使用该模块中的成员（变量、函数、类）时，需添加“包名.模块名”为前缀。当然，如果使用 as 给包名.模块名”起一个别名的话，就使用直接使用这个别名作为前缀使用该模块中的方法了，例如：

import my_package.my_package_module_1 as module
module.display("http://c.biancheng.net/python/")

from my_package import my_package_module_1
my_package_module_1.display("http://c.biancheng.net/golang/")

from my_package import my_package_module_1 as mod
mod.display("http://c.biancheng.net/golang/")
# 同样，既然包也是模块，那么这种语法格式自然也支持 “from 包名 import *” 这种写法，它和 import 包名 的作用一样，都只是将该包的 __init__.py 文件导入并执行。

from my_package.my_package_module_1 import display
display("http://c.biancheng.net/shell/")

from my_package.my_package_module_1 import display as dis
dis("http://c.biancheng.net/shell/")

from my_package.my_package_module_1 import *
display("http://c.biancheng.net/shell/")