# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2021/07/03
# Desc: 数学公式

import numpy as np

# 平均值

# Numpy
'''
N维数组容器，数组越大，Numpy优势越明显
ndarray：支持并行化运算(底层为C，解除了GIL）
'''

# Pandas 表格容器
'''
数据分析.
'''
a = list(range(10))
b = np.array(a)

# 直接生成数组
a = np.zeros(10)
print(a, a.dtype)
b = np.zeros(10, dtype=int)
print(b, b.dtype)

# 多维数组
a = np.zeros((4, 5), dtype=int)
print(a)

a = np.ones((4, 5), dtype=int)
print(a)
print(a[0, :])  # 获取某一行
print(a[:, 0])  # 获取某一列

a = np.full((3, 2), 124)  # 用特定的数字填充
print(a)

# 随机数
a = np.random.random((3, 3))
print(a)

a = np.random.randint(0, 10, (3, 3))
print(a)

a = np.arange(0, 10, 2)
print(a)
print(a[:2])

# 在0-3范围内，取100个数
a = np.linspace(0, 3, 100)
print(a)

# 生成矩阵

a = np.eye(10)
print(a)
###############################################################
print("############## Pandas ###################")

import pandas as pd

# Series 默认左边为索引，值在右边，不指定索引，则为0-N数字
stock = pd.Series([1,2,3,4,], index=['a', 'b', 'c', 'd'])
print(stock)
a = {
    'tencent': 11, 'alibaba': 190.1, 'baidu': 230
}

stock = pd.Series(a)
print(stock.iloc[1])

print(stock.loc['alibaba'])

# 运算
a = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
b = pd.Series([1,2,3,4], index=['a', 'e', 'f', 'g'])
c = a + b

print(c.dropna()) # 去掉缺失值

c = a.add(b, fill_value=0)  # 填充缺失值
print(c)















