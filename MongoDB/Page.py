# -*- coding: utf-8 -*-
# 导入连接数据库的库
from pymongo import MongoClient
# 导入生成图表的函数
from pyecharts.charts import Page
from MongoDB.db_for_echarts import city_salary, education_salary, grouped_number, map_salary, wordcloud

if __name__ == "__main__":
    # 连接数据库
    client = MongoClient('mongodb://localhost:27017/')
    db = client['local']
    collection = db['python_crawl_51job']

    # 对薪资字段进行清洗并更新回数据库
    #clean_salary_field(collection)

    # 创建一个 Page 实例
    page = (
        Page(layout=Page.DraggablePageLayout)
    )

    # 获取城市数据分析师平均薪资对比图
    city_salary_chart = city_salary(collection)
    page.add(city_salary_chart)

    # 获取数据分析师不同学历的平均工资对比图
    education_salary_chart = education_salary(collection)
    page.add(education_salary_chart)

    # 获取不同规模公司数据分析师招聘数量的饼图
    grouped_number_chart = grouped_number(collection)
    page.add(grouped_number_chart)

    # 获取中国各省份数据分析师平均工资地图
    map_salary_chart = map_salary(collection)
    page.add(map_salary_chart)

    # 获取数据分析师岗位描述词云
    wordcloud_chart = wordcloud(collection)
    page.add(wordcloud_chart)

    # 将所有图表保存到一个 HTML 文件中
    #page.render("html/visualization_dashboard.html")

    page.save_resize_html('html/visualization_dashboard.html', cfg_file='js/chart_config.json', dest='html/可视化大屏.html')
