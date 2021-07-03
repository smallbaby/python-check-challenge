# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2021/06/29
# Desc: 股票测试.

import pandas as pd
import tushare as ts
import numpy as np

TOKEN = "5d64f24075ac4befe59146ba4d5326b869db4c97d54fca36bb4f48e8"

df = ts.get_k_data("300104")
days = [5, 15, 50]
for ma in days:
    column_name = "MA{}".format(ma)
    df[column_name] = np.round(pd.Series.rolling(df.close,window=ma).mean())

# 计算浮动比例
df["pchange"] = df.close.pct_change()
# 计算浮动点数
df["change"] = df.close.diff()

print(df.head())
# N就是真实波动幅度的20日指数移动平均值
# 每天 真实波动幅度=Max（H-L，H-PDC，PDC-L）
# H=当日最高价 L=当日最低价 PDC=前一日收盘价

