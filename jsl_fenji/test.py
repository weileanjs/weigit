#下载基础数据
import time
import pandas as pd
import pymongo
import json
import numpy as np
import time
import random
import tushare as ts
client = pymongo.MongoClient('localhost',27017)
db = client['stock_basic_datas']
stock_basics_d = db['bascis']

df = ts.get_stock_basics()
code_l=list(df.index)
df['code'] = pd.Series(code_l,index=df.index)
stock_basics_d.insert(json.loads(df.to_json(orient='records')))

# files_path=['stock_basics','report_data','profit_data','operation_data',
# 			'growth_data','debtpaying_data','cashflow_data']
# def create_files_path(f):
# 	path1 = os.path.join('stock_datas',f)
# 	if not os.path.exists(path1):
# 		os.makedirs(os.path.join( path1))
# 		#相对路径下新建多个文件夹
# for file_path in files_path:
# 	create_files_path(file_path)
#
# class getbasicdata:
#     def __init__(self,startY,stopY):
#         self.startY = startY
#         self.stopY = stopY
#     def report_data(self):
#         for ye in range(self.startY,self.stopY):
#             for th in [1,2,3,4]:
#                 if os.path.isfile("stock_datas\\report_data\\report_data%s%s.csv" %(ye,th)):
#                     print("report_data%s%s.csv" %(ye,th)+'  is exist')
#                 else:
#                     try:
#                         print("report_data%s%s.csv" %(ye,th)+'  is downloading')
#                         time.sleep(random.random()*2)
#                         df_report_data = ts.get_report_data(ye,th)
#                         df_report_data.to_csv('stock_datas\\report_data\\report_data%s%s.csv' %(ye,th))
#                     except AttributeError:
#                         print("report_data%s%s.csv" %(ye,th)+'  and later is not Allowed')
#                         break
#
#     def profit_data(self):
#         for ye in range(2007, 2016):
#             for th in [1, 2, 3, 4]:
#                 if os.path.isfile("stock_datas\\profit_data\\profit_data%s%s.csv" % (ye, th)):
#                     print("profit_data%s%s.csv" % (ye, th) + '  is exist')
#                 else:
#                     try:
#                         print("profit_data%s%s.csv" % (ye, th) + '  is downloading')
#                         time.sleep(random.random() * 2)
#                         df_profit_data = ts.get_profit_data(ye, th)
#                         df_profit_data.to_csv('stock_datas\\profit_data\\profit_data%s%s.csv' % (ye, th))
#                     except AttributeError:
#                         print("profit_data%s%s.csv" % (ye, th) + ' and later is not Allowed')
#                         break
#
#     def operation_data(self):
#         for ye in range(self.startY, self.stopY):
#             for th in [1, 2, 3, 4]:
#                 if os.path.isfile("stock_datas\\operation_data\\operation_data%s%s.csv" % (ye, th)):
#                     print("operation_data%s%s.csv" % (ye, th) + '  is exist')
#                 else:
#                     try:
#                         print("operation_data%s%s.csv" % (ye, th) + '  is downloading')
#                         time.sleep(random.random() * 2)
#                         df_operation_data = ts.get_operation_data(ye, th)
#                         df_operation_data.to_csv('stock_datas\\operation_data\\operation_data%s%s.csv' % (ye, th))
#                     except AttributeError:
#                         print("operation_data%s%s.csv" % (ye, th) + '  and later is not Allowed')
#                         break
#
#
#     def growth_data(self):
#         for ye in range(self.startY, self.stopY):
#             for th in [1, 2, 3, 4]:
#                 if os.path.isfile("stock_datas\\growth_data\\growth_data%s%s.csv" % (ye, th)):
#                     print("growth_data%s%s.csv" % (ye, th) + '  is exist')
#                 else:
#                     try:
#                         print("growth_data%s%s.csv" % (ye, th) + '  is downloading')
#                         time.sleep(random.random() * 2)
#                         df_growth_data = ts.get_growth_data(ye, th)
#                         df_growth_data.to_csv('stock_datas\\growth_data\\growth_data%s%s.csv' % (ye, th))
#                     except AttributeError:
#                         print("growth_data%s%s.csv" % (ye, th) + '  and later is not Allowed')
#                         break
#
#
#     def debtpaying_data(self):
#         for ye in range(self.startY, self.stopY):
#             for th in [1, 2, 3, 4]:
#                 if os.path.isfile("stock_datas\\debtpaying_data\\debtpaying_data%s%s.csv" % (ye, th)):
#                     print("debtpaying_data%s%s.csv" % (ye, th) + '  is exist')
#                 else:
#                     try:
#                         print("debtpaying_data%s%s.csv" % (ye, th) + '  is downloading')
#                         time.sleep(random.random() * 2)
#                         df_debtpaying_data = ts.get_debtpaying_data(ye, th)
#                         df_debtpaying_data.to_csv('stock_datas\\debtpaying_data\\debtpaying_data%s%s.csv' % (ye, th))
#                     except AttributeError:
#                         print("debtpaying_data%s%s.csv" % (ye, th) + '  and later is not Allowed')
#                         break
#     def cashflow_data(self):
#         for ye in range(self.startY, self.stopY):
#             for th in [1, 2, 3, 4]:
#                 if os.path.isfile("stock_datas\\cashflow_data\\cashflow_data%s%s.csv" % (ye, th)):
#                     print("cashflow_data%s%s.csv" % (ye, th) + '  is exist')
#                 else:
#                     try:
#                         print("cashflow_data%s%s.csv" % (ye, th) + '  is downloading')
#                         time.sleep(random.random() * 2)
#                         df_cashflow_data = ts.get_cashflow_data(ye, th)
#                         df_cashflow_data.to_csv('stock_datas\\cashflow_data\\cashflow_data%s%s.csv' % (ye, th))
#                     except AttributeError:
#                         print("cashflow_data%s%s.csv" % (ye, th) + '  and later is not Allowed')
#                         break
#
#
#     def stock_basics(self):
#         df_stock_basics = ts.get_stock_basics()
#         df_stock_basics.to_csv(r'stock_datas\stock_basics\stock_basics.csv')
#
#
#
# def to_getstockdata(a1,a2):
#     aaa=getbasicdata(a1,a2)
#     aaa.report_data()
#     aaa.profit_data()
#     aaa.operation_data()
#     aaa.growth_data()
#     aaa.debtpaying_data()
#     aaa.cashflow_data()
#     aaa.stock_basics()
#
# if __name__=="__main__":
#     to_getstockdata(2007,2017)
#
#
#
#
#
