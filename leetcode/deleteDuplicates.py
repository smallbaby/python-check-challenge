# -*- coding: utf-8 -*-
# Author: kaizhang01

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        current = head
        while current.next is not None:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(2)
    a.next = b
    b.next = c
    h = Solution().deleteDuplicates(a)
    while h:
        print(h.val)
        h = h.next
