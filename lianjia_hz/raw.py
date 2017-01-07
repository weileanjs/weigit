
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


    house = pd.DataFrame({'totalprice':total_price,'houseinfo':house_datas,'followinfo':gzd})
    houseinfo_split = pd.DataFrame((x.split('|') for x in house.houseinfo),index=house.index,columns=['xiaoqu','huxing','mianji','chaoxiang','zhuangxiu','dianti'])
    xiaoqu_l = []
    for x in houseinfo_split.xiaoqu:
        a1 = x.replace("\n"," ")
        xiaoqu_l.append(a1)
    houseinfo_split['xiaoqu']=xiaoqu_l
    house=pd.merge(house,houseinfo_split,right_index=True, left_index=True)
    followinfo_split = pd.DataFrame((x.split('/') for x in house.followinfo),index=house.index,columns=['guanzhu','daikan','fabu'])
    #将分列后的关注度信息拼接回原数据表
    house=pd.merge(house,followinfo_split,right_index=True, left_index=True)
    house.groupby('huxing')['huxing'].agg(len)   #各户型数量
    chaoxiang_l = []
    for i in range(0,len(house.index)):
        x =house.chaoxiang[i] if ('东' in house.chaoxiang[i]) or ('南' in house.chaoxiang[i]) or ('西' in house.chaoxiang[i]) or ('北' in house.chaoxiang[i]) else house.zhuangxiu[i]
        chaoxiang_l.append(x)
    house['chaoxiang'] = chaoxiang_l
    mianji_l = []
    for i in range(0,len(house.index)):
        x =house.mianji[i] if '平' in house.mianji[i] else house.chaoxiang[i]
        mianji_l.append(x)
    house['mianji'] = mianji_l
    mianji_num_split = pd.DataFrame(((x.split('平')[0]).strip() for x in house.mianji),index=house.index,columns=['mianji_num'])
    house=pd.merge(house,mianji_num_split,right_index=True, left_index=True)

    # #对房源面积进行分组
    # bins = [0, 90, 150, 250, 350, 1000]
    # group_mianji = ['小于90', '90-150', '150-250', '250-350','350+']
    #
    # house['group_mianji'] = pd.cut(house['mianji_num'].astype(float), bins, labels=group_mianji)
    # #按房源面积分组对房源数量进行汇总
    # group_mianji=house.groupby('group_mianji')['group_mianji'].agg(len)
    # print(group_mianji)
    # #绘制房源面积分布图
    # plt.rc('font', family='STXihei', size=15)
    # a=np.array([1,2,3,4,5])
    # plt.barh([1,2,3,4,5],group_mianji,color='#052B6C',alpha=0.7,align='center',edgecolor='white')
    # plt.ylabel('面积分组')
    # plt.xlabel('数量')
    # plt.title('房源面积分布')
    # plt.legend(['数量'], loc='upper right')
    # plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
    # plt.yticks(a,('小于90', '90-150', '150-250', '250-350','350+'))
    # plt.show()


    #对房源关注度进行二次分列
    guanzhu_num_split = pd.DataFrame((x.split('人')[0] for x in house.guanzhu),index=house.index,columns=['guanzhu_num'])
    #将分列后的关注度数据拼接回原数据表
    house=pd.merge(house,guanzhu_num_split,right_index=True, left_index=True)
    house[['guanzhu_num','totalprice']]=house[['guanzhu_num','totalprice']].astype(float)
    bins = [0, 30, 60, 90, 150, 250, 10000]
    group_guanzhu = ['小于30', '30-60', '60-90', '90-150','150-250','250+']
    house['group_guanzhu'] = pd.cut(house['guanzhu_num'], bins, labels=group_guanzhu)
    group_guanzhu=house.groupby('group_guanzhu')['group_guanzhu'].agg(len)




    #绘制房源关注度分布图
    # plt.rc('font', family='STXihei', size=15)
    # a=np.array([1,2,3,4,5,6])
    # plt.barh([1,2,3,4,5,6],group_guanzhu,color='#052B6C',alpha=0.8,align='center',edgecolor='white')
    # plt.ylabel('关注度分组')
    # plt.xlabel('数量')
    # plt.xlim(0,300)
    # plt.title('房源关注度分布')
    # plt.legend(['数量'], loc='upper right')
    # plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
    # plt.yticks(a,('小于30', '30-60', '60-90', '90-150','150-250','250+'))
    # plt.show()







    # house_type = np.array(house[['totalprice','mianji_num','guanzhu_num']])
    # #设置质心数量为3
    # clf=KMeans(n_clusters=3)
    # #计算聚类结果
    # clf=clf.fit(house_type)
    # print(clf.cluster_centers_)
    #
    # house['label']= clf.labels_
    # print(house['label'])

def page_num(area):
    url_p_num = 'http://hz.lianjia.com/ershoufang/{}'
    response = urllib.request.urlopen(url_p_num.format(area))
    html = response.read().decode('utf-8',errors='replace')
    h_parser=BeautifulSoup(html,'lxml')
    p_num = int(h_parser.select('div.page-box.fr div ')[0].get('page-data').split(',')[0].split(':')[1])+1
    return p_num


# for i in area_l:
#     get_house_info(i)
if __name__ == '__main__':
    pool = Pool(processes=6)
    pool.map(get_house_info,area_l)
    pool.close()
    pool.join()



