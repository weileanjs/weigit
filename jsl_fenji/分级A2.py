from bs4 import BeautifulSoup
import pymongo
import requests
import time
import datetime
import urllib

sell_url = 'https://www.jisilu.cn/data/sfnew/get_fund_quote_list/150331'


def he_yi_jia_data():
    start_url = 'https://www.jisilu.cn/data/sfnew/funda_list/'
    response = urllib.request.urlopen(start_url)
    html = response.read().decode('utf-8',errors='replace')
    soup = BeautifulSoup(html,'lxml')
    an = soup.select('p ')[0].text[19:].split('},{')
    # for x,y ,n in zip(a1[0].split(':'),a1[1].split(':'),range(0,50)):
    #     data_test={x:n
    #     }
    #     print(data_test)
    for l in an:
        ll=l.split(':')
        gd1 = ll[37].split('"')[1].split('%')[0]
        lrxzsy = lambda x: float(x) if '.' in x else None
        t1yjl =  lambda x: float(ll[41].split('"')[1].split('%')[0]) if len(ll)==48 else float(ll[42].split('"')[1].split('%')[0])
        t1yj2 =  lambda x: float(ll[42].split('"')[1].split('%')[0]) if len(ll)==48 else float(ll[43].split('"')[1].split('%')[0])
        now_data = {
            'Acode':ll[1].split('"')[1],
            '成交额':float(ll[7].split('"')[1]),
            '母鸡涨幅%':float(ll[8].split('"')[1].split('%')[0]),
            'A涨幅%':float(ll[11].split('"')[1].split('%')[0]),
            '母鸡code':ll[13].split('"')[1],
            'A价格': float(ll[19].split('"')[1]),
            '理论下折收益%':lrxzsy(gd1),
            '溢价率%':float(ll[32].split('"')[1].split('%')[0]),
            'T-1溢价率%':t1yjl(1),
            'T-2溢价率%':t1yj2(1),
        }
    #     if now_data['溢价率%'] < -1:
    #         print('合并赎回，溢价率小于-1')
    #         print(now_data['Acode'])
    #     elif now_data['溢价率%'] > 1.2:
    #         print('申购，溢价率大于1.2%')
    #         print(now_data)
    # return now_data


def gold_zheyi_data():
    gold_url = 'https://www.jisilu.cn/jisiludata/etf.php?qtype=pmetf'
    response = urllib.request.urlopen(gold_url)
    html = response.read().decode('utf-8',errors='replace')
    soup = BeautifulSoup(html,'lxml')
    a_god = soup.select('p ')[0].text[19:].split('},{')
    for i in a_god:
        gold_i = i.split(':')
        gold_data={
            'ETFcode':gold_i[1].split('"')[1],
            '跟踪目标':gold_i[5].split('"')[1],
            '指数涨跌幅%':float(gold_i[7].split('"')[1].split('%')[0]),
            'ETF现价':float(gold_i[8].split('"')[1]),
            'ETF成交额':float(gold_i[9].split('"')[1]),
            'ETF涨跌幅%':float(gold_i[13].split('"')[1].split('%')[0]),
            '指数估值':float(gold_i[14].split('"')[1]),
            '溢价率%':float(gold_i[18].split('"')[1].split('%')[0]),
            'T-1净值':float(gold_i[19].split('"')[1]),
            '规模（亿元）':float(gold_i[22].split('"')[1]),
        }
        if gold_data['溢价率%'] < -0.2:
            print('买入，溢价率小于-0.2%')
            print(gold_data)
        elif gold_data['溢价率%'] > 0.24:
            print('卖出，溢价率大于0.24%')
            print(gold_data)
    # for x,y,n in zip(a_god[2].split(':'),a_god[3].split(':'),range(0,50)):
    #     data_test={x:y,'index':n }
    #     print(data_test)




def get_detail(code):
    base_url = 'https://www.jisilu.cn/data/sfnew/detail/'+code
    test_url= 'https://www.jisilu.cn/data/sfnew/detail/150022'
    response = urllib.request.urlopen(test_url)
    html = response.read().decode('utf-8',errors='replace')
    soup = BeautifulSoup(html,'lxml')
    shfy = soup.select(' tr td table.tablesorter td[colspan="2"]')[1].text  #赎回费用
    mjdm = soup.select(' tr td table.tablesorter td')[1].text  #母鸡代码
    gsjz = soup.select('  tr td table.tablesorter td')  #估算净值
    print(gsjz)
get_detail('gsjz')
#\31 63109 > td:nth-child(21)
#td[colspan="2"]
#body > div.i_bd.w95.i_clear.i_allbg > div:nth-child(2) > table > tbody > tr > td:nth-child(5) > table:nth-child(1) > tbody > tr:nth-child(6) > td
# while 1==1:
#     gold_zheyi_data()
#     he_yi_jia_data()
#     time.sleep(30)
#     print(datetime.datetime.now())
