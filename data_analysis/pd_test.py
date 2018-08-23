# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/15
# Desc:
import pandas as pd
import numpy as np
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


##################

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
df = pd.read_csv(url, header = None)
df.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash',
              'Alcalinity of ash', 'Magnesium', 'Total phenols',
              'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
              'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']

np.unique(df['Class label'])


### DataFrame
from pandas import DataFrame
from pandas import Series
data = {
    'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5, 1.7, 3.6, 2.4, 2.9]
}

frame = DataFrame(data, columns=['year','state','pop'])

# columns  表头  index:行索引
frame2 = DataFrame(data, columns=['year','state','pop','debt'],
                   index=['one','two','three','four','five'])

frame2.columns

frame2.ix['three'] # 行索引，取第几行

# 赋值
frame2['debt'] = 17

frame2['debt'] = np.arange(5.)

val = Series([-1.2,-1.5,-1.7], index=['two','four','five'])

frame2['debt'] = val

frame2['eastern'] = frame2.state == 'Ohio'


pop = {
    'Nevada':{2001:2.4,2002:2.9},
    'Ohio':{2000:1.5,2001:1.7,2002:3.6}
}

frame3 = DataFrame(pop)


frame3.T # 装置

# DataFrame(pop, index=[2001,2002,2003])

obj = Series(range(3), index=['a','b','c'])

index = obj.index

# index[1]='d' 不可修改性
index = pd.Index(np.arange(3))  # Int64Index([0, 1, 2], dtype='int64') 针对整型的index：Int64Index



'Ohio' in frame3.columns # True

# 重新索引
obj = Series([4.5,7.2,-5.3,3.6], index = ['d','b','a','e'])

obj.reindex(['a','b','c','d','e'], fill_value=0)
obj = Series(['blue','purple','yellow'], index=[0,1,2])
obj.reindex(range(6), method='ffill') # 往后填充
'''
ffill/pad 前向填充
bfill或backfill 后向填充


'''

new_obj = obj.drop(0)


obj = Series(np.arange(4.0), index=['a','b','c','d'])

f = DataFrame(np.random.randn(4,3), columns=list('bcd'), index=['uu', 'oo', 'tt', 'ooo'])
f.sort_index(by=['uu','oo'])


obj = Series(['c','a','d','a','a','a','b','b','c','c'])
uniques = obj.unique() # 去重
obj.value_counts() # group by sum
pd.value_counts(obj.values, sort=False)

o = obj.isin(['b','c'])
print(o)





























































