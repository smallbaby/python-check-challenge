# -*- coding: utf-8 -*-
import socket

# ip = socket.gethostbyname(socket.getfqdn(socket.gethostname()))

# echo "TESTMSG, "`hostname` > /opt/log/test.log
import time


def str_data_to_num(str_data):
    # 格式时间成毫秒
    strptime = time.strptime(str_data, "%Y-%m-%d %H:%M:%S")
    print("strptime", strptime)
    mktime = int(time.mktime(strptime) * 1000)
    print("mktime", mktime)
    return mktime


def date_data_to_num(str_data):
    mktime = int(time.mktime(str_data) * 1000)
    print("mktime", mktime)
    return mktime


def num_to_str_data(str_data):
    str_data = str_data / 1000
    # 格式毫秒成指定格式时间
    str_data = time.localtime(str_data)  # 生成一个元祖式的时间
    print(str_data)
    strptime = time.strftime("%Y-%m-%d %H:%M:%S", str_data)  # 格式化元祖
    print("strptime", strptime)


import datetime


def test():
    return int(time.mktime(datetime.datetime.now().timetuple()) * 1000)


print(test())
