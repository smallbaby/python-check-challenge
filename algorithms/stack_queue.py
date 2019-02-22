# -*- coding: utf-8 -*-
# Author: kaizhang01
# Date: 2019/2/11
# Desc:

class queue:
    def __init__(self, head, tail):
        self.data = []
        self.head = head
        self.tail = tail


def test_qq():
    q = [0, 6, 3, 1, 7, 5, 8, 9, 2, 4]
    head = 0
    tail = len(q) - 1
    while (head < tail):
        print(q[head])
        head += 1
        q[tail] = q[head]
        tail += 1
        head += 1


if __name__ == '__main__':
    test_qq()
