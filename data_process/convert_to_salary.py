def convert_to_salary(salary):
    cleaned_lower = 0
    cleaned_upper = 0

    # 新增：先处理包含“薪”的情况，提取基础薪资和额外薪资月份数
    if '薪' in salary:
        salary_parts = salary.split('·')
        salary = salary_parts[0]  # 重新设置薪资范围，暂时忽略13薪等信息以进行基本处理
        if len(salary_parts) > 1:
            bonus_month = int(salary_parts[1].replace('薪', ''))  # 提取额外薪资月份数
        else:
            bonus_month = 12
    else:
        bonus_month = 12

    lower, upper = salary.split('-')

    # 处理较高值，分为两步，单位和年薪月薪区分
    if '千' in upper:
        cleaned_upper = float(upper.replace('千', '')) * 0.1*bonus_month
        cleaned_lower = float(lower)*0.1*bonus_month
    else:  # 当前分支处理不含'千'的情况，需区分'万/年'和仅'万'
        if '/年' in upper:
            cleaned_upper = float(upper.replace('/年', '').replace('万', ''))
            cleaned_lower = float(lower)
        else:  # 仅含'万'，说明是月薪，转换为年薪
            # 处理较低值
            if '千' in lower:
                cleaned_lower = float(lower.replace('千', '')) * 0.1*bonus_month
            cleaned_upper = float(upper.replace('万', ''))*bonus_month

    annual_midpoint = (cleaned_upper+cleaned_lower)/2
    return annual_midpoint

# 示例数据处理
# data_example = ['8千-1.2万', '2.5-3.5万/年', '15-25万/年', '6-8千','4.5-7千·13薪']
# uniform_salaries = [convert_to_uniform(salary) for salary in data_example]
# print(uniform_salaries)
