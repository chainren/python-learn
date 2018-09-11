# 进程通信
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

# -- coding: utf-8 --

# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：

from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码:

def writeProc(q):
    print('Process to write %s' % os.getpid())
    for value in ['A', 'B', 'C', 'D']:
        print('Put %s to queue' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def readProc(q):
    print('Process to read %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=writeProc, args=(q,))
    pr = Process(target=readProc, args=(q,))
    # 启动写进程
    pw.start()

    # 启动读进程
    pr.start()

    # 等待pw结束:
    pw.join()

    # pr进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()

