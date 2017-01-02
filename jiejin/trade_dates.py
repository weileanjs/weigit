import datetime
import easyutils
import pymongo
import pandas as pd
client = pymongo.MongoClient('localhost',27017)
db = client['trade_date']
tradedates =db['tarade_date']
raw_data1 = pd.read_csv(r'D:\W\python\data_history\day\raw_data\sh.csv',encoding='gbk')

dates_d = {}
for i in range(0,len(list(raw_data1['date']))):
    dates_d[str(i)] =list(raw_data1['date'])[i]
for x in tradedates.find():
    td = x.values()
    print(len(td))
date_1 = datetime.datetime.strptime('2016-12-01','%Y-%m-%d')
for i in range(len(td),len(td)+300):
    dates_d2 = {}
    oneday=datetime.timedelta(days=1)
    date_1=date_1+oneday
    dn1 =str(date_1)[0:10]
    dates_d2[str(i)] =dn1
    tradedates.insert_one(dates_d2)


#tradedates.insert_one(dates_d)

# def trade_date(datestr):
#     oneday = datetime.timedelta(days=1)
#     #now =datetime.datetime.now()
#     now = datetime.datetime.strptime('2017-12-31','%Y-%m-%d')
#     date_str = datetime.datetime.strptime(datestr,'%Y-%m-%d')
#     tradeday_d = {}
#     while date_str < now:
#         tradeday = datetime.datetime.strptime(totradedate(date_str),'%Y-%m-%d')
#         tradeday_d[str(num1+1)] = str(tradeday.strftime('%Y-%m-%d'))[0:10]
#         #print(tradeday)
#         date_str =tradeday +oneday
#         num1 = num1 +1
#
#         tradedates.insert_one(tradeday_d)
#
#
#
# def totradedate(date_1):
#     oneday=datetime.timedelta(days=1)
#     while easyutils.is_holiday(date_1.strftime('%Y%m%d'))==True:
#         date_1=date_1+oneday
#     return str(date_1)[0:10]
#
#
# trade_date('2016-12-01')
