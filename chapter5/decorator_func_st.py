import time
import functools
##装饰器
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。

def now():
    print(time.time())

f = now

print(f())

#函数对象有一个__name__属性，可以拿到函数的名字：

name = now.__name__
print(name)
print(f.__name__)

#现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
#本质上，decorator就是一个返回函数的高阶函数。
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#借助Python的@语法，把decorator置于函数的定义处
@log
def now1():
    print(time.time())

print(now1())

#把@log放到now()函数的定义处，相当于执行了语句 now = log(now)


## 小结
#在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。
#decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。