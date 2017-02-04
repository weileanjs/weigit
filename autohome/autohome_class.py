import json
from multiprocessing import Pool
import datetime
from bs4 import BeautifulSoup
import requests
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
def ready_url(chexing,num = 1001):
    client = pymongo.MongoClient('localhost',27017)
    db = client['autohome']
    ready_url= pd.DataFrame(list(db['ready_url_'+chexing].find()))['done'].tolist()
    all_ = [i for i in range(1,num)]
    now_url_l =list(set(all_).difference(set(ready_url))) # b中有而a中没有的
    print('剩余:  '+str(len(now_url_l)))
    return now_url_l

class Autohome(object):
    def __init__(self,base_url,chexing,idx):
        self.base_url = base_url
        # base_url = 'http://club.autohome.com.cn/bbs/forum-c-3788-{}.html?qaType=-1'
        self.chexing = chexing
        self.idx = idx
        self.view_reply_api = 'http://club.ajax.autohome.com.cn/topic/rv?fun=jsonprv&callback=jsonprv&ids={}'

    # 储存已导入mongodb的url
    def ready_th(self,url):
        db['ready_url_'+self.chexing].insert_one({'done':url})

    def get_view_reply(self,id):
        req2 = requests.get(self.view_reply_api.format(id))  #,proxies=proxies
        get_v_r = eval(req2.text.strip('jsonprv([').strip('])'))
        return get_v_r
    def to_list(self,sp):
        for i in sp:
            yield i.text.strip(' ').replace('\r\n','')
    def to_list_lang(self,sp):
        for i in sp:
            yield i.get('lang')


    def get_urldata(self):
        print(self,self.idx)
        url = self.base_url.format(self.idx)
        req1 = requests.get(url,)              #proxies=proxies
        soup = BeautifulSoup(req1.text,'lxml')
        title = soup.select('#subcontent a.a_topic')
        fb_date = soup.select('#subcontent span.tdate')
        fb_id = soup.select('#subcontent dd.cli_dd')[1:]
        author = soup.select('#subcontent  a.linkblack')[0::2]
        views = []
        replys = []
        v_r = self.get_view_reply('%2C'.join(list(self.to_list_lang(fb_id))))
        for x in list(self.to_list_lang(fb_id)):
            for i in v_r:
                if int(x) == i['topicid']:
                    views.append(i['views'])
                    replys.append(i['replys'])

        data = pd.DataFrame({'title':list(self.to_list(title)),'fb_date':list(self.to_list(fb_date)),'author':list(self.to_list(author)),'fb_id':list(self.to_list_lang(fb_id)),'views':views,'replys':replys})
        db[self.chexing].insert_many(data.to_dict('records'))
        self.ready_th(self.idx)
        time.sleep(3)






base_url = 'http://club.autohome.com.cn/bbs/forum-c-2615-{}.html'
chexing = 'h2'
def input_idx(idx):
    # idx = [1,2,3,4]
    a_cla = Autohome(base_url,chexing,idx)
    a_cla.get_urldata()




if __name__ == '__main__':
    pool = Pool(processes=4)
    try:
        pool.map(input_idx,ready_url(chexing,num = 1000))
        pool.close()
        pool.join()
    except KeyError:
        pool.map(input_idx,[1,2,3,4])
        pool.close()
        pool.join()
        print('try again')



