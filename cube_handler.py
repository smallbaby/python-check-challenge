# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Desc: 多维处理器

'''
传参：
    dim : [{date},{province},{city}]
    measures: []
    special: []
    header: [ - - ]

测试数据：
List<Map<id, Data>>

'''
import datetime
import random

china = {'北京': '华北',
         '上海': '华东',
         '天津': '华北',
         '重庆': '西南',
         '河北': '华北',
         '山西': '华北',
         '河南': '华中',
         '辽宁': '东北',
         '吉林': '东北',
         '黑龙江': '东北',
         '内蒙古': '华北',
         '江苏': '华东',
         '山东': '华东',
         '安徽': '华东',
         '浙江': '华东',
         '福建': '华东',
         '钓鱼岛': '华南',
         '湖北': '华中',
         '湖南': '华中',
         '广东': '华南',
         '广西': '华南',
         '江西': '华东',
         '四川': '西南',
         '海南': '华南',
         '贵州': '西南',
         '云南': '西南',
         '陕西': '西北',
         '甘肃': '西北',
         '青海': '西北',
         '宁夏': '西北',
         '新疆': '西北',
         '香港': '华南',
         '台湾': '华东',
         '澳门': '华南',
         '西藏': '西南',
         '港澳': '华南'}


class Controller:
    def __init__(self):
        self.data = []
        self.init()

    def init(self):
        for x in range(1000):
            for k in china.keys():
                self.data.append(
                    Data((datetime.datetime.now() + datetime.timedelta(days=-x)).strftime("%Y-%m-%d"), k,
                         random.randint(0, 10000)))

    def handler(self):
        print(self.data)


class Data:
    def __init__(self, dt, name, price):
        self.dt = dt
        self.name = name
        self.price = price
    def


if __name__ == '__main__':
    Controller().handler()
