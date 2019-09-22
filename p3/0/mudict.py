# -*- coding: utf-8 -*-
# Author: kaizhang01
# Desc:

from collections import defaultdict

d = defaultdict(list)
d['a'].append('hello')
d['a'].append('world')
print(d['a'])

# OrderedDict 内部维护着一个根据键插入顺序排序的双向链表
from collections import OrderedDict

d = OrderedDict()
d['a'] = 4
d['e'] = 3
d['c'] = 2
d['d'] = 1
for key in d:
    print(key, d[key])

# 字典运算
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))
print(sorted(zip(prices.values(), prices.keys())))

# 查找俩个字典的相同点
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}
print(a.keys() & b.keys())

a = [1, 2, 3, 333, 4, 5, 6, 7, 6, 7]
print(set(a))


def dedupe(items):
    se = set()
    for item in items:
        if item not in se:
            yield item
            se.add(item)


print(list(dedupe(a)))

a = 'abcde'
CUT = slice(1, 3)
print(a[CUT])

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

wc = Counter(words)
print(wc.most_common(3))
