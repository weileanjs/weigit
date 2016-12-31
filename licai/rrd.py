import json
from multiprocessing import Pool
import datetime
from bs4 import BeautifulSoup
import urllib
import pandas as pd
import time
#导入图表库
import matplotlib.pyplot as plt
#导入数值计算库
import numpy as np
from sklearn.cluster import KMeans
#设置列表页URL的固定部分
import pymongo
client = pymongo.MongoClient('localhost',27017)
db = client['renrendai']
rrdb =db['renrendai']
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Connection':'close',
'Referer':'http://bzclk.baidu.com/'
}
now =datetime.datetime.now().strftime('%Y-%m-%d')[0:10]


def get_rrd_data():
    base_url = 'https://www.we.com/lend/loanList!json.action?pageIndex='
    for i in range(1,500):
        print(i)
        req = urllib.request.Request(url=(base_url+str(i)),headers=headers)
        response=urllib.request.urlopen(req)
        html = response.read().decode('utf-8',errors='replace')
        data_json = json.loads(html)
        if len(data_json['data']['loans']) !=0:
            title = [x['title'] for x in data_json['data']['loans']]
            amount = [x['amount'] for x in data_json['data']['loans']]
            interest= [x['interest'] for x in data_json['data']['loans']]
            months = [x['months'] for x in data_json['data']['loans']]
            date = [str(now)]*len(title)
            rrd=pd.DataFrame({'title':title,'amount':amount,'interest':interest,'months':months,'date':date})
            rrd[['amount','interest','months']]=rrd[['amount','interest','months']].astype(np.float64)
            db['rrd'+'_loan'].insert_many(rrd.to_dict('records'))
            time.sleep(1)
        else:
            print(str(i)+'is nothing')
            break



get_rrd_data()



