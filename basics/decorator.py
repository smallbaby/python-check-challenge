# -*- coding: utf-8 -*-
# Author: kaizhang01

import time


def exTime(fun):
    def wrapper(*args, **kwargs):
        _l = time.time()
        fun(*args, **kwargs)
        _e = time.time()
        print(_e - _l)

    return wrapper


@exTime
def p(msg):
    time.sleep(1)
    print(msg)


def test_dp(arr):
    """求集合中子集的最大和"""
    arr = [-13, 5, 2, 1, -2, 3]
    max_v = 0
    lens = len(arr)
    tmp = 0
    for i in range(lens):
        tmp = max(tmp + arr[i], arr[i])
        max_v = max(tmp, max_v)
    return max_v


def hello(s):
    _s = []
    _sign = {
        ']': '[',
        ')': '(',
        '}': '{'
    }
    for i in s:
        if i not in _sign:
            _s.append(i)
        else:
            _k = _sign[i]
            if _s.pop() == _k:
                continue
            else:
                return False
    return True


if __name__ == '__main__':
    print(hello("[([]]"))
    # p('helloworold')
    # _max = test_dp(None)
    # print(_max)
