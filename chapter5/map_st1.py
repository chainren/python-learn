# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

def f(x):
    return x * x

nums = [1,2,3,4,5,6,7,8,9]
r = map(f,nums)


for n in r:
    print(n)

numtostr = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(numtostr)


# 练习：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

def f(str):
    return str[1].upper() + str[1:].lower()

names = list(map(f, ['adam', 'LISA', 'barT']))

for name in names:
    print(name)
