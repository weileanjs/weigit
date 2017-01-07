import tushare as ts
from bs4 import BeautifulSoup
import requests
import urllib
import json
import pandas as pd
import pymongo
from multiprocessing import Pool
client = pymongo.MongoClient('localhost',27017)
db = client['stock_basics']

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
          'Accept':'application/json, text/javascript, */*; q=0.01',
          'Accept-Encoding':'gzip, deflate, sdch, br',
          'Accept-Language':'zh-CN,zh;q=0.8',
          'cache-control':'no-cache',
          'Connection':'keep-alive',
          'Host':'xueqiu.com',
          #'Referer':'https://xueqiu.com/S/SZ002454/ZYCWZB',
          'X-Requested-With':'XMLHttpRequest',
          'Cookie':'bid=a43806d9fcfbd235cf27098aaad8fd53_ixag9qs7; __utmt=1; __utma=1.209884112.1483020349.1483020349.1483438774.2; __utmb=1.12.10.1483438774; __utmz=1.1483020349.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); s=6111bfh98v; xq_a_token=faad54bc6ef67cf39d757db5842bbbe5bcffc6be; xq_r_token=61d51eb4c04cf5d8aca667bc37dc0e82337c9eb1; u=1944945575; xq_token_expire=Sat%20Jan%2028%202017%2019%3A11%3A30%20GMT%2B0800%20(CST); xq_is_login=1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1483020349,1483438768,1483441746; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1483441901'
          }
# 储存已导入mongodb的code
def ready_th(code):
    db['ready_code'].insert_one({'done':code})
# ready_th('300583')
ready_code = pd.DataFrame(list(db['ready_code'].find()))['done'].values
code_list_raw = ('%06d'%x for x in pd.read_csv(r'D:\W\python\stockFdate2\stock_datas\stock_basics\stock_basics.csv',encoding='gbk')['code'])
code_list = list(set(code_list_raw)^set(ready_code))
# code_list.remove('300588')
# code_list.remove(11111)
# code_list.remove('603032')
# code_list.remove('603035')
# code_list.remove('300587')
print(len(code_list),'left')

def stock_detail_data(code,th,info):
    db[code].update({},{"$set":{th:str(info)}})


base_url = 'https://xueqiu.com/stock/f10/finmainindex.json?symbol={0}&page=1&size=199'

def get_basics(code):
    code_1 = 'sh'+str(code) if int(code) > 599999 else 'sz'+str(code)
    print(code_1)
    r2 = requests.get(base_url.format(code_1),headers=header)
    json_data = json.loads(r2.text)
    j_data = json_data['list']
    for i in j_data:
        year_ = i['reportdate'][:4]
        th_ = str(int(i['reportdate'][4:6])//3)
        ye_th = '%s_%s'%(year_,th_)
        stock_detail_data(code,ye_th,i)
    ready_th(code)
    print(code,'appended')

if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map( get_basics,code_list)
    pool.close()
    pool.join()



# get_basics('600000')
# for code in code_list:
#     get_basics(code)

# get_basics('sz002244')







# r1 = response.read().decode('utf-8',errors='replace')
# req = urllib.request.Request(url=base_url,headers=header)
