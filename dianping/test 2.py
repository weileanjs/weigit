

# -*- coding: utf-8 -*-
import urllib
import requests
from bs4 import BeautifulSoup
from lxml import etree
base_url = 'https://book.douban.com/top250'
# req = urllib.request.Request(url=base_url)
# response=urllib.request.urlopen(req)

req1 = requests.get(base_url)
# print(req1.encoding)
# req1.encoding = 'SO-8859-1'
# req1.encoding = 'gb2312'
dom = etree.HTML(req1.text)
#//*[@id="content"]/div/div[1]/div/div/span[1]
item_info  = dom.xpath('//tr[@class="item"]')
for i in item_info:
    title = i.xpath('//td/div/a/@title')
    author = [x.split('/')[0] for x in i.xpath('//td[2]/p[1]/text()')]
    price = [x.split('/')[-1].split('元')[0] for x in i.xpath('//td[2]/p[1]/text()')]
    publish_time = [x.split('/')[-2] for x in i.xpath('//td[2]/p[1]/text()')]
    publish = [x.split('/')[-3] for x in i.xpath('//td[2]/p[1]/text()')]

print(publish)
print(len(publish))
#['[美] 卡勒德·胡赛尼 / 李继宏 / 上海人民出版社 / 2006-5 / 29.00元',
# url_page = dom.xpath('//tr[@class="item"]/td[2]/p[1]/text()')
# title ='//tr[@class="item"]/td/div/a/@title'

#x1 = [str(x).replace(r'\n','1').strip('') for x in url_page]
# for x in url_page:
#     a =str(x)
#     print(a.replace('\n','').replace(' ',''))
# print(x1)
# print(len(x1))
# print(url_page)
# print(len(url_page))
