#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
demo 模块中包含以下内容：
name 字符串变量：初始值为 “Python教程”
add  字符串变量：初始值为 “http://c.biancheng.net/python”
say() 函数
CLanguage类：包含 name 和 add 属性和 say() 方法。
"""

name = "Python教程"
add = "http://c.biancheng.net/python"
print(name, add)

def say():
    print("人生苦短，我学Python！")
def _disPython():
    print("Python教程：http://c.biancheng.net/python")
def __disPython():
    print("Python教程：http://c.biancheng.net/python")
class CLanguage:
    def __init__(self, name, add):
        self.name = name
        self.add = add
    def say(self):
        print(self.name, self.add)
# 可以看到，我们在 demo.py 文件中放置了变量（name 和 add）、函数（ say() ）以及一个 Clanguage 类，该文件就可以作为一个模板。

# 只有以 “from 模块名 import *” 形式导入的模块，当该模块 设有 __all__ 变量时，只能导入该变量指定的成员，未指定的成员是无法导入的。
# 再次声明，__all__ 变量仅限于在其它文件中以“from 模块名 import *”的方式引入。也就是说，如果使用以下 2 种方式引入模块，则 __all__ 变量的设置是无效的。
# 1) 以 “import 模块名” 的形式导入 模块。通过该方式导入模块后，总可以通过 模块名前缀（如果为 模块 指定了 别名，则可以使用模快的 别名 作为前缀）来调用模块内的所有成员（除了 以 下划线 开头命名的成员）。
# 2) 以 “from 模块名 import 成员” 的形式 直接 导入 指定成员。使用此方式导入的模块，__all__ 变量即便设置，也形同虚设。
__all__ = ["say", "CLanguage"]

# 但通常情况下，为了检验模板中代码的正确性，我们往往需要为其设计一段测试代码，例如：
if __name__ == '__main__':
    say()
    clangs = CLanguage("C语言中文网","http://c.biancheng.net")
    clangs.say()
    _disPython()
    __disPython()