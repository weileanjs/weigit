from bs4 import BeautifulSoup
import requests
import pandas as pd
from test_date import get_prick,get_sh_index
from test_holiday import strtodatetime
import time




def get_price_p(code,date):

    date_take = strtodatetime(date)
    pri_6 = get_prick(code,date_take[0])
    if pri_6 != 'n':
        pri_6 = float(get_prick(code,date_take[0]))
        sh_index6 = float(get_sh_index(date_take[0]))
        try:
            fqq6_p=float('%0.2f'%((pri_6-pri_6)/pri_6*100))
            sh_index6_p = float('%0.2f'%((float(get_sh_index(date_take[0]))-sh_index6)/sh_index6*100))
            sh_index6_pp=-sh_index6_p+fqq6_p
            #print(date_take[0],sh_index6_p,fqq6_p)
        except ValueError:
            fqq6_p='n'
            sh_index6_pp='n'

        try:
            pri_5 = float(get_prick(code,date_take[1]))
            fqq5_p=float('%0.2f'%((pri_5-pri_6)/pri_6*100))
            sh_index5_p =float( '%0.2f'%((float(get_sh_index(date_take[1]))-sh_index6)/sh_index6*100))
            sh_index5_pp=-sh_index5_p+fqq5_p
            #print(date_take[1],sh_index5_p,fqq5_p)
        except ValueError:
            fqq5_p='n'
            sh_index5_pp='n'

        try:
            pri_4 = float(get_prick(code,date_take[2]))
            sh_index4_p = float('%0.2f'%((float(get_sh_index(date_take[2]))-sh_index6)/sh_index6*100))
            fqq4_p=float('%0.2f'%((pri_4-pri_6)/pri_6*100))
            sh_index4_pp=-sh_index4_p+fqq4_p
            #print(date_take[2],sh_index4_p,fqq4_p)
        except ValueError:
            fqq4_p='n'
            sh_index4_pp='n'
        try:
            pri_3 = float(get_prick(code,date_take[3]))
            sh_index3_p =float( '%0.2f'%((float(get_sh_index(date_take[3]))-sh_index6)/sh_index6*100))
            fqq3_p=float('%0.2f'%((pri_3-pri_6)/pri_6*100))
            sh_index3_pp=-sh_index3_p+fqq3_p
            #print(date_take[3],sh_index3_p,fqq3_p)
        except ValueError:
            fqq3_p='n'
            sh_index3_pp='n'
        try:
            pri_2 = float(get_prick(code,date_take[4]))
            sh_index2_p = float('%0.2f'%((float(get_sh_index(date_take[4]))-sh_index6)/sh_index6*100))
            fqq2_p =float( '%0.2f'%((pri_2-pri_6)/pri_6*100))
            sh_index2_pp=-sh_index2_p+fqq2_p
            #print(date_take[4],get_sh_index(date_take[4]),pri_2)
        except ValueError:
            fqq2_p ='n'
            sh_index2_pp='n'
        try:
            pri_1 = float(get_prick(code,date_take[5]))
            sh_index1_p =float( '%0.2f'%((float(get_sh_index(date_take[5]))-sh_index6)/sh_index6*100))
            fqq1_p=float('%0.2f'%((pri_1-pri_6)/pri_6*100))
            sh_index1_pp=-sh_index1_p+fqq1_p
            #print(date_take[5],get_sh_index(date_take[5]),pri_1)
        except ValueError:
            fqq1_p='n'
            sh_index1_pp='n'
        try:
            pri_0 = float(get_prick(code,date_take[6]))
            sh_index0_p = float('%0.2f'%((float(get_sh_index(date_take[6]))-sh_index6)/sh_index6*100))
            fqq0_p=float('%0.2f'%((pri_0-pri_6)/pri_6*100))
            sh_index0_pp=-sh_index0_p+fqq0_p
            #print(date_take[6],get_sh_index(date_take[6]),pri_0)
        except ValueError:
            fqq0_p='n'
            sh_index0_pp='n'
        try:
            pri_h1 = float(get_prick(code,date_take[7]))
            sh_indexh1_p =float( '%0.2f'%((float(get_sh_index(date_take[7]))-sh_index6)/sh_index6*100))
            fqh1_p=float('%0.2f'%((pri_h1-pri_6)/pri_6*100))
            sh_indexh1_pp=-sh_indexh1_p+fqh1_p
            #print(date_take[7],get_sh_index(date_take[7]),pri_h1)
        except ValueError:
            fqh1_p='n'
            sh_indexh1_pp='n'

        try:
            pri_h2 = float(get_prick(code,date_take[8]))
            sh_indexh2_p =float( '%0.2f'%((float(get_sh_index(date_take[8]))-sh_index6)/sh_index6*100))
            fqh2_p=float('%0.2f'%((pri_h2-pri_6)/pri_6*100))
            sh_indexh2_pp=-sh_indexh2_p+fqh2_p
            #print(date_take[8],get_sh_index(date_take[8]),pri_h2)
        except ValueError:
            fqh2_p='n'
            sh_indexh2_pp='n'

        try:
            pri_h3 = float(get_prick(code,date_take[9]))
            sh_indexh3_p =float( '%0.2f'%((float(get_sh_index(date_take[9]))-sh_index6)/sh_index6*100))
            fqh3_p=float('%0.2f'%((pri_h3-pri_6)/pri_6*100))
            sh_indexh3_pp=-sh_indexh3_p+fqh3_p
            #print(date_take[9],get_sh_index(date_take[9]),pri_h3)
        except ValueError:
            fqh3_p='n'
            sh_indexh3_pp='n'
    else:
        fqq6_p='0'
        fqq5_p='0'
        fqq4_p='0'
        fqq3_p='0'
        fqq2_p='0'
        fqq1_p='0'
        fqq0_p='0'
        fqh1_p='0'
        fqh2_p='0'
        fqh3_p='0'
        sh_index6_pp='0'
        sh_index5_pp='0'
        sh_index4_pp='0'
        sh_index3_pp='0'
        sh_index2_pp='0'
        sh_index1_pp='0'
        sh_index0_pp='0'
        sh_indexh1_pp='0'
        sh_indexh2_pp='0'
        sh_indexh3_pp='0'
    pri_l=[fqq6_p,fqq5_p,fqq4_p,fqq3_p,fqq2_p,fqq1_p,fqq0_p,fqh1_p,fqh2_p,fqh3_p,
           sh_index6_pp,sh_index5_pp,sh_index4_pp,sh_index3_pp,sh_index2_pp,sh_index1_pp,
           sh_index0_pp,sh_indexh1_pp,sh_indexh2_pp,sh_indexh3_pp,]


    return pri_l





#print(get_price_p('002208','2016-01-29'))
