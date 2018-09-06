# Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程

import os

print('process (%s) start...' % os.getppid())

# pid = os.fork()

# if pid == 0 :
#     print('I am child process (%s) and my parent is %s' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' %(os.getpid(), pid))


# multiprocessing
# multiprocessing模块提供了一个Process类来代表一个进程对象

from multiprocessing import Process

import os

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')


# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
