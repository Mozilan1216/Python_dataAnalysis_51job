from os import path
import jieba
import jieba.analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 加载停用词列表（示例路径，请根据实际情况调整）
stopwords_path = 'stopwords.txt'  # 确保此路径指向你的停用词文件
with open(stopwords_path, 'r', encoding='utf-8') as f:
    stopwords = set([line.strip() for line in f.readlines()])

# 读取文本文件内容
text_path = path.join('../info/job_info.txt')
with open(text_path, 'r', encoding='utf-8') as file:
    text = file.read()

# 使用jieba进行中文分词并筛去停用词
words = " ".join(jieba.cut(text))
filtered_words = [word for word in words if word not in stopwords]

# 构建词频字典，可以在这里加入词频筛选逻辑
word_counts = {}
for word in filtered_words:
    word_counts[word] = word_counts.get(word, 0) + 1

# 过滤低频词，例如只保留出现次数大于5的词
filtered_word_counts = {k: v for k, v in word_counts.items() if v > 5}

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
word_cloud = wc.generate_from_frequencies(filtered_word_counts)

# 显示词云图
plt.figure(figsize=(10, 8))
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis('off')  # 关闭坐标轴
plt.show()

# 如果你想保存生成的词云图，取消下面一行的注释并指定保存路径
# word_cloud.to_file('wordcloud.png')