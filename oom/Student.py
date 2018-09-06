# 对象模型 student

import  sys

class Student(object):
    def __init__(self,name, score):
        self.name = name
        self.score = score

    def printInfo(self):
        print('%s : %s' % self.name, self.score)

stua  = Student('stua', 88)
stub = Student('stub',90)

stua.printInfo()
stub.printInfo()