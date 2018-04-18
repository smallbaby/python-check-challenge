# -*- coding:utf8 -*-

def binary_search(li, key, low, high):

    if low == high or key < li[0] or key > li[-1]:
        return None
    #   1 2 3 mid = 1
    mid = (low + high)/ 2
    if li[mid] > key:
        high = mid
        return binary_search(li, key, low, high)
    elif li[mid] < key:
        low = mid
        return binary_search(li, key, low, high)
    else:
        return mid, li[mid]

a = [1,2,3,4,5,6,7,8]
key = 7
b = binary_search(a, key, 0, len(a))
print b

