# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/9/6 
# Desc:
import pandas as pd
import numpy as np
# 3行4列
arr = np.arange(12).reshape(3,4)

arr1 = np.concatenate([arr, arr], axis = 1)
d1 = pd.DataFrame(arr)
print(d1.stack())