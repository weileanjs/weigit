import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import re
import lxml
import time
import os
from multiprocessing import Pool
import pymongo
import time


client = pymongo.MongoClient('localhost',27017)
db = client['abcam']
info =db['abcam']
saved = pd.DataFrame(list(db['saved_items'].find()))['saved'].tolist()
err = pd.DataFrame(list(db['outlist'].find()))['outlist'].tolist()

def com_url(u):
    return 'http://www.abcam.com'+u
item_urls =[i for i in map(com_url,pd.read_csv('1-6000.csv')['item_url'].tolist())]
left = set(item_urls)-set(saved)
print(len(item_urls),len(saved),'剩余__',len(left))



proxies = {"http": "http://123.59.187.44:8118","https": "https://123.59.187.44:8118"}


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
'Accept':'text/html, */*; q=0.01',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Accept-Encoding':'gzip, deflate, sdch',
'Connection':'keep-alive',
'Referer':'http://www.abcam.com/products?selected.productType=Primary+antibodies&pageNumber=2',
'X-NewRelic-ID':'VQIAU1ZQGwsDU1JQBw==',
'X-Requested-With':'XMLHttpRequest'
}



def code_price_size(url):
    match = re.search(r'-([a-zA-Z]+)(\d+).html',url)
    jsn = 'http://www.abcam.com/datasheetproperties/availability?{}Id={}'.format(match.group(1),match.group(2))
    req = requests.get(jsn,headers=headers)
    d_ = json.loads(req.text)
    try:
        product_code = d_['size-information']['ProductCode']
    except KeyError:
        product_code ='{}{}'.format(match.group(1),match.group(2))
    try:
        price = d_['size-information']['Sizes'][0]['Price']
    except IndexError:
        price = 0
    try:
        size = d_['size-information']['Sizes'][0]['Size']
    except IndexError:
        size = 0
    return {'product_code':product_code,'price':price,'size':size}

def outoflist(url):
    db['outlist'].insert({'outlist':url})


def get_item_page(url):
    print(url)
    pd_date = code_price_size(url)
    req2 = requests.get(url)
    soup = BeautifulSoup(req2.text,'lxml')
    try:
        product_name_ = soup.select('#description_primaries_suboverview > ul > li > span.value')[0]
        if re.search(r'">(.*)<b',str(product_name_)):
            product_name = re.search(r'">(.*)<b',str(product_name_)).group(1)
        else:
            product_name = soup.select('#description_primaries_suboverview > ul > li > span.value')[0].text
        try:
            description = soup.select('#description_primaries_suboverview > ul > li:nth-of-type(2) > div')[0].text
        except IndexError:
            description = 'none'

        tbody_tr = soup.select('#description_applications > table > tbody > tr')

        applic = {}
        application =[]
        abreviews = []
        notes = []
        for tr in tbody_tr:
            # print(tr)
            application_ = tr.select(' td.name > abbr')[0].text
            abreviews_ = (tr.select('td.value.value1--addon > span')[0].get('class')[1] if len(tr.select('td.value.value1--addon > span'))!=0 else 0)
            notes_ = tr.select(' td.value.value2--addon')[0].text
            application.append(application_)
            abreviews.append(abreviews_)
            notes.append(notes_)
        applic['application'] = application
        applic['abreviews'] = abreviews
        applic['notes'] = notes
        pd_date['applic'] = applic
        pd_date['product_name'] = product_name
        pd_date['description'] = description
        pd_date['url'] = url
        db['item'].insert(pd_date)
        db['saved_items'].insert_one({'saved':url})
        # pd_date['product_name'] = product_name
        # pd_date['product_name'] = product_name
        print('ok')
        time.sleep(1)

    except IndexError:
        print(soup.select('#site-body > div > div > div > h1')[0].text)
        db['notavailable'].insert({'url':url})


if __name__ == '__main__':

    pool = Pool(processes=1)
    pool.map(get_item_page,left)    #item_urls
    pool.close()
    pool.join()




