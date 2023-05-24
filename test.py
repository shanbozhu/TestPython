import json

json_str = "{\"1\": \"2\", \"2\": \"3\"}"

json_dict = json.loads(json_str)
print(json_dict)
json_str = json.dumps(json_dict)
print(json_str)
pass


b5 = "C语言中文网8岁了".encode('UTF-8')
print("b5: ", b5)

str1 = b5.decode('UTF-8')
print("str1: ", str1)


print(100 and 200)
print(45 and 0)
print(0 and 45)
print("" or "http://c.biancheng.net/python/")
print(18.5 or "http://c.biancheng.net/python/")


#将字典转换成列表
dict1 = {'a':100, 'b':42, 'c':9, }
list3 = list(dict1) # 只取key
print(list3)

#将字典转换成元组
dict1 = {'a':100, 'b':42, '1':9}
tup3 = tuple(dict1) # 只取key
print(tup3)

course = ("Python教程",)
print(course)

#将区间转换成元组
range1 = range(1, 6) # 左闭右开区间
tup4 = tuple(range1)
print(tup4)

print(tuple())

# tuplename[start : end : step]
# star: end: step

tup1 = (100, 0.5, -36, 73)
tup2 = (3+12j, -54.6, 99)
# print(tup1+tup2) # 直接打印,没有存储
print(tup1)
print(tup2)