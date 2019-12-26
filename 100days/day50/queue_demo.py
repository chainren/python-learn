'''
 使用queue实现生产者-消费者模式
'''

import threading
import time
import queue


# 消费者
def consume(thread_nume, q):
    while True:
        time.sleep(2)
        product = q.get()
        print('%s consume %s' % (thread_nume, product))
        # 任务处理结束后，调用task_done，
        q.task_done()

# 生产者
def produce(thread_name, q):
    for i in range(3):
        product = 'product-'+str(i)
        q.put(product)
        print('%s produce %s' % (thread_name, product))
        time.sleep(1)
    # join() 就是在监听队列是否为空，一旦条件满足则结束阻塞状态。
    q.join()


# 队列
q = queue.Queue()

p = threading.Thread(target=produce, args=('producer', q))
p.start()

# 将消费者线程设置为daemon，主线程结束时，消费者线程也会自动结束
c0 = threading.Thread(target=consume, args=('consumer-0', q), daemon=True)
c1 = threading.Thread(target=consume, args=('consumer-1', q), daemon=True)

c0.start()
c1.start()

p.join()
