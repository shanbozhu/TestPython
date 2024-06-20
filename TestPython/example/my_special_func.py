#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python __new__()方法详解
# __new__() 是一种负责创建类实例的静态方法，它无需使用 staticmethod 装饰器修饰，且该方法会优先 __init__() 初始化方法被调用。
class demoClass:
    instances_created = 0
    def __new__(cls, *args, **kwargs):
        print("__new__():", cls, args, kwargs)
        instance = super().__new__(cls)
        instance.number = cls.instances_created
        cls.instances_created += 1
        return instance
    def __init__(self, attribute):
        print("__init__():", self, attribute)
        self.attribute = attribute
test1 = demoClass("abc")
test2 = demoClass("xyz")
print(test1.number, test1.instances_created)
print(test2.number, test2.instances_created)
# 那么，什么情况下使用 __new__() 呢？答案很简单，在 __init__() 不够用的时候。
# Python中大量使用 __new__() 方法且合理的，就是 MetaClass 元类。

# Python __repr__()方法：显示属性
class CLanguage:
    pass
clangs = CLanguage()
print(clangs)
# 以本节开头的程序为例，执行 print(clangs) 等同于执行 print(clangs.__repr__())，程序的输出结果是一样的。
print(clangs.__repr__())

class CLanguage:
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    def __repr__(self):
        return "CLanguage[name=" + self.name + ", add=" + self.add +"]"
clangs = CLanguage()
print(clangs)

# Python __del__()方法：销毁对象
# 无论是手动销毁，还是 Python 自动帮我们销毁，都会调用 __del__() 方法。举个例子：
class CLanguage:
    def __init__(self):
        print("调用 __init__() 方法构造对象")
    def __del__(self):
        print("调用__del__() ，对象被销毁时调用该方法")
clangs = CLanguage()
del clangs # 手动销毁

class CLanguage:
    def __init__(self):
        print("调用 __init__() 方法构造对象")
    def __del__(self):
        print("调用__del__() 销毁对象，释放其空间")
clangs = CLanguage()
# 添加一个引用 clangs对象 的实例对象
cl = clangs
del clangs # 引用计数减一
print("***********")
# 可以看到，当程序中有其它变量（比如这里的 cl）引用该实例对象时，即便手动调用 del 方法，__del__() 也不会立即执行。这和 Python 的垃圾回收机制的实现有关。
# Python 采用自动引用计数（简称 ARC）的方式实现垃圾回收机制。该方法的核心思想是：每个 Python 对象都会配置一个计数器，初始 Python 实例对象的计数器值都为 0，如果有变量引用该实例对象，其计数器的值会加 1，依次类推；反之，每当一个变量取消对该实例对象的引用，计数器会减 1。如果一个 Python 对象的的计数器值为 0，则表明没有变量引用该 Python 对象，即证明程序不再需要它，此时 Python 就会自动将其回收。

class CLanguage:
    def __del__(self):
        print("调用父类 __del__() 方法")
class cl(CLanguage):
    def __del__(self):
        super().__del__()
        print("调用子类 __del__() 方法")
c = cl()
del c

# Python __dir__()用法：列出对象的所有属性（方法）名
class CLanguage:
    def __init__ (self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    def say():
        pass
clangs = CLanguage()
print(dir(clangs))
# 注意，通过 dir() 函数，不仅仅输出本类中新添加的属性名和方法（最后 3 个），还会输出从父类（这里为 object 类）继承得到的属性名和方法名。
# 值得一提的是，dir() 函数的内部实现，其实是在调用 __dir__() 方法的基础上，对该方法返回的属性名和方法名做了 排序。
class CLanguage:
    def __init__ (self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    def say():
        pass
clangs = CLanguage()
print(clangs.__dir__())

# Python __dict__属性：查看对象内部所有属性名和属性值组成的字典
# 在 Python 类的内部，无论是 类属性 还是 实例属性，都是以字典的形式进行存储的，其中属性名作为键，而值作为该键对应的值。
# 为了方便用户查看类中包含哪些属性，Python 类提供了 __dict__ 属性。需要注意的一点是，该属性可以用 类名 或者 类的实例对象 来调用，用 类名 直接调用 __dict__，会输出该由类中所有 类属性 组成的字典；而使用 类的实例对象 调用 __dict__，会输出由类中所有 实例属性 组成的字典。
class CLanguage:
    a = 1
    b = 2
    def __init__ (self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    def say():
        pass
# 通过类名调用__dict__
print(CLanguage.__dict__)
# 通过类实例对象调用 __dict__
clangs = CLanguage()
print(clangs.__dict__)

# 除此之外，借助由 类的实例对象 调用 __dict__ 属性获取的字典，可以使用字典的方式对其中 实例属性 的 值 进行 修改，例如：
class CLanguage:
    a = "aaa"
    b = 2
    def __init__ (self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
# 通过 类的实例对象 调用 __dict__
clangs = CLanguage()
print(clangs.__dict__)
clangs.__dict__['name'] = "Python教程"
print(clangs.name)
# 注意，无法通过类似的方式修改 类属性 的值。

# Python hasattr()函数
# hasattr() 函数用来判断某个类的实例对象 是否包含指定名称的 属性或方法。该函数的语法格式如下：
class CLanguage:
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    def say(self):
        print("我正在学Python")
clangs = CLanguage()
print(hasattr(clangs, "name"))
print(hasattr(clangs, "add"))
print(hasattr(clangs, "say"))
# 显然，无论是属性名还是方法名，都在 hasattr() 函数的匹配范围内。因此，我们只能通过该函数判断实例对象是否包含该名称的属性或方法，但不能精确判断，该名称代表的是属性还是方法。

# Python getattr() 函数
# getattr() 函数获取某个 类的实例对象 中指定属性的值。没错，和 hasattr() 函数不同，该函数只会从 类的对象 包含的所有属性中进行查找。
class CLanguage:
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    def say(self):
        print("我正在学Python")
clangs = CLanguage()
print(getattr(clangs, "name"))
print(getattr(clangs, "add"))
print(getattr(clangs, "say"))
print(getattr(clangs, "display", 'nodisplay'))
# 可以看到，对于类中已有的属性，getattr() 会返回它们的值，而如果该名称为方法名，则返回该方法的状态信息；反之，如果该 属性 不为 类的对象 所有，要么返回默认的参数，要么程序报 AttributeError 错误。

# Python setattr()函数
# setattr() 函数的功能相对比较复杂，它最基础的功能是修改 类的实例对象 中的属性值。其次，它还可以实现为实例对象动态添加属性或者方法。
class CLanguage:
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    def say(self):
        print("我正在学Python")
clangs = CLanguage()
print(clangs.name)
print(clangs.add)
setattr(clangs, "name", "Python教程")
setattr(clangs, "add", "http://c.biancheng.net/python")
print(clangs.name)
print(clangs.add)

# 甚至利用 setattr() 函数，还可以将 类的属性 修改为一个 类的方法，同样也可以将 类的方法 修改成一个 类的属性。例如：
def say(self):
    print("我正在学Python")
class CLanguage:
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
clangs = CLanguage()
print(clangs.name)
print(clangs.add)
setattr(clangs, "name", say)
clangs.name(clangs)

# 使用 setattr() 函数对 实例对象 中执行名称的 属性或方法 进行修改时，如果该名称查找失败，Python 解释器不会报错，而是会给该 实例对象 动态添加一个指定名称的 属性或方法。例如：
def say(self):
    print("我正在学Python")
class CLanguage:
    pass
clangs = CLanguage()
setattr(clangs, "name", "C语言中文网")
setattr(clangs, "say", say)
print(clangs.name)
clangs.say(clangs)
# 可以看到，虽然 CLanguage 为空类，但通过 setattr() 函数，我们为 clangs 对象动态添加了一个 name 属性和一个 say() 方法。

# Python issubclass和isinstance函数：检查类型
# Python 提供了如下两个函数来检查类型：
# issubclass(cls, class_or_tuple)：检查 cls 是否为后一个类或元组包含的多个类中任意类的子类。
# isinstance(obj, class_or_tuple)：检查 obj 是否为后一个类或元组包含的多个类中任意类的对象。
# 通过使用上面两个函数，程序可以方便地先执行检查，然后才调用方法，这样可以保证程序不会出现意外情况。
# 定义一个字符串
hello = "Hello"
# "Hello"是str类的实例，输出True
print('"Hello"是否是str类的实例: ', isinstance(hello, str))
# "Hello"是object类的子类的实例，输出True
print('"Hello"是否是object类的实例: ', isinstance(hello, object))
# str是object类的子类，输出True
print('str是否是object类的子类: ', issubclass(str, object))
# "Hello"不是tuple类及其子类的实例，输出False
print('"Hello"是否是tuple类的实例: ', isinstance(hello, tuple))
# str不是tuple类的子类，输出False
print('str是否是tuple类的子类: ', issubclass(str, tuple))
# 定义一个列表
my_list = [2, 4]
# [2, 4]是list类的实例，输出True
print('[2, 4]是否是list类的实例: ', isinstance(my_list, list))
# [2, 4]是object类的子类的实例，输出True
print('[2, 4]是否是object类及其子类的实例: ', isinstance(my_list, object))
# list是object类的子类，输出True
print('list是否是object类的子类: ', issubclass(list, object))
# [2, 4]不是tuple类及其子类的实例，输出False
print('[2, 4]是否是tuple类及其子类的实例: ', isinstance([2, 4], tuple))
# list不是tuple类的子类，输出False
print('list是否是tuple类的子类: ', issubclass(list, tuple))

# 通过上面程序可以看出，issubclass() 和 isinstance() 两个函数的用法差不多，区别只是 issubclass() 的第一个参数是 类名，而 isinstance() 的第一个参数是 变量，这也与两个函数的意义对应：issubclass 用于判断是否为 子类，而 isinstance() 用于判断是否为该类或子类的 实例。

data = (20, 'fkit')
print('data是否为列表或元组: ', isinstance(data, (list, tuple))) # True
# str不是list或者tuple的子类，输出False
print('str是否为list或tuple的子类: ', issubclass(str, (list, tuple)))
# str是list或tuple或object的子类，输出True
print('str是否为list或tuple或object的子类 ', issubclass(str, (list, tuple, object)))

# 此外，Python 为所有类都提供了一个 __bases__ 属性，通过该属性可以查看该类的所有 直接父类，该属性返回所有 直接父类 组成的元组。例如如下代码：
class A:
    pass
class B:
    pass
class C(A, B):
    pass
print('类A的直接父类:', A.__bases__)
print('类B的直接父类:', B.__bases__)
print('类C的直接父类:', C.__bases__)
# 从上面的运行结果也可以看出，如果在定义类时没有显式指定它的父类，则这些类 默认的父类 是 object 类。

# Python 还为所有类都提供了一个 __subclasses__() 方法，通过该方法可以查看该类的所有 直接子类，该方法返回该类的所有子类组成的列表。例如在上面程序中增加如下两行：
print('类A的直接子类:', A.__subclasses__())
print('类B的直接子类:', B.__subclasses__())

# Python __call__()方法
# 本节再介绍 Python 类中一个非常特殊的 实例方法，即 __call__()。该方法的功能类似于在类中重载 () 运算符，使得 类的实例对象 可以像调用普通函数那样，以“对象名()”的形式使用。
class CLanguage:
    # 定义__call__方法
    def __call__(self, name, add):
        print("调用__call__()方法", name, add)
clangs = CLanguage()
clangs("C语言中文网","http://c.biancheng.net")
clangs.__call__("C语言中文网","http://c.biancheng.net")
# 可以看到，通过在 CLanguage 类中实现 __call__() 方法，使的 clangs 实例对象 变为了 可调用对象。
# Python 中，凡是可以将 () 直接应用到自身并执行，都称为 可调用对象。可调用对象包括自定义的函数、Python 内置函数以及本节所讲的类的实例对象。

def say():
    print("Python教程：http://c.biancheng.net/python")
say()
say.__call__()

# 用 __call__() 弥补 hasattr() 函数的短板
# 前面章节介绍了 hasattr() 函数的用法，该函数的功能是查找类的实例对象中是否包含指定名称的属性或者方法，但该函数有一个缺陷，即它无法判断该指定的名称，到底是 类的属性 还是 类的方法。
# 要解决这个问题，我们可以借助 可调用对象 的概念。要知道，类的实例对象包含的方法，其实也属于 可调用对象，但类的属性却不是。举个例子：
class CLanguage:
    def __init__ (self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    def say(self):
        print("我正在学Python")
clangs = CLanguage()
if hasattr(clangs, "name"):
    print(hasattr(clangs.name, "__call__"))
print("**********")
if hasattr(clangs, "say"):
    print(hasattr(clangs.say, "__call__"))
# 可以看到，由于 name 是类的属性，它没有以 __call__ 为名的 __call__() 方法；而 say 是类的方法，它是 可调用对象，因此它有 __call__() 方法。

# Python @函数装饰器及用法（超级详细）
# 前面章节中，我们已经讲解了 Python 内置的 3 种函数装饰器，分别是 ＠staticmethod、＠classmethod 和 @property，其中 staticmethod()、classmethod() 和 property() 都是 Python 的内置函数。

# funA 作为装饰器函数
def funA(fn):
    print("C语言中文网")
    fn() # 执行传入的fn参数
    print("http://c.biancheng.net")
    return "装饰器函数的返回值"
@funA
def funB():
    print("学习 Python")
# 等价于下面语句
# funB = funA(funB)
print(funB)
# 显然，被“＠函数”修饰的函数不再是原来的函数，而是被替换成一个新的东西（取决于装饰器的返回值），即如果装饰器函数的返回值为普通变量，那么被修饰的函数名就变成了变量名；同样，如果装饰器返回的是一个函数的名称，那么被修饰的函数名依然表示一个函数。
# 实际上，所谓函数装饰器，就是通过 装饰器函数，在不修改 原函数 的前提下，来对 函数 的功能进行合理的扩充。

def funA(fn):
    # 定义一个嵌套函数
    def say(arc):
        print("Python教程:", arc)
    return say
@funA
def funB(arc):
    print("funB():", a)
funB("http://c.biancheng.net/python")

# 这里有必要给读者分析一下这个程序，其实，它和如下程序是等价的：
def funA(fn):
    # 定义一个嵌套函数
    def say(arc):
        print("Python教程:", arc)
    return say
def funB(arc):
    print("funB():", a)
funB = funA(funB)
funB("http://c.biancheng.net/python")

# *args 和 **kwargs 表示接受任意数量和类型的参数。