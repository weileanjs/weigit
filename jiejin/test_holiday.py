import datetime
import pymongo
client = pymongo.MongoClient('localhost',27017)
db = client['trade_date']
tradedates =db['tarade_date']
td = []
for x in tradedates.find():
    x1 = x.values()
    for x2 in x1:
        td.append(x2)


    # for x11 in x.trade2016:
    #     td.append(x11)



def strtodatetime(datestr):
    onemonth=datetime.timedelta(days=30)
    date_str = datetime.datetime.strptime(datestr,'%Y-%m-%d')
    data_q6 = str(totradedate(date_str - onemonth*6))[0:10]
    data_q5 = str(totradedate(date_str - onemonth*5))[0:10]
    data_q4 = str(totradedate(date_str - onemonth*4))[0:10]
    data_q3 = str(totradedate(date_str - onemonth*3))[0:10]
    data_q2 = str(totradedate(date_str - onemonth*2))[0:10]
    data_q1 = str(totradedate(date_str - onemonth*1))[0:10]
    data_q0 = str(totradedate(date_str))[0:10]
    data_h1 = str(totradedate(date_str + onemonth*1))[0:10]
    data_h2 = str(totradedate(date_str + onemonth*2))[0:10]
    data_h3 = str(totradedate(date_str + onemonth*3))[0:10]
    date_list = [data_q6,data_q5,data_q4,data_q3,data_q2,data_q1,data_q0,data_h1,data_h2,data_h3]
    return date_list
def totradedate(date_1):
    oneday=datetime.timedelta(days=1)
    while str(date_1)[0:10] not in td:
        date_1=date_1+oneday
    return str(date_1)[0:10]

print(strtodatetime('2013-10-05'))

