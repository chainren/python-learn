import time
import threadpool

import threading

def sayhello(name):
    print('%s say hello to %s' % (threading.current_thread().getName, name))
    time.sleep(1)
    return name


# 回调函数，用于取回结果
def callback(request, result):
    print('callback result = %s' % result)

name_list = ['admin', 'root', 'scott', 'tiger']
start_time = time.time()
# 创建线程池
pool = threadpool.ThreadPool(2)
# 创建任务
requests = threadpool.makeRequests(sayhello, name_list, callback)
# 加入任务
[pool.putRequest(req) for req in requests]

pool.wait()
print('%s cost %d second' % (threading.current_thread().getName(), time.time()-start_time))
