"""
python test.py --input 3 --output 4
python test.py -i 3 -o 4
"""

# 方式一
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--input')
# parser.add_argument('--output')
# args = parser.parse_args()
# print(args.input)
# print(args.output)

# 方式二
import sys
import getopt

# argv0 = sys.argv[0]
# argv1 = sys.argv[1]
# argv2 = sys.argv[2]
# print(argv0)
# print(argv1)
# print(argv2)

# 方式三
(opts, args) = getopt.getopt(sys.argv[1:], "hi:o:", ["input=", "output=", "help"])
input_file = ""
output_file = ""
for op, value in opts:
    if op == "-i" or op == "--input":
        input_file = value
    elif op in ["-o", "--output"]: # python中的if in用法是一种非常常见的条件语句,它可以用来判断一个元素是否在一个序列中.在python中序列可以是列表\元组\字符串等.
        output_file = value
    elif op == "-h":
        print("帮助信息")
        sys.exit()
print("input_file =", input_file)
print("output_file = %s" % output_file)