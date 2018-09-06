# filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def even(x):
    return x % 2 == 0


f = filter(even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(list(f))

print('----------------------------')


# 素数
# step1.构造一个从3开始的奇数序列
def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# step2.定义筛选函数
def not_divisible(n):
    return lambda x: x % n > 0


# step3.定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible, it)


# 输出序列
for x in primes():
    if x < 1000:
        print(x)
    else:
        break;

#filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。