# -*- coding:utf8 -*-
import random

# 第一步生成10个随机数
numbers = [random.randint(0,10000) for _ in range(10)]
print numbers

# output
'''

[7584, 5108, 321, 4713, 875, 9525, 3631, 1007, 5784, 4972]

'''

# TODO : 不重复的随机数
# 查了文档，python直接提供了不重复的函数
# random.sample(list,k)   从list随机获取k个不重复的数

print random.sample(xrange(10000000), 1000)

# 查看sample源码探个究竟

