import json
from multiprocessing import Pool
import datetime
from bs4 import BeautifulSoup
import urllib
import pandas as pd
import numpy as np
import time
import pymongo
client = pymongo.MongoClient('localhost',27017)
db = client['lufax']
now =datetime.datetime.now().strftime('%Y-%m-%d')[0:10]
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Connection':'close',
'Referer':'http://bzclk.baidu.com/'
}


base_url = 'https://list.lu.com/list/transfer-dingqi?minMoney=&maxMoney=&minDays=&maxDays=&minRate=&maxRate=&mode=&tradingMode=&isOverdueTransfer=&isCx=&currentPage={}'

def get_lu_zr():
    for i in range(1,25):
        print(str(i)+' is parser')
        req = urllib.request.Request(url=(base_url.format(i)),headers=headers)
        response=urllib.request.urlopen(req)
        html = response.read().decode('utf-8',errors='replace')
        soup = BeautifulSoup(html,'lxml')
        title_ = soup.select('div.main-body > ul > li > dl > dt > a')
        interest_ = soup.select('div.main-body > ul > li > dl > dd > ul > li.interest-rate > p')
        days_ = soup.select('div.main-body > ul > li > dl > dd > ul > li.invest-period > p')
        zhuanr_bianxian_ = soup.select('body > div.main-wide-wrap > div > div.main-body > ul > li > dl > dt')
        zhuan_days_ = soup.select('div.main-body > ul > li > dl > dd > ul > li.invest-period > p ')
        price_ = soup.select(' div.main-body > ul > li > div.product-amount > p > em')
        price = [x.text.replace(',','') for x in price_]
        title = [x.text for x in title_]
        interest = [x.text.strip('%') for x in interest_]
        days = [x.text.split('天')[0].replace("\n"," ").strip() for x in days_]
        # zhuan_days = [x.text.split('天')[0].replace("\n"," ").strip() for x in zhuan_days_]
        zhuan_days = []
        for x in zhuan_days_:
            if x.span != None:
                x1 = x.text.split('天')[0].replace("\n"," ").strip()
            else:
                x1 = 'n'
            zhuan_days.append(x1)
        bianxian = []
        date = [str(now)]*len(title)
        for x in zhuanr_bianxian_:
            if '可变现' in x.text:
                bianxian.append(1)
            else:
                bianxian.append(0)
        lufax_zr=pd.DataFrame({'title':title,'zhuan_days':zhuan_days,'interest':interest,'days':days,
                               'bianxian':bianxian,'date':date,'price':price})
        db['lu_zhuanr'].insert_many(lufax_zr.to_dict('records'))
        time.sleep(1)

get_lu_zr()
