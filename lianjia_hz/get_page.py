from save_read import save_house_info
import json
from multiprocessing import Pool
import datetime
from bs4 import BeautifulSoup
import urllib
import pandas as pd
import scipy
#导入图表库
import matplotlib.pyplot as plt
#导入数值计算库
import numpy as np
from sklearn.cluster import KMeans
#设置列表页URL的固定部分
import pymongo
client = pymongo.MongoClient('localhost',27017)
db = client['hz_fc']
hzfc =db['hz_fc']

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;amp;wd=&amp;amp;eqid=c3435a7d00006bd600000003582bfd1f'
}
now =datetime.datetime.now().strftime('%Y-%m-%d')[0:10]
area_l = ['xihu','jianggan','gongshu','shangcheng','xiacheng','binjiang','xiaoshan','yuhang']
base_url = 'http://hz.lianjia.com/ershoufang/'
def get_house_info(area):
    total_price =[]
    house_datas = []
    gzd = []
    p_price = []
    for i in range(1,page_num(area)):
        print(i)
        response = urllib.request.urlopen(base_url+area+'/'+str(i))
        html = response.read().decode('utf-8',errors='replace')
        h_parser=BeautifulSoup(html,'lxml')
        tot_price = h_parser.select('div.totalPrice  span')
        for p in tot_price:
            total_price.append(p.text)
        houseinfo = h_parser.select(' div.info.clear > div.address > div')
        for h in houseinfo:
            house_datas.append(h.text)
        guanzhudu = h_parser.select(' div.info.clear   div.followInfo')
        for g in guanzhudu:
            gzd.append(g.text)
        per_price = h_parser.select('div.priceInfo   div.unitPrice  span')
        for i in per_price:
            p_price.append(i.text.strip('元/平米').strip('单价'))

    house = pd.DataFrame({'totalprice':total_price,'houseinfo':house_datas,'followinfo':gzd,'danjia':p_price})
    houseinfo_split = pd.DataFrame((x.split('|') for x in house.houseinfo),index=house.index,columns=['xiaoqu','huxing','mianji','chaoxiang','zhuangxiu','dianti'])
    xiaoqu_l = []
    #去除小区 前换行符\n
    for x in houseinfo_split.xiaoqu:
        a1 = x.replace("\n"," ")
        xiaoqu_l.append(a1)
    houseinfo_split['xiaoqu']=xiaoqu_l
    house=pd.merge(house,houseinfo_split,right_index=True, left_index=True)
    followinfo_split = pd.DataFrame((x.split('/') for x in house.followinfo),index=house.index,columns=['guanzhu','daikan','fabu'])
    #将分列后的关注度信息拼接回原数据表
    house=pd.merge(house,followinfo_split,right_index=True, left_index=True)
    house.groupby('huxing')['huxing'].agg(len)   #各户型数量
    mianji_l = []
    for i in range(0,len(house.index)):
        x =house.mianji[i] if '平' in house.mianji[i] else house.chaoxiang[i]
        mianji_l.append(x)
    house['mianji'] = mianji_l
    chaoxiang_l = []
    for i in range(0,len(house.index)):
        x =house.chaoxiang[i] if ('东' in house.chaoxiang[i]) or ('南' in house.chaoxiang[i]) or ('西' in house.chaoxiang[i]) or ('北' in house.chaoxiang[i]) else house.zhuangxiu[i]
        chaoxiang_l.append(x)
    house['chaoxiang'] = chaoxiang_l

    mianji_num_split = pd.DataFrame(((x.split('平')[0]).strip() for x in house.mianji),index=house.index,columns=['mianji_num'])
    house=pd.merge(house,mianji_num_split,right_index=True, left_index=True)

    #对房源关注度进行二次分列
    guanzhu_num_split = pd.DataFrame((x.split('人')[0] for x in house.guanzhu),index=house.index,columns=['guanzhu_num'])
    #将分列后的关注度数据拼接回原数据表
    house=pd.merge(house,guanzhu_num_split,right_index=True, left_index=True)
    house[['guanzhu_num','totalprice']]=house[['guanzhu_num','totalprice']].astype(float)
    bins = [0, 30, 60, 90, 150, 250, 10000]
    group_guanzhu = ['小于30', '30-60', '60-90', '90-150','150-250','250+']
    house['group_guanzhu'] = pd.cut(house['guanzhu_num'], bins, labels=group_guanzhu)
    house['area'] = [area]*len(house.index)
    save_house_info(house)


def page_num(area):
    url_p_num = 'http://hz.lianjia.com/ershoufang/{}'
    response = urllib.request.urlopen(url_p_num.format(area))
    html = response.read().decode('utf-8',errors='replace')
    h_parser=BeautifulSoup(html,'lxml')
    p_num = int(h_parser.select('div.page-box.fr div ')[0].get('page-data').split(',')[0].split(':')[1])+1
    return p_num

if __name__ == '__main__':
    pool = Pool(processes=5)
    pool.map(get_house_info,area_l)
    pool.close()
    pool.join()



