# -*- coding: utf-8 -*-
# Author: kaizhang01
# Desc:

# 使用heapq实现一个优先级队列
# 利用heapq每次pop总是返回优先级最高的特性

import heapq


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({self.name})'


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (property, self._index, item))

    def pop(self):
        return heapq.heappop(self._queue)[-1]


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item("zhang"), 2)
    q.push(Item("kai"), 3)
    q.push(Item("wu"), 4)
    print(q.pop())
