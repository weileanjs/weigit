# coding: utf-8
import numpy as np
import os
import pandas as pd

raw_data1 = pd.read_excel(r'D:\GP\jiejin1016read2.xlsx',encoding='gbk')
raw_data = raw_data1.loc[ (raw_data1["解禁日期"] <= '2016-12-01')&(raw_data1["解禁日期"] >= '2014-01-01')]


#xdh_3:["相对后3_%"] 存在值
xdh_3 = raw_data.loc[(raw_data["相对后3_%"] !='0')& (raw_data["相对后3_%"] !='n')]
xdh_3_d = xdh_3.loc[xdh_3["相对后3_%"] > 0]
xdh_3_x = xdh_3.loc[xdh_3["相对后3_%"] < 0]
xdh_3_d_p = len(xdh_3_d)/len(xdh_3)*100
xdh_3_av = xdh_3["相对后3_%"].mean()



xdh_2 = raw_data.loc[(raw_data["相对后2_%"] !='0')& (raw_data["相对后2_%"] !='n')]
xdh_2_d = xdh_2.loc[xdh_2["相对后2_%"] > 0]
xdh_2_x = xdh_2.loc[xdh_2["相对后2_%"] < 0]
xdh_2_d_p = len(xdh_2_d)/len(xdh_2)*100
xdh_2_av = xdh_2["相对后2_%"].mean()

xdh_1 = raw_data.loc[(raw_data["相对后1_%"] !='0')& (raw_data["相对后1_%"] !='n')]
xdh_1_d = xdh_1.loc[xdh_1["相对后1_%"] > 0]
xdh_1_x = xdh_1.loc[xdh_1["相对后1_%"] < 0]
xdh_1_d_p = len(xdh_1_d)/len(xdh_1)*100
xdh_1_av = xdh_1["相对后1_%"].mean()

xd = raw_data.loc[(raw_data["相对解禁_%"] !='0')& (raw_data["相对解禁_%"] !='n')]
xd_d = xd.loc[xd["相对解禁_%"] >= 0]
xd_x = xd.loc[xd["相对解禁_%"] < 0]
xd_p = len(xd_d)/len(xd)*100
xd_av = xd["相对解禁_%"].mean()

xdq_1 = raw_data.loc[(raw_data["相对前1_%"] !='0')& (raw_data["相对前1_%"] !='n')]
xdq_1_d = xdq_1.loc[xdq_1["相对前1_%"] > 0]
xdq_1_x = xdq_1.loc[xdq_1["相对前1_%"] < 0]
xdq_1_d_p = len(xdq_1_d)/len(xdq_1)*100
xdq_1_av = xdq_1["相对前1_%"].mean()


xdq_2 = raw_data.loc[(raw_data["相对前2_%"] !='0')& (raw_data["相对前2_%"] !='n')]
xdq_2_d = xdq_2.loc[xdq_2["相对前2_%"] > 0]
xdq_2_x = xdq_2.loc[xdq_2["相对前2_%"] < 0]
xdq_2_d_p = len(xdq_2_d)/len(xdq_2)*100
xdq_2_av = xdq_2["相对前2_%"].mean()

xdq_3 = raw_data.loc[(raw_data["相对前3_%"] !='0')& (raw_data["相对前3_%"] !='n')]
xdq_3_d = xdq_3.loc[xdq_3["相对前3_%"] > 0]
xdq_3_x = xdq_3.loc[xdq_3["相对前3_%"] < 0]
xdq_3_d_p = len(xdq_3_d)/len(xdq_3)*100
xdq_3_av = xdq_3["相对前3_%"].mean()

xdq_4 = raw_data.loc[(raw_data["相对前4_%"] !='0')& (raw_data["相对前4_%"] !='n')]
xdq_4_d = xdq_4.loc[xdq_4["相对前4_%"] > 0]
xdq_4_x = xdq_4.loc[xdq_4["相对前4_%"] < 0]
xdq_4_d_p = len(xdq_4_d)/len(xdq_4)*100
xdq_4_av = xdq_4["相对前4_%"].mean()

xdq_5 = raw_data.loc[(raw_data["相对前5_%"] !='0')& (raw_data["相对前5_%"] !='n')]
xdq_5_d = xdq_5.loc[xdq_5["相对前5_%"] > 0]
xdq_5_x = xdq_5.loc[xdq_5["相对前5_%"] < 0]
xdq_5_d_p = len(xdq_5_d)/len(xdq_5)*100
xdq_5_av = xdq_5["相对前5_%"].mean()

xdq_6 = raw_data

#print(len(xdh_3),len(xdh_3_d),len(xdh_3_x))


print('以解禁日第前6个月价格为基准：')
print('第前5月有效样本数：',len(xdq_5 ),'强于大盘数量%：','%0.2f'%xdq_5_d_p,'强于上证指数平均值：','%0.2f'%xdq_5_av)
print('第前4月有效样本数：',len(xdq_4 ),'强于大盘数量%：','%0.2f'%xdq_4_d_p,'强于上证指数平均值：','%0.2f'%xdq_4_av)
print('第前3月有效样本数：',len(xdq_3 ),'强于大盘数量%：','%0.2f'%xdq_3_d_p,'强于上证指数平均值：','%0.2f'%xdq_3_av)
print('第前2月有效样本数：',len(xdq_2 ),'强于大盘数量%：','%0.2f'%xdq_2_d_p,'强于上证指数平均值：','%0.2f'%xdq_2_av)
print('第前1月有效样本数：',len(xdq_1 ),'强于大盘数量%：','%0.2f'%xdq_1_d_p,'强于上证指数平均值：','%0.2f'%xdq_1_av)
print('第0月有效样本数：',len(xd ),'强于大盘数量%：','%0.2f'%xd_p,'强于上证指数平均值：','%0.2f'%xd_av)
print('第后1月有效样本数：',len(xdh_1 ),'强于大盘数量%：','%0.2f'%xdh_1_d_p,'强于上证指数平均值：','%0.2f'%xdh_1_av)
print('第后2月有效样本数：',len(xdh_2 ),'强于大盘数量%：','%0.2f'%xdh_2_d_p,'强于上证指数平均值：','%0.2f'%xdh_2_av)
print('第后3月有效样本数：',len(xdh_3 ),'强于大盘数量%：','%0.2f'%xdh_3_d_p,'强于上证指数平均值：','%0.2f'%xdh_3_av)




#nnnn.sort(["相对后3_%"],ascending=False)
#print(len(xdh_3),len(xdh_2),len(xdh_2),len(xd),len(xdq_1),len(xdq_2),len(xdq_3),len(xdq_4),len(xdq_5),len(xdq_6))
# print(xdh_3_d_p,xdh_2_d_p,xdh_1_d_p,xd_p,xdq_1_d_p,xdq_2_d_p,xdq_3_d_p,xdq_4_d_p,xdq_5_d_p)
# print(xdh_3_av,xdh_2_av,xdh_1_av,xd_av,xdq_1_av,xdq_2_av,xdq_3_av,xdq_4_av,xdq_5_av)

#print(xdh_3_d_p,xdh_2_d_p)
