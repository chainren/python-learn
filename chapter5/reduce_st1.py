# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#效里如 reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce

def add(x,y):
    return x + y

res = reduce(add, [1,3,5,7,9])
print(res)



#练习：编写一个prod()函数，可以接受一个list并利用reduce()求积
print('---------------------------')

def prod(x,y):
    return  x*y

res = reduce(prod,[1,3,5,7,9])
print(res)

