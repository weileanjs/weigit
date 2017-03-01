import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import re
import lxml
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
'Accept':'text/html, */*; q=0.01',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Accept-Encoding':'gzip, deflate, sdch',
'Connection':'keep-alive',
'Referer':'https://www.cellsignal.com/',
}


def price_page(p_url,num):
    req_p = requests.get(p_url,headers = headers)
    price_l = []
    name_l = []
    size_l = []
    soup_p = BeautifulSoup(req_p.text,'lxml')
    names = soup_p.select('#purchase > tbody > tr > td:nth-of-type(1)')
    sizes = soup_p.select('#purchase > tbody > tr > td:nth-of-type(2)')
    prices = soup_p.select('#purchase > tbody > tr > td:nth-of-type(3)')
    for price in  prices[:num]:
        if '现货查询' in price.text:
            price=str(price.text).replace('现货查询','').strip()
            price_l.append(price)
        else:
            price_l.append(str(price.text).strip())
    for name in  names[:num]:
        name_l.append(name.text.strip())
    for size in  sizes[:num]:
        size_l.append(size.text.strip().replace('\r\n\t\t\t\t\t\t\t\t\t\t\t',''))
    return price_l,name_l,size_l


print(price_page('http://www.cst-c.com.cn/products/4084.html',2))