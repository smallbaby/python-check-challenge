# -*- coding: utf-8 -*-
# Author: kaizhang01
# Date: 2019/1/9
# Desc:

import os

LOG_PATH = '/data/fdw-job-server-mq/exec_logs/2019-01-10'
TARGET_PATH = '/home/supdev/tmp/data/'


def _start():
    pass


def upload():
    _load = 'curl  - F "filename=@file.tar.gz" http://localhost:9002/upload'


def write(file, content):
    with open(file, 'a+') as f:
        f.write(content + '\n')


prefix = [1, 2, 3, 4, 5, 6]

files = os.listdir(LOG_PATH)
files=['136995567196176.log']
s = []
i = 0
for file in files:
    is_sql = False
    _res = ''
    if not os.path.isdir(file):
        with open(LOG_PATH + '/' + file) as _f:
            j = 0
            tfile = None
            for line in _f.readlines():
                line = line.strip()
                if is_sql:
                    if line.startswith('[') or line.startswith('SLF4J') :
                        is_sql = False
                        tfile = None
                        j += 1
                    else:
                        write(tfile, line)
                        _res += line + '\n'
                if not is_sql and (line.lower().startswith('insert') or line.lower().startswith('set')  or line.lower().startswith('use') ):
                    is_sql = True
                    tfile = TARGET_PATH + file + '_' + str(j)
                    write(tfile, line)
                    _res += line + '\n'
    print(_res)

