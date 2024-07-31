#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 程序运行时常会碰到一些错误，例如除数为 0、年龄为负数、数组下标越界等，这些错误如果不能发现并加以处理，很可能会导致程序崩溃。
# 和 C++、Java 这些编程语言一样，Python 也提供了处理异常的机制，可以让我们捕获并处理这些错误，让程序继续沿着一条不会出错的路径执行。
# 可以简单的理解异常处理机制，就是在程序运行出现错误时，让 Python 解释器执行事先准备好的 除错程序，进而尝试 恢复程序 的执行。
# Python 异常处理机制会涉及 try、except、else、finally 这 4 个关键字，同时还提供了可主动使程序引发异常的 raise 语句。

# a = 1 / 0

# 以上运行输出结果中，前两段指明了错误的位置，最后一句表示出错的类型。在 Python 中，把这种运行时产生错误的情况叫做异常（Exceptions）。这种异常情况还有很多，常见的几种异常情况如表 1 所示。
# 当一个程序发生异常时，代表该程序在执行时出现了非正常的情况，无法再执行下去。默认情况下，程序是要终止的。如果要避免程序退出，可以使用捕获异常的方式获取这个异常的名称，再通过其他的逻辑代码让程序继续运行，这种根据异常做出的逻辑处理叫作 异常处理。

# try except 语句的执行流程如下：
# 首先执行 try 中的代码块，如果执行过程中出现异常，系统会自动生成一个异常类型，并将该异常提交给 Python 解释器，此过程称为 捕获异常。
# 当 Python 解释器收到异常对象时，会寻找能处理该异常对象的 except 块，如果找到合适的 except 块，则把该 异常对象 交给该 except 块处理，这个过程被称为 处理异常。如果 Python 解释器找不到处理异常的 except 块，则 程序运行终止，Python 解释器也将退出。
# 事实上，不管程序代码块是否处于 try 块中，甚至包括 except 块中的代码，只要执行该代码块时出现了异常，系统都会 自动生成 对应类型的异常。但是，如果此段程序没有用 try 包裹，又或者没有为该异常配置处理它的 except 块，则 Python 解释器将无法处理，程序就会停止运行；反之，如果程序发生的异常经 try 捕获并由 except 处理完成，则程序可以继续执行。
try:
    c = 1 / 0
    print("您输入的两个数相除的结果是：", c)
except (ValueError, ArithmeticError):
    print("程序发生了数字格式异常、算术异常之一")
except :
    print("未知异常")
print("程序继续运行") # 由于 try 块中引发了异常，并被 except 块成功捕获，因此程序才可以继续执行，才有了 “程序继续运行” 的输出结果。

# 其实，每种异常类型都提供了如下几个属性和方法，通过调用它们，就可以获取当前处理异常类型的相关信息：
# args：返回异常的错误编号和描述字符串；
# str(e)：返回异常信息，但不包括异常信息的类型；
# repr(e)：返回较全的异常信息，包括异常信息的类型。
try:
    1/0
except Exception as e:
    # 访问异常的错误编号和详细信息
    print(e.args)
    print(str(e))
    print(repr(e))

# 使用 else 包裹的代码，只有当 try 块没有捕获到任何异常时，才会得到执行；反之，如果 try 块捕获到异常，即便调用对应的 except 处理完异常，else 块中的代码也不会得到执行。跟for循环里的else很像。
try:
    result = 20 / int( input('请输入除数:') )
    print(result)
except ValueError:
    print('必须输入整数')
except ArithmeticError:
    print('算术错误，除数不能为 0')
else:
    print('没有出现异常')
print("继续执行")
# 如上所示，当我们输入正确的数据时，try 块中的程序正常执行，Python 解释器执行完 try 块中的程序之后，会继续执行 else 块中的程序，继而执行后续的程序。

# Python 异常处理机制还提供了一个 finally 语句，通常用来为 try 块中的程序做扫尾清理工作。
# 注意，和 else 语句不同，finally 只要求和 try 搭配使用，而至于该结构中是否包含 except 以及 else，对于 finally 不是必须的（else 必须和 try except 搭配使用）。
# 在整个异常处理机制中，finally 语句的功能是：无论 try 块是否发生异常，最终都要进入 finally 语句，并执行其中的代码块。
# Python 垃圾回收机制，只能帮我们回收变量、类对象占用的内存，而无法自动完成类似关闭文件、数据库连接等这些的工作。
# 读者可能会问，回收这些物理资源，必须使用 finally 块吗？当然不是，但使用 finally 块是比较好的选择。首先，try 块不适合做资源回收工作，因为一旦 try 块中的某行代码发生异常，则其后续的代码将不会得到执行；其次 except 和 else 也不适合，它们都可能不会得到执行。而 finally 块中的代码，无论 try 块是否发生异常，该块中的代码都会被执行。
try:
    a = int(input("请输入 a 的值:"))
    print(20 / a)
except:
    print("发生异常！")
else:
    print("执行 else 块中的代码")
finally:
    print("执行 finally 块中的代码")
# 可以看到，当 try 块中代码 未发生 异常时，except 块不会执行，else 块和 finally 块中的代码会被执行。
# 可以看到，当 try 块中代码 发生 异常时，except 块得到执行，而 else 块中的代码将不执行，finally 块中的代码仍然会被执行。
# finally 块的强大还远不止此，即便当 try 块发生异常，且没有合适和 except 处理异常时，finally 块中的代码也会得到执行。例如：
try:
    # 发生异常
    # print(20/0)
    pass
finally:
    print("程序终止，仍然会 执行 finally 块中的代码")

# 在前面章节的学习中，遗留过一个问题，即是否可以在程序的指定位置手动抛出一个异常？答案是肯定的，Python 允许我们在程序中手动设置异常，使用 raise 语句即可。
# 当然，我们手动让程序引发异常，很多时候并不是为了让其 崩溃。事实上，raise 语句引发的异常通常用 try except（else finally）异常处理结构来 捕获 并进行处理。例如：
try:
    a = input("输入一个数：")
    # 判断用户输入的是否为数字
    if (not a.isdigit()):
        raise ValueError("a 必须是数字")
except ValueError as e:
    print("引发异常：", repr(e))

# raise 不需要参数
try:
    a = input("输入一个数：")
    if (not a.isdigit()):
        raise ValueError("a 必须是数字")
except ValueError as e:
    print("引发异常：", repr(e))
    # raise # 这里重点关注位于 except 块中的 raise，由于在其之前我们已经手动引发了 ValueError 异常，因此这里当再使用 raise 语句时，它会再次引发一次。

# 当在没有引发过异常的程序使用无参的 raise 语句时，它默认引发的是 RuntimeError 异常。例如：
try:
    a = input("输入一个数：")
    if (not a.isdigit()):
        raise
except RuntimeError as e:
    print("引发异常：", repr(e))