# 导入自动化模块
# 模拟人的行为去操作浏览器 -->获取网页上面的数据内容
# selenium --> 需要下载浏览器对应的驱动，进行操作浏览器
# DrissionPage --> 不需要下载驱动
from DrissionPage import ChromiumPage
# 导入json模块
import json
from pprint import pprint
# 打开浏览器
driver = ChromiumPage()
# 访问网站
driver.get('https://we.51job.com/pc/search?keyword=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88')

"""解析数据，可以通过元素定位的方法，获取相关的数据内容"""
# 获取所有职位对应的div标签
divs = driver.eles('css:joblist-item')
# for循环遍历
for div in divs:
    info = div.ele('css:div:nth-child(2)').attr('sensorsdata')
    json_data = json.loads(info)
    pprint(json_data)
    break