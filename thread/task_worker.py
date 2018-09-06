# encoding = utf8

import time
from multiprocessing.managers import BaseManager
from queue import Queue


# 创建类似的QueueManager:


class QueueManager(BaseManager):
    pass


# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器task_master
server_addr = '127.0.0.1'
print('Connect to server %s' % server_addr)

# 端口和验证码注意保持与task_master.py设置的完全一致:
manager = QueueManager(address=(server_addr, 5000), authkey=b'abc')

# 开启网络连接
manager.connect()

# 获取队列
task_queue = manager.get_task_queue()

result_queue = manager.get_result_queue()

# 从task_queue获取任务，并将结果写入result_queue
for i in range(10):
    try:
        n = task_queue.get(timeout=1)
        print('run task %d * %d' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result_queue.put(r)
    except Queue.Empty:
        print('Task queue is empty.')

# 处理结束
print('workder exit.')

if __name__ == '__main__':
    pass

