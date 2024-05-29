# -*- coding: utf-8 -*-
from os import path
import jieba
import re
from collections import Counter
from pyecharts import options as opts
from pyecharts.charts import WordCloud

# 读取文本文件内容
text_path = path.join('../info/job_info.txt')
with open(text_path, 'r', encoding='utf-8',errors='ignore') as file:
    text = file.read()

# 停用词列表
stopwords = [
    '工作职责', '任职要求', '关键字', '年龄要求', '职能', '技能要求', '年龄要求', '任职资格', '工作', '内容', '性质', '描述', '负责', '类别',
    '良好', '的', '及', '和', '公司', '以上', '学历', '并', '有', '已经', '具备', '建议', '报告', '专业', '体系',
    '优先', '分析师', '团队', '需求', '已经', '与', '等', '对', '以上学历', '要求', '相关', '能', '做', '行业',
    '进行', '数据', '关键字', '工作', '较强', '或', '能力', '提出', '较', '强', '熟悉', '岗位', '熟练掌握', '能够', '快速',
    '职能', '类别','工具','不同','竞争对手','重点','基于','为','中','熟练','了解','一个','一门','白云',
]

# 使用jieba进行中文分词并筛去停用词
words = [word for word in jieba.cut(text) if word not in stopwords and re.match('[\u4e00-\u9fa5]+', word) and len(word)>1]
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
