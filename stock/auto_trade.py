# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2021/07/03
# Desc: 自动交易

import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
import mplfinance
import baostock as bs

bs.login()
# 下载股票历史数据
# adjustflag 默认不复权：3；1：后复权；2：前复权
# frequency 默认为d，日k线；d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据
rs = bs.query_history_k_data_plus("sh.600000",
                                  "date,code,open,high,low,close,volume,amount,adjustflag,pctChg,isST",
                                  start_date='2022-01-01', end_date='2022-06-30',
                                  frequency="5", adjustflag="3")
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    print(rs.get_row_data())
bs.logout()
# 自动下载最新数据

# 画K线图
