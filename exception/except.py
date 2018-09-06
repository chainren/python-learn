# 异常处理
import logging

try:
    print('try')
    r = 10 / 0  # 会出现错误
    print('result is ', r)
except ZeroDivisionError as e:
    print('except:', e)
except ValueError as e:
    logging.exception("exception", e)
    print("value except:", e)
finally:
    print('finally:')
print('end')


# 自定义异常
class FooError(ValueError):
    pass


# raise抛出一个错误实例

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError("invalid value:%s" % s)
    return 10 / n


foo('0')

# BaseException
try:
    pass
except BaseException as e:
    pass

# 断言， 凡是用print()来辅助查看的地方，都可以用断言 assert来替代。如果断言失败，assert语句本身就会抛出AssertionError：
def foo(s):
    n = int(s)
    assert n !=0, 'n is zero!'
    return 10/n

foo('0')


# logging 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：

logging.basicConfig(level=logging.INFO) #　设置日志级别

logging.info('msg')
logging.warn('msg')
logging.error('msg')


#　pdb 启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。

