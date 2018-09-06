# set 集合
s1 = set([1,2,3])
print(s1)
# 添加元素
s1.add('home')
print(s1)
# 移除元素
s1.remove(1)
#s1.remove('NotExistKey')

print(s1)

# 交集、并集
s2 = set([1,2,3])
s3 = set([2,3,5])

#交集
print(s2 & s3)

#并集
print(s2 | s3)
