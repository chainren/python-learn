# Python内置的@property装饰器就是负责把一个方法变成属性调用的：
#把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, birth):
        self._birth = birth

    @property
    def age(self):
        return 2018 - self._birth


stu = Student()

# 实际转化为s.set_score(60)
stu.score = 90

#实际转化为s.get_score()
print(stu.score)

stu.score = 999 #值不合法
