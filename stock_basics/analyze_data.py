import time, random
import pandas as pd
import os
import pymongo
import numpy as np
import matplotlib.pyplot as plt
client = pymongo.MongoClient('localhost',27017)
db = client['stock_basics']
dbM_p = client['month_price']

stock_basic = pd.DataFrame(list(db['basic'].find({},{'_id':0})))
sk_area = stock_basic.groupby('area')['code'].agg(len)
sk_ar_ind = stock_basic.loc[(stock_basic['area'] == '浙江') & (stock_basic['industry'] == '元器件')]
#print(stock_basic.head())
# print(sk_area)
#print(sk_ar_ind)

sg_data = db['600000'].find({},{'_id':0,'area':0,'name':0,'timeToMarket':0,'industry':0})
data_ = pd.DataFrame(list(sg_data))
print(data_.head())
for b in sg_data:
    #for i,j in zip():
    k_raw = list(b.keys())
    # k_remove = ['area','name','timeToMarket','industry']
    # k_ = list(set(k_raw)-set(k_remove))
    v_ =[i for i in  map(eval,list(b.values()))]
    # print(v_)
    # print(k_raw)


    #print(list(v_raw))
    #eval(b)

