# slice 切片
L=['one','two','three']

print(L[0:1])

print(L[1:3])

# 如果从0开始，可省略
print(L[:2])

# 从后往前
print(L[-2:])

L1 = list(range(100))

print(L1)

# 隔两个元素取一次
print(L1[:10:2])

#所有数，每5个取一个：
print(L1[::5])

#复制一个list
L2 = L1[:]
print(L2)

#tuple 同样可能用切片操作，结果仍是tuple
T1 = (1,2,3)

print(T1[:2])


## 字符串也可用切片操作，操作结果仍是字符串
S1 = 'hello world!'

print(S1[:5])

print(S1[-6:-1])

