# 导入数据请求模块
import json
import requests
# 导入格式化输出模块
from pprint import pprint
# 导入csv模块
import csv

# 创建文件对象
f = open('../info/DS_product.csv',mode='w',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=[
    '职位',
    '公司',
    '薪资',
    '城市',
    '区域',
    '学历',
    '经验',
    '领域',
    '性质',
    '规模',
    '标签',
    '职位详情页',
    '公司详情页',
])
csv_writer.writeheader()

# 模拟浏览器
headers = {
'Cookie':'acw_tc=ac11000117160335549637363e02b330e7502622b09d81d50069b441afcd74; sajssdk_2015_cross_new_user=1; guid=eb511e889036b22c3772aa81bca16ee2; acw_sc__v2=664898159fe748b0d0f43657c5e7f3bd4d92aa2e; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; privacy=1716033694; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1716033695; adv=ad_logid_url%3Dhttps%253A%252F%252Ftrace.51job.com%252Ftrace.php%253Fpartner%253Dsem_pcbaidubd_19689%2526ajp%253DaHR0cHM6Ly9ta3QuNTFqb2IuY29tL3RnL3NlbS9MUF8yMDIzX0JDMS5odG1sP2Zyb209YmFpZHVhZCZwYXJ0bmVyPXNlbV9wY2JhaWR1YmRfMTk2ODk%253D%2526k%253D060815abd400e557ee73bc8d01237816%2526bd_vid%253D10510455646887921855%26%7C%26; partner=www_baidu_com; seo_refer_info_2023=%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fwww.baidu.com%5C%2Flink%3Furl%3D3vzadVCBBvIivloI45rUgATrpL68UcdDPb5QTSPnlg_%26wd%3D%26eqid%3Ded8bac61009000c00000000366489973%22%2C%22referHost%22%3A%22www.baidu.com%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1716034169; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22eb511e889036b22c3772aa81bca16ee2%22%2C%22first_id%22%3A%2218f8b920a4e937-0eb826c4cb1d498-26001d51-1327104-18f8b920a4f15ae%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmOGI5MjBhNGU5MzctMGViODI2YzRjYjFkNDk4LTI2MDAxZDUxLTEzMjcxMDQtMThmOGI5MjBhNGYxNWFlIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiZWI1MTFlODg5MDM2YjIyYzM3NzJhYTgxYmNhMTZlZTIifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22eb511e889036b22c3772aa81bca16ee2%22%7D%2C%22%24device_id%22%3A%2218f8b920a4e937-0eb826c4cb1d498-26001d51-1327104-18f8b920a4f15ae%22%7D; search=jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%BB%A5%C1%AA%CD%F8%B2%FA%C6%B7%BE%AD%C0%ED%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%B2%FA%C6%B7%BE%AD%C0%ED%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%BA%F3%B6%CB%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C7%B0%B6%CB%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CB%E3%B7%A8%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; JSESSIONID=82DF2A46FBE523363AD79735C332FEBB; ssxmod_itna=WqRxuD0D2D9DnQDBDlREI30==m2KrCCQIKDmxqGNphoDZDiqAPGhDC8b9xCRe2CD+YObPmedqQbPgr2Qeb2G0GWYf9k4GLDmKDyQGf2eDxOq0rD74irDDxD3wxneD+D04kguOqi3DhxGQD3qGySR=DA3tDbh=uDiU/DDt794G2D7UyiDDli0uP7Y4P7CU6CQ03xGtqITxP7qDMUeGXK7Fe7db86PhMIwaHaQPuKCiDtqD94m=DbfL3x0pyRT2zCYPTC74eSh4fW0DP+GD5SBhz7gxPQhxNvGGsYi/Q7Dw665xDG8GdBFxxD=; ssxmod_itna2=WqRxuD0D2D9DnQDBDlREI30==m2KrCCQIKDmxA=WqwxD/t5DF2YbhUcPApQO5gHS7BTIE1qVgBY=sMIOAEtAVQ3PhQPi507y6LCc1MFc2DyOb9cGzw3UBUYeD4=bmUf2UTtWq1dT/IsFdi8Uwop4wX9UO3Z7Rt1mq=PGLYuB2b32e6GKSIGA3N1+Ddjf8brVg3YapK=rMfQDw=Rbd37pxQCuBQkMT5Wre3niCILe9RGIx6s5/9mMfnsrq=YoaxKhn=PixG2i0PDFqD2iiD==; tfstk=fQYIOPM_EJ2B7zO1EMhN5dMz4y_5Vpg4N71JiQUUwwQLez61G6dP80x1Fdp1pTkhJTUWUQ8eUUOuP_dJEXXrtcRHtab-3x7SuBAHPp-OUA7-wCelRRRsuqRH9_XwIf0qZ5mruTXRyMILXVBGaTepeMITWOflwJC8JfOOI_QRwzC8B1CRMyeR2XLrC1mCpBMy-uE3ZbWW9OaXsF1dGkAdCzUJ5psCHrW_yzL1OCvTe1zj4tKcLiWMBVzCPCCWhs9QBA_J1eYfXeHgPK96DN1MjYZ5h3dem3Is92d1R9sX7iN7vwtJKUsHA7cD6wpMmtjKjAf68ES5nGwtpCR1pitWLA4RLnO9Ci8aQr79Mh_14O4VhF-QV5s0P16q1fZu4GtaEdr-3loNv1fwufG_dujds16q1fZuqMCG_ils1JZl.',
'From-Domain':'51job_web',
'Host':'we.51job.com',
'Referer':'https://we.51job.com/pc/search?jobArea=000000&keyword=%E4%BA%92%E8%81%94%E7%BD%91%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86&searchType=2&keywordType=',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}
for page in range(1,11):
    # 请求连接
    url = f'https://we.51job.com/api/job/search-pc?api_key=51job&timestamp=1716034181&keyword=%E4%BA%92%E8%81%94%E7%BD%91%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum={page}&requestId=&keywordType=&pageSize=20&source=1&accountId=&pageCode=sou%7Csou%7Csoulb'
    # 发送请求
    response = requests.get(url=url, headers=headers)
    # <Response [200]> 响应对象
    print(response)
    # 获取响应json数据
    # 代码请求得到的数据和开发者工具响应数据不同
    # 你可能被反爬 --> 被识别出来你是爬虫程序  < 模拟浏览器  伪装不够好>
    json_data = response.json()
    # 解析数据，字典取值+ for循环遍历
    # 字典取值：键值对取值
    # 根据冒号左边的内容，提取冒号右边的内容
    for index in json_data['resultbody']['job']['items']:
        # 处理城市信息
        area_info = index['jobAreaString'].split('·')
        if len(area_info) == 2:
            city = area_info[0]
            area = area_info[1]
        else:
            city = area_info[0]
            area = '未知'
        # index --> 字典数据类型 提取具体职位信息内容
        job_info = {
            '职位': index['jobName'],
            '公司': index['companyName'],
            '薪资': index['provideSalaryString'],
            '城市': city,
            '区域': area,
            '学历': index['degreeString'],
            '经验': index['workYearString'],
            '领域': index['industryType1Str'],
            '性质': index['companyIndustryType1Str'],
            '规模': index['companySizeString'],
            '标签': ','.join(index['jobTags']),
            '职位详情页': index['jobHref'],
            '公司详情页': index['companyHref'],
        }
        # 一行一行写入数据
        csv_writer.writerow(job_info)
        #pprint(job_info)


