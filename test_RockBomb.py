# -*- coding:utf8 -*-

__author__ = 'kai.zhang01'
import sys
import urllib2

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

print str(len(xList)),'行', len(xList[1]),'列'
