# -*- coding: utf-8 -*-
# 导入连接数据库的库
from pymongo import MongoClient
# 导入数据可视化的库
import pandas as pd
from pyecharts.charts import Bar, Pie, Map, WordCloud, Grid, Page
from pyecharts import options as opts
from os import path
import jieba
import re
from collections import Counter
from data_process.convert_to_salary import convert_to_salary  # 此函数已定义并用于统一薪资格式
from data_process.convert_to_province import get_province_by_city  # 此函数已定义并用于将城市转化为省份

def clean_salary_field(collection):
    """
    对薪资字段进行清洗并更新回数据库
    Args:
        collection: MongoDB集合对象
    """
    for doc in collection.find():
        # 获取薪资字段的值
        salary_str = doc.get('薪资')
        if salary_str:  # 确保薪资字段不为空
            # 清洗薪资数据
            cleaned_salary = convert_to_salary(salary_str)
            # 更新数据库中的薪资字段值
            collection.update_one({'_id': doc['_id']}, {'$set': {'薪资': cleaned_salary}})

""" 通过pyecharts绘制图像并组装在一个页面中 """
# 各城市数据分析师平均薪资对比（从高到低）
def city_salary(collection):
    # 从MongoDB中获取数据
    documents = collection.find()

    # 将获取的数据转换为DataFrame
    data = pd.DataFrame(documents)

    # 聚合数据，按城市分组计算薪资的平均值
    city_salary_avg = data.groupby('城市')['薪资'].mean()

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
    )
    return bar

# 数据分析师不同学历的平均工资
def education_salary(collection):
    # 从MongoDB中获取数据
    documents = collection.find()

    # 将获取的数据转换为DataFrame
    data = pd.DataFrame(documents)

    # 数据清洗和预处理
    valid_educations = ['高中', '大专', '本科']
    filtered_data = data[data['学历'].isin(valid_educations)]

    # 计算每个学历水平的平均工资
    average_salary_by_education = filtered_data.groupby('学历')['薪资'].mean().reset_index()

    # 排序学历水平，确保正确的顺序
    average_salary_by_education['学历'] = pd.Categorical(average_salary_by_education['学历'], categories=valid_educations, ordered=True)
    average_salary_by_education = average_salary_by_education.sort_values('学历')

    # 提取用于绘图的学历和工资数据，并按照指定顺序排序
    education = average_salary_by_education['学历'].tolist()
    salary = average_salary_by_education['薪资'].tolist()

    # 绘图
    bar = (
        Bar()
        .add_xaxis(education)
        .add_yaxis("平均工资", salary, category_gap="50%")  # 调整柱状图之间的间隔
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))  # 调整标签位置
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),
            title_opts=opts.TitleOpts(title="数据分析师不同学历的平均工资"),
        )
    )
    return bar

# 不同规模公司数据分析师招聘数量
def grouped_number(collection):
    # 从MongoDB中获取数据
    documents = collection.find()

    # 将获取的数据转换为DataFrame
    df = pd.DataFrame(documents)

    # 根据公司规模分组并统计数量
    group_size = df.groupby('规模').size()

    # 自定义顺序
    custom_order = ['少于50人', '50-150人', '150-500人', '500-1000人', '1000-5000人', '5000-10000人', '10000人以上']
    group_size = group_size.reindex(custom_order)

    # 将 Pandas Series 转换为列表格式
    data_list = [(key, value) for key, value in zip(group_size.index, group_size.values)]

    # 创建 Pie 图
    pie = (
        Pie()
        .add(
            "",
            data_list,
            radius=["40%", "75%"],
            label_opts=opts.LabelOpts(formatter="{b}: {c}"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="不同规模公司数据分析师招聘数量"),
            legend_opts=opts.LegendOpts(
                type_="scroll", pos_left="80%", orient="vertical"
            ),
        )
    )
    return pie

# 中国各省份数据分析师平均工资地图
def map_salary(collection):
    documents = collection.find()
    data = pd.DataFrame(documents)

    # 假设'城市'列包含的是城市名，且需要转换薪资数据为统一格式
    data['salary'] = data['薪资']
    data['province'] = data['城市'].apply(get_province_by_city)

    # 按省份分组计算平均工资
    province_salary_avg = data.groupby('province')['salary'].mean().reset_index()

    # 创建 Pyecharts 地图
    map_chart = (
        Map()
        .add("平均工资", [list(z) for z in zip(province_salary_avg['province'], province_salary_avg['salary'])],
             "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="中国各省份数据分析师平均工资地图"),
            visualmap_opts=opts.VisualMapOpts(max_=max(province_salary_avg['salary'])),
        )
    )
    return map_chart

# 数据分析师岗位描述词云
def wordcloud(collection):
    documents = collection.find()
    data = pd.DataFrame(documents)

    # 读取文本文件内容
    text_path = path.join('../info/job_info.txt')
    with open(text_path, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()

    # 停用词列表
    stopwords = [
        '工作职责', '任职要求', '关键字', '年龄要求', '职能', '技能要求', '年龄要求', '任职资格', '工作', '内容',
        '性质', '描述', '负责', '类别',
        '良好', '的', '及', '和', '公司', '以上', '学历', '并', '有', '已经', '具备', '建议', '报告', '专业', '体系',
        '优先', '分析师', '团队', '需求', '已经', '与', '等', '对', '以上学历', '要求', '相关', '能', '做', '行业',
        '进行', '数据', '关键字', '工作', '较强', '或', '能力', '提出', '较', '强', '熟悉', '岗位', '熟练掌握', '能够',
        '快速',
        '职能', '类别', '工具', '不同', '竞争对手', '重点', '基于', '为', '中', '熟练', '了解', '一个', '一门', '白云',
    ]

    # 使用jieba进行中文分词并筛去停用词
    words = [word for word in jieba.cut(text) if
             word not in stopwords and re.match('[\u4e00-\u9fa5]+', word) and len(word) > 1]
    word_counts = Counter(words)

    # 转换为Pyecharts所需的格式
    wordcloud_data = [(word, count) for word, count in word_counts.items()]

    # 绘制词云图
    wordcloud = (
        WordCloud()
        .add(series_name="词频", data_pair=wordcloud_data, word_size_range=[20, 100])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="数据分析师岗位描述词云"),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    return wordcloud

# 示例用法
