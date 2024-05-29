# 导入自动化模块
# 模拟人的行为去操作浏览器 -->获取网页上面的数据内容
# selenium --> 需要下载浏览器对应的驱动，进行操作浏览器
# DrissionPage --> 不需要下载驱动
import csv

from DrissionPage import ChromiumPage
# 导入json模块
import json
from pprint import pprint
import pandas as pd

# 创建数据存储列表
job_info = []

# 读取csv里的岗位详情页信息
infos = pd.read_csv('../../info/DS_front_end.csv')
jobHerfs = infos['职位详情页']

for jobHerf in jobHerfs:
    try:
        # 打开浏览器
        driver = ChromiumPage()
        # 访问网站
        driver.get(jobHerf)

        """解析数据，可以通过元素定位的方法，获取相关的数据内容"""
        # 获取所有职位对应的div标签
        divs = driver.eles('css:bmsg job_msg inbox')
        # for循环遍历
        for div in divs:
            info = div.text.strip()
            job_info.append(info)
            break
    except Exception as e:
        print(f"访问链接{jobHerf}时出错：{e}")
    finally:
        # 确保每次循环结束后都关闭浏览器，避免资源泄露
        driver.quit()

# 创建文件对象
with open('../info/details_front.txt', 'w',encoding='utf-8') as file:
    file.write('\n'.join(job_info))
