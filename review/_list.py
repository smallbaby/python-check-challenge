# -*- coding: utf-8 -*-
# Author: kaizhang01
# Date: 2018/12/6
# Desc:



class Array(object):
    """定长集合"""

    def __init__(self, size=32):
        self.size = size
        self._items = [None] * self.size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self.size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    """链接表"""

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)
        if self.tailnode is None:
            self.tailnode = node

        headnode = self.root.next
        self.root.next = node
        node.next = headnode
        self.length += 1

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        currnode = self.root.next
        while currnode is not self.tailnode:
            yield currnode
            currnode = currnode.next
        if currnode is not None:
            yield currnode

    def remove(self, value):
        prevnode = self.root
        for currnode in self.iter_node():
            if currnode.value == value:
                prevnode.next = currnode.next
                if currnode is self.tailnode:
                    self.tailnode = prevnode
                del currnode
                self.length -= 1
                return 1
            else:
                prevnode = currnode
        return -1

    def find(self, value):
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1

    def popleft(self):
        if self.root.next is None:
            raise Exception('pop from empty linklist')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value

        if self.tailnode is headnode:
            self.tailnode = None
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0
        self.tailnode = None


class CircularDoubleLinkedList(object):
    """循环双端队列"""

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is None and len(self) >= self.maxsize:
            raise Exception('List  is Full')
        node = Node(value)
        tailnode = self.tailnode() or self.root
        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is None or len(self) >= self.maxsize:
            raise Exception('List is Full')
        node = Node(value)

        if self.root.next is self.root:
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.prev = self.root
            headnode = self.root.next
            node.next = headnode
            headnode.prev = node
            self.root.next = node
        self.length += 1

    def remove(self, node):
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        currnode = self.root.next
        while currnode.next is not self.root:
            yield currnode
            currnode = currnode.next
        yield currnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return

        currnode = self.root.prev
        while currnode.prev is not self.root:
            yield currnode
            currnode = currnode.prev
        yield currnode

    def pop(self):
        pass

    def popleft(self):
        pass
