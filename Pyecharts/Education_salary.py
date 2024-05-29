import pandas as pd
from data_process.convert_to_salary import convert_to_salary  # 此函数已定义并用于统一薪资格式
from pyecharts.charts import Bar
from pyecharts import options as opts

# 读取文件获取内容
data = pd.read_csv('../info/51job_data.csv')
datas = data[['学历', '薪资']]

# 数据清洗和预处理
valid_educations = ['高中', '大专', '本科']
filtered_data = data[data['学历'].isin(valid_educations)]

# 将薪资转换为统一格式
filtered_data.loc[:, '薪资'] = filtered_data['薪资'].apply(convert_to_salary)

# 指定学历列为 Categorical 类型，并按指定顺序排序
filtered_data.loc[:, '学历'] = pd.Categorical(filtered_data['学历'], categories=valid_educations, ordered=True)

# 计算每个学历水平的平均工资
average_salary_by_education = filtered_data.groupby('学历', observed=True)['薪资'].mean().reset_index()

# 提取用于绘图的学历和工资数据，并按照指定顺序排序
education = average_salary_by_education['学历'].tolist()
salary = average_salary_by_education['薪资'].tolist()

# 绘图
bar = (
    Bar()
    .add_xaxis(education)
    .add_yaxis("平均工资", salary)
    .reversal_axis()
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),
        title_opts=opts.TitleOpts(title="数据分析师不同学历的平均工资"),
    )
    .render("html/education_salary.html")
)
