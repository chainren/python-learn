#　-- coding: utf-8 --
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。

# 首先，我们看看itertools提供的几个“无限”迭代器：

import itertools

natuals = itertools.count(1)
# for n in natuals:
#    print(n)

# cycle()会把传入的一个序列无限重复下去：

cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)


# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
rp = itertools.repeat('A', 10)
for c in rp:
    print(c)

# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x <=10, natuals)
ls = list(ns)
print(ls)


# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('abc', 'xyz'):
    print(c)


# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AABBCWAACCD'):
    print(key, list(group))

print('------------------')

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))


