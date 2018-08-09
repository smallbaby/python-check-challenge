# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/10 
# Desc:

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

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


np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)  # 有效性检查

def get_top1000(group):
    return group.sort_index(by='births', ascending=False)[:1000]


grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)

#p(top1000)


boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

p(boys)

total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)


subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]

subset.plot(subplots=True, figsize=(12,10), grid=False, title='Number of births per year')

#plt.show()

table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)

table.plot(title='Sum of table1000.prop by year and sex', yticks=np.linspace(0, 1.2, 13),
           xticks=range(1880, 2020, 10))

# plt.show()

df = boys[boys.year == 2010]

prop_cumsum = df.sort_index(by='prop', ascending=False).prop.cumsum()


p(prop_cumsum[:10])

p(prop_cumsum.searchsorted(0.5) + 1)


# 1900年验证

df = boys[boys.year == 1900]

in1900 = df.sort_index(by='prop', ascending=False).prop.cumsum()
p(in1900.searchsorted(0.5) + 1)

def get_quantile_count(group, q=0.5):
    group = group.sort_index(by='prop', ascending=False)
    return group.prop.cumsum().searchsorted(0.5) + 1



diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
# 每年、性别
p(diversity.head())
diversity = diversity.unstack('sex')
# diversity.plot(title='Number of popular names in top 50%')

# 最后一个字母

get_last_letter = lambda x: x[-1]

last_letters = names.name.map(get_last_letter)

last_letters_name = 'last_letter'


table = names.pivot_table('births', index=last_letters, columns=['sex', 'year'], aggfunc=sum)

subtable = table.reindex(columns=[1990, 1960, 2010], level='year')

p(subtable.head())

p(subtable.sum())

letter_prop = subtable / subtable.sum().astype(float)

fig, axes = plt.subplots(2, 1, figsize=(10,8))
letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)
#plt.show()


# 男女名字各个末字母的比例

letter_prop = table / table.sum().astype(float)

dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T


p(dny_ts.head())

dny_ts.plot()

# plt.show()

# 变成女孩名字的男孩名字

all_names = top1000.name.unique()

mask = np.array(['lesl' in x.lower() for x in all_names])

lesley_like = all_names[mask]

filtered = top1000[top1000.name.isin(lesley_like)]

filtered.groupby('name').births.sum()

table = filtered.pivot_table('births', index='year', columns='sex', aggfunc='sum')
table = table.div(table.sum(1), axis=0)

p(table.tail())

table.plot(style={'M': 'k-', 'F': 'k--'})
plt.show()




















































































































