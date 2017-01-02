# coding: utf-8
import numpy as np
import os
import pandas as pd
from jiejin2 import get_price_p
import csv
from multiprocessing import Pool
def read_xlsx():
    fqq6_p=[]
    fqq5_p=[]
    fqq4_p=[]
    fqq3_p=[]
    fqq2_p=[]
    fqq1_p=[]
    fqq0_p=[]
    fqh1_p=[]
    fqh2_p=[]
    fqh3_p=[]
    sh_index6_p = []
    sh_index5_p = []
    sh_index4_p = []
    sh_index3_p = []
    sh_index2_p = []
    sh_index1_p = []
    sh_index0_p = []
    sh_indexh1_p = []
    sh_indexh2_p = []
    sh_indexh3_p = []
    s_data = pd.read_excel(r'D:\GP\jiejin1016.xlsx',encoding='gbk')
    for i in range(0,len(s_data.index)):
        code_t ='%06d'% int(s_data.loc[i,'code'])
        date_t = s_data.loc[i,'解禁日期']
        print(code_t,date_t)
        pri_p=get_price_p(code_t,date_t)
        fqq6_p.append(pri_p[0])
        fqq5_p.append(pri_p[1])
        fqq4_p.append(pri_p[2])
        fqq3_p.append(pri_p[3])
        fqq2_p.append(pri_p[4])
        fqq1_p.append(pri_p[5])
        fqq0_p.append(pri_p[6])
        fqh1_p.append(pri_p[7])
        fqh2_p.append(pri_p[8])
        fqh3_p.append(pri_p[9])
        sh_index6_p.append(pri_p[10])
        sh_index5_p.append(pri_p[11])
        sh_index4_p.append(pri_p[12])
        sh_index3_p.append(pri_p[13])
        sh_index2_p.append(pri_p[14])
        sh_index1_p.append(pri_p[15])
        sh_index0_p.append(pri_p[16])
        sh_indexh1_p.append(pri_p[17])
        sh_indexh2_p.append(pri_p[18])
        sh_indexh3_p.append(pri_p[19])
    s_data['前6_%']=fqq6_p
    s_data['前5_%']=fqq5_p
    s_data['前4_%']=fqq4_p
    s_data['前3_%']=fqq3_p
    s_data['前2_%']=fqq2_p
    s_data['前1_%']=fqq1_p
    s_data['解禁_%']=fqq0_p
    s_data['后1_%']=fqh1_p
    s_data['后2_%']=fqh2_p
    s_data['后3_%']=fqh3_p
    s_data['相对前6_%']=sh_index6_p
    s_data['相对前5_%']=sh_index5_p
    s_data['相对前4_%']=sh_index4_p
    s_data['相对前3_%']=sh_index3_p
    s_data['相对前2_%']=sh_index2_p
    s_data['相对前1_%']=sh_index1_p
    s_data['相对解禁_%']=sh_index0_p
    s_data['相对后1_%']=sh_indexh1_p
    s_data['相对后2_%']=sh_indexh2_p
    s_data['相对后3_%']=sh_indexh3_p
    s_data.to_excel(r'D:\GP\jiejin1016read2.xlsx', index=False)
    return s_data



read_xlsx()



#print(get_price_p('002330','2016-01-13'))
