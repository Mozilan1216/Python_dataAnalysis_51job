import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from data_process.convert_to_salary import convert_to_salary

# 读取文件获取内容
data = pd.read_csv('../info/51job_data.csv')
cities = data['城市']
salaries = data['薪资']

# 处理薪资范围
data['salary_mid'] = [convert_to_salary(salary) for salary in salaries]

# 聚合数据，按城市分组计算薪资的平均值
city_salary_avg = data.groupby('城市')['salary_mid'].mean()
# 聚合数据，按城市分组计算薪资的平均值，并排序
city_salary_avg_sorted = city_salary_avg.sort_values(ascending=False)

# 可视化呈现
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体作为默认字体
plt.figure(figsize=(10, 6))
city_salary_avg_sorted.plot(kind='bar')
plt.title('各城市数据分析师平均薪资对比（从高到低）')
plt.xlabel('城市')
plt.ylabel('平均薪资（万/年）')
plt.xticks(rotation=90)
plt.tight_layout()  # 自动调整子图参数, 使之填充整个图像区域
#如果增加show，则图片无法正常保存
time.sleep(2)
plt.savefig('picture/city_salary.jpg')