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
db = client['dianping']
data = pd.DataFrame(list(db['hz_foods'].find()))
shop_l = list(data['id'])
got = list(pd.DataFrame(list(db['got'].find()))['got'])
now_url_l =list(set(shop_l).difference(set(got))) # b中有而a中没有的

print('剩余:  '+str(len(now_url_l)))

rul = 'http://www.dianping.com/shop/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Connection':'close',
'Referer':'http://bzclk.baidu.com/'
}

def add_shop_info(id,info):
    #shop_raw_info = pd.DataFrame(list(db['hz_foods'].find({'id':23954417})))
    db['hz_foods'].update_one({'id':id},{"$set":info})
    x_dict = {'got':id}
    db['got'].insert_one(x_dict)
#print(shop_raw_info)

def get_shop_allinfo(id):
    shop_url = rul+str(id)
    print(shop_url)
    try:
        req = urllib.request.Request(url=shop_url,headers=headers)
        response=urllib.request.urlopen(req)
        html = response.read().decode('utf-8',errors='replace')
        soup = BeautifulSoup(html,'lxml')
        s_dict = {}
        address = soup.select('#basic-info > div.expand-info.address > span.item')[0].text.replace(r'\n','').strip()
        try:
            tel = soup.select('#basic-info > p.expand-info.tel > span.item')[0].text
        except IndexError:
            tel = 0
        #basic-info > div.brief-info
        shop_det = soup.select('#basic-info > div.brief-info > span')
        if len(shop_det) == 6:
            pinlun = shop_det[1].text.replace('条评论','')
            kouwei = shop_det[3].text.replace('口味：','')
            huanjing = shop_det[4].text.replace('环境：','')
            fuwu = shop_det[5].text.replace('服务：','')
        elif len(shop_det) == 5:
            pinlun = 0
            kouwei = shop_det[2].text.replace('口味：','')
            huanjing = shop_det[3].text.replace('环境：','')
            fuwu = shop_det[4].text.replace('服务：','')
        else:
            print(id)

        #print(address,pinlun,tel,kouwei,huanjing,fuwu)

        s_dict['address'] = address
        s_dict['tel'] = tel
        s_dict['评论'] = pinlun
        s_dict['口味'] = kouwei
        s_dict['环境'] = huanjing
        s_dict['服务'] = fuwu
        print(s_dict)
        add_shop_info(id,s_dict)
        time.sleep(0.3)
    except urllib.error.HTTPError:
        pass



# shop_raw_info = pd.DataFrame(list(db['hz_foods'].find({'id':23954417})))
# print(shop_raw_info)

if __name__ == '__main__':
    pool = Pool(processes=5)
    pool.map( get_shop_allinfo,map(int, now_url_l))
    pool.close()
    pool.join()


# for x in now_url_l:
#     i = int (x)
#     get_shop_allinfo(i)
