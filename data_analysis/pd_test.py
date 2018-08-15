# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/15 
# Desc:
import pandas as pd
from pandas import Series, DataFrame


obj = Series([1,2,3,4])

obj.values

obj.index

obj2 = Series([3,2,1,4], index=['a','b','c','d'])


obj2['a']

obj2['a'] = 6
obj2[['a','b','c']]

obj2[obj2>0]

'a' in obj2

sdata = {'a':1, 'b':2,'c':3}

obj3 = Series(sdata)

states = ['a','bb','cc']
obj4 = Series(sdata, index=states)

print(pd.isnull(obj4))

pd.notnull(obj4)

obj4.isnull()

print(obj4.name)












