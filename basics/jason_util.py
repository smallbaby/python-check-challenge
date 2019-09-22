# -*- coding: utf-8 -*-
# Author: kaizhang01

from decimal import Decimal
from decimal import localcontext


class Node:
    def __init__(self, val):
        self._value = val
        self._children = []

    def __repr__(self):
        return f'Node({self._value})'

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


def _round(k, p):
    """四舍五入
       P > 0 四舍五入
       P < 0 末尾变为p个0
    """
    return round(k, p)


def _dec_oper(a, b):
    return Decimal(a) + Decimal(b)


def _dec_division(a, b):
    a = Decimal(a)
    b = Decimal(b)
    with localcontext() as ctx:
        ctx.prec = 30
        return a / b


def frange(start, end, incr):
    x = start
    while x < end:
        yield x
        x += incr


def binary_conversion(k):
    """进制转换
        bin: 二进制
        oct: 八进制
        hex: 十六进制
    """
    return (bin(k), oct(k), hex(k))

def ip_topN(file, n=100):
    """

    :param file:
    :param n:
    :return:
    """
    # 生成ip
    pass




def str_add_int(a: str = "123", b: int = 60) -> str:
    """
    字符串加整数，返回字符串
    :param a: 字符串
    :param b: 整数
    :return:  字符串
    """
    i = -1
    a = list(a)
    _delt=[]
    a.insert(0, '0')
    while b > 0:
        tmp = b % 10
        b = int(b / 10)
        if abs(i+1) >= len(a):
            _delt.insert(0, str(tmp))
            continue
        curr = int(a[i]) + tmp
        j = i
        if curr >= 10:
            while curr >= 10:
                a[j] = str(curr % 10)
                _s = int(a[j - 1]) + 1
                if _s < 10:
                    a[j - 1] = str(_s)
                    break
                else:
                    curr = _s
                    j -= 1
        else:
            a[i] = str(curr)
        i -= 1
    return ''.join(_delt) + ''.join(a[1:]) if a[0] == '0' else ''.join(a)


if __name__ == '__main__':

    # print(_round(11.23, -1))  # 10.0
    # print(_round(11.23, 1))  # 11.2
    # print(_round(1234, -2))  # 1200
    # print(_dec_division(1, 3))
    # xx = 1
    # print(f"hello{xx}")
    # root = Node(0)
    # root.add_child(Node(1))
    # root.add_child(Node(2))
    # for ch in root:
    #     print(ch)
    # for x in frange(0, 4, 0.5):
    #     print(x)
    a= str_add_int("199999999999999999999999999999999999999999", 9223372036854774807)
    print(a)
