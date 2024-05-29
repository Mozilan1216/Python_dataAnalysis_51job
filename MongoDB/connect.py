# -*- coding: utf-8 -*-
import pandas as pd
from pymongo import MongoClient

# 使用 pandas 加载 CSV 文件并将其转换为 DataFrame：
#file = '../info/51job_data.csv'
#df = pd.read_csv(file)

#连接数据库
client = MongoClient('mongodb://localhost:27017/')
db = client['local']
collection = db['python_crawl_51job']

# 获取集合中的所有文档
documents= collection.find()

# 打印所有文档
for document in documents:
    print(document['薪资'])