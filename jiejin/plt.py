import numpy as np
import pandas as pd
#导入图表库以进行图表绘制
import matplotlib.pyplot as plt


#设置日期字段issue_d为loandata数据表索引字段
#loandata = loandata.set_index('issue_d')
#按月对贷款金额loan_amnt求均值，以0填充空值

loan_plot=[0,1.38,1.93,2.69,2.54,1.38,-0.29,-1.54,-3.49,-3.80]
#图表字体为华文细黑，字号为15
plt.rc('font', family='STXihei', size=15)
#创建一个一维数组赋值给a
a=np.array([1,2,3,4,5,6,7,8,9,10])
#创建折线图，数据源为按月贷款均值，标记点，标记线样式，线条宽度，标记点颜色和透明度
plt.plot(loan_plot,'g^',loan_plot,'g-',color='#99CC01',linewidth=3,markeredgewidth=3,markeredgecolor='#99CC01',alpha=0.8)
#添加x轴标签
plt.xlabel('月')
#添加y周标签
plt.ylabel('平均值')
#添加图表标题
plt.title('解禁月强于上证指数相对平均值%')
#添加图表网格线，设置网格线颜色，线形，宽度和透明度
plt.grid( color='#95a5a6',linestyle='--', linewidth=1 ,axis='y',alpha=0.4)
#设置数据分类名称
plt.xticks(a, ('前6月','前5月','前4月','前3月','前2月','前1月','解禁月','后1月','后2月','后3月') )
#输出图表
plt.show()


1.38,1.93,2.69,2.54,1.38,-0.29,-1.54,-3.49,-3.80
