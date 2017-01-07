from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import pymongo
client = pymongo.MongoClient('localhost',27017)
xingu = client['xingu']
xingu_info = xingu['sheet_tab']


def get_page_link(page_number):
    name_1 = []
    code_1 = []
    open = []
    new = []
    zql = []
    wxzql = []
    wxyxsg = []
    fxl = []
    ssrq = []

    for each_number in range(1,page_number):
        time.sleep(2)
        full_url = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=NS&sty=NSDXSYL&st=16&sr=-1&p={}'.format(each_number)
        wb_data = requests.get(full_url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        stock_datas = soup.select('body > p')[0].text.strip('([').strip('])').split('"')
        for i1 in stock_datas:
            i=i1.split(',')
            if len(i) > 12:
                name_1.append(i[0])
                code_1.append(i[1])
                open.append(i[2])
                new.append(i[3])
                zql.append('%.5f'%float(i[4]))
                wxzql.append('%.5f'%float(i[8]))
                wxyxsg .append(i[9])
                fxl.append(i[12])
                ssrq.append(i[-2])

    stock_info={
        'code':name_1,
        'name':code_1,
         '开盘价':open,
        '现价':new,
        '网上中签率%':zql,
        '网下中签率': wxzql,
        '网下有效申购数':wxyxsg,
        '总发行量(万股)':fxl,
        '上市日期':ssrq
    }




    '''
    print(wxzql,fxl)
    df = pd.DataFrame(stock_info,columns=['code', 'name', '开盘价', '现价', '网上中签率%', '网下中签率', '网下有效申购数','总发行量(万股)','上市日期'])
    print(df)
    df.to_excel(r'D:\GP\new_stock_datas.xlsx', index=False)
    '''
get_page_link(6)
