# coding: utf-8
#下载基础数据
import pandas
import os
import pandas as pd
import numpy as np
import time
import random
import tushare as ts
import pymongo


class getbasicdata:
    def __init__(self,startY,stopY):
        self.startY = startY
        self.stopY = stopY
        client = pymongo.MongoClient('localhost',27017)
        db = client['stock_basics']
    def get_basic(self):
        client = pymongo.MongoClient('localhost',27017)
        db = client['stock_basics']
        df_stock_basics = ts.get_stock_basics()
        for code in df_stock_basics.index:
            dict_1 = {}
            dict_1['industry'] = df_stock_basics.loc[code]['industry'],
            dict_1['area'] = df_stock_basics.loc[code]['area'],
            dict_1['timeToMarket'] = str(df_stock_basics.loc[code]['timeToMarket']),
            db[code].insert_one(dict_1)


    def report_data(self):
        for ye in range(self.startY,self.stopY):
            for th in [1,2,3,4]:
                df_report_data = ts.get_report_data(ye,th).drop_duplicates(),
                df_profit_data = ts.get_profit_data(ye, th).drop_duplicates(),
                df_operation_data = ts.get_operation_data(ye, th).drop_duplicates(),
                df_growth_data = ts.get_growth_data(ye, th).drop_duplicates(),
                df_debtpaying_data = ts.get_debtpaying_data(ye, th).drop_duplicates(),
                df_cashflow_data = ts.get_cashflow_data(ye, th).drop_duplicates(),

                df_combime = pd.merge(df_report_data,df_profit_data,on='code',how='outer')
                df_combime1 = pd.merge(df_combime,df_operation_data,on='code',how='outer')
                df_combime2 = pd.merge(df_combime1,df_growth_data,on='code',how='outer')
                df_combime3 = pd.merge(df_combime2,df_debtpaying_data,on='code',how='outer')
                df_combime4 = pd.merge(df_combime3,df_cashflow_data,on='code',how='outer')

# def to_getstockdata(a1,a2):
#     aaa=getbasicdata(a1,a2)
#     aaa.report_data()
#     aaa.profit_data()
#     aaa.operation_data()
#     aaa.growth_data()
#     aaa.debtpaying_data()
#     aaa.cashflow_data()
#     aaa.stock_basics()

if __name__=="__main__":
    p = getbasicdata
    #start = p.get_basic('a')

    #to_getstockdata(2007,2017)




# df3 = pd.merge(report_data.drop_duplicates(),profit_data.drop_duplicates(),on='code')
# print(len(report_data.drop_duplicates()))


    #             if os.path.isfile("stock_datas\\report_data\\report_data%s%s.csv" %(ye,th)):
    #                 print("report_data%s%s.csv" %(ye,th)+'  is exist')
    #             else:
    #                 try:
    #                     print("report_data%s%s.csv" %(ye,th)+'  is downloading')
    #                     time.sleep(random.random()*2)
    #                     df_report_data = ts.get_report_data(ye,th)
    #                     df_report_data.to_csv('stock_datas\\report_data\\report_data%s%s.csv' %(ye,th))
    #                 except AttributeError:
    #                     print("report_data%s%s.csv" %(ye,th)+'  and later is not Allowed')
    #                     break
    #
    # def profit_data(self):
    #     for ye in range(2007, 2016):
    #         for th in [1, 2, 3, 4]:
    #             if os.path.isfile("stock_datas\\profit_data\\profit_data%s%s.csv" % (ye, th)):
    #                 print("profit_data%s%s.csv" % (ye, th) + '  is exist')
    #             else:
    #                 try:
    #                     print("profit_data%s%s.csv" % (ye, th) + '  is downloading')
    #                     time.sleep(random.random() * 2)
    #                     df_profit_data = ts.get_profit_data(ye, th)
    #                     df_profit_data.to_csv('stock_datas\\profit_data\\profit_data%s%s.csv' % (ye, th))
    #                 except AttributeError:
    #                     print("profit_data%s%s.csv" % (ye, th) + ' and later is not Allowed')
    #                     break
    #
    # def operation_data(self):
    #     for ye in range(self.startY, self.stopY):
    #         for th in [1, 2, 3, 4]:
    #             if os.path.isfile("stock_datas\\operation_data\\operation_data%s%s.csv" % (ye, th)):
    #                 print("operation_data%s%s.csv" % (ye, th) + '  is exist')
    #             else:
    #                 try:
    #                     print("operation_data%s%s.csv" % (ye, th) + '  is downloading')
    #                     time.sleep(random.random() * 2)
    #                     df_operation_data = ts.get_operation_data(ye, th)
    #                     df_operation_data.to_csv('stock_datas\\operation_data\\operation_data%s%s.csv' % (ye, th))
    #                 except AttributeError:
    #                     print("operation_data%s%s.csv" % (ye, th) + '  and later is not Allowed')
    #                     break
    #
    #
    # def growth_data(self):
    #     for ye in range(self.startY, self.stopY):
    #         for th in [1, 2, 3, 4]:
    #             if os.path.isfile("stock_datas\\growth_data\\growth_data%s%s.csv" % (ye, th)):
    #                 print("growth_data%s%s.csv" % (ye, th) + '  is exist')
    #             else:
    #                 try:
    #                     print("growth_data%s%s.csv" % (ye, th) + '  is downloading')
    #                     time.sleep(random.random() * 2)
    #                     df_growth_data = ts.get_growth_data(ye, th)
    #                     df_growth_data.to_csv('stock_datas\\growth_data\\growth_data%s%s.csv' % (ye, th))
    #                 except AttributeError:
    #                     print("growth_data%s%s.csv" % (ye, th) + '  and later is not Allowed')
    #                     break
    #
    #
    # def debtpaying_data(self):
    #     for ye in range(self.startY, self.stopY):
    #         for th in [1, 2, 3, 4]:
    #             if os.path.isfile("stock_datas\\debtpaying_data\\debtpaying_data%s%s.csv" % (ye, th)):
    #                 print("debtpaying_data%s%s.csv" % (ye, th) + '  is exist')
    #             else:
    #                 try:
    #                     print("debtpaying_data%s%s.csv" % (ye, th) + '  is downloading')
    #                     time.sleep(random.random() * 2)
    #                     df_debtpaying_data = ts.get_debtpaying_data(ye, th)
    #                     df_debtpaying_data.to_csv('stock_datas\\debtpaying_data\\debtpaying_data%s%s.csv' % (ye, th))
    #                 except AttributeError:
    #                     print("debtpaying_data%s%s.csv" % (ye, th) + '  and later is not Allowed')
    #                     break
    # def cashflow_data(self):
    #     for ye in range(self.startY, self.stopY):
    #         for th in [1, 2, 3, 4]:
    #             if os.path.isfile("stock_datas\\cashflow_data\\cashflow_data%s%s.csv" % (ye, th)):
    #                 print("cashflow_data%s%s.csv" % (ye, th) + '  is exist')
    #             else:
    #                 try:
    #                     print("cashflow_data%s%s.csv" % (ye, th) + '  is downloading')
    #                     time.sleep(random.random() * 2)
    #                     df_cashflow_data = ts.get_cashflow_data(ye, th)
    #                     df_cashflow_data.to_csv('stock_datas\\cashflow_data\\cashflow_data%s%s.csv' % (ye, th))
    #                 except AttributeError:
    #                     print("cashflow_data%s%s.csv" % (ye, th) + '  and later is not Allowed')
    #                     break
    #
    #
