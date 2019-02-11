# -*- coding: utf-8 -*-
# Author: kaizhang01
# Date: 2019/1/12
# Desc:
class Solution:
    def Fibonacci(self, n):
        # 递归，效率低
        # write code here
        #        if n == 1 or n == 0:
        #            return n
        #        else:
        #            return self.Fibonacci(n - 1) + self.Fibonacci(n - 2);
        fib = []
        fib.insert(0, 0)
        fib.insert(1, 1)
        fib.insert(2, 1)
        for i in range(3, n + 1):
            fib.insert(i, fib[i - 1] + fib[i - 2])
        return fib[n]
