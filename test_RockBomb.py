# -*- coding:utf8 -*-

__author__ = 'kai.zhang01'
import sys
import urllib2
import numpy as np

# read data from url
# 数据源已经失效....通过google找到了所有的数据源，发现不是失效，而是必须墙....
# 求得输入数据有多少行，每行有多少列
#target_url = ('https://archive.ics.uci.edu/m1/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data')

# data = urllib2.urlopen(target_url)
file = open('sonar.all-data', 'r')

xList = []
labels = []
for line in file.readlines():
    row = line.strip().split(',')
    xList.append(row)

print(str(len(xList)),'行', len(xList[1]),'列')

print('------------ Next 3 ---------')
# 3. 各类型的属性数量分布

# column 3

_col = 3
colData = []
for _row in xList:
    colData.append(float(_row[_col]))

# 转为numpy的array
colArray = np.array(colData)

#取均值
colMean = np.mean(colArray)# 所有数据求均值
print(colMean)

'''
numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<class numpy._globals._NoValue at 0x40b6a26c>)
求取均值 m*n矩阵
axis =  0 压缩行，对各列求均值，返回1*n矩阵
axis = 1 压缩列， 行均值，返回m*1矩阵
'''
# 标准差，观察数据的波动大小
colsd = np.std(colArray)

'''
np.std 求标准差
axis = 0 每列的标准差
axis = 1 每行的标准差
'''
print(colsd)

ntiles = 4

perchentBdry = []
for i in range(ntiles + 1):
    perchentBdry.append(np.percentile(colArray, i * 100/ntiles))

print(perchentBdry)


# a = [60,45,43,21,56,89,76,32,22,10,12,14,23,35,45,43,23,23,43,23]
# a = sorted(a)
# print math.ceil(95/100*89)
# print len(a), int(len(a) * 0.95),a[int(len(a) * 0.95)],a[int(math.ceil(95/100*89))]
#
#
# colArray = sorted(colArray)
# print len(colArray), 100/4,int(len(colArray) * 0.25),colArray[0], colArray[int(len(colArray) * 0.25)]

ntiles = 10

for i in range(ntiles + 1):
    perchentBdry.append(np.percentile(colArray, i*100/ntiles))

print(perchentBdry)

# label
col = 60
_colData = []
for row in xList:
    _colData.append(row[col])
print(_colData)

unique = set(_colData) # 去重
print(unique)

catDict = dict(zip(list(unique), range(len(unique))))

print(catDict) # {'R': 0, 'M': 1}

catCount = [0] * 2

for elt in _colData:
    catCount[catDict[elt]] += 1
print(list(unique)) # ['R', 'M']
print(catCount) # [97, 111]

print(colData)
# stats.probplot(colData, dist='norm', plot=pylab)
# pylab.show()

#--------------- pandas 统计

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

# pandas

file = open('sonar.all-data', 'r')

rocksVmines = pd.read_csv(file, header = None, prefix='V')
print(rocksVmines.head())
print(rocksVmines.tail())

summary = rocksVmines.describe()
print(summary)


