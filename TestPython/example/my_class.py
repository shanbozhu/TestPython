#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 打个比方，若在某游戏中设计一个乌龟的角色，应该如何来实现呢？使用面向对象的思想会更简单，可以分为如下两个方面进行描述：
# 从表面特征来描述，例如，绿色的、有 4 条腿、重 10 kg、有外壳等等。
# 从所具有的的行为来描述，例如，它会爬、会吃东西、会睡觉、会将头和四肢缩到壳里，等等。
class tortoise:
    bodyColor = "绿色"
    footNum = 4
    weight = 10
    hasShell = True
    # 会爬
    def crawl(self):
        print("乌龟会爬")
    # 会吃东西
    def eat(self):
        print("乌龟吃东西")
    # 会睡觉
    def sleep(self):
        print("乌龟在睡觉")
    # 会缩到壳里
    def protect(self):
        print("乌龟缩进了壳里")

# 不仅如此，在 Python 中，所有的变量其实也都是对象，包括整形（int）、浮点型（float）、字符串（str）、列表(list)、元组(tuple)、字典（dict）和集合（set）。以字典（dict）为例，它包含多个函数供我们使用，例如使用 keys() 获取字典中所有的键，使用 values() 获取字典中所有的值，使用 item() 获取字典中所有的键值对，等等。

# 面向对象中，常用术语包括：
# 类：可以理解是一个模板，通过它可以创建出无数个具体实例。比如，前面编写的 tortoise 表示的只是乌龟这个物种，通过它可以创建出无数个实例来代表各种不同特征的乌龟（这一过程又称为类的实例化）。
# 对象：类并不能直接使用，通过类创建出的实例（又称对象）才能使用。这有点像汽车图纸和汽车的关系，图纸本身（类）并不能为人们使用，通过图纸创建出的一辆辆车（对象）才能使用。
# 属性：类中的所有变量称为属性。例如，tortoise 这个类中，bodyColor、footNum、weight、hasShell 都是这个类拥有的属性。
# 方法：类中的所有函数通常称为方法。不过，和函数所有不同的是，类方法至少要包含一个 self 参数（后续会做详细介绍）。例如，tortoise 类中，crawl()、eat()、sleep()、protect() 都是这个类所拥有的方法，类的方法无法单独使用，只能和类的对象一起使用。

# Python 类中属性和方法所在的位置是任意的，即它们之间并没有固定的前后次序。
class TheFirstDemo:
    """这是一个学习Python定义的第一个类"""
    # 下面定义了一个类属性
    add = 'http://c.biancheng.net'
    # 下面定义了一个say方法
    def say(self, content):
        print(content)
# 另外分析上面的代码可以看到，我们创建了一个名为 TheFirstDemo 的类，其包含了一个名为 add 的类属性。注意，根据定义属性位置的不同，在各个类方法之外定义的变量称为类属性或类变量（如 add 属性），而在类方法中定义的属性称为实例属性（或实例变量）。say() 是一个实例方法，除此之外，Python 类中还可以定义类方法和静态方法。

# 构造方法用于创建对象时使用，每当创建一个类的实例对象时，Python 解释器都会自动调用它。
# 注意，即便不手动为类添加任何构造方法，Python 也会自动为类添加一个仅包含 self 参数的构造方法。
class TheFirstDemo:
    """这是一个学习Python定义的第一个类"""
    # 构造方法
    def __init__(self):
        print("调用构造方法")

    # 下面定义了一个类属性
    add = 'http://c.biancheng.net'

    # 下面定义了一个say方法
    def say(self, content):
        print(content)

zhangsan = TheFirstDemo() # 显然，在创建 zhangsan 这个对象时，隐式调用了我们手动创建的 __init__() 构造方法。

class CLanguage:
    """这是一个学习Python定义的一个类"""
    def __init__(self, name, add):
        print(name, "的网址为:", add)
# 创建 add 对象，并传递参数给构造函数
add = CLanguage("C语言中文网","http://c.biancheng.net") # 可以看到，虽然构造方法中有 self、name、add 3 个参数，但实际需要传参的仅有 name 和 add，也就是说，self 不需要手动传递参数。

# 定义类时，如果没有手动添加 __init__() 构造方法，又或者添加的 __init__() 中仅有一个 self 参数，则创建类对象时的参数可以省略不写。
class CLanguage:
    # 下面定义了 2 个 类变量
    name = "C语言中文网"
    add = "http://c.biancheng.net"

    def __init__(self, name, add):
        # 下面定义 2 个 实例变量
        self.name = name
        self.add = add
        print(name, "网址为：", add)
    # 下面定义了一个say 实例方法
    def say(self, content):
        print(content)
# 将该CLanguage对象赋给 clanguage变量
clanguage = CLanguage("C语言","biancheng")
# 类变量和实例变量，简单地理解，定义在各个类方法之外（包含在类中）的变量为类变量（或者类属性），定义在类方法中的变量为实例变量（或者实例属性）
# 输出name和add实例变量的值
print(clanguage.name, clanguage.add)
# 修改实例变量的值
clanguage.name = "Python教程"
clanguage.add = "http://c.biancheng.net/python"
# 调用clanguage的say()方法
clanguage.say("人生苦短，我用Python")
# 再次输出name和add的值
print(clanguage.name, clanguage.add)

# Python 支持为已创建好的对象动态增加实例变量，方法也很简单，举个例子：
# 为clanguage对象增加一个money实例变量
clanguage.money = 159.9 # 可以看到，通过直接增加一个新的实例变量并为其赋值，就成功地为 clanguage 对象添加了 money 变量。
print(clanguage.money)
# 删除新添加的 money 实例变量
del clanguage.money
# 再次尝试输出 money，此时会报错
# print(clanguage.money)

# Python 也允许为对象动态增加方法。以本节开头的 Clanguage 类为例，由于其内部只包含一个 say() 方法，因此该类实例化出的 clanguage 对象也只包含一个 say() 方法。但其实，我们还可以为 clanguage 对象动态添加其它方法。
# 先定义一个函数
def info(self):
    print("---info函数---", self)
# 使用info对clanguage的foo方法赋值（动态绑定方法）
clanguage.foo = info
# Python不会自动将调用者绑定到第一个参数，
# 因此程序需要手动将调用者绑定为第一个参数
clanguage.foo(clanguage)  # ①
# 使用lambda表达式为clanguage对象的bar方法赋值（动态绑定方法）
clanguage.bar = lambda self: print('--lambda表达式--', self)
clanguage.bar(clanguage) # ②
# 上面的第 5 行和第 11 行代码分别使用函数、lambda 表达式为 clanguage 对象动态增加了方法，但对于动态增加的方法，Python 不会自动将方法调用者绑定到它们的第一个参数，因此程序必须手动为第一个参数传入参数值，如上面程序中 ① 号、② 号代码所示。

# 有读者可能会问，有没有不用手动给 self 传值的方法呢？通过借助 types 模块下的 MethodType 可以实现，仍以上面的 info() 函数为例：
def info(self, content):
    print("C语言中文网地址为：%s" % content)
# 导入MethodType
from types import MethodType
clanguage.info = MethodType(info, clanguage)
# 第一个参数已经绑定了，无需传入
clanguage.info("http://c.biancheng.net")

class Person:
    def __init__(self):
        print("正在执行构造方法")
    # 定义一个study()实例方法
    def study(self, name):
        print(name,"正在学Python")

# 如果你接触过其他面向对象的编程语言（例如 C++），其实 Python 类方法中的 self 参数就相当于 C++ 中的 this 指针。
# 也就是说，同一个类可以产生多个对象，当某个对象调用类方法时，该对象会把自身的引用作为第一个参数自动传给该方法，换句话说，Python 会自动绑定类方法的第一个参数指向调用该方法的对象。如此，Python解释器就能知道到底要操作哪个对象的方法了。

class Person:
    def __init__(self):
        print("正在执行构造方法")
    # 定义一个study()实例方法
    def study(self):
        print(self, "正在学Python")
zhangsan = Person()
zhangsan.study()
lisi = Person()
lisi.study()

# 另外，对于构造函数中的 self 参数，其代表的是当前正在初始化的类对象。举个例子：
class Person:
    name = "xxx"
    def __init__(self, name):
        self.name = name
zhangsan = Person("zhangsan")
print(zhangsan.name)
lisi = Person("lisi")
print(lisi.name)

class Person:
    def who(self):
        print(self)
zhangsan = Person()
# 第一种方式
zhangsan.who()
# 第二种方式
who = zhangsan.who
who() # 通过 who 变量调用 zhangsan对象 中的 who() 方法

# 前面章节提到过，在类体中，根据变量定义的位置不同，以及定义的方式不同，类的属性又可细分为以下 3 种类型：
# 类体中、所有函数之外：此范围定义的变量，称为类属性或类变量；
# 类体中，所有函数内部：以 “self.变量名” 的方式定义的变量，称为实例属性或实例变量；
# 类体中，所有函数内部：以 “变量名=变量值” 的方式定义的变量，称为局部变量。

# 类属性
# 指的是在类中，但在各个类方法外定义的变量。举个例子：
class CLanguage:
    # 下面定义了2个类属性
    name = "C语言中文网"
    add = "http://c.biancheng.net"
    # 下面定义了一个say实例方法
    def say(self, content):
        print(content)
# 上面程序中，name 和 add 就属于类属性。
# 类属性的特点是，所有类的实例化对象都同时共享类属性，也就是说，类属性在所有实例化对象中是作为公用资源存在的。类属性 的调用方式有 2 种，既可以使用类名直接调用，也可以使用类的实例化对象调用。

# 使用类名直接调用
print(CLanguage.name)
print(CLanguage.add)
# 修改类属性的值
CLanguage.name = "Python教程"
CLanguage.add = "http://c.biancheng.net/python"
print(CLanguage.name)
print(CLanguage.add)

# 当然，也可以使用类的对象来调用所属类中的类属性（此方式不推荐使用，原因后续会讲）。例如，在 CLanguage 类的外部，添加如下代码：
clang = CLanguage()
print(clang.name)
print(clang.add)

# 注意，因为 类属性 为所有实例化对象共有，通过类名修改 类属性 的值，会影响所有的实例化对象。例如，在 CLanguage 类体外部，添加如下代码：
print("修改前，各类对象中 类属性 的值：")
clang1 = CLanguage()
print(clang1.name)
print(clang1.add)
clang2 = CLanguage()
print(clang2.name)
print(clang2.add)
print("修改后，各类对象中 类属性 的值：")
CLanguage.name = "Python教程Python教程"
CLanguage.add = "http://c.biancheng.net/pythonhttp://c.biancheng.net/python"
print(clang1.name)
print(clang1.add)
print(clang2.name)
print(clang2.add)
# 显然，通过类名修改 类属性，会作用到所有的实例化对象（例如这里的 clang1 和 clang2）。
# 注意，通过 类的对象 是无法修改 类属性 的。通过 类的对象 对 类属性 赋值，其本质将不再是修改 类属性 的值，而是在给该 对象 定义新的 实例变量。

# 值得一提的是，除了可以通过 类名 访问 类属性 之外，还可以动态地为 类和对象 添加 类属性。例如，在 CLanguage 类的基础上，添加以下代码：
clang = CLanguage()
CLanguage.catalog = 13
print(clang.catalog)
print(CLanguage.catalog)

# 实例属性
# 实例变量指的是在任意类方法内部，以 “self.变量名” 的方式定义的变量，其特点是只作用于调用方法的 对象。另外，实例变量 只能通过对象名访问，无法通过类名访问。
class CLanguage:
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    # 下面定义了一个say实例方法
    def say(self):
        self.catalog = 13
# 此 CLanguage 类中，name、add 以及 catalog 都是实例变量。其中，由于 __init__() 函数在创建 类的对象 时会自动调用，而 say() 方法需要 类的对象 手动调用。因此，CLanguage 类的 类的对象 都会包含 name 和 add 实例变量，而只有调用了 say() 方法的 类的对象，才包含 catalog 实例变量。
clang = CLanguage()
print(clang.name)
print(clang.add)
# 由于 clang 对象未调用 say() 方法，因此其没有 catalog 变量，下面这行代码会报错
# print(clang.catalog)

clang2 = CLanguage()
print(clang2.name)
print(clang2.add)
# 只有调用 say()，才会拥有 catalog 实例变量
clang2.say()
print(clang2.catalog)

# 前面讲过，通过 类的对象 可以访问 类属性，但无法修改 类属性 的值。这是因为，通过 类的对象 修改 类属性 的值，不是在给 “类属性赋值”，而是定义新的 实例变量。例如：
class CLanguageCLanguage :
    # 下面定义了2个 类属性
    name = "C语言中文网"
    add = "http://c.biancheng.net"
    # 下面定义了一个say实例方法
    def say(self, content):
        print(content)

clang = CLanguageCLanguage()
# clang访问 类属性
print(clang.name)
print(clang.add)
clang.name = "Python教程"
clang.add = "http://c.biancheng.net/python"
# clang 实例变量 的值
print(clang.name)
print(clang.add)
# 类属性 的值
print(CLanguageCLanguage.name)
print(CLanguageCLanguage.add)
# 显然，通过 类的对象 是无法修改 类属性 的值的，本质其实是给 clang 对象新添加 name 和 add 这 2 个 实例变量。
# 类中，实例变量 和 类属性 可以同名，但这种情况下使用 类的对象 将无法调用 类属性，它会首选 实例变量，这也是 不推荐“类属性使用对象名调用” 的原因。

# 另外，和 类属性 不同，通过某个 对象 修改 实例变量 的值，不会影响类的其它 实例化对象，更不会影响同名的 类属性。例如：
class CLanguage :
    name = "xxx"  # 类属性
    add = "http://"  # 类属性
    def __init__(self):
        self.name = "C语言中文网"   # 实例变量
        self.add = "http://c.biancheng.net"   # 实例变量
    # 下面定义了一个say实例方法
    def say(self):
        self.catalog = 13  # 实例变量
clang = CLanguage()
# 修改 clang 对象的 实例变量
clang.name = "python教程"
clang.add = "http://c.biancheng.net/python"
print(clang.name)
print(clang.add)
clang2 = CLanguage()
print(clang2.name)
print(clang2.add)
# 输出 类属性 的值
print(CLanguage.name)
print(CLanguage.add)
# 不仅如此，Python 只支持为 特定的对象 添加 实例变量。例如，在之前代码的基础上，为 clang 对象添加 money 实例变量，实现代码为：
clang.money = 30
print(clang.money)
# print(clang2.money) # 'CLanguage' object has no attribute 'money'

# 除了实例变量，类方法中还可以定义 局部变量。和前者不同，局部变量 直接以 “变量名=值” 的方式进行定义，例如：
class CLanguage:
    # 下面定义了一个say实例方法
    def count(self, money):
        sale = 0.8 * money
        print("优惠后的价格为：", sale) # sale为 局部变量
clang = CLanguage()
clang.count(100)