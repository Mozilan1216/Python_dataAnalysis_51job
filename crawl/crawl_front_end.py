# 导入数据请求模块
import json
import requests
# 导入格式化输出模块
from pprint import pprint
# 导入csv模块
import csv

# 创建文件对象
f = open('../info/DS_front_end.csv',mode='w',encoding='utf-8',newline='')
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
'Cookie':'acw_tc=ac11000117160335549637363e02b330e7502622b09d81d50069b441afcd74; sajssdk_2015_cross_new_user=1; guid=eb511e889036b22c3772aa81bca16ee2; acw_sc__v2=664898159fe748b0d0f43657c5e7f3bd4d92aa2e; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; privacy=1716033694; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1716033695; search=jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C7%B0%B6%CB%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CB%E3%B7%A8%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CA%FD%BE%DD%B7%D6%CE%F6%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; adv=ad_logid_url%3Dhttps%253A%252F%252Ftrace.51job.com%252Ftrace.php%253Fpartner%253Dsem_pcbaidubd_19689%2526ajp%253DaHR0cHM6Ly9ta3QuNTFqb2IuY29tL3RnL3NlbS9MUF8yMDIzX0JDMS5odG1sP2Zyb209YmFpZHVhZCZwYXJ0bmVyPXNlbV9wY2JhaWR1YmRfMTk2ODk%253D%2526k%253D060815abd400e557ee73bc8d01237816%2526bd_vid%253D10510455646887921855%26%7C%26; partner=www_baidu_com; seo_refer_info_2023=%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fwww.baidu.com%5C%2Flink%3Furl%3D3vzadVCBBvIivloI45rUgATrpL68UcdDPb5QTSPnlg_%26wd%3D%26eqid%3Ded8bac61009000c00000000366489973%22%2C%22referHost%22%3A%22www.baidu.com%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1716033910; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22eb511e889036b22c3772aa81bca16ee2%22%2C%22first_id%22%3A%2218f8b920a4e937-0eb826c4cb1d498-26001d51-1327104-18f8b920a4f15ae%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmOGI5MjBhNGU5MzctMGViODI2YzRjYjFkNDk4LTI2MDAxZDUxLTEzMjcxMDQtMThmOGI5MjBhNGYxNWFlIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiZWI1MTFlODg5MDM2YjIyYzM3NzJhYTgxYmNhMTZlZTIifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22eb511e889036b22c3772aa81bca16ee2%22%7D%2C%22%24device_id%22%3A%2218f8b920a4e937-0eb826c4cb1d498-26001d51-1327104-18f8b920a4f15ae%22%7D; JSESSIONID=A3FFCCBCDBC887A3965640F0D65C0866; ssxmod_itna2=QqRhqGxx8iD50=DXFG7ma7P7q8WBKfKmKDf2eA6WYT4D/DmhYK7PuX85mfBHGFfWqr=sVjrnxih4aKjKTwYL67gi1FTIPdrhaNzcEi6NoUxBnzXYbQFPnhhyU3M+kGjK3n7Iz=zXQclnD/oAiZ=Ph9DFaqYA=Y8YaXBBNtbB4b9HIF4cdC8TaiYAwZO4EciBEVj2mw/uE+37IR4M=XBGG2+LG6bYxSzd0VQ3hgRSmainNg9y0wFc0aBPXxrWa5LlmOTZLTX6hWu=BxozBUzz68LzkXnfcT/tnUdBlCIkaC98wZtOpn/EO=EPx0PgAfYekapPPf4cEP+3Y/i5b6Pr6e90p1roh0Yb2mgrQ+PKSor95r32K+RD=rbb5tRbkAYNf2xfENbAaFuu72+eukaT46jbZuWI3FFfWDG2GDs0w9GiI0rI8fozfi+rTX2D8cn9GqD08DiQeBv4jKTjDyB5qjIeGwcAjT4yQWxxD===; ssxmod_itna=YqGO0KYKY5Dv1DfxBPGInQxUo1YGO/G8nWRRDBdh4iNDnD8x7YDvIGL8YI3mYYrPxWIYstGf2h3xcjDchPrir73XoDU4i8DCMuGQ5IDYY8Dt4DTD34DYDirQGIDieDFF5H/8DbxYQDmxiODl9F6xDa0xi3LaKDR25D0gbFDQKDugKxDG5x1bi5=m0+RpawDboDnZhCom08D7vpDlaeRb08itk6e7vCL98+AWIG440OD0KGLxibkroDUBKzoRubqW2eMQiqTYa4sm0qaD+blj+boGivTjGxdlzovjqKeYD===; tfstk=fkgtOVYdupvMgGKm5ftn3K-WTudnMVhZjAl5o-2GcvHKNYEfflimHoeK3Rqg5r2xpjMJ_SvZo1oEEb_iShzckPz4lLvkrUci_rzjvV2PbRlITS9r6wmK_fzVT-Zj8HlNDV-t9VajhyaQw5UbGrwX9yNYwr__cNsCdJPbl-MbCM6Qw76fcrwbOXER6-f_HZ3hrpvkIMeOlZgBule-1ibfl2FTXbG_pXcnJ5ETFkD-fVusKjgi7k-Pqrln2xnjdeQtHfiShR0BFZem4ShbwzTPwJgtM2EZxOs_wPeTVVZCZwcQcD3LSV9V4XcLCuUnxHJgmPHt48r6Ypkx9RDjWk69K-motVZKFpbK3onsBWa54xuoya11E8FcfBdd0ir_t5gr3RunXTU098AhxiS4xWPLEBdd0ir_TWektejV0kVF.',
'From-Domain':'51job_web',
'Host':'we.51job.com',
'Referer':'https://we.51job.com/pc/search?jobArea=000000&keyword=%E5%89%8D%E7%AB%AF%E5%B7%A5%E7%A8%8B%E5%B8%88&searchType=2&keywordType=',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}
for page in range(1,11):
    # 请求连接
    url = f'https://we.51job.com/api/job/search-pc?api_key=51job&timestamp=1716033929&keyword=%E5%89%8D%E7%AB%AF%E5%B7%A5%E7%A8%8B%E5%B8%88&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum={page}&requestId=&keywordType=&pageSize=20&source=1&accountId=&pageCode=sou%7Csou%7Csoulb'
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


