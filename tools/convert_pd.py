# -*- coding: utf-8 -*-
# Author: kai.zhang01
import pandas as pd

data = {'name': ['zs','ls','ww','zl'], 'hello': [2,0,0,0]}
pp = pd.DataFrame.from_dict(data)
#print(pp)


ticker = [{
    'symbol': 'BTCUSDT',
    'open':6500,
    'close':6600,
    'low': 100,
    'high': 200,
    'vol': 240023
}]

dd = pd.DataFrame([x.values() for x in ticker], columns=('a','b','c','d','e','f'))

print(dd)

