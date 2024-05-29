# 导入数据请求模块
import json
import requests
# 导入格式化输出模块
from pprint import pprint
# 导入csv模块
import csv

# 创建文件对象
f = open('../info/51job_data_analyse.csv',mode='w',encoding='utf-8',newline='')
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
'Cookie':'acw_tc=ac11000117160335549637363e02b330e7502622b09d81d50069b441afcd74; sajssdk_2015_cross_new_user=1; guid=eb511e889036b22c3772aa81bca16ee2; acw_sc__v2=664898159fe748b0d0f43657c5e7f3bd4d92aa2e; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CA%FD%BE%DD%B7%D6%CE%F6%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; JSESSIONID=60468B680A1BDA330FBD2A64DAFF2756; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22eb511e889036b22c3772aa81bca16ee2%22%2C%22first_id%22%3A%2218f8b920a4e937-0eb826c4cb1d498-26001d51-1327104-18f8b920a4f15ae%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmOGI5MjBhNGU5MzctMGViODI2YzRjYjFkNDk4LTI2MDAxZDUxLTEzMjcxMDQtMThmOGI5MjBhNGYxNWFlIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiZWI1MTFlODg5MDM2YjIyYzM3NzJhYTgxYmNhMTZlZTIifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22eb511e889036b22c3772aa81bca16ee2%22%7D%2C%22%24device_id%22%3A%2218f8b920a4e937-0eb826c4cb1d498-26001d51-1327104-18f8b920a4f15ae%22%7D; ssxmod_itna=eqUxuDcD9DRiD=qDtDX+nRixG2mWqNkYWt7Dl=i4A5D8D6DQeGTWXNbkpkQYkbetguDKeKWCb++5El1bxGCmC48fbWDCPGnDBIxK7WixiiuDCeDIDWeDiDGR7D=xGYDj0F/C9Dm4i7DYqGRDB=UCqDf+qGW7uQDmLNDGLP6D7QDIM6=DDX=lCq=m7DKvTd5qjbDAuGgK7D9D0UdxBdeI1q9+mFkyBUg7caPN2jx5eGuDG6DOqGmBfbDCg6lWjeI7Bx3nhh3iYPqID3rt3kKWOEx7Gq1G+5AzvD2KikSyDDAWv/xeD===; ssxmod_itna2=eqUxuDcD9DRiD=qDtDX+nRixG2mWqNkYWtD6OUQD0HYx03K=XfLD6YZRjZ4mu6vHNSPw26xlnAwp6xXbzqK+H8Fpm9=KNsogBFezgc6gdRNRF9gORm5MWjHk8NuuQ8znTdnf/c8kwKOVWvTGrKNV0KQKmv=Kic3eDTTNlBeQ74Dw623DjKD+6hDD; tfstk=fGWjOVaSSq0XuFjWSIEyFaOwV291lZwEfctOxGHqXKpxWATWAnIw35fW5aQWkFzDHFH17GWV7OsiChIOSoYam7ScmdvT8yJ_LijmynvCjzJTXg3Mh4S7LJScDhYPru2Uj0mwGFY9BIdxw8LkbFKAWId-wUxMXqKtHusJrhp9DChvy0K9xfKvMXh3P3VXkiaNnj_jZzTODUMCqTtvIjjvPAHOFZOXJ98SBABWcgb-W3kQ_eCHuB8ly8kXCgK1RH_jyz9OVtXBwtUoCw_59LtlZPG6R1IVt1d7D-IWhEOCUBisMK1OoOOcGcqh2KQlteAYZzx539R6-Qg8kgSWkB11uzD9u6sRPBWrzvJRv_954kMeRT5j10OnC3TUVuGi_Q1rSalT8bPyM3xPLuZSlfAvq3TuVuGi_IKk4QE7VX01.',
'From-Domain':'51job_web',
'Host':'we.51job.com',
'Referer':'https://we.51job.com/pc/search?jobArea=000000&keyword=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&searchType=2&keywordType=',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}
for page in range(1,11):
    # 请求连接
    url = f'https://we.51job.com/api/job/search-pc?api_key=51job&timestamp=1716033562&keyword=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum={page}&requestId=&keywordType=&pageSize=20&source=1&accountId=&pageCode=sou%7Csou%7Csoulb'
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


