import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from data_process.convert_to_salary import convert_to_salary # 此函数已定义并用于统一薪资格式
from data_process.convert_to_province import get_province_by_city # 此函数已定义并用于将城市转化为省份

# 加载中国地图Shapefile
china_map_path = 'shapefile/China.shp'  # 确保该路径指向正确的Shapefile
gdf = gpd.read_file(china_map_path)

# 读取薪资数据
data = pd.read_csv('../info/51job_data.csv')

# 假设'城市'列包含的是城市名，且需要转换薪资数据为统一格式
data['salary'] = data['薪资'].apply(convert_to_salary)
data['province'] = data['城市'].apply(get_province_by_city)

# 读取shapefile和相关的工资数据
gdf['salary'] = data['salary']  # 假设'income_column'是工资数据列

# 设置图形和轴
fig, ax = plt.subplots(1)

# 根据平均工资进行填充
gdf.plot(column='salary', cmap='Blues', ax=ax, legend=True)

# 设置标题和轴标签
ax.set_title('Average Salary Map')
ax.set_axis_off()  # 关闭坐标轴显示

plt.savefig('picture/map_salary.png')