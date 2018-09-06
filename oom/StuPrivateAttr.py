## 通过在变量前加__，使定义的变量成为私有变量，外部不能直接访问

class Student(object):
    def __init__(self, name, score, clasz):
        self.__name = name # 不能直接进行修改，需要提借对外的修改方法
        self.__score = score
        self.clasz = clasz # 可以通过实例对其直接修改

    def print_self(self):
        print('%s: %s' % (self.__name, self.__score))

    def print_claz(self):
        print(self.clasz)

    #定义一个可以设置私有属性的方法，通过调用该方法可以修改属性值
    def set_name(self, name):
        self.__name = name


#验证
sta = Student('chenrg', 99, 'A')

sta.print_self()

# 不会更改
sta.__score = 21
sta.print_self()

# 调用方法修改name
sta.set_name('chenrengui')
sta.print_self()


sta.print_claz()

sta.clasz = 'B'
sta.print_claz()
