import tushare as ts
import pymongo
import pandas as pd
client = pymongo.MongoClient('localhost',27017)
db = client['stock_basics']
import json


df_basic = pd.read_csv(r'D:\W\python\stockFdate2\stock_datas\stock_basics\stock_basics.csv',encoding='gbk')

df_basic_r = df_basic.set_index('code',drop=False).loc[:,['code','industry','area','timeToMarket','name']]
db['basic'].insert_many(df_basic_r.to_dict('records'))
# print(df_basic_r['code'].values)
# print( df_basic_r.loc[600000]['industry'])
# def stoct_basic_info(code):
#     dict_1 = {}
#     dict_1['industry'] = df_basic_r.loc[code]['industry'],
#     dict_1['area'] = df_basic_r.loc[code]['area'],
#     dict_1['timeToMarket'] = str(df_basic_r.loc[code]['timeToMarket']),
#     dict_1['name'] = df_basic_r.loc[code]['name'],
#     db['%06d'%code].insert_one(dict_1)
# for code in df_basic['code'].values:
#     print('%06d'%code)
#     stoct_basic_info(code)      #存储'industry','area','timeToMarket'

'''
# report_data_raw = ts.get_report_data(2014,3)
# report_data_raw.to_csv('xxxx.csv')
report_data = pd.read_csv('xxxx.csv',encoding='gbk')
report_data_r = report_data.set_index('code',drop=True).loc[:,['eps', 'eps_yoy', 'bvps', 'roe', 'epcf', 'net_profits', 'profits_yoy', 'distrib', 'report_date']]
report_data_r1 = report_data_r.drop_duplicates()

# profit_data_raw = ts.get_profit_data(2014,3)
# profit_data_raw.to_csv('xxxxx.csv')
profit_data = pd.read_csv('xxxxx.csv',encoding='gbk').drop_duplicates()
columns_p = profit_data.columns.tolist()
# print(profit_data.head(5))
# print(columns_p)
# print(profit_data.index.astype(str))

df3 = pd.merge(report_data.drop_duplicates(),profit_data.drop_duplicates(),on='code')
print(len(report_data.drop_duplicates()))
print(len(profit_data.drop_duplicates()))
print(len(df3))
# df3.to_csv('df333.csv')
# print(df3.head(10))
# profit_data_r = report_data.set_index('code',drop=True).loc[:,['eps', 'eps_yoy', 'bvps', 'roe', 'epcf', 'net_profits', 'profits_yoy', 'distrib', 'report_date']]
# profit_data_r1 = report_data_r.drop_duplicates()





# series 转 json 格式
def series_to_json(s):
    dict_s_j = {}
    s_k = s.index.tolist()
    s_v = s.values.tolist()
    for k ,v in zip(s_k ,s_v):
        dict_s_j[k] = str(v)
    return str(dict_s_j)




def stock_detail_data(code,th):
    dict_1 = {}
    dict_1[th] = str(report_data_r1.loc[code])
    s = report_data_r1.loc[code]
    ret = series_to_json(s)
    db[str(code)].insert_one({th:str(ret)})


def stock_profit_data(code,th):
    dict_1 = {}
    dict_1[th] = str(report_data_r1.loc[code])
    s = report_data_r1.loc[code]
    ret = series_to_json(s)
    db[str(code)].insert_one({th:str(ret)})



# for co in report_data_r1.index:
#     print(co)
#     stoct_report_data(co,'2014-3')
#
#
# read_ = db['600720'].find({},{'2014-3':1,"_id":0})
# for i in read_:
#     print(i)
# a1 = list(read_[2].values())[0]
# print(a1)
# a2 = eval(a1)
# a3 = pd.Series(a2)
# print(a3['roe'])


# roe,净资产收益率(%)
# net_profit_ratio,净利率(%)
# gross_profit_rate,毛利率(%)
# net_profits,净利润(万元)
# esp,每股收益
# business_income,营业收入(百万元)
# bips,每股主营业务收入(元)
# code,代码
# name,名称
# industry,所属行业
# area,地区
# pe,市盈率
# outstanding,流通股本(亿)
# totals,总股本(亿)
# totalAssets,总资产(万)
# liquidAssets,流动资产
# fixedAssets,固定资产
# reserved,公积金
# reservedPerShare,每股公积金
# esp,每股收益
# bvps,每股净资
# pb,市净率
# timeToMarket,上市日期
# undp,未分利润
# perundp, 每股未分配
# rev,收入同比(%)
# profit,利润同比(%)
# gpr,毛利率(%)
# npr,净利润率(%)
# holders,股东人数
'''
