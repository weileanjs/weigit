from multiprocessing import Pool
import datetime
from bs4 import BeautifulSoup
import urllib
import pandas as pd
import pymongo
import matplotlib.pyplot as plt
import numpy as np
client = pymongo.MongoClient('localhost',27017)
db = client['hz_fc']
import charts

# date = '2016-12-07'
# area_l = ['xihu','jianggan','gongshu','shangcheng','xiacheng','binjiang','xiaoshan','yuhang']
# f_l = []
# for x in area_l:
#     f_name = date+'_'+x
#     f_l.append(f_name)

# def read_house_info(area):
#     f_name = str(date+'_'+area)
#     data = pd.DataFrame(list(db[f_name].find()))
#     data.pop('_id')
#
#     data['area'] = [area]*len(data.index)
#     db['2016-12-07'].insert_many(data.to_dict('records'))
# for x in area_l:
#     read_house_info(x)


#read_house_info('2016-12-07_xiaoshan')

#
# a = map(lambda  x:x+1 ,[1,2])
# for i in a:
#     print(i)


def read_house_info():
    data = pd.DataFrame(list(db['2016-12-27'].find()))
    data.pop('_id')
    data.pop('followinfo')
    data.pop('mianji_num')
    print(data.head())
    data.to_excel(r'D:\hz2016-12-27.xlsx')
read_house_info()
