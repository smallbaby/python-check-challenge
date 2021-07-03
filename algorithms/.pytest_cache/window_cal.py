# -*- coding: utf-8 -*-
# Author: kaizhang01


a = [1,2,3,4,5,6,7]
b = a[0:2]
for x in a[3:]:
    if len(b) == 3 and sum(b)/len(b) > 1:
        print('start', b[0], 'end', b[len(b) - 1], 'cpu:', sum(b)/len(b))
        del b[0]
    b.append(x)

