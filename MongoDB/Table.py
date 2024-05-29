# -*- coding: utf-8 -*-
# 导入连接数据库的库
from pymongo import MongoClient
# 导入生成图表的函数
from pyecharts.charts import Table, Tab
from MongoDB.db_for_echarts import city_salary, education_salary, grouped_number, map_salary, wordcloud


# 使用Table生成可视化分类页面
if __name__ == "__main__":
    # 连接数据库
    client = MongoClient('mongodb://localhost:27017/')
    db = client['local']
    collection = db['python_crawl_51job']

    # 创建一个 Tab 实例
    tab = Tab()

    # 获取城市数据分析师平均薪资对比图
    city_salary_chart = city_salary(collection)

    # 获取数据分析师不同学历的平均工资对比图
    education_salary_chart = education_salary(collection)

    # 获取不同规模公司数据分析师招聘数量的饼图
    grouped_number_chart = grouped_number(collection)

    # 获取中国各省份数据分析师平均工资地图
    map_salary_chart = map_salary(collection)

    # 获取数据分析师岗位描述词云
    wordcloud_chart = wordcloud(collection)

    # 将各个图表加入 Tab 实例中
    tab.add(city_salary_chart, "城市薪资对比")
    tab.add(education_salary_chart, "学历工资对比")
    tab.add(grouped_number_chart, "公司规模招聘数量")
    tab.add(map_salary_chart, "各省份平均工资")
    tab.add(wordcloud_chart, "岗位描述词云")

    # 将 Tab 实例保存到一个 HTML 文件中
    tab.render("html/visualization_table.html")