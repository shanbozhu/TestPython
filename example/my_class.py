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

# 和 类属性 一样，类的方法 也可以进行更细致的划分，具体可分为 类方法、实例方法和静态方法。
# 和 类属性 的分类不同，对于初学者来说，区分这 3 种 类的方法 是非常简单的，即采用 @classmethod 修饰的方法为 类方法；采用 @staticmethod 修饰的方法为 静态方法；不用任何修改的方法为 实例方法。
class CLanguage:
    # 类构造方法，也属于 实例方法
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    # 下面定义了一个say 实例方法
    def say(self):
        print("正在调用 say() 实例方法")
# 实例方法 最大的特点就是，它最少也要包含一个 self 参数，用于绑定调用此方法的 实例对象（Python 会自动完成绑定）。实例方法 通常会用 类的对象 直接调用，例如：
clang = CLanguage()
clang.say()
# 当然，Python 也支持使用 类名 调用 实例方法，但此方式需要手动给 self 参数传值。例如：
# 类名 调用 实例方法，需手动给 self 参数传值
clang = CLanguage()
CLanguage.say(clang)

# Python 类方法 和 实例方法 相似，它最少也要包含一个参数，只不过 类方法 中通常将其命名为 cls，Python 会自动将 类本身 绑定给 cls 参数（注意，绑定的不是 类对象）。也就是说，我们在调用 类方法 时，无需显式为 cls 参数传参。
class CLanguage:
    # 类构造方法，也属于 实例方法
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    # 下面定义了一个类方法
    @classmethod
    def info(cls):
        print("正在调用类方法", cls)
# 类方法推荐使用 类名 直接调用，当然也可以使用 实例对象 来调用（不推荐）。
# 使用 类名 直接调用 类方法
CLanguage.info()
# 使用 类的对象 调用 类方法
clang = CLanguage()
clang.info()

# 静态方法，其实就是我们学过的函数，和函数唯一的区别是，静态方法定义在类这个空间（类命名空间）中，而函数则定义在程序所在的空间（全局命名空间）中。
# 静态方法没有类似 self、cls 这样的特殊参数，因此 Python 解释器不会对它包含的参数做任何类或对象的绑定。也正因为如此，类的静态方法中无法调用任何 类的属性 和 类的方法。
class CLanguage:
    @staticmethod
    def info(name, add):
        print(name, add)
# 静态方法的调用，既可以使用类名，也可以使用类对象，例如：
# 使用 类名 直接调用 静态方法
CLanguage.info("C语言中文网","http://c.biancheng.net")
# 使用 类的对象 调用 静态方法
clang = CLanguage()
clang.info("Python教程","http://c.biancheng.net/python")
# 在实际编程中，几乎不会用到 类方法 和 静态方法，因为我们完全可以使用函数代替它们实现想要的功能，但在一些特殊的场景中（例如工厂模式中），使用 类方法 和 静态方法 也是很不错的选择。

# 通过前面的学习，类方法大体分为 3 类，分别是 类方法、实例方法和静态方法，其中 实例方法 用的是最多的。我们知道，实例方法 的调用方式其实有 2 种，既可以采用 类的对象 调用，也可以直接通过 类名 调用。
# 如果想通过类名直接调用实例方法，就必须手动为 self 参数传值。
class CLanguage:
    def info(self):
        print("我正在学 Python")
clang = CLanguage()
# 通过 类名 直接调用 实例方法
CLanguage.info(clang) # 读者想想也应该明白，self 参数需要的是方法的 实际调用者（是 类的对象），而这里只提供了 类名，当然无法自动传值。

# 值得一提的是，上面的报错信息只是让我们手动为 self 参数传值，但并没有规定必须传一个该 类的对象，其实完全可以任意传入一个参数，例如：
class CLanguage:
    def info(self):
        print(self, "正在学 Python")
# 通过 类名 直接调用 实例方法
CLanguage.info("zhangsan")
# 可以看到，"zhangsan" 这个字符串传给了 info() 方法的 self 参数。显然，无论是 info() 方法中使用 self 参数调用其它类方法，还是使用 self 参数定义新的实例变量，胡乱的给 self 参数传参都将会导致程序运行崩溃。

# 用类的 实例对象 访问 类成员 的方式称为 绑定方法，而用 类名 调用 类成员 的方式称为 非绑定方法。

# 描述符类
# 本质上看，描述符就是一个类，只不过它定义了另一个类中属性的访问方式。换句话说，一个类可以将属性管理全权委托给描述符类。
# 从这个例子可以看到，如果一个类的某个属性有数据描述符，那么每次查找这个属性时，都会调用描述符的 __get__() 方法，并返回它的值；同样，每次在对该属性赋值时，也会调用 __set__() 方法。
class revealAccess:
    def __init__(self, initval = None, name = 'var'):
        self.val = initval
        self.name = name
    def __get__(self, obj, objtype):
        print("Retrieving", self.name)
        return self.val
    def __set__(self, obj, val):
        print("updating", self.name)
        self.val = val
class myClass:
    x = revealAccess(10,'var "x"')
    y = 5
m = myClass()
print(m.x)
m.x = 20
print(m.x)
print(m.y)

# 前面章节中，我们一直在用 “类的对象.属性” 的方式访问类中定义的 属性，其实这种做法是欠妥的，因为它破坏了类的封装原则。正常情况下，类包含的 属性 应该是 隐藏 的，只允许通过类提供的 方法 来 间接 实现对 类的属性 的访问和操作。
# 因此，在不破坏类封装原则的基础上，为了能够有效操作类中的 属性，类中应包含读（或写） 类的属性 的多个 getter（或 setter）方法，这样就可以通过 “类的对象.方法(参数)” 的方式操作属性，例如：
class CLanguage:
    # 构造函数
    def __init__(self, name):
        self.name = name
        # 设置 name 属性值的函数
    def setname(self, name):
        self.name = name
    # 访问nema属性值的函数
    def getname(self):
        return self.name
    # 删除name属性值的函数
    def delname(self):
        self.name = "xxx"
clang = CLanguage("C语言中文网")
# 获取name属性值
print(clang.getname())
# 设置name属性值
clang.setname("Python教程")
print(clang.getname())
# 删除name属性值
clang.delname()
print(clang.getname())

# 可能有读者觉得，这种操作 类的属性 的方式比较麻烦，更习惯使用 “类的对象.属性” 这种方式。
# 庆幸的是，Python 中提供了 property() 函数，可以实现在不破坏 类封装 原则的前提下，让开发者依旧使用 “类的对象.属性” 的方式操作类中的 属性。

# 例如，修改上面的程序，为 name 属性配置 property() 函数：
# property() 函数的基本使用格式：属性名=property(fget=None, fset=None, fdel=None, doc=None)
# 注意，在使用 property() 函数时，以上 4 个参数可以仅指定第 1 个、或者前 2 个、或者前 3 个，也可以全部指定。也就是说，property() 函数中参数的指定 并不是完全随意的。
class CLanguage:
    # 构造函数
    def __init__(self,n):
        self.__name = n
    # 设置 name 属性值的函数
    def setname(self,n):
        self.__name = n
    # 访问 name 属性值的函数
    def getname(self):
        return self.__name
    # 删除 name 属性值的函数
    def delname(self):
        self.__name="xxx"
    # 为 name 属性配置 property() 函数
    name = property(getname, setname, delname, '指明出处')
# 调取说明文档的 2 种方式
print(CLanguage.name.__doc__)
help(CLanguage.name)
clang = CLanguage("C语言中文网")
# 调用 getname() 方法
print(clang.name)
# 调用 setname() 方法
clang.name = "Python教程"
print(clang.name)
# 调用 delname() 方法
del clang.name
print(clang.name)
# 注意，在此程序中，由于 getname() 方法中需要返回 name 属性，如果使用 self.name 的话，其本身又被调用 getname()，这将会先入无限死循环。为了避免这种情况的出现，程序中的 name 属性必须设置为 私有属性，即使用 __name（前面有 2 个下划线）。
# 当然，property() 函数也可以少传入几个参数。以上面的程序为例，我们可以修改 property() 函数如下所示
# name = property(getname, setname)
# 这意味着，name 是一个可读写的属性，但不能删除，因为 property() 函数中并没有为 name 配置用于函数该属性的方法。也就是说，即便 CLanguage 类中设计有 delname() 函数，这种情况下也不能用来删除 name 属性。
# 同理，还可以像如下这样使用 property() 函数：
# name = property(getname)    # name 属性可读，不可写，也不能删除
# name = property(getname, setname, delname)    # name属性可读、可写、也可删除，就是没有说明文档

# 封装、继承和多态
# 注意，封装绝不是将类中所有的方法都隐藏起来，一定要留一些像键盘、鼠标这样可供外界使用的 类的方法。
# Python 类中的 变量和函数，不是公有的（类似 public 属性），就是私有的（类似 private），这 2 种属性的区别如下：
# public：公有属性的 类的变量和类的函数，在类的外部、类内部以及子类（后续讲继承特性时会做详细介绍）中，都可以正常访问；
# private：私有属性的 类的变量和类的函数，只能在 本类内部 使用，类的外部 以及 子类 都无法使用。

# 但是，Python 并没有提供 public、private 这些修饰符。为了实现类的封装，Python 采取了下面的方法：
# 默认情况下，Python 类中的变量和方法都是公有（public）的，它们的名称前都没有下划线（_）；
# 如果类中的变量和函数，其名称以双下划线 “__” 开头，则该变量（函数）为 私有变量（私有函数），其属性等同于 private。
# 除此之外，还可以定义以单下划线 “_” 开头的 类的属性 或者 类的方法（例如 _name、_display(self)），这种 类的属性 和 类的方法 通常被 视为 私有属性和私有方法，虽然它们也能通过 类的对象正常访问，但这是一种 约定俗成 的用法，初学者一定 要遵守。
# 注意，Python 类中还有以 双下划线开头和结尾 的类的方法（例如类的构造函数__init__(self)），这些都是 Python 内部定义的，用于 Python 内部调用。我们自己定义 类的属性 或者 类的方法 时，不要 使用这种格式。
class CLanguage:
    def setname(self, name):
        if len(name) < 3:
            raise ValueError('名称长度必须大于3！')
        self.__name = name
    def getname(self):
        return self.__name
    # 为 name 配置 setter 和 getter 方法
    name = property(getname, setname)

    def setadd(self, add):
        if add.startswith("http://"):
            self.__add = add
        else:
            raise ValueError('地址必须以 http:// 开头')
    def getadd(self):
        return self.__add
    # 为 add 配置 setter 和 getter 方法
    add = property(getadd, setadd)

    # 定义个私有方法
    def __display(self):
        print(self.__name, self.__add)

clang = CLanguage()
clang.name = "C语言中文网"
clang.add = "http://c.biancheng.net"
print(clang.name)
print(clang.add)
# 尝试调用私有的 display() 方法
# clang.__display() # 私有的，无法在 类外部 访问

# Python继承机制及其使用
# 子类继承父类时，只需在定义子类时，将父类（可以是多个）放在子类之后的圆括号里即可。
# 注意，如果该类没有 显式 指定继承自哪个类，则 默认 继承 object 类（object 类是 Python 中 所有类的父类，即要么是 直接父类，要么是 间接父类）。另外，Python 的继承是 多继承 机制（和 C++ 一样），即一个 子类 可以同时拥有 多个 直接父类。
class People:
    def say(self):
        print("我是一个人，名字是：", self.name)
class Animal:
    def display(self):
        print("人也是高级动物")
# 同时继承 People 和 Animal 类
# 其同时拥有 name 属性、say() 和 display() 方法
class Person(People, Animal):
    pass
zhangsan = Person()
zhangsan.name = "张三"
zhangsan.say()
zhangsan.display()
# 没错，子类拥有父类 所有的 属性和方法，即便该 属性或方法 是 私有（private）的。

# 事实上，大部分面向对象的编程语言，都只支持单继承，即子类有且只能有一个 直接父类。而 Python 却支持多继承（C++也支持多继承）。
# 和单继承相比，多继承容易让代码 逻辑复杂、思路混乱，一直备受争议，中小型项目中较少使用，后来的 Java、C#、PHP 等干脆取消了多继承。
# 使用多继承经常需要面临的问题是，多个父类中包含同名的类方法。对于这种情况，Python 的处置措施是：根据子类继承多个父类时这些父类的前后次序决定，即 排在前面 父类中的类的方法会 覆盖 排在后面 父类中的同名类的方法。
class People:
    def __init__(self):
        self.name = People
    def say(self):
        print("People类", self.name)
class Animal:
    def __init__(self):
        self.name = Animal
    def say(self):
        print("Animal类", self.name)
# People中的 name 属性和 say() 会覆盖 Animal 类中的
class Person(People, Animal):
    pass
zhangsan = Person()
zhangsan.name = "张三"
zhangsan.say()
# 可以看到，当 Person 同时继承 People 类和 Animal 类时，People 类在前，因此如果 People 和 Animal 拥有同名的 类的方法，实际调用的是 People 类中的。
# 虽然 Python 在语法上支持 多继承，但逼不得已，建议大家 不要使用多继承。

# 前面讲过在 Python 中，子类继承了父类，那么子类就拥有了父类所有的 类的属性 和 类的方法。通常情况下，子类会在此基础上，扩展一些新的 类的属性 和 类的方法。
# 但凡事都有例外，我们可能会遇到这样一种情况，即子类从父类继承得来的 类的方法 中，大部分是适合子类使用的，但有个别的 类的方法，并不能直接照搬 父类 的，如果不对这部分 类的方法 进行修改，子类对象 无法使用。针对这种情况，我们就需要在子类中重写父类的方法。
class Bird:
    # 鸟有翅膀
    def isWing(self):
        print("鸟有翅膀")
    # 鸟会飞
    def fly(self):
        print("鸟会飞")
class Ostrich(Bird):
    # 重写Bird类的fly()方法
    def fly(self):
        print("鸵鸟不会飞")
# 创建Ostrich对象
ostrich = Ostrich()
# 调用 Ostrich 类中重写的 fly() 类的方法
ostrich.fly()
# 事实上，如果我们在子类中重写了从父类继承来的 类的方法，那么当在 类的外部 通过 子类对象 调用该方法时，Python 总是会执行 子类 中重写的方法。
# 这就产生一个新的问题，即如果想调用 父类 中被重写的这个方法，该怎么办呢？
# 很简单，前面讲过，Python 中的类可以看做是一个 独立空间，而 类的方法 其实就是出于该空间中的一个函数。而如果想要全局空间中，调用 类空间 中的函数，只需要在 调用该函数时 备注类名 即可。举个例子：
# 调用 Bird 类中的 fly() 方法
Bird.fly(ostrich)
# 此程序中，需要大家注意的一点是，使用 类名 调用其 类的方法，Python 不会 为该方法的第一个 self 参数 自动绑定值，因此采用这种调用方法，需要手动为 self 参数赋值。
# 通过 类名 调用 实例方法 的这种方式，又被称为 未绑定方法。

# 但我们知道，Python 是一门支持多继承的面向对象编程语言，如果子类继承的多个父类中包含同名的类 实例方法，则子类对象在调用该方法时，会优先选择排在 最前面的父类 中的 实例方法。显然，构造方法也是如此。
class People:
    def __init__(self, name):
        self.name = name
    def say(self):
        print("我是人，名字为：", self.name)
class Animal:
    def __init__(self, food):
        self.food = food
    def display(self):
        print("我是动物,我吃", self.food)
# People中的 name 属性和 say() 会覆盖 Animal 类中的
class Person(People, Animal):
    pass
per = Person("zhangsan")
per.say()
# per.display()
# 上面程序中，Person 类同时继承 People 和 Animal，其中 People 在前。这意味着，在创建 per 对象时，其将会调用从 People 继承来的构造函数。因此我们看到，上面程序在创建 per 对象的同时，还要给 name 属性进行赋值。
# 但如果去掉最后一行的注释，运行此行代码，Python 解释器会报错误：
# 从 Animal 类中继承的 display() 方法中，需要用到 food 属性的值，但由于 People 类的构造方法 “覆盖” 了Animal 类的构造方法，使得在创建 per 对象时，Animal 类的 构造方法 未得到执行，所以程序出错。
# 针对这种情况，正确的做法是定义 Person 类自己的 构造方法（等同于 重写 第一个 直接父类 的 构造方法）。

# 但需要注意，如果在 子类 中定义 构造方法，则 必须 在该方法中调用 父类的 构造方法。

# 在子类中的构造方法中，调用父类构造方法的方式有 2 种，分别是：
# 类可以看做一个独立空间，在类的外部调用其中的实例方法，可以向调用普通函数那样，只不过需要额外备注类名（此方式又称为未绑定方法）；
# 使用 super() 函数。但如果涉及多继承，该函数只能调用 第一个 直接父类 的构造方法。
# 也就是说，涉及到多继承时，在子类构造函数中，调用 第一个 父类构造方法的方式有以上 2 种，而调用 其它父类 构造方法的方式只能使用 未绑定方法。
# 值得一提的是，Python 2.x 中，super() 函数的使用语法格式如下：super(Class, obj).__init__(...) ，其中，Class 是子类的 类名，obj 通常指的就是 self。
# 但在 Python 3.x 中，super() 函数有一种更简单的语法格式，推荐大家使用这种格式：super().__init__(...)
class People:
    def __init__(self, name):
        self.name = name
    def say(self):
        print("我是人，名字为：", self.name)
class Animal:
    def __init__(self, food):
        self.food = food
    def display(self):
        print("我是动物，我吃", self.food)
class Person(People, Animal):
    # 自定义构造方法
    def __init__(self, name, food):
        # 调用 People 类的构造方法
        super().__init__(name)
        # super(Person, self).__init__(name) # 执行效果和上一行相同
        # People.__init__(self, name) # 使用未绑定方法调用 People 类构造方法

        # 调用 其它父类 的构造方法，需手动给 self 传值
        Animal.__init__(self, food)
per = Person("zhangsan","熟食")
per.say()
per.display()
# 可以看到，Person 类自定义的 构造方法中，调用 People 类 构造方法，可以使用 super() 函数，也可以使用 未绑定方法。但是调用 Animal 类的 构造方法，只能使用 未绑定方法。

# 我们知道，类方法又可细分为实例方法、静态方法和类方法，Python 语言允许为类动态地添加这 3 种方法；但对于 实例对象，则只允许动态地添加 实例方法，不能添加类方法和静态方法。
class CLanguage:
    pass
# 下面定义了一个实例方法
def info(self):
    print("正在调用实例方法")
# 下面定义了一个类方法
@classmethod
def info2(cls):
    print("正在调用类方法")
# 下面定义个静态方法
@staticmethod
def info3():
    print("正在调用静态方法")
# 类可以动态添加以上 3 种方法，会影响所有实例对象
CLanguage.info = info
CLanguage.info2 = info2
CLanguage.info3 = info3
clang = CLanguage()
# 如今，clang 具有以上 3 种方法
clang.info()
clang.info2()
clang.info3()
# 类实例对象只能动态添加实例方法，不会影响其它实例对象
clang1 = CLanguage()
clang1.info = info
# 必须手动为 self 传值
clang1.info(clang1)

# __slots__ 只能限制为 实例对象 动态添加属性和方法，而无法限制动态地为 类 添加属性和方法。
# __slots__ 属性值其实就是一个元组，只有其中指定的元素，才可以作为动态添加的属性或者方法的名称。
# __slots__ 属性对由该类派生出来的子类，也是不起作用的。__slots__ 属性只对当前所在的类起限制作用。
class CLanguage:
    __slots__ = ('name','add','info')

def info(self, name):
    print("正在调用实例方法", self.name)
clang = CLanguage()
clang.name = "C语言中文网"
# 为 clang 对象动态添加 info 实例方法
clang.info = info
clang.info(clang,"Python教程")

# Python type()函数：动态创建类
# 查看 3.4 的类型
print(type(3.4))
# 查看类的对象的类型
class CLanguage:
    pass
clangs = CLanguage()
print(type(clangs))
# 这里重点介绍 type() 函数的另一种用法，即创建一个新类，先来分析一个样例：
# type(name, bases, dict) 用来创建类，其中 name 表示类的名称；bases 表示一个元组，其中存储的是该类的 父类；dict 表示一个字典，用于表示类内定义的属性或者方法。
# 定义一个实例方法
def say(self):
    print("我要学 Python！")
# 使用 type() 函数创建类
CLanguage = type("CLanguage", (object,), dict(say = say, name = "C语言中文网"))
# 创建一个 CLanguage 实例对象
clangs = CLanguage()
# 调用 say() 方法和 name 属性
clangs.say()
print(clangs.name)
# 可以看到，使用 type() 函数创建的类，和直接使用 class 定义的类并无差别。事实上，我们在使用 class 定义类时，Python 解释器底层依然是用 type() 来创建这个类。

# Python MetaClass元类详解
# 举个例子，根据实际场景的需要，我们要为 多个类 添加一个 name 属性和一个 say() 方法。显然有多种方法可以实现，但其中一种方法就是使用 MetaClass 元类。
# 如果在创建类时，想用 MetaClass 元类动态地修改内部的属性或者方法，则类的创建过程将变得复杂：先创建 MetaClass 元类，然后用元类去创建类，最后使用该类的实例化对象实现功能。
# 定义一个元类
class FirstMetaClass(type):
    # cls代表动态修改的类
    # name代表动态修改的类名
    # bases代表被动态修改的 类的 所有父类
    # attr代表被动态修改的 类的 所有属性、方法组成的字典
    def __new__(cls, name, bases, attrs):
        # 动态为该类添加一个name属性
        attrs['name'] = "C语言中文网"
        attrs['say'] = lambda self: print("调用 say() 实例方法")
        return super().__new__(cls, name, bases, attrs)
# 此程序中，首先可以断定 FirstMetaClass 是一个类。其次，由于该类继承自 type 类，并且内部实现了 __new__() 方法，因此可以断定 FirstMetaCLass 是一个元类。

# 定义类时，指定元类
class CLanguage(object, metaclass=FirstMetaClass):
    pass
clangs = CLanguage()
print(clangs.name)
clangs.say()

class CLanguageCLanguage(object, metaclass=FirstMetaClass):
    pass
clangs1 = CLanguageCLanguage()
print(clangs1.name)
clangs1.say()
# 可以看到，在创建类时，通过在 标注父类 的同时 指定元类（格式为metaclass=元类名），则当 Python 解释器在创建这该类时，FirstMetaClass 元类中的 __new__ 方法就会被调用，从而实现动态修改 类的属性 或者 类的方法 的目的。

# Python 类使用 多态 特性的精髓。其实，Python 在多态的基础上，衍生出了一种更灵活的编程机制。
class WhoSay:
    def say(self, who):
        who.say()
class CLanguage:
    def say(self):
        print("调用的是 Clanguage 类的say方法")
class CPython(CLanguage):
    def say(self):
        print("调用的是 CPython 类的say方法")
class CLinux(CLanguage):
    def say(self):
        print("调用的是 CLinux 类的say方法")
a = WhoSay()
# 调用 CLanguage 类的 say() 方法
a.say(CLanguage())
# 调用 CPython 类的 say() 方法
a.say(CPython())
# 调用 CLinux 类的 say() 方法
a.say(CLinux())
# 在其它教程中，Python 这种由多态衍生出的更灵活的编程机制，又称为“鸭子模型”或“鸭子类型”。