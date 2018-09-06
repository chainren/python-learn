d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
#- 放入key
d['Tom']=88
d['Jerry']=99

print(d['Tom'])

# 获取不存在的key
#print(d['NotExistKey'])

# 判断key是否存在
print('Jerry' in d)

print(d.get('NotExistKey'))

# 删除key
d.pop('Tom')

print(d)


