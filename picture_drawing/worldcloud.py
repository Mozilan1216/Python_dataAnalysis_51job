from os import path
import jieba
import collections
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator

# 读取文本文件内容
text_path = path.join('../info/job_info.txt')
with open(text_path, 'r', encoding='utf-8') as file:
    text = file.read()

# 停用词列表
stopwords = [
    '工作职责', '任职要求', '关键字', '年龄要求', '职能', '技能要求', '年龄要求', '任职资格', '工作', '内容', '性质', '描述', '负责', '类别',
    '良好', '的', '及', '和', '公司', '以上', '学历', '并', '有', '已经', '具备', '建议', '报告', '专业', '体系',
    '优先', '分析师', '团队', '需求', '已经', '与', '等', '对', '以上学历', '要求', '相关', '能', '做', '行业',
    '进行', '数据', '关键字', '工作', '较强', '或', '能力', '提出', '较', '强', '熟悉', '岗位', '熟练掌握', '能够', '快速',
    '职能', '类别','工具','不同','竞争对手','重点','基于','为','中','熟练',
]

# 使用jieba进行中文分词
words = jieba.cut(text)

# 使用jieba进行中文分词并筛去停用词
words = [word for word in jieba.cut(text) if word not in stopwords]
words = " ".join(words)

# 统计词频
#word_counts = collections.Counter(words)
# 设定频率阈值，过滤掉出现频率较低的词
#frequency_threshold = 6  # 你可以根据需要调整这个阈值
#filtered_words = {word: count for word, count in word_counts.items() if word not in stopwords and count >= frequency_threshold}
# 将过滤后的词转换为字符串，词与词之间用空格分隔
#filtered_text = " ".join(filtered_words.keys())

# 设置词云参数
wc = WordCloud(
    background_color='white',  # 背景颜色
    width=800, height=600,  # 图片尺寸
    font_path='simhei.ttf',  # 中文字体路径，确保你的环境中已安装该字体
    max_words=200,  # 显示最大词数
    max_font_size=100,  # 字体最大尺寸
    random_state=42,  # 随机种子，保持每次生成的词云图一致
)

# 生成词云
word_cloud = wc.generate(words)

# 显示词云图
plt.figure(figsize=(10, 8))
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis('off')  # 关闭坐标轴
plt.show()

# 如果你想保存生成的词云图，取消下面一行的注释并指定保存路径
word_cloud.to_file('picture/wordcloud.png')