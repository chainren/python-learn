# 继承和多态

class Animal(object):
    def run(self):
        print('Animal is running...')

#定义子类，继承Animal
class Dog(Animal):
    pass

class Cat(Animal):
    pass


#子类调用父类方法

dog = Dog()
dog.run()

cat = Cat()
cat.run()

#重写父类方法，扩展子类方法
class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Dog is eating...')

dog = Dog()
dog.run()
dog.eat()


#判断变量类型
flag = isinstance(dog, Animal)
print(flag)

isinstance(dog, Dog)
print(flag)

animal = Animal()

#父类的实例不可能是子类的类型
falg1 = isinstance(animal, Dog)
print(falg1)


def run_twice(animal):
    animal.run()
    animal.run()

#根据传入的实例不同，调用的实例方法也不同
run_twice(animal)
run_twice(dog)


#多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，

