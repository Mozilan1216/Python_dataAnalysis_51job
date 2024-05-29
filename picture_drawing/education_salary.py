# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from data_process.convert_to_salary import convert_to_salary  # 此函数已定义并用于统一薪资格式

# 读取文件获取内容
data = pd.read_csv('../info/51job_data.csv')
datas = data[['学历', '薪资']]

# 数据清洗和预处理
valid_educations = ['大专', '本科', '高中']
filtered_data = data[data['学历'].isin(valid_educations)]

# 将薪资转换为统一格式
filtered_data.loc[:, '薪资'] = filtered_data['薪资'].apply(convert_to_salary)

# 计算每个学历水平的平均工资
average_salary_by_education = filtered_data.groupby('学历')['薪资'].mean().reset_index()

# 提取用于绘图的学历和工资数据
education = average_salary_by_education['学历']
salary = average_salary_by_education['薪资']

# 绘图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体作为默认字体
plt.figure(figsize=(10, 6))
plt.bar(education, salary)
plt.xlabel('学历')
plt.ylabel('平均工资')
plt.title('数据分析师不同学历的平均工资')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 如果你想将图保存到文件中
plt.savefig('picture/education_salary.png')
