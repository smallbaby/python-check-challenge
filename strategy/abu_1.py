# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/9/9 
# Desc:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
sys.path.insert(0, os.path.abspath('../'))
import abupy
abupy.env.enable_example_env_ipython()
# abupy.env.disable_example_env_ipython() 关闭本地模式，从url获取

from abupy import ABuSymbolPd

jd = ABuSymbolPd.make_kl_df('usJD')

print(jd)

# 回测模块、实盘模块
# 买入规则、卖出规则、选股规则、仓位控制及滑点策略
# 回测最重要的就是（择时）（选股）
# 海龟交易法
# 趋势突破定义为当天收盘价格超过N天内的最高价或最低价，
#  超过最高价格作为买入信号买入股票持有，超过最低价格作为卖出信号

from abupy import AbuFactorBuyXD, BuyCallMixin

# BuyCallMixin 做多，正向策略
# BuyPutMixin 做空 期货

# 买入因子实现请查看 #AbuFactorBuyBase

class AbuFactorBuyBreak(AbuFactorBuyXD, BuyCallMixin):
    def fit_day(self, today):
        """
        针对每一个交易日拟合买入交易策略，寻找向上突破买入机会
        :param today:当前驱动的交易日金融时间序列数据
        :return:
        """
        # 今天的收盘价 达到X天最高
        if today.close == self.xd_kl.close.max():
            # 明天买
            return self.buy_tomorrow()
            # return self.buy_today()

from abupy import AbuBenchmark
from abupy import AbuCapital
from abupy import ABuPickTimeExecute
#
buy_factors = [
    {'xd':60, 'class':AbuFactorBuyBreak},
    {'xd':42, 'class':AbuFactorBuyBreak}
]
benchmark = AbuBenchmark()
capital = AbuCapital(1000000, benchmark)
orders_pd, action_pd, _ = ABuPickTimeExecute.\
    do_symbols_with_same_factors(['usTSLA'],benchmark,
                                 buy_factors,None,capital,show=True)

















