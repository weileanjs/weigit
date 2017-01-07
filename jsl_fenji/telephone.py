from bs4 import BeautifulSoup
import pymongo
import requests
import random
import time
client = pymongo.MongoClient('localhost',27017)
tele_num = client['ceshi']
telephone = tele_num['url_list']
base_url = 'http://hz.58.com/shoujihao/pn1'
def get_tele(url,pages):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    tele_urls = soup.select('div.boxlist ul li a.t')

    for tele in tele_urls:
        if tele.find('span','jz-title'):
            print('jz-title')
            pass
        else:
            tele_url = tele.get('href').split('?')[0]
            print(tele_url)

get_tele('http://hz.58.com/shoujihao/pn1/',1)
