import array
import numpy as np
m = 3 #行数
n = 4 #列数
list = np.zeros((m, n), dtype=np.int)
list[0][1] = 1
count = 1
#k记录下标和。每个斜线上下标和相等，从0到m+n-2递增
for k in range(m+n-1):
    for i in range(max(k-m+1, 0), min(k+1, n)):
        list[k-i][i] = count
        count += 1
print(list)