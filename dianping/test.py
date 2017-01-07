# -*- coding: utf-8 -*-
import urllib
import requests
from bs4 import BeautifulSoup
from lxml import etree
base_url = 'http://www.jb51.net/list/list_15_1.htm'
req = urllib.request.Request(url=base_url)
response=urllib.request.urlopen(req)

req1 = requests.get(base_url)
req1.encoding = 'SO-8859-1'
req1.encoding = 'gb2312'
#print(req1.text)
#html = response.read().decode('utf-8',errors='replace')

#soup = BeautifulSoup(html,'lxml')
dom = etree.HTML(req1.text)
# print(req1.text)
# print(req)
# print(response)
# print(html)
# print(soup)
# item = []
item =dom.xpath('//div[@id="contents"]/div/div[1]/div/div[2]/div/div/h2/a/text()')
co_url_list = dom.xpath('//div[@id="contents"]/div/div[1]/div/div[2]/div/div/h2/a/@href')
# print(item,co_url_list)
# print(len(item))
# //div[@id="newslist"]/table[1]/tbody//tr/td/table/tbody/tr/td[1]/a/font
# //div[@class="indexlist clearfix"]/span/a
fenilei_zongye = (dom.xpath('//div[@id="contents"]/div/div[1]/div/div[5]/a[last()]/@href')[0]).split('_')
article_urls = dom.xpath('//div[@class="artlist clearfix"]/dl/dt/a/@href')
print(article_urls)
print(len(article_urls))
