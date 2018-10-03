# -*- coding: utf-8 -*-
# Author: kai.zhang01

import time
import datetime as dt
from dateutil import tz

from quant.strategy_template import StrategyTemplate

class Strategy(StrategyTemplate):
    name='策略A'

    def init(self):
        now = time.time()

    def strategy(self, event):
        pass
