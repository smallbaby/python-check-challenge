# -*- coding: utf-8 -*-
# Author: kaizhang01
# Date: 2019/1/12
# Desc:
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def reverse(self, head):
        last = None
        while head:
            temp = head.next
            head.next = last
            last = head
            head = temp
