#返回函数

#普通求和函数
def sum(*args):
    nums = 0
    for n in args:
        nums = nums + n
    return nums

print(sum(1,2,3,4))

#但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        n = 0
        for x in args:
            n = n+x
        return n
    return sum

#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
f = lazy_sum(1,2,3,4)
print(f)

#调用函数f时，才真正计算求和的结果：
print(f())

#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1,2,3,4)
f2 = lazy_sum(1,2,3,4)
print(f1 == f2)

#缺点是代码较长，可利用lambda函数缩短代码。

## 小结
#一个函数可以返回一个计算结果，也可以返回一个函数。
#返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

#练习 利用闭包返回一个计数器函数，每次调用它返回递增整数
def create_counter():
    n = 0
    def counter():
        nonlocal n
        n = n + 1
        return n
    return counter

f  = create_counter()
print(f())
print(f())
print(f())

#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。