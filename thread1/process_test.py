# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/9/5 
# Desc:

## 子进程之间通讯，需要用到 from multiprocessing import Process,Queue,Pool,Pipe

from multiprocessing import Process,Queue, Pool, Pipe
import os,time,random


def write(p):
    for v in ['A', 'B', 'C']:
        print('write --- put %s to queue' % v)
        p.put(v)
        time.sleep(random.random())


def read(p):
    print('read ...')
    while True:
        v = p.get(True)
        if v:
            print('read ...get %s from queue' % v)

if __name__ == '__main__':
    p = Queue()
    pw = Process(target=write, args=(p,))
    pr = Process(target=read, args=(p,))
    pw.start()
    pr.start()