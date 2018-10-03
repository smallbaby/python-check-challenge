# -*- coding: utf-8 -*-


def test():
    list = range(3)
    for i in list:
        yield i*i


generator = test()
for i in generator:
    print(i)


import itertools
horse = [1,2,3,4]
print(list(itertools.permutations(horse)))