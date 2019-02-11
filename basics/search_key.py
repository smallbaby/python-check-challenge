# -*- coding: utf-8 -*-
# Author: kaizhang01
# Date: 2019/1/10
# Desc:


def find(key, array):
    row = len(array) - 1
    col = len(array[0]) - 1
    i, j = row, 0
    while (i >= 0 and j <= col):
        if (array[i][j] == key):
            return True
        if key > array[i][j]:
            j += 1
        elif key < array[i][j]:
            i -= 1
    return False


arr = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]

# k = find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
k = find(16, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]])
print(k)
