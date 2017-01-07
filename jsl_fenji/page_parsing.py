from bs4 import BeautifulSoup
import pymongo
import requests
import random
import time
client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list']
#spider1
def get_links_from(channel,pages,who_sell=0):
    #http://hz.58.com/iphonesj/pn2/
    list_view = '{}{}/pn{}'.format(channel,str(who_sell),str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find('div','noinfo aaa'):
        print('no info')
    else:
        for link in soup.select('div.infocon td.t a'):
            item_link  = link.get('href').split('?')[0]
            url_list.insert_one({'url':item_link})

#get_links_from('http://hz.58.com/iphonesj/',2)

# def get_item_info(url):
#     wb_data = requests.get(url)
#     time.sleep(1)
#     soup = BeautifulSoup(wb_data.text,'lxml')
#     title = soup.title.text
#     price = soup.select('span.price_now i')[0].text
#     area = soup.select('div.palce_li i')[0].text
#     view = soup.select('span.look_time')[0].text
#     print(title,price,area,view)
# get_item_info('http://zhuanzhuan.58.com/detail/790016256478085124z.shtml')


