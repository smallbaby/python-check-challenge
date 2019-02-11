# -*- coding: utf-8 -*-
# Author: kaizhang01
# Date: 2019/1/16
# Desc:


def quick(data: list) -> list:
    _l = len(data)
    for i in range(0, _l - 1):
        for j in range(0, _l - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


# quick sort
def quickSort(array):
    if len(array) < 2:  # 基线条件（停止递归的条件）
        return array
    else:  # 递归条件
        baseValue = array[0]  # 选择基准值
        less, equal, greater = [], [baseValue], []
        for m in array[1:]:
            if m < baseValue:
                # 由所有小于基准值的元素组成的子数组
                less.append(m)
            elif m > baseValue:
                # 由所有大于基准值的元素组成的子数组
                greater.append(m)
            else:
                # 包括基准在内的同时和基准相等的元素，在上一个版本的百科当中，并没有考虑相等元素
                equal.append(m)
        return quickSort(less) + equal + quickSort(greater)


d = quick([2, 56, 1, 5, 72, 2, 7, 8, 9, 2, 34])
print(d)


def quickSort(array):
    if len(array) < 2:
        return array
    else:
        # 基准
        base = array[0]
        l, c, g = [], [base], []

        for x in array[1:]:
            if x < base:
                l.append(x)

            elif x > base:
                g.append(x)
            else:
                c.append(x)
        return quickSort(l) + c + quickSort(g)


print(quickSort([5, 2, 8, 2, 4, 9, 2, 3]))

quick_sort = lambda array: array if len(array) <= 1 else quick_sort(
    [item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort(
    [item for item in array[1:] if item > array[0]])

qs = lambda d: d if len(d) <= 1 else qs([i for i in d[1:] if i <= d[0]]) + [d[0]] + qs([i for i in d[1:] if i > d[0]])
print(qs([4, 2, 7, 3, 72, 9, 8, 6, 45]))

qs = lambda x: x if len(x) <= 1 else qs([i for i in x[1:] if i <= x[0]]) + [x[0]] + qs([i for i in x[1:] if i > x[0]])
print(qs([6, 43, 7, 8, 23, 11, 99, 12]))


def qs(x):
    if len(x) < 2:
        return x
    else:
        base = x[0]
        l, e, g = [], [base], []
        for i in x[1:]:
            if i < base:
                l.append(i)
            elif i > base:
                g.append(i)
            else:
                e.append(i)
        return qs(l) + e + qs(g)


print(qs([5, 2, 8, 2, 4, 5, 8, 2, 2, 9, 6, 4]))

import itertools

_l = list(itertools.permutations([0, 1, 2], 3))


def helloworld(fn):
    pass


def quick(x):
    if len(x) <= 2:
        return x
    else:
        _base = x[0]
        l, e, g = [], [_base], []
        for m in x[1:]:
            if m < _base:
                l.append(m)
            elif m > _base:
                g.append(m)
            else:
                e.append(m)
        return quick(l) + e + quick(g)


quick = lambda x: x if len(x) <= 1 else quick([i for i in x[1:] if i <= x[0]]) + [x[0]] + quick(
    [i for i in x[1:] if i > x[0]])
print(quick([2, 4, 6, 9, 1, 0, 5, 4, 1, 4, 5]))


def binarySearch(x, k):
    left, right = 0, len(x) - 1
    while left <= right:
        mid = int((left + right) / 2)
        print(left, right, mid, len(x))
        if k < x[mid]:
            right = mid - 1
        elif k > x[mid]:
            left = mid + 1
        else:
            return mid


x = binarySearch([2, 4, 8, 9, 12, 34], 34)
print(x)


def binary_search(x, _k):
    left, right = 0, len(x) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if _k > x[mid]:
            left = mid + 1
        elif _k < x[mid]:
            right = mid - 1
        else:
            return (mid)


x = binary_search([2, 4, 8, 9, 12, 34], 2)
print(x)

# 算法
# hadoop运行过程
# spark/ scala /


qc = lambda x: x if len(x) <= 1 else qc([i for i in x[1:] if i <= x[0]]) + [x[0]] + qc([i for i in x[1:] if i > x[0]])
print(qc([5, 3, 7, 4, 8, 4, 10, 2, 7]))


def qc(x):
    if len(x) <= 1:
        return x
    else:
        _b = x[0]
        l, e, h = [], [x[0]], []

        for m in x[1:]:
            if m > _b:
                h.append(m)
            elif m < _b:
                l.append(m)
            else:
                e.append(m)
        return qc(l) + e + qc(h)


print(qc([5, 3, 8, 5, 2, 9, 4, 5, 0]))


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LList:
    def __init__(self):
        self.head_ = None

    def is_empty(self):
        return self.head_ is None

    def prepend(self, elem):
        self.head_ = Node(elem, self.head_)

    def pop(self):
        if self.head_ is None:
            return None
        else:
            e = self.head_.data
            self.head_ = self.head_.next
            return e

    def append(self, elem):
        if self.head_ is None:
            self.head_ = Node(elem)
            return
        p = self.head_
        while p.next is not None:
            p = p.next
        p.next = Node(elem)


qs1 = lambda x: x if len(x) <= 1 else qs1(i for i in x[1:] if i <=x[0]) + [x[0]] + qs1(i for i in x[1:] if i>x[0])
