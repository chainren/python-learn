#列表生成式List Comprehensions
L1 = [x*x for x in range(1,100) if x % 2 == 0]
print(L1)

L2 = [m + n for m in 'ABC' for n in 'XYZ']
print(L2)

#列出当前目录下的所有文件
import os
files = [d for d in os.listdir('.')]

for f in files:
    print(f)

#
L3 = ['Hello', 'World', 18, 'Apple', None]

lower_l3 = [s.lower() for s in L3 if isinstance(s, str)]
print(lower_l3)


##生成器
L4 = [x*x for x in range(1,10)]

print(L4)

g = (x*x for x in range(1,10))

for x in g:
    print(x)

print('-------------------------')
## yield关键字
def fib(max):
    n,a,b = 0, 0 , 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(100):
    print(n)

#杨辉三角
