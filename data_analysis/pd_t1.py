# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/9/4 
# Desc:

import numpy as np
import pandas as pd
from pandas import DataFrame

df=pd.DataFrame(data=[[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],
                index=["a","b","c","d"],
                columns=["one","two"])


print(df)
print('-----df.sum()-----')
print(df.sum()) # 按列求和
print('---按行sum----')
print(df.sum(axis=1)) # 按行求和

df1 = DataFrame({  # 两列数据
    'key1':['b','b','a','c','a','a','b','d'],
    'data1': range(8)
})

df2 = DataFrame({
    'key2':['a','b','c'],
    'data2': range(3)
})

#df3 = pd.merge(df1,df2)  # 合并能关联到的
#df4 = pd.merge(df1,df2,on='key')
df4 = pd.merge(df1, df2, left_on='key1', right_on='key2')
print(df4)



