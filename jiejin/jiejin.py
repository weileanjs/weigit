from bs4 import BeautifulSoup
import requests
from .test_date import get_prick
from .test_holiday import strtodatetime
import time
import pandas as pd
import pymongo



def get_page_link():
    name_1 = []
    code_1 = []
    jjrq = []
    zzgbl = []
    amount = []
    now = []
    dqsz = []
    fqq6 = []
    fqq5 = []
    fqq4 = []
    fqq3 = []
    fqq2 = []
    fqq1 = []
    fqq0 = []
    fqh1 = []
    fqh2 = []
    fqh3 = []

    for year in range(2010,2017):
        for month in range(1,13):
            full_url = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=FD&sty=BST&st=3&sr=true&fd={}&stat={}'.format(year,month)
            wb_data = requests.get(full_url).text
            rep = wb_data.strip('(["').strip('"])').split('","')
            print(year,month,'is downloading')
            for i in rep:
                 time.sleep(0.5)
                 a = i.split(',')
                 name_1.append(a[3])
                 print(a[3])
                 code_1.append(a[1])
                 jjrq.append(a[4])
                 now.append(a[7])
                 date_take = strtodatetime(a[4])
                 fqq6.append(get_prick(a[1],date_take[0]))
                 fqq5.append(get_prick(a[1],date_take[1]))
                 fqq4.append(get_prick(a[1],date_take[2]))
                 fqq3.append(get_prick(a[1],date_take[3]))
                 fqq2.append(get_prick(a[1],date_take[4]))
                 fqq1.append(get_prick(a[1],date_take[5]))
                 fqq0.append(get_prick(a[1],date_take[6]))
                 fqh1.append(get_prick(a[1],date_take[7]))
                 fqh2.append(get_prick(a[1],date_take[8]))
                 fqh3.append(get_prick(a[1],date_take[9]))

                 try:
                     zzgbl.append('%0.2f'%(float(a[6])*100))
                 except ValueError:
                     zzgbl.append('n')
                 try:
                     amount.append('%0.2f'%(float(a[5])/10000))
                 except ValueError:
                     amount.append('n')
                 try:
                     dqsz.append('%0.2f'%(float(a[8])/100000000))
                 except ValueError:
                     dqsz.append('n')

    stock_info={
    'code':code_1,
    'name':name_1,
    '解禁日期':jjrq,
    '占总股本比例%':zzgbl,
    '解禁数量（万股）':amount,
    '现价':now,
    '当前市值（亿）':dqsz,
    '前6m':fqq6,
    '前5m':fqq5,
    '前4m':fqq4,
    '前3m':fqq3,
    '前2m':fqq2,
    '前1m':fqq1,
    '解禁日':fqq0,
    '后1m':fqh1,
    '后2m':fqh2,
    '后3m':fqh3,
     }

    df = pd.DataFrame(stock_info,columns=['code', 'name', '解禁日期', '占总股本比例%','解禁数量（万股）','现价','当前市值（亿）',
    '前6m','前5m','前4m','前3m','前2m','前1m','解禁日','后1m','后2m','后3m'])
    df.to_excel(r'D:\GP\jiejin1016.xlsx', index=False)

get_page_link()
