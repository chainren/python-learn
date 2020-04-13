import matplotlib.pyplot as plt

import numpy as numpy

import fetch_covid19

# 正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False


#获取数据
names = fetch_covid19.all_data.keys()

nums = fetch_covid19.all_data.values()


# 绘图
plt.figure(figsize=[11,7])
plt.bar(names, nums, width=0.8, color='purple')

#设置标题
plt.xlabel('地区', fontproperties='SimHei', size = 15)
plt.ylabel('人数', fontproperties='SimHei', rotation=90, size=12)
plt.title('全国疫情确诊图', fontproperties='SimHei', size=16)
plt.xticks(list(names), fontproperties = 'SimHei', rotation=-60,size=10)

# 显示数字
for a, b in zip(list(names), list(nums)):
    plt.text(a, b, b, ha='center', va = 'bottom', size = 6)

#图形展示
plt.show()