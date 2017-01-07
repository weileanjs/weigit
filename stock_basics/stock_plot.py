# coding: utf-8

import time, random
import pandas as pd
import os
import pymongo
import numpy as np
import matplotlib.pyplot as plt
client = pymongo.MongoClient('localhost',27017)
db = client['stock_basics']
dbM_p = client['month_price']
stock_basic = pd.DataFrame(list(db['basic'].find({},{'_id':0})))
k_area = stock_basic.groupby('area')['code'].agg(len)
import matplotlib.pyplot as plt
d = {"reportdate":"20160930","basiceps":'基本每股收益',"epsdiluted":'每股收益(摊薄)',"epsweighted":'每股收益(加权)',"naps":'每股净资产',
 "opercashpershare":'每股现金流',"peropecashpershare":'每股经营性现金流',"netassgrowrate":'净资产增长率(%)',"dilutedroe":'净资产收益率(摊薄)(%)',
  "weightedroe":'净资产收益率(加权)(%)',"mainbusincgrowrate":'主营业务收入增长率(%)',"netincgrowrate":'净利润增长率(%)',"totassgrowrate":'总资产增长率(%)',
  "salegrossprofitrto":'销售毛利率(%)',"mainbusiincome":'主营业务收入',"mainbusiprofit":'主营业务利润',"totprofit":'利润总额',
  "netprofit":'净利润',"totalassets":'资产总额',"totalliab":'负债总额',"totsharequi":'股东权益合计',"operrevenue":'经营活动产生的现金流量净额',
  "invnetcashflow":'投资活动产生的现金流量净额',"finnetcflow":'筹资活动产生的现金流量净额',"chgexchgchgs":'汇率变动对现金及现金等价物的影响',
  "cashnetr":'现金及现金等价物净增加额',"cashequfinbal":'期末现金及现金等价物余额','pe':'pe','fzl':'负债率'}


class Stock_show(object):
    def __init__(self,code,cs='pe',q='all',sty=2010,cpl = None,**code_kw):
        self.code = code            #stock_code
        self.cs = cs                 # default stock indicator
        self.q = q                   # period   all = 年报  one = 单季报   mid = 中报+年报
        self.sty = sty                # strat year
        self.cpl =cpl                  # double y  indicators
        self.codes = code_kw
    def to_pandas(self,c =None):
        if c == None:
            info = db[self.code].find({},{'_id':0,'name':0,'industry':0,'area':0,'timeToMarket':0})
        else:
            info = db[c].find({},{'_id':0,'name':0,'industry':0,'area':0,'timeToMarket':0})
        data_ = pd.DataFrame(list(info)).T
        k_ = data_.index.tolist()
        v_ = data_.values.tolist()
        pds_l = []
        for i in v_:
            pds_l.append(pd.Series(eval(i[0])))
        data_DF = pd.DataFrame(pds_l,index = k_).reset_index()
        # return data_DF

    # def get_price(self):
        if c == None:
            sg_priceM = dbM_p[self.code].find({},{'_id':0})
        else:
            sg_priceM = dbM_p[c].find({},{'_id':0})
        priceM_ = pd.DataFrame(list(sg_priceM)).T
        idx_ = list(priceM_.index)
        Q_idx = []
        Q_val = []
        three_ = []
        for j in idx_:
            a = 1 if int(j[-2:])%3==0 else 2
            three_.append(a)
        priceM_['3']=three_
        price3M_ = priceM_.loc[priceM_['3']==1]

        for x in price3M_.index:
            Q_idx.append('%s_%s'%(x[:4],int(x[-2:])//3))
        for y in price3M_.values:
            Q_val.append(y[0][1])
        pdP = pd.DataFrame({'price':Q_val},index = Q_idx).reset_index()
        # return pdP


    #合并basic、价格
    # def merge_datas(self):
        pdA = pd.merge( data_DF,pdP,how = 'left').rename(columns={'index': 'index_t'})
        #对年度、季度进行分列
        yeth_split = pd.DataFrame((x.split('_') for x in pdA.index_t),index=pdA.index,columns=['year','th'])
        pdA_split = pd.merge(pdA,yeth_split,right_index = True, left_index = True)
        price_ = [0]
        for p in pdA_split['price'].values:
            x =price_[-1] if isinstance(p,float) else p
            price_.append(x)
        pdA_split['price'] =price_[1:]

        # col = pdA_split.columns.tolist()
        #PE
        yeth_pe = pd.DataFrame(pdA_split['price'].astype(float)/(pdA_split['basiceps'].astype(float))*pdA_split['th'].astype(int)/4,index=pdA.index,columns=['pe'])
        pdA_pe = pd.merge(pdA_split,yeth_pe,right_index = True, left_index = True)
        # print(pdA_pe.loc[:,['index_t','basiceps','price','pe']])
        # 负债率 "totalassets":'资产总额',"totalliab":'负债总额',
        yeth_fzl = pd.DataFrame(pdA_split['totalliab'].astype(float)/(pdA_split['totalassets'].astype(float)),index=pdA.index,columns=['fzl'])
        pdA_fzl = pd.merge(pdA_pe,yeth_fzl,right_index = True, left_index = True)
        if self.q == 'one':
            pdA_ = pdA_fzl.loc[pdA_fzl['year'].astype(int) >= self.sty]
        elif self.q == 'mid':
            pdA_ = pdA_fzl.loc[(pdA_fzl['th'].astype(int) % 2 ==0) & (pdA_pe['year'].astype(int) >= self.sty)]
        else:
            pdA_ = pdA_fzl.loc[(pdA_fzl['th'].astype(int) % 4 ==0) & (pdA_pe['year'].astype(int) >= self.sty)]
        return pdA_

    def polshow(self):
        plt.rc('font', family='STXihei', size=9)
        show_data = self.to_pandas().dropna(subset=[self.cs])
        a=np.array([i for i in range(1,len(show_data['index_t'])+1)])
        code_x = show_data['index_t']
        data_y1 = show_data[self.cs]
        # data_y2 = self.merge_datas()['totsharequi']
        plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
        plt.xlabel('季度')
        plt.ylabel('pe')
        plt.title(self.code)
        #plt.ylim(2300000000)
        plt.xticks(a,code_x)
        plt.plot(a, data_y1,color='#99CC01',alpha=0.8)
        plt.show()

    def polshows(self):
        plt.rc('font', family='STXihei', size=9)
        show_datas = self.to_pandas()
        a=np.array([i for i in range(1,len(show_datas['index_t'])+1)])
        code_x = show_datas['index_t']
        data_y1 = show_datas[self.cpl[0]]
        data_y2 = show_datas[self.cpl[1]]
        fig, ax1 = plt.subplots()  # 使用subplots()创建窗口
        ax2 = ax1.twinx() # 创建第二个坐标轴
        ax1.plot(a, data_y1, linewidth = 1,label=d[self.cpl[0]])
        ax2.plot(a, data_y2, linewidth = 1,color='#99CC01',label=d[self.cpl[1]])
        ax1.set_xlabel('季度')  # fontsize使用方法和plt.xlabel()中一样
        ax1.set_ylabel(d[self.cpl[0]])
        ax2.set_ylabel(d[self.cpl[1]])
    #     ax1.set_xlim([0, max(pos_z)]) # 设置坐标轴范围的语句有所变化
    #     ax1.set_ylim(0, max(E_z))
    #     ax2.set_ylim([0, max(Enhance_z)])
        plt.title(self.code)
        plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
        # plt.legend(bbox_to_anchor=[0.2, 0.8])
        legend1=ax1.legend(loc=(.02,.92),fontsize=10) #shadow=True
        legend2=ax2.legend(loc=(.02,.86),fontsize=10)
        legend1.get_frame().set_facecolor('#FFFFFF')
        # legend2.get_frame().set_facecolor('#FFFFFF')
        plt.xticks(a,code_x)
        plt.show()


    def stocks_comp(self):
        if self.codes != 0:
            y_codes = self.codes['codes'].split(',')
            y_ccs = self.codes['ccs']              # 进行对比指标
            pdccs_first = self.to_pandas(y_codes[0])[['index_t',y_ccs]].rename(columns={y_ccs:y_codes[0]})
            for code in y_codes:
                pdccs = self.to_pandas(code)[['index_t',y_ccs]].rename(columns={y_ccs:code})
                pdccs_first = pd.merge(pdccs_first,pdccs,how = 'outer')
            pdccs_ed = pdccs_first.fillna(0).sort('index_t')
            pdccs_ed['mean_'] = pdccs_first.mean(axis=1)
            plt.rc('font', family='STXihei', size=9)
            a=np.array([i for i in range(1,len(pdccs_ed['index_t'])+1)])
            code_x = pdccs_ed['index_t']
            for co in y_codes:
                code_name = db[co].find({},{'name':1})[0]['name'][0]
                plt.plot(a, pdccs_ed[co],label = code_name, linewidth=0.9)
            plt.plot(a, pdccs_ed['mean_'],label = '均值',linestyle='-.', linewidth=2,alpha=5)
            plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
            plt.xlabel('季度')
            plt.ylabel(y_ccs)
            if 'title' in self.codes:
                plt.title(self.codes['title'])
            else:
                plt.title('%s:%s'%(y_codes,y_ccs))
            # plt.ylim(0,50)
            plt.xticks(a,code_x)
            plt.legend()
            plt.show()
        else:
            print('code_kw is None')


code_args = {'codes':'601633,000625,600104,601238','ccs':'pe',}

a = Stock_show('601633',cs='pe',q='one',sty=2005,**code_args)
# print(a.to_pandas()[['price','pe','index_t',"basiceps"]])
# a. polshow()
# # a.polshows()
a.stocks_comp()
