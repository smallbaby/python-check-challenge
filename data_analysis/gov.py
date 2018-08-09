# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/9 
# Desc:
import json

def p(str):
    print(str)


from collections import defaultdict

path = '../data/usagov_bitly_data2012-03-16-1331923249.txt'


def get_count(se):
    counts = defaultdict(int)
    for x in se:
        counts[x] += 1
    return counts





records = [json.loads(line) for line in open(path)]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]

counts = get_count(time_zones)

#print(counts['America/New_York'])


# 前十分区
'''
#第一种
value_key_pairs = [(count,tz) for tz, count in counts.items()]

value_key_pairs.sort()
print(value_key_pairs[-10:])'''

# 使用counter
from collections import Counter

counts = Counter(time_zones)

# print(counts.most_common(10))

# 使用pandas操作
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
frame = DataFrame(records)
#print(frame['tz'][:10])  # 摘要

tz_counts = frame['tz'].value_counts()
#print(tz_counts[:10]


clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unkown'

tz_counts = clean_tz.value_counts()

# print(tz_counts[:10])

# tz_counts[:10].plot(kind='barh', rot=0)

# print(frame['a'][51])


results = Series([x.split()[0] for x in frame.a.dropna()])  # 删除缺失数据(pd.dropna()方法)

p(results[:5])

p(results.value_counts()[:8])


cframe = frame[frame.a.notnull()]

op = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')

p(op[:5])


by_tz_os = cframe.groupby(['tz', op])


agg_counts = by_tz_os.size().unstack().fillna(0)

p(agg_counts[:10])


indexer = agg_counts.sum(1).argsort()

p(indexer[:10])

count_subset = agg_counts.take(indexer)[-10:]


p(count_subset)

count_subset.plot(kind='barh', stacked = True)











































