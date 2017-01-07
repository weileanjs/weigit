from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import pymongo

# client = pymongo.MongoClient('localhost',27017)
# xingu = client['xingu']
# xingu_info = xingu['sheet_tab']

def get_page_link():
    name_1 = []
    code_1 = []
    jjrq = []
    zzgbl = []
    amount = []
    now = []
    dqsz = []

    for year in range(2016,2017):
        for month in range(1,2):
            full_url = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=FD&sty=BST&st=3&sr=true&fd={}&stat={}'.format(year,month)
            wb_data = requests.get(full_url).text
            rep = wb_data.strip('(["').strip('"])').split('","')
            print(year,month,'is downloading')
            for i in rep:
                 a = i.split(',')
                 name_1.append(a[3])
                 code_1.append(a[1])
                 jjrq.append(a[4])
                 now.append(a[7])
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
     }

    df = pd.DataFrame(stock_info,columns=['code', 'name', '解禁日期', '占总股本比例%','解禁数量（万股）','现价','当前市值（亿）'])
    df.to_excel(r'D:\GP\jiejin01.xlsx', index=False)

get_page_link()
