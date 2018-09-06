# 使用__slots__限制类可定义的属性

class Student(object):
    __slots__ = ("name","age")

#测试绑定其它属性

s = Student()

s.score = 90

