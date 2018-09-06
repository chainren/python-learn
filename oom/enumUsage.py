#定义枚举类
from enum import  Enum

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

#使用枚举
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)




from enum import Enum, unique

@unique #@unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0 #Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

#访问枚举值
day1 = Weekday.Sun

print(day1)

print(Weekday(4))


