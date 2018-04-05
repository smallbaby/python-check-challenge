# -*- coding:utf8 -*-
import random

'''
全排列递归编码
'''
arr = [1,2,3,4,5]
di = {}
a = {}
for i in arr:
    di[i] = 0

def dfs(step):

    if step == len(arr) + 1:
        print a.values()

    for i in arr:
        if di[i] == 0:
            a[step] = i
            di[i] = 1
            dfs(step + 1)
            di[i] = 0


if __name__ == '__main__':
    dfs(1)