#sorted函数，用于排序

s = sorted((230,32,191,3,-11,39))
print(s)

##sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
s1 = sorted([-1,20,301,-11,39,-400],key=abs)
print(s1)

## 字符串排序
s2 = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(s2)

