#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/9 
# Desc:

import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']

users = pd.read_table('../data/users.dat', sep='::', header=None, names = unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('../data/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']

movies = pd.read_table('../data/movies.dat', sep='::', header=None, names=mnames)


# print(users[:5])
# print(ratings[:5])
# print(movies[:5])

data = pd.merge(pd.merge(ratings, users), movies)

mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')

print(mean_ratings[:-5])


ratings_by_title = data.groupby('title').size()  # 先对title分组，size() 分组大小

print(ratings_by_title[:10])


active_titles = ratings_by_title.index[ratings_by_title >= 250] # 过滤掉评分分数不够250条的电影


mean_ratings = mean_ratings.ix[active_titles]

print(mean_ratings)


# 女性 最喜欢的电影。。 根据F降序

top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)

print(top_female_ratings[:10])


# 计算性别分歧最大的电影


mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']


sorted_by_diff = mean_ratings.sort_values(by='diff')

print(sorted_by_diff[:15])

# 对结果反序，取15.就是男性最喜欢的电影

print(sorted_by_diff[::-1][:15])

# 求分歧最大的电影，计算分数的方差或标准差

ratings_std_by_title = data.groupby('title')['rating'].std()

# 根据active过滤

ratings_std_by_title = ratings_std_by_title.ix[active_titles]

# 降序

print(ratings_std_by_title.order(ascending=False)[:10])





















































