# coding: utf-8
import numpy as np
import os
import pandas as pd
import csv

code = '601988'
date = '2016-11-30'
def get_prick(code,date):
    s_data = pd.read_csv(r'D:\W\python\data_history\day\raw_data\%s.csv'%code,encoding='gbk').set_index('date')
    price_dict = {}
    try:
        price_dict['price'] = '%0.2f'%s_data.loc[date,'close']
        price_dict['factor'] = '%0.3f'%s_data.loc[date,'factor']
        re_price = '%0.2f'%(float(price_dict['price'])/float(price_dict['factor']))
    except KeyError:
        price_dict['price'] = 'n'
        price_dict['factor'] = 'n'
        re_price = 'n'
    return re_price
def get_sh_index(date):
    sh_df = pd.read_csv(r'D:\W\python\data_history\day\raw_data\sh.csv',encoding='gbk').set_index('date')
    try:
        sh_index = '%0.2f'%sh_df.loc[date,'close']
    except KeyError:
        sh_index = 'n'
    return sh_index

# print(get_prick(code,date))
# print(get_sh_index('2016-11-29'))

# def fq_price()
