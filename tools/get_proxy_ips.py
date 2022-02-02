# -*- coding: utf-8 -*-
# Author: kaizhang01

import requests
from lxml import etree
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "helloworld"
}

proxies = {
    "http": "xx"
}


def get_text(url, headers):
    res = requests.get(url, headers=headers, proxies={'http': proxy_ip})
    res.encoding = 'utf-8'
    return res.text


def main():
    page = 1
    url = 'https://www.kuaidaili.com/free/inha/{page}'
    dbHtml = etree.HTML(get_text(url, headers))
    x = dbHtml.xpath("//tbody")
    for xx in x:
        for _x in xx.xpath("//tr"):
            IP = _x.xpath("//td[@data-title='IP']")
            PORT = _x.xpath("//td[@data-title='PORT']")
            protocol = "HTTP"
            i = 0
            for _xx in _x.xpath("//td[@data-title='IP']"):
                print(protocol + "://" + _xx.text + ":" + PORT[i].text)
                i = i + 1


import json


def main2():
    res = requests.get("https://ip.jiangxianli.com/api/proxy_ips")
    cont = json.loads(res.content)
    for x in cont['data']['data']:
        print(x['ip'], x['port'], x['protocol'])


main2()
