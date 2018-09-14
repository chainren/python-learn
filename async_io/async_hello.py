# -*- coding: utf-8 -*-

# asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
import asyncio


@asyncio.coroutine
def hello():
    print('Hello world')
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again! %s" % r)

# 获取EventLoop
loop= asyncio.get_event_loop()

# 执行coroutine 协程
loop.run_until_complete(hello())

# 多个协程由同一个线程执行
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))

loop.close()


# @asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。
# yield from语法可以让我们方便地调用另一个generatoryield from语法可以让我们方便地调用另一个generator
# asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
# 当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。

