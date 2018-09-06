#使用type()判断对象类型
print(type(123))

#也可以判断函数
print(type(abs))

#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types

def fn():
    pass

print(type(fn) == types.FunctionType)

print(type(abs) == types.BuiltinFunctionType)

print(type(lambda x : x) == types.LambdaType)

print(type(x for x in range(100)) == types.GeneratorType)


# isinstance()

class Animal(object):
    pass

a = Animal()

flag = isinstance(a, Animal)
print(flag) # True


# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObj(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObj()

#判断是否有该属性
print(hasattr(obj, 'x')) # True

#设置一个属性
setattr(obj, 'y', 10)

#获取一个属性值，可以设置一个默认值，如果属性不存在，返回404
getattr(obj,'y','404')

print(obj.y)



# 练习，定义一个计数器，每生成一个实例，计数器累加
class InstanceCounter(object):
    count = 0
    def __init__(self,name):
        InstanceCounter.count += 1
        print(self.count)

ic1 = InstanceCounter('counter1')
ic2 = InstanceCounter('counter2')
ic3 = InstanceCounter('counter3')


