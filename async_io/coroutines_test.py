# -*- coding:utf-8 -*-

# 协程


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSOUMER] cosuming %s ...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n +1
        print('[PRODUCE] producing %s ...' % n)
        r = c.send(n)
        print('[PRODUCE] consumer return : %s' % r)
    c.close()


c = consumer()

produce(c)


# 首先调用c.send(None)启动生成器；

# 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

# consumer通过yield拿到消息，处理，又通过yield把结果传回；

# produce拿到consumer处理的结果，继续生产下一条消息；

# produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

