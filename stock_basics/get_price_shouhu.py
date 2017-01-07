import tushare as ts
from bs4 import BeautifulSoup
import requests
import urllib
import json
import pandas as pd
import pymongo
import time
from multiprocessing import Pool
client = pymongo.MongoClient('localhost',27017)
db = client['month_price']

def ready_th(code):
    db['ready_code'].insert_one({'done':code})

# for i in ['300591','603165','300588','300593','603032','002842','603877']:
#     print(i)
#     ready_th(i)
ready_code = pd.DataFrame(list(db['ready_code'].find()))['done'].values
code_list_raw = ('%06d'%x for x in pd.read_csv(r'D:\W\python\stockFdate2\stock_datas\stock_basics\stock_basics.csv',encoding='gbk')['code'])
code_list = list(set(code_list_raw)-set(ready_code))
print(len(code_list),'left')


def stockM_price(code,price_m):
    db[code].insert_one(price_m)


header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
          'Accept':'*/*',
          'Accept-Encoding':'gzip, deflate, sdch',
          'Accept-Language':'zh-CN,zh;q=0.8',
          'Connection':'keep-alive',
          'Host':'q.stock.sohu.com',
          #'Referer':'https://xueqiu.com/S/SZ002454/ZYCWZB',
          'Cookie':'vjuids=-1ca0bc9ff.15969557f9a.0.7248b509f7fa4; vjlast=1483530928.1483530928.30; IPLOC=CN; SUV=1610152104565302'
          }

base_url = 'http://q.stock.sohu.com/hisHq?code=cn_{0}&start=20000601&end=20170104&stat=1&order=D&period=m&callback=historySearchHandler'

def get_priceM(code):
    print(code)
    priceM_d = {}
    r2 = requests.get(base_url.format(code),headers=header)
    price_l = (eval(r2.text)[0])['hq']
    for i in price_l:
        priceM_d[i[0][:7]] = i[1:]
    stockM_price(code,priceM_d)
    ready_th(code)
    print(code,'appended')


if __name__ == '__main__':
    count = 0
    while count < 2:
        try:
            pool = Pool(processes=10)
            pool.map( get_priceM,code_list)
            pool.close()
            pool.join()
        except KeyError as e:
            count = count +1
            print(count)
            time.sleep(5)
