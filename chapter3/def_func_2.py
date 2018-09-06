def pwoer(x,n):
	s = 1
	while n > 0 :
		s = s * x
		n = n - 1
            return s

# 默认参数
def power(x,n = 2):
	s = 1
	while n > 0 :
	    s = s * x
	    n = n - 1
            return s

#可变参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 关键字参数
def person(name,age, **kw):
    print('name:',name,'age:',age,'other:',kw)
    
person('crg',28)

person('crg',28, city='beijing')

extra ={'city':'beijing','job':'programmer'}

person('crg',28,**extra)

# 命名关键字参数
def person(name,age,*,city,job):
    print(name, age, city,job)

    
person('crg',28,city='beijing',job='engineer')


def person(name,age, *args,city,job):
     print(name, age, args, city,job)


def person(name,age, *args,city='beijing',job):
     print(name, age, args, city,job)
