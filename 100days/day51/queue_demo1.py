import queue

# 先进先出队列。 maxsize设置可入队的任务数量。如果 maxsize 小于等于零，则队列尺寸为无限大。
q1 = queue.Queue(maxsize=100)
# 后进先出队列
q2 = queue.LifoQueue()
# 优先级队列，优先级高的先出列
q3 = queue.PriorityQueue()


# 放置任务
q1.put(100)
# 获取任务
q1.get()
# 获得队列大小
q1.qsize()
# 判断队列是否为空
q1.empty()
# 判断队列是否已满
q1.full()
