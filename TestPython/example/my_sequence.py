#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## 序列

# str
s = "C语言中文网"
print(s[0], "==", s[-6])
print(s[5], "==", s[-1])

# sname[start : end : step]
s = "C语言中文网"
# 取索引区间为[0, 2)之间的字符串
print(s[:2])
# 隔1个字符取一个字符，区间是整个字符串
print(s[::2])
# 取整个字符串，此时[]中只需一个冒号即可
print(s[:])

s = "c.biancheng.net"
print("C语言" + "中文网:" + s)