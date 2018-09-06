# 分布式进程

# Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。
# 一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。

# 原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。

# 我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：



import queue
import random
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()

# 接收结果的队列
result_queue = queue.Queue()


# 从BaseManager继承
class QueueManager(BaseManager):
    pass


# pickle模块不能序列化lambda function，故我们需要自行定义函数，实现序列化
def get_task_queue():
    global task_queue
    return task_queue


def get_result_queue():
    global result_queue
    return result_queue


def start_master():
    # 把两个Queue都注册到网上，callable参数关联了Queue对象
    QueueManager.register('get_task_queue', callable=get_task_queue)
    QueueManager.register('get_result_queue', callable=get_result_queue)

    # 绑定端口5000, 设置验证码'abc':
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # 启动Queue
    manager.start()

    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()

    result = manager.get_result_queue()

    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    print('Try get results...')

    # 从result队列读取结果:
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)

    # 关闭
    manager.shutdown()

    print('master exit.')


# 请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，但是，
# 在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。

# 启动服务端

if __name__ == '__main__':
    start_master()




# 这个简单的Master/Worker模型有什么用？其实这就是一个简单但真正的分布式计算，把代码稍加改造，启动多个worker，就可以把任务分布到几台甚至几十台机器上，比如把计算n*n的代码换成发送邮件，就实现了邮件队列的异步发送。
#
# Queue对象存储在哪？注意到task_worker.py中根本没有创建Queue的代码，所以，Queue对象存储在task_master.py进程中：
#
# │
# ┌─────────────────────────────────────────┐     ┌──────────────────────────────────────┐
# │task_master.py                           │  │  │task_worker.py                        │
# │                                         │     │                                      │
# │  task = manager.get_task_queue()        │  │  │  task = manager.get_task_queue()     │
# │  result = manager.get_result_queue()    │     │  result = manager.get_result_queue() │
# │              │                          │  │  │              │                       │
# │              │                          │     │              │                       │
# │              ▼                          │  │  │              │                       │
# │  ┌─────────────────────────────────┐    │     │              │                       │
# │  │QueueManager                     │    │  │  │              │                       │
# │  │ ┌────────────┐ ┌──────────────┐ │    │     │              │                       │
# │  │ │ task_queue │ │ result_queue │ │<───┼──┼──┼──────────────┘                       │
# │  │ └────────────┘ └──────────────┘ │    │     │                                      │
# │  └─────────────────────────────────┘    │  │  │                                      │
# └─────────────────────────────────────────┘     └──────────────────────────────────────┘
# │
#
#                                             Network

# 而Queue之所以能通过网络访问，就是通过QueueManager实现的。由于QueueManager管理的不止一个Queue，所以，要给每个Queue的网络调用接口起个名字，比如get_task_queue。

# authkey有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果task_worker.py的authkey和task_master.py的authkey不一致，肯定连接不上。


# 小结
# Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。
#
# 注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，
# 而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。