class Student(object):
    def __init__(self, name, score, address):
        self.__name = name
        self.__score = score
        self.address = address

    def print_score(self):
        print('%s : %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


bart = Student('Jack', 89, 'beijing')
lisa = Student('lisa', 99, 'henan')

print(bart.get_name)
print(bart.address)

bart.print_score()
lisa.print_score()


class Animal(object):
    def run(self):
        print("animal is run")


class Dog(Animal):
    def run(self):
        print("Dog is run")


class Cat(Animal):
    def run(self):
        print("Cat is run")


def run_twince(Animal):
    Animal.run()
    Animal.run()


run_twince(Dog())

run_twince(Cat())


# 这个是动态语言的特性  只有在使用的时候判断类型
class Time(object):
    def run(self):
        print("Time is run")


run_twince(Time())

print("-------------------获得类的属性-------------------")

print(hasattr(bart, '__name'))
print(getattr(bart, 'address'))

print("-------------------实例属性 和 类属性-------------------")


# 类属性
class Person(object):
    name = 'person'


pp = Person()

# 动态添加属性
pp.address = 'beijing'

# 实例属性
print(pp.name)
print(Person.name)
print(pp.address)

pp.name = 'pp-person'

print(pp.name)
print(Person.name)

print("-------------------面向对象高级编程-------------------")


class Student(object):
    pass


s = Student()

s.name = 'yang'
print(s.name)


# 给单个实例绑定方法
def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)

print(s.age)

# 给所有实例添加方法
s2 = Student()


def set_score(self, score):
    self.score = score


Student.set_score = set_score

s.set_score(100)
s2.set_score(99)

print(s.score)
print(s2.score)

print("-------------------__slots__的使用-------------------")


# 限制属性

class StudentOne(object):
    # 限制不能新增属性
    __slots__ = ('name', 'age')
    pass

    def get_att(self):
        print('%s %s' % (self.name, self.age))


StudentOne.set_score = set_score

s1 = StudentOne()

s1.name = 'yang'
s1.age = 90
# s1.score = 88
# print(s1.score)

s1.get_att()

print("-------------------@property的使用-------------------")


class StudentTwo(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer")

        if value < 0 or value > 100:
            raise ValueError("score must between 0 - 100")
        self._score = value


s = StudentTwo()
s.set_score(90)

print(s.get_score())


# s.set_score(400)

# 虽然是定义一个方法  其实是个属性

class StudentTwo(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

s = StudentTwo()
s._birth = 2000

print(s.age)


# 定制类

print("-------------------定制类的使用-------------------")

class StudentThree(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'StudentThree object (name : %s) ' % self.name

s3 = StudentThree('yang')
print(s3)

print("-------------------enum 枚举-------------------")

from enum import Enum

Mounth = Enum('Month', ('Jan', 'Feb'))

for name, member in Mounth.__members__.items():
    print(name, '=>', member, ',', member.value)

from enum import  Enum,unique

# unique 用来检测唯一
@unique
class Weekday(Enum):
    sun = 0
    mon = 1
    tue = 2
    wed = 3
    thu = 4
    fri = 5
    sat = 6

day1 = Weekday.mon
print(day1, ',',day1.value)

day6 = Weekday(6)
print(day6, ',',day6.value)


print("-------------------使用元类-------------------")