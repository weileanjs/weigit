# coding: utf-8
'''run'''
import time, random
import pandas as pd
import os
import pymongo

client = pymongo.MongoClient('localhost',27017)
db = client['stock_basics']




#path1 csv 路径
path1 = 'D:\W\python\stockFdate2\stock_datas'
#业绩报告
report_data_path = os.path.join( path1,'report_data')
df_combine_basics = pd.read_csv(os.path.join( path1,'stock_basics\stock_basics.csv'),encoding='gbk').loc[:,['code','name','industry','area','timeToMarket']]

print(df_combine_basics.head()['code'])

'''
# 获取报表季度解析式
def get_year_season():
    y_s = []
    for ye in range(2000,2017):
        for th in [1,2,3,4]:
            y_s.append([ye,th])
    return y_s

# series 转 json 格式
def series_to_json(s):
    dict_s_j = {}
    s_k = s.index.tolist()
    s_v = s.values.tolist()
    for k ,v in zip(s_k ,s_v):
        dict_s_j[k] = str(v)
    return str(dict_s_j)

# 季度报表导入pymongo
def stock_detail_data(all_,code,th):
    s = all_.loc[int(code)]
    ret = series_to_json(s)
    #print(ret)
    db[code].update({},{"$set":{th:str(ret)}})

# 储存已导入mongodb的季度
def ready_th(th):
    db['readyth'].insert_one({'r_t':'%s_%s'%(th[0],th[1])})

# 保存已导入mongodb的季度
def csv_not_exist(th):
    db['not_exist'].insert_one({'not_exist':'%s_%s'%(th[0],th[1])})
# 删除之前未保存csv的季度
def csv_exist(th):
    db['not_exist'].delete_one({'not_exist':'%s_%s'%(th[0],th[1])})
    #print(th,'delete')



# 读取已经导入mongodb的季度
def saved_th():
    ready_l = pd.DataFrame(list(db['readyth'].find({},{'r_t':1,'_id':0}))).values
    ready_ll =[x[0] for x in ready_l]
    return ready_ll

def csv_to_mongo(i):
    print(readyth_,'is saving')
    df_report_data = pd.read_csv(os.path.join(report_data_path,'report_data%s%s.csv')%(i[0],i[1]),encoding='gbk').drop(['Unnamed: 0','name'],axis = 1).drop_duplicates()
    #print(df_report_data.head())
    df_profit_data = pd.read_csv(os.path.join(path1,'profit_data\profit_data%s%s.csv')%(i[0],i[1]),encoding='gbk').drop(['Unnamed: 0','name','roe','eps','net_profits'],axis = 1).drop_duplicates()
    df_operation_data = pd.read_csv(os.path.join(path1,'operation_data\operation_data%s%s.csv')%(i[0],i[1]),encoding='gbk').drop(['Unnamed: 0','name'],axis = 1).drop_duplicates()
    df_growth_data = pd.read_csv(os.path.join(path1,'growth_data\growth_data%s%s.csv')%(i[0],i[1]),encoding='gbk').drop(['Unnamed: 0','name'],axis = 1).drop_duplicates()
    df_debtpaying_data = pd.read_csv(os.path.join(path1,'debtpaying_data\debtpaying_data%s%s.csv')%(i[0],i[1]),encoding='gbk').drop(['Unnamed: 0','name'],axis = 1).drop_duplicates()
    df_cashflow_data = pd.read_csv(os.path.join(path1,'cashflow_data\cashflow_data%s%s.csv')%(i[0],i[1]),encoding='gbk').drop(['Unnamed: 0','name'],axis = 1).drop_duplicates()
    df_combine1 = pd.merge(df_combine_basics,df_report_data,on='code',how='outer').drop_duplicates()
    df_combine2 = pd.merge(df_combine1,df_profit_data,on='code',how='outer').drop_duplicates()
    df_combine3 = pd.merge(df_combine2,df_operation_data,on='code',how='outer').drop_duplicates()
    df_combine4 = pd.merge(df_combine3,df_growth_data,on='code',how='outer').drop_duplicates()
    df_combine5 = pd.merge(df_combine4,df_debtpaying_data,on='code',how='outer').drop_duplicates()
    df_combine6 = pd.merge(df_combine5,df_cashflow_data,on='code',how='outer').set_index('code',drop=True).drop_duplicates()
    df6_index = df_combine6.index.tolist()
    for co in df6_index:
        code = '%06d'%co
        stock_detail_data(df_combine6,code,'%s_%s'%(i[0],i[1]))
        csv_exist(i)
    ready_th(i)
    print(i,'is ok ~~~~~~~~~~~')





for i in get_year_season():
    readyth_= '%s_%s'%(i[0],i[1])
    if readyth_ in saved_th():
        print(readyth_,'has saved')
    else:
        try:
            csv_to_mongo(i)
        except FileNotFoundError as e:
            csv_not_exist(i)
            print(e)
            print(i,'does not exist')




#ready_th([2008,3])



# for x in ready_l:
#     print(x)

    # if os.path.isfile(r'stock_datas\combine\stock_cb%s%s.csv'%(ye,th)):
    #     print("stock_cb%s%s.csv" %(ye,th)+'  is exist')
    # else:
    #     df_combine6.to_csv(r'stock_datas\combine\stock_cb%s%s.csv'%(ye,th),encoding='gbk')
    # except OSError:
    #     print("stock_cb%s%s.csv" %(ye,th)+'  is not found')
    #     pass
'''
