# JSON 序列化成标准的数据格式，比如json、xml等，可以在不同语言程序之间通信
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
# encoding=utf8

import json

stu = dict(name = 'chainren', age = 29, score = 99)

# dumps()方法返回一个str，内容就是标准的JSON。
obj = json.dumps(stu)

print(obj)

# json反序列化

stu = json.loads(obj)

print(stu)


# 将实例对象序列化成json

class Student(object):
    def __init__(self,name, age, score):
        self.name = name
        self.age = age
        self.score = score


stu = Student('Tom', 9 , 80)

print(stu)

# 直接使用json序列化会有问题，json模块不知道如何将实例对象序列化为json字符串
# json.dumps(stu)


#可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可
# Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON

def stutodict(stu):
    return {
        'name': stu.name,
        'age': stu.age,
        'score': stu.score
    }

stuJson = json.dumps(stu, default=stutodict)

print(stuJson)

# 使用lambda表达式，可以将任务实例对象的属性转换成dict,然后通过json.dumps就可以序列化成json了
print(json.dumps(stu, default= lambda obj:obj.__dict__))

# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。


# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

jsonStr = '{"name": "Tom", "score": 80, "age": 9}'

print(json.loads(jsonStr, object_hook=dict2student))
