import requests
import urllib
from bs4 import BeautifulSoup
import re
import time
import pymongo
client = pymongo.MongoClient('localhost',27017)
db = client['515f']

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Referer':'http://www.515fa.com/',
'Host':'www.515fa.com',
}


base_url = 'http://www.515fa.com/qcxl/list_1_{}.html'
for i in range(35,114):
    print(i)
    req1 = requests.get(base_url.format(i),headers=headers)
    req1.encoding = 'SO-8859-1'
    req1.encoding = 'utf-8'
    soup = BeautifulSoup(req1.text,'lxml')
    titles = soup.select('body > div.zhutics > div > div.zhuti01 > div > div')
    for i in titles:
        t = i.select('div.w_tit > a ')
        if len(t) != 0 :
            pattern = re.compile(r'.*201\d年\d+月(国产|.{0,2}自主.{0,2})SUV销量.*')
            # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
            match = pattern.match(str(t[0]))
            if match:
                d_ = {}
                d_['title'] = t[0].text
                d_['url'] = t[0].get('href')
                db['zz_suv'].insert(d_)
                print(t[0].text)
                print(t[0].get('href'))
                print('~~~~~~~~~~~~~~~~~')
    time.sleep(3)



'''
2016年7月国产SUV销量排行榜1-81名完整版
2016年8月自主品牌SUV销量排行榜1-85名完整版
2014年7月中国自主品牌SUV销量排行榜完整版
'''
