# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

# 读取文件获取内容
data = pd.read_csv('../info/51job_data.csv')
group = data.groupby('规模')
group_size = group.size()
print(group_size)

# 自定义顺序
custom_order = ['少于50人','50-150人','150-500人','500-1000人','1000-5000人','5000-10000人','10000人以上']
group_size = group_size.reindex(custom_order)

# 绘制环形图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(10, 8))
plt.pie(group_size,labels=group_size.index,autopct='%1.1f%%')
plt.title('不同规模公司数据分析师招聘数量')
#plt.show()
plt.savefig('picture/grouped_number.png')



