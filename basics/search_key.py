# -*- coding: utf-8 -*-
# Author: kaizhang01
# Date: 2019/1/10
# Desc:


def merge(a, b):
    _l=None# = Node(0)
    head = _l
    while  a != None and b != None:
        if a.val > b.val:
            head.next = b
            b = b.next
        else:
            head.next = a
            a = a.next
        head = head.next
    if a is None:
        head.next = b
    if b is None:
        head.next = a
    return head.next


def sum(item):
    _i, *item = item
    return _i + sum(item) if item else _i

print(sum([1,2,3,4]))
import heapq
heapq.nlargest(1,[1,2])
heapq.nsmallest(2,[1,2,3,4])
portfolio = [{'name': 'IBM', 'shares': 100, 'price': 91.1}]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heap = list(nums)
heapq.heapify(heap) # 排序

# 最小的三个
heapq.heappop(heap)
heapq.heappop(heap)
heapq.heappop(heap) # 三次








def find(key, array):
    row = len(array) - 1
    col = len(array[0]) - 1
    i, j = row, 0
    while (i >= 0 and j <= col):
        if (array[i][j] == key):
            return True
        if key > array[i][j]:
            j += 1
        elif key < array[i][j]:
            i -= 1
    return False


arr = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]

# k = find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
k = find(16, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]])
print(k)
