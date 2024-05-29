import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie

# 读取文件获取内容
data = pd.read_csv('../info/51job_data.csv')
group = data.groupby('规模')
group_size = group.size()

# 自定义顺序
custom_order = ['少于50人','50-150人','150-500人','500-1000人','1000-5000人','5000-10000人','10000人以上']
group_size = group_size.reindex(custom_order)

# 将 Pandas Series 转换为列表格式
data_list = [(key, value) for key, value in zip(group_size.index, group_size.values)]

# 计算百分比
total = sum(group_size)
percent_data_list = [(key, "{:.2f}%".format(value / total * 100)) for key, value in data_list]

# 创建 Pie 图
pie = (
    Pie()
    .add(
        "",
        percent_data_list,
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

# 保存为 HTML 文件
pie.render("html/grouped_number.html")
