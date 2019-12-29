import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

def sayhello(name):
    print('%s say hello to %s' % (threading.current_thread().getName(), name))
    time.sleep(1)
    return name

name_list =['admin','root','scott','tiger']
start_time = time.time()
# 创建线程池
with ThreadPoolExecutor(2) as executor:
    # 提交任务
    future_list = [executor.submit(sayhello, name) for name in name_list]


for future in as_completed(future_list):
     # 获取任务结果
    result = future.result()   
    print("%s get result : %s" % (threading.current_thread().getName(), result))

print('%s cost %d second' % (threading.current_thread().getName(), time.time()-start_time))
