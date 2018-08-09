# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/10 
# Desc:

import pandas as pd
import numpy as np

def p(s):
    print(s)

def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group


names1880 = pd.read_csv('../data/ssa/yob1880.txt', names=['name', 'sex', 'births'])

print(len(names1880), names1880.groupby('sex').births.sum())

years = range(1880, 2011)

pieces = []

columns = ['name', 'sex', 'births']

for year in years:
    path = '../data/ssa/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)  # ignore_index 忽略原始行号

total_births = names.pivot_table('births', index= 'year', columns='sex', aggfunc=sum)


p(total_births.tail())

# prop

names = names.groupby(['year', 'sex']).apply(add_prop)


np.allclose(names.groupby(['year', 'age']).prop.sum(), 1)  # 有效性检查
































