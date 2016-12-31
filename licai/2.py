import json
from multiprocessing import Pool
import datetime
from sklearn.cluster import k_means
from bs4 import BeautifulSoup
import requests
import urllib
import pandas as pd
import numpy as np
import time
import charts
import requests
now =datetime.datetime.now().strftime('%Y-%m-%d')[0:10]
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Connection':'keep-alive',
'Referer':'http://wap.dianping.com/shoplist/3/r/62/c/10/s/s'
}
params = {'start':'50','regionid':'62','categoryid':'10','sortid':'3','locatecityid':'3','cityid':'3'}
base_url = 'http://wap.dianping.com/shoplist/3/r/62/c/10/s/s'
req = requests.get(url=base_url,headers=headers,params=params)

# soup = BeautifulSoup(html,'lxml')
# area_ = soup.select('#region-nav > a > span')
# area_id = soup.select('#region-nav > a ')
# title = soup.select('#shop-all-list > ul > li > div.txt > div.tit > a > h4')
print(req.text)
# print(area_id)
# print(area_)
# print(title)

