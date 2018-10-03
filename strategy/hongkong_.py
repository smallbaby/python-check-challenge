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
from abupy import AbuFactorAtrNStop, AbuFactorPreAtrNStop\
    , AbuFactorCloseAtrNStop, AbuFactorBuyBreak,ABuProgress

from abupy import abu, tl, get_price, ABuSymbolPd, EMarketTargetType, AbuMetricsBase, AbuHkUnit, six

# 初始化金额
read_cash = 1000000
#买入因子
buy_factors = [
    {'xd':60, 'class':AbuFactorBuyBreak},
    {'xd':42, 'class':AbuFactorBuyBreak}
]
# 卖出因子

sell_factors = [
    {'stop_loss_n':1.0, 'stop_win_n':3.0, 'class':AbuFactorAtrNStop},
    {'class':AbuFactorPreAtrNStop, 'pre_atr_n':1.5},
    {'class':AbuFactorCloseAtrNStop, 'close_atr_n':1.5}
]

# 择时股票池
choice_symbols = ['hk03333', 'hk00700', 'hk02333', 'hk01359', 'hk00656', 'hk03888', 'hk02318']

# 设置市场类型为港股
abupy.env.g_market_target = EMarketTargetType.E_MARKET_TARGET_HK

abu_result_tuple, kl_pd_manger = \
    abu.run_loop_back(read_cash,
                      buy_factors,
                      sell_factors,
                      n_folds=6,choice_symbols=choice_symbols)

ABuProgress.clear_output()
AbuMetricsBase.show_general(*abu_result_tuple, only_show_returns=True)





