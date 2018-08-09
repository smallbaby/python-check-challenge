# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/7/26 
# Desc:  协程测试

def lazy_range(number):
    index = 0
    while index <= number:
        yield index
        index += 1


def jumping_range(number):
    index = 0
    while index <= number:
        jump = yield index
        if jump is None:
            jump = 1
        index += jump

# def lazy_ranges(number):
#     index = 0
#     def gratuitous_refactor():
#         while index < number:
#             yield index
#             index += 1
#     yield from gratuitous_refactor()


iter = jumping_range(100)
print(next(iter))
print(iter.send(10))


import async








