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
