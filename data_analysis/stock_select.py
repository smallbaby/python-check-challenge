# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/9/4 
# Desc: 择股

import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('expand_frame_repr', False)

# 导入数据

stock_data = pd.read_csv('../data/stock_data.csv', encoding='gbk')

stock_data_columns = [i for i in stock_data.columns] # header

stock_data['交易日期'] = pd.to_datetime(stock_data['交易日期'])

# 排序
stock_data.sort_values(by=['交易日期', '股票代码'], inplace=True)
####

# 排查开始时间太早
stock_data = stock_data[stock_data['交易日期'] > pd.to_datetime('20090101')]

# 将月末停牌股票去掉
stock_data = stock_data[stock_data['是否交易'] != 0]

# 去掉交易天数<10的
stock_data = stock_data[stock_data['交易天数'] >= 10]
# 当天涨停的不能买入
stock_data = stock_data[stock_data['最后一天涨跌幅'] <= 0.097]

# 计算所有股票在下个月的平均涨幅
output = pd.DataFrame()
# 平均数.
output['所有股票下月涨幅'] = stock_data.groupby('交易日期')['下月涨幅'].mean()
# 计算每月市值排名
stock_data['市值_排名'] = stock_data.groupby('交易日期')['总市值'].rank()
# 选取前10的股票

stock_data = stock_data[stock_data['市值_排名'] <= 300]
# 计算选中的股票在下个月的涨幅
output['选中股票下月涨幅'] = stock_data.groupby('交易日期')['下月涨幅'].mean()

### 输出
stock_data['股票代码'] += ''
output['股票代码'] = stock_data.groupby('交易日期')['股票代码'].sum()
output['line_benchmark'] = (output['所有股票下月涨幅'] + 1).cumprod()
output['line'] = (output['选中股票下月涨幅'] + 1).cumprod()
output.to_csv('../data/output.csv', encoding='gbk')  # 此处填入数据输出的路径
print(output)

# 画图
plt.plot(output['line'])
plt.plot(output['line_benchmark'])
plt.legend(loc='best')
plt.show()


