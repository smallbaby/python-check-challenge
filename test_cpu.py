# -*- coding:utf8 -*-

# 计算密集型的要开启多进程
from multiprocessing import Process
from threading import Thread
import time


def work():
    res = 0
    for i in range(100000000):
        res += i


if __name__ == '__main__':
    l = []
    start = time.time()
    for i in range(4):
        p = Process(target=work)  # 1.9371106624603271  #可以利用多核（也就是多个cpu）
        # p  = Thread(target=work)  #3.0401737689971924
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop = time.time()
    print('%s' % (stop - start))
