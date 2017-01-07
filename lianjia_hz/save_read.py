from multiprocessing import Pool
import datetime
from bs4 import BeautifulSoup
import urllib
import pandas as pd
import pymongo
import matplotlib.pyplot as plt
import numpy as np
client = pymongo.MongoClient('localhost',27017)
db = client['hz_fc']
import charts

now =datetime.datetime.now().strftime('%Y-%m-%d')[0:10]
area_l = ['xihu','jianggan','gongshu','shangcheng','xiacheng','binjiang','xiaoshan','yuhang']
base_url = 'http://hz.lianjia.com/ershoufang/'
name = '2016-12-06_jianggan.xlsx'
def save_house_info(raw_data):
    db[now].insert_many(raw_data.to_dict('records'))

def read_house_info(area):
    data = pd.DataFrame(list(db[area].find()))
    data.pop('_id')
    xiaoqu_=data.groupby('xiaoqu')['xiaoqu'].agg(len)
    #对房源面积进行分组
    bins = [0, 90, 150, 250, 350, 1000]
    group_mianji = ['小于90', '90-150', '150-250', '250-350','350+']

    data['group_mianji'] = pd.cut(data['mianji_num'].astype(float), bins, labels=group_mianji)
    #按房源面积分组对房源数量进行汇总
    group_mianji=data.groupby('group_mianji')['group_mianji'].agg(len)
    print(group_mianji)
    #绘制房源面积分布图
    plt.rc('font', family='STXihei', size=15)
    a=np.array([1,2,3,4,5])
    plt.barh([1,2,3,4,5],group_mianji,color='#052B6C',alpha=0.7,align='center',edgecolor='white')
    plt.ylabel('面积分组')
    plt.xlabel('数量')
    plt.title('房源面积分布')
    plt.legend(['数量'], loc='upper right')
    plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
    plt.yticks(a,('小于90', '90-150', '150-250', '250-350','350+'))
    plt.show()
    return xiaoqu_


#read_house_info('2016-12-07_xiaoshan')

# if __name__ == '__main__':
#     pool = Pool(processes=8)
#     pool.map(get_house_info,area_l)
#     pool.close()
#     pool.join()



