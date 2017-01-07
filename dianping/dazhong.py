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


now =datetime.datetime.now().strftime('%Y-%m-%d')[0:10]
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Connection':'close',
'Referer':'http://bzclk.baidu.com/'
}
base_url = 'http://www.dianping.com/search/category/3/10'
req = urllib.request.Request(url=base_url,headers=headers)
response=urllib.request.urlopen(req)
html = response.read().decode('utf-8',errors='replace')
soup = BeautifulSoup(html,'lxml')
area_ = soup.select('#region-nav > a > span')
area_id = soup.select('#region-nav > a ')
area_name = []
area_id_l =[]
area_d = {}
for x in area_id:
    area_d[x.get('href')[-2:]]=x.span.text
    # area_name.append(x.span.text)
    # area_id_l.append(x.get('href')[-2:])
#print(area_d)

def formatshopjson(json_data,ar,x):
    name = []
    priceText = []
    categoryName = []
    id = []
    shopType = []
    regionName = []
    categoryId = []
    shopPower = []
    get_l = []
    for shop in json_data['list']:
        try:
            name.append(shop['name'])
        except KeyError:
            name.append('n')
        priceText.append(shop['priceText'].replace('￥','').replace('/人',''))
        categoryName.append(shop['categoryName'])
        id.append(shop['id'])
        shopType.append(shop['shopType'])
        regionName.append(shop['regionName'])
        categoryId.append(shop['categoryId'])
        shopPower.append(shop['shopPower'])
    area_h = [ar]*len(name)
    shop_info = pd.DataFrame({'name':name,'priceText':priceText,'categoryName':categoryName,'id':id,'shopType':shopType,'regionName':regionName,'categoryId':categoryId,'shopPower':shopPower,'area':area_h})
    if len(shop_info.index) != 0:
        db['dianping'].insert_many(shop_info.to_dict('records'))
    else:
        pass

api_url = 'http://mapi.dianping.com/searchshop.json?start={0}&regionid={1}&categoryid=10&sortid=3&locatecityid=3&cityid=3'
def get_api_info(a_id):
    for x in range(1,5000,25):
        print(a_id,x)
        api_url_= api_url.format(x,a_id)
        req =requests.get(api_url_,headers=headers)
        #shop_data = json.loads(req.text)
        shop_data = json.loads(req.text)
        ar = area_d[a_id]
        formatshopjson(shop_data,ar,x)
        count = int(shop_data['recordCount'])
        if x > 4975 or x > (count-25):
            print(ar+'  is ok ')
            break


# get_api_info('58')
# if __name__ == '__main__':
#     pool = Pool(processes=13)
#     pool.map(get_api_info,area_d.keys())
#     pool.close()
#     pool.join()
data = pd.DataFrame(list(db['hz_foods'].find()))
data.pop('_id')
print(data.head(20))
print(data.shape)

