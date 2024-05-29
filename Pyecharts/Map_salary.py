# -*- coding: utf-8 -*-
import pandas as pd
from pyecharts.charts import Map
from pyecharts import options as opts
from data_process.convert_to_salary import convert_to_salary # 此函数已定义并用于统一薪资格式
from data_process.convert_to_province import get_province_by_city # 此函数已定义并用于将城市转化为省份

# 读取薪资数据
data = pd.read_csv('../info/51job_data.csv')

# 假设'城市'列包含的是城市名，且需要转换薪资数据为统一格式
data['salary'] = data['薪资'].apply(convert_to_salary)
data['province'] = data['城市'].apply(get_province_by_city)

# 按省份分组计算平均工资
province_salary_avg = data.groupby('province')['salary'].mean().reset_index()

# 创建 Pyecharts 地图
map_chart = (
    Map()
    .add("平均工资", [list(z) for z in zip(province_salary_avg['province'], province_salary_avg['salary'])], "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国各省份数据分析师平均工资地图"),
        visualmap_opts=opts.VisualMapOpts(max_=max(province_salary_avg['salary'])),
    )
    .render("html/map_salary.html")
)
