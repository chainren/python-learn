"""
python 操作redis
step1. 安装redis模块 pip install redis
"""

import redis

# 创建连接池
# 设置decode_responses=True，写入的KV对中的V为string类型，不加则写入的为字节类型。
pool = redis.ConnectionPool(host='127.0.0.1', port = 6379, db=0, decode_responses=True)

# 获取连接
rs = redis.Redis(connection_pool=pool)

# 操作字符串类型数据

# ex 设置过期时间，秒
rs.set(name='color',value='red', ex = 5)
print(rs.get('color'))

# nx 即setNX，如果key已经存在，则不执行； 否则才set值。 
rs.set('color', 'green', nx=True)
print(rs.get('color')) # red

# xx 如果设置为True，则只有name存在时，当前set操作才执行
rs.set('color', 'green', xx=True)
print(rs.get('color')) # green

# 批量设置、获取值
rs.mset({'key1':'value1', 'key2':'value2', 'key3':'value3'})

print(rs.mget('key1', 'key2','key3'))

# 自增长数字，每次按1增长
num = rs.incrby('number', amount=1)
print(num)
# 自减数字
num = rs.decr('number')
print(num)

## list类型

# 插入元素到List ,从左边插入
# rs.lpush('list', 1, 2, 3, 4, 5)
# 获取list中元素
# print(rs.lrange('list', 0, -1))

# 从右边插入元素
# rs.rpush('list', 6, 7, 8, 9, 10)
print(rs.lrange('list', 0, -1))

# 从左边弹出元素
# print(rs.lpop('list'))

# 获取索引位置的元素
print(rs.lindex('list', 1))

# hash类型
print('================================================')

# hset设置key-value键值对到一个hash结构中
rs.hset('person_1', 'name','tom')
rs.hset('person_1', 'age','31')
# 获取hash中的数据
print(rs.hget('person_1', 'name'))
print(rs.hgetall('person_1'))

# 设置多个key-value
rs.hmset('person_1', {'mobile':'15510792994','addr':'湖北麻城'})

# 获取多个key值
person_1 = rs.hmget('person_1', 'name', 'mobile', 'addr')
print(person_1)

# 获取hash中所有key
print(rs.hkeys('person_1'))

# 获取hash中所有value值
print(rs.hvals('person_1'))

# 获取键值对个数
print(rs.hlen('person_1'))

# 是否存在某个key
print(rs.hexists('person_1', 'email'))

# 删除某个key
print(rs.hdel('person_1', 'age'))


# set类型方法

print('===========================================')

# 增加集合元素，如集合不存在则新建
rs.sadd('my_set', 'one', 'two', 3)

# 返回集合元素个数
print(rs.scard('my_set')) 

# 返回所有元素
print(rs.smembers('my_set'))

# 返回所有成员
print(rs.sscan('my_set'))

rs.sadd('my_set1', 'one', 'three')

# 求交集
sinter = rs.sinter('my_set', 'my_set1')
print(sinter)

# 求并集
sunion = rs.sunion('my_set', 'my_set1')
print(sunion)

# 求差集
diff = rs.sdiff('my_set', 'my_set1')
print(diff)
diff = rs.sdiff('my_set1', 'my_set')
print(diff)

# 求交集并存入另一个集合
rs.sinterstore('my_set_inter', 'my_set', 'my_set1')
print(rs.smembers('my_set_inter'))

# 判断'one'是否在集合中
res = rs.sismember('my_set', 'one')
print(res)

# 随机删除并返回集合中的一个元素
# print(rs.spop('my_set'))

# 删除集合元素中值为5的元素
print(rs.srem('my_set1', 5))


## zset 类型方法

print('======================================')

# 增加集合元素，如集合不存在则新建
rs.zadd('fruits', {'apple':1, 'banana':3, 'orange':5})

# 遍历所有元素
print(rs.zrange("fruits", 0, -1))    #结果：['apple', 'banana', 'orange']

# withscores=True指带上分数
print(rs.zrange("fruits", 0, -1, withscores=True))   #结果：[('apple', 1.0), ('banana', 3.0), ('orange', 5.0)]

# 根据分数由大到小遍历所有元素
print(rs.zrevrange("fruits", 0, -1))   #结果：['orange', 'banana', 'apple']

# 获取orange元素对应的分数
rs.zscore('fruits', 'orange')     #结果：5.0

# 取出分数>=3 and 分数<=5的元素
print(rs.zrangebyscore('fruits', 3, 5))

# 取出分数<=5 and 分数>=3的元素，根据分数从大到小排序
print(rs.zrevrangebyscore('fruits', 5, 3))

# 遍历所有元素，返回一个元组
print(rs.zscan('fruits'))   #结果：(0, [('apple', 1.0), ('banana', 3.0), ('orange', 5.0)])

# 打印集合元素个数
print(rs.zcard('fruits'))    #结果：3

# 返回集合中分数>=1 and 分数<=3元素个数
print(rs.zcount('fruits', 1, 3))

# 将集合中apple元素的分数+5
rs.zincrby('fruits', 5, 'apple')
print(rs.zrange("fruits", 0, -1, withscores=True))   #返回结果：[('banana', 3.0), ('orange', 5.0), ('apple', 6.0)]

# 返回orange元素在集合中的索引号
rs.zrank('fruits', 'orange')     #结果：1

# 按分数从大到小排序，取出banana元素索引号
rs.zrevrank('fruits', 'banana')   #结果：2

# #删除集合中apple元素
rs.zrem('fruits', 'apple')
print(rs.zrange("fruits", 0, -1))   #返回结果：['banana', 'orange']

# #删除集合索引号>=0 and 索引号<=2的元素
rs.zremrangebyrank('fruits', 0, 2)

# 删除集合分数>=1 and 分数<=5的元素
rs.zremrangebyscore('fruits', 1, 5)

## 针对key可操作方法
print('==========================================')
# 删除key为color的对象
rs.delete('color')

# 查询key为color的对象是否存在
print(rs.exists('color'))    #结果：False
rs.sadd('mySet5', 'one', 'two')

# 设置key的超时时间
rs.expire('mySet5', time=5)   #单位：秒

# 重命名key的值
rs.rename('mySet5', 'set5')

# 随机返回当前库中一个key，但不会删除
print(rs.randomkey())

# 查看某个key对应值的类型
print(rs.type('mySet'))   #返回结果：set

# 通过模糊匹配出满足条件的key
print(rs.keys('my*'))    #返回结果：['mySet', 'mySet2']

#各类型元素迭代方式
#hash类型迭代
for i in rs.hscan_iter("hName"):
    print(i)

#set类型迭代
for j in rs.sscan_iter("mySet"):
    print(j)

#zset类型迭代
for k in rs.zscan_iter("fruits"):
    print(k)


# 发布订阅

# 发布者
rs.publish('chat','hello friends!')

# 订阅者
sub = rs.pubsub()

# 阻塞监听
sub.psubscribe(['chat'])

for item in sub.listen():
    print(item['channel'], item['data'])

import time

# 非阻塞监听
sub.psubscribe(['chat'])
while True:
    item = sub.get_message()
    if item:
        print(item['channel'], item['data'])
    time.sleep(1)


# 线程非阻塞监听
def my_handle(item):
    print(item['channel'], item['data'])

sub = rs.pubsub(*{'chat': my_handle})
th = sub.run_in_thread(0.3)

# 开始监听后,若要停止,可执行如下语句
th.stop()
