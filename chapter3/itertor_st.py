##list 、tuple迭代
list1 = ['one','two','three']

for item in list1:
    print(item)

print('------------------')

##字典迭代
dict1 = {"a":"A","b":"B","c":"C"}

# 迭代key
for key in dict1:
    print(key)

#迭代value

for val in dict1.values():
    print(val)

#迭代k,v

for k,v in dict1.items():
    print(k +":" + v)


##迭代字符串
for chr in 'angry':
    print(chr)


## 判断对像是否可迭代

from collections import Iterable
print(isinstance('abc', Iterable))

print(isinstance(list1, Iterable))

print(isinstance(dict1, Iterable))


## list下循环迭代 enumerate
for i,val in enumerate(list1):
    print(i,val)

