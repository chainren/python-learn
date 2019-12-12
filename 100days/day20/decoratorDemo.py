"""
装饰器 decorator
使用装饰器的@语法，就相当于是将具体定义的函数作为参数传入装饰器函数，而装饰器函数则经过一系列操作，返回一个新的函数，然后再将这个新的函数赋值给原先的函数名。
"""

# 定义一个装饰器。 装饰函数有且只能有一个参数，即要被修饰的原函数


def decorator(func):
    print("This is decorator....")

    # 定义一个内部函数，增强原函数功能
    def wapper(*args, **kw):
        print("Wapper the orign func...")
        return func(*args, **kw)

    # 返回增强函数
    return wapper


@decorator
def tobeDecoratedFunc(some):
    print("This func is decorated..., params: %s" % some)


if __name__ == '__main__':
    f = decorator(tobeDecoratedFunc)
    print(f.__name__)