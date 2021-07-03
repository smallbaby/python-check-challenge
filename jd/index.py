from lxml import etree
import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException

url = 'https://item.jd.com/58143640238.html'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

res = requests.get('https://p.3.cn/prices/mgets\?callback\=jQuery4697118\&type\=1\&area\=1_2901_55548_0\&pdtk\=\&pduid\=15973124229741346530610\&pdpin\=zhangkai001\&pin\=zhangkai001\&pdbp\=0\&skuIds\=J_58143640241%2CJ_63671917072%2CJ_58143640240%2CJ_58143640242%2CJ_58143640251%2CJ_57974479552\&ext\=11100000\&source\=item-pc', headers  = headers)
print(res.content)

def get_price(url, sku, name):
    res = requests.get(url, headers=headers)
    tree = etree.HTML(res.content)
    xp = '/html/body/div[6]/div/div[2]/div[3]/div/div[1]/div[2]/span[1]/span[2]'
    for x in tree.xpath(xp):
        print(name, x, sku, url)


res = requests.get(url, headers=headers)

tree = etree.HTML(res.content)

xp = '/html/body/div[6]/div/div[2]/div[4]/div[7]/div[1]/div[2]'
nodetitle = tree.xpath(xp)
for n in nodetitle:
    for sku in n.xpath('//*[@id="choose-attr-1"]/div[2]/div'):
        _sku, name = sku.get("data-sku"), sku.get("data-value")
        url = f"https://item.jd.com/{_sku}.html"
        get_price(url, _sku, name)
        break
