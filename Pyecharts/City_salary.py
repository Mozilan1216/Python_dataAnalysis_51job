# -*- coding: utf-8 -*-
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
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

# 创建 Pyecharts 的柱状图
bar = (
    Bar()
    .add_xaxis(list(city_salary_avg_sorted.index))
    .add_yaxis("平均薪资（万/年）", list(city_salary_avg_sorted.values))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="各城市数据分析师平均薪资对比（从高到低）"),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),
        yaxis_opts=opts.AxisOpts(name="平均薪资（万/年）"),
    )
    .render("html/city_salary.html")
)
