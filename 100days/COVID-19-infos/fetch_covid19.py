import json, requests, time

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)

# 获取疫情数据
data = json.loads(requests.get(url=url).json()['data'])

# print(data)

# with open('data.json', 'w') as f:
#     f.write(json.dumps(data))

# print(data.keys())


# 统计省份信息
num = data['areaTree'][0]['children']
print(len(num))

for item in num:
    print(item['name'], end = ' ')
else:
    print('\n')


# 解析所有确诊数据
all_data = {}
for item in num:
    # 输出省市名称
    if item['name'] not in all_data:
        all_data.update({item['name']:0})

    # 输出省市对应的数据
    for city_data in item['children']:
        all_data[item['name']]+=int(city_data['total']['confirm'])

print(all_data)
