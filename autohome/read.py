# coding: utf-8


import numpy as np
#导入科学计算库(拼表及各种分析汇总)
import pandas as pd
#导入绘制图表库(数据可视化)
import matplotlib.pyplot as plt
#导入结巴分词库(分词)
import jieba as jb
#导入结巴分词(关键词提取)
import jieba.analyse
import pymongo
client = pymongo.MongoClient('localhost',27017)
db = client['autohome']
chexing = 'dihaoGS'
info = db[chexing]



table_raw =pd.DataFrame(list(info.find()))
table_raw.pop('_id')
table_raw['fb_date']=pd.to_datetime(table_raw['fb_date'])
table_raw=table_raw.set_index('fb_date')
table = table_raw.drop_duplicates()
st = 10



table_month=table.resample('M',how=len)
month=table_month['fb_id']
m_index = [str(i)[2:7] for i in month.index[st:]]
month_ylab =month[st:]
# print(month,len(month))
# print(m_index,len(m_index))

xlab= [i for i in range(1,len(m_index)+1)]
plt.rc('font', family='STXihei', size=9)
a=np.array(xlab)
plt.bar(xlab,month_ylab,color='#99CC01',alpha=0.8,align='center',edgecolor='white')
plt.xlabel('月份')
plt.ylabel('发帖数量')
plt.title(chexing+'分月发帖数量变化趋势')
plt.legend(['发帖数量'], loc='upper right')
plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
plt.xticks(a,m_index,rotation=45)
plt.show()


# In[107]:

table_month2=table.resample('M',how=sum)
month=table_month2['replys']
m_index = [str(i)[2:7] for i in month.index[st:]]
month_ylab =month[st:]

xlab= [i for i in range(1,len(m_index)+1)]
plt.rc('font', family='STXihei', size=9)
a=np.array(xlab)
plt.bar(xlab,month_ylab,color='#99CC01',alpha=0.8,align='center',edgecolor='white')
plt.xlabel('月份')
plt.ylabel('回帖数量')
plt.title(chexing+'分月发回帖数变化趋势')
plt.legend(['回帖量'], loc='upper right')
plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
plt.xticks(a,m_index,rotation=45)
plt.show()


# In[108]:

table_month3=table.resample('M',how=sum)
month=table_month3['views']
m_index = [str(i)[2:7] for i in month.index[st:]]
month_ylab =month[st:]
# print(month_ylab)

xlab= [i for i in range(1,len(m_index)+1)]
plt.rc('font', family='STXihei', size=9)
a=np.array(xlab)
plt.bar(xlab,month_ylab,color='#99CC01',alpha=0.8,align='center',edgecolor='white')
plt.xlabel('月份')
plt.ylabel('浏览量')
plt.title(chexing+'分月浏览量变化趋势')
# plt.legend(['浏览量'], loc='upper right')
plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
plt.xticks(a,m_index,rotation=45)
plt.show()


# In[104]:

# content_1 = table['title']
# #文本数据格式转换
# word_str = ''.join(content_1)
# #提取文字关键词
# word_rank=jieba.analyse.extract_tags(word_str, topK=20, withWeight=True, allowPOS=())
# #转化为数据表
# word_rank = pd.DataFrame(word_rank,columns=['word','rank'])
# #查看关键词及权重
# word_rank.sort('rank',ascending=False)





