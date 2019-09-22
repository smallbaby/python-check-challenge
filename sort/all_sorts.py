# -*- coding: utf-8 -*-
# Author: kaizhang01


# 快速排序、归并排序、堆排序、冒泡排序等属于比较排序

# 快排
qs = lambda x: x if len(x) <= 1 else qs([i for i in x[1:] if i < x[0]]) + [x[0]] + qs([i for i in x[1:] if i >= x[0]])


# 冒泡排序

def bubble(x=[]):
    for i,j in enumerate(x):
        for ii, jj in enumerate(x[1:]):
            if x[i] > x[ii]:
                x[i] = x[ii]
                x[ii] = j
    print(x)

# 选择排序（Selection Sort）



if __name__ == '__main__':
    y = [2, 6, 3, 1, 4, 9, 2, 1, 9, 1, 2]
    x = qs(y)
    bubble(y)
