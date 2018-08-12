# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/10 
# Desc: numpy

import numpy as np

'''
ndarray  通用的数据多维容器，必须相同类型，每个数组都有一个shape，表示各维度大小
dtype ： 类型

'''

# ndarray

data = [6, 7.5, 8, 0, 1]
arr = np.array(data)

# shape = (5,)
# dtype = float64

data2 = [[1,2,3,4], [5,6,7,8]]
arr2 = np.array(data2)

# shape = (2,4)

np.zeros(10)
np.zeros((2,10)) # 2维 10列
np.empty((2,3,2)) # 垃圾值

np.arange(15)


np.ones(10) # 全是1
np.ones_like(arr2) # 参考arr2的shape，dtype

np.eye(5,5) # 对角线是1，其余为0

np.identity(5, 'float64') # 正方矩阵


arr1 = np.array([1,2,3,4], dtype=np.float64)
arr2 = np.array([1,2,3,4], dtype=np.int32)


arr3 = arr2.astype(np.float64) # 转换类型

numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)


arr = np.array([[1.,2.,3.], [4.,5.,6.]])

arr*arr
1/arr
# 不同大小数组之间的运算叫做广播

arr = np.arange(10)

arr3d = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])


print(arr3d)

print(arr3d[0])

val = arr3[0]

val = 32
arr3d[0]=32
print(arr3d)


### 布尔型索引

names = np.array(['a','b','c','d','e'])
from numpy.random import randn
data = randn(7,4)

print(data)

# 花式索引  将数据复制到新数组

arr = np.empty((8,4))

print(arr)


for i in range(8):
    arr[i] = i

print(arr)

a1 = arr[[4,3,0,6]]
print(a1)


a2 = arr[[-3,-5,-7]]
print(a2)

arr = np.arange(32).reshape((8,4))

print(arr)

a3 = arr[[1,5,7,2],[0,3,1,2]]
# 最终选的元素是 (1,0),(5,3),(7,1),(2,2)
print(a3)

a3 = arr[[1,5,7,2]][:,[0,3,1,2]]
print(a3)

a3 = arr[np.ix_([1,5,7,2],[0,3,1,2])]  # 够花式。。。


# 转置 transpose ,返回视图，不进行数据复制

arr = np.arange(15).reshape((3,5)) # 3行5列

print(arr)
print(arr.T) # 转置 5行3列

"""
[[0,1,2,3,4],
 [5,6,7,8,9].
 [10,11,12,13,14]
]
.T
[[0,5,10],
 [1,6,11],
 [2,7,12],
 [3,8,13],
 [4,9,14]
]

"""

arr = np.random.randn(6,3)

print(arr)

arr1 = np.dot(arr.T,arr)
print(arr1)

arr = np.arange(16).reshape((2, 2, 4))

print(arr)

# 通用函数 元素级运算的函数

arr = np.arange(10)

np.sqrt(arr)

np.exp(arr)

# binary ufunc

x = randn(8)

y = randn(8)


z = np.maximum(x,y)
print(z)

arr = randn(7) * 5
print(arr)

print(np.modf(arr))

xarr = np.array([1.1,1.2,1.3,1.4,1.5])

yarr = np.array([2.1,2.2,2.3,2.4,2.5])

cond = np.array([True, False, True, True, False])

result = [(x if c else y) for x,y,c in zip(xarr, yarr,cond)]

print(result)



result = np.where(cond, xarr, yarr)

print(result)

arr = randn(4,4)
print(np.where(arr>0, 2,-2))

## 方法太多了。。。晕..

# 保存数组

# np.save('xx',arr)
# # 保存多个
# np.savez('xx', a=arr,b=arr)
#
# np.load('xx')['a']

# np.loadtxt('',delimiter=',') # load csv
# np.savetxt('', delimiter=',') # save

# 线性代数   矩阵乘法、矩阵分解、行列式

x = np.array([[1.,2.,3.],[4.,5.,6.]])

y = np.array([[6.,23.], [-1,7], [8,9]])

z = x.dot(y) # np.dot(x,y)
print(z)



# 随机数

samples = np.random.normal(size=(4, 4))
print(samples)

























































































