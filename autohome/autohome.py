import json
from multiprocessing import Pool
import datetime
from bs4 import BeautifulSoup
import requests
from remain import now_url_l
import urllib
import pandas as pd
import numpy as np
import time
import pymongo
client = pymongo.MongoClient('localhost',27017)
db = client['autohome']

proxies = {"http": "http://120.77.210.7:80","https": "https://120.77.210.7:80"}

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Referer':'http://club.autohome.com.cn/bbs',
'Host':'club.autohome.com.cn',
}

base_url = 'http://club.autohome.com.cn/bbs/forum-c-3788-{}.html?qaType=-1'
view_reply_api = 'http://club.ajax.autohome.com.cn/topic/rv?fun=jsonprv&callback=jsonprv&ids={}'

# 储存已导入mongodb的url
def ready_th(url):
    db['ready_url_boyue'].insert_one({'done':url})

def get_view_reply(id):
    req2 = requests.get(view_reply_api.format(id),proxies=proxies)
    print(req2.text)
    get_v_r = eval(req2.text.strip('jsonprv([').strip('])'))
    return get_v_r
def to_list(sp):
    for i in sp:
        yield i.text.strip(' ').replace('\r\n','')
def to_list_lang(sp):
    for i in sp:
        yield i.get('lang')

def get_urldata(idx):
    print(idx)
    url = base_url.format(idx)
    req1 = requests.get(url,proxies=proxies)
    soup = BeautifulSoup(req1.text,'lxml')
    title = soup.select('#subcontent a.a_topic')
    fb_date = soup.select('#subcontent span.tdate')
    fb_id = soup.select('#subcontent dd.cli_dd')[1:]
    author = soup.select('#subcontent  a.linkblack')[0::2]
    views = []
    replys = []
    v_r = get_view_reply('%2C'.join(list(to_list_lang(fb_id))))
    for x in list(to_list_lang(fb_id)):
        for i in v_r:
            if int(x) == i['topicid']:
                views.append(i['views'])
                replys.append(i['replys'])

    data = pd.DataFrame({'title':list(to_list(title)),'fb_date':list(to_list(fb_date)),'author':list(to_list(author)),'fb_id':list(to_list_lang(fb_id)),'views':views,'replys':replys})
    db['boyue'].insert_many(data.to_dict('records'))
    ready_th(idx)
    time.sleep(3)

# for i in now_url_l:
#     get_urldata(i)
#     time.sleep(2)

if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map(get_urldata,now_url_l)
    pool.close()
    pool.join()
# data = pd.DataFrame(list(db['hz_foods'].find()))
# data.pop('_id')
# print(data.head(20))
# print(data.shape)

