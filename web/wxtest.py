# -*- coding: utf-8 -*-
# Author: kaizhang01
# coding: utf-8
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


html = getHtml("http://baidu.com")
