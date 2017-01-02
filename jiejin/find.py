import datetime
import easyutils
import pymongo
client = pymongo.MongoClient('localhost',27017)
db = client['trade_date']
tradedates =db['tarade_date']
date = '2016-11-07'
tradedate_1 = []
for x in tradedates.find():
    tradedate_1 = list(x.values())+tradedate_1
if date not in tradedate_1:
    print('in')



