# -*- coding: utf-8 -*-
# Author: kaizhang01

from random import randint
import collections


class ip_top_solution:
    def __init__(self):
        self.db = collections.defaultdict(list)
        self.ips = []
        self.init()

    def init(self):
        # 随机生成1w条ip
        for i in range(0, 10000):
            ip = f'192.168.{str(randint(0, 100))}.{str(randint(0, 255))}'
            self.ips.append(ip)

    def split(self):
        """
        拆成10个子序列
        :return:
        """
        for ip in self.ips:
            _key = int(ip.split('.')[-1]) % 10
            self.db[_key].append(ip)
        return self

    def handler(self):
        """
        分别统计10个序列中的top10
        :return:
        """
        res = {}
        for k, v in self.db:
            _d = {}
            for vv in v:
                _d[vv] = 1 if vv not in _d else _d[vv] = _d[vv] + 1
            sorted(_d, key=lambda x: x[1])

    def start(self):
        self.split().handler()


if __name__ == '__main__':
    ip_top_solution().start()
