#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'a test module'

__author__ = 'chenrg'

import sys


def test():
    args = sys.argv
    print(args)
    if (len(args) == 1):
        print("hello world!")
    elif (len(args) == 2):
        print("hello,%s!" % args[1])
    else:
        print("too many args!")


if __name__ == '__main__':
    test()


## 作用域
# 1.正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
# 2.类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
