# 抽象数据类型: 通过class实现,创造特定数据类型
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self,others):
        x_dis = (self.x - others.x) ** 2
        y_dis = (self.y - others.y) ** 2
        return (x_dis + y_dis) ** 0.5
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
c = Coordinate(3,4)
zero = Coordinate(0,0)
print(c.distance(zero))
# print(Coordinate.distance(c, zero))
print(c)
print(type(c))
# print(Coordinate)
print(type(Coordinate))
print(isinstance(c, Coordinate))
# isinstance() is to check if an object is a Coordinate

# Animal例子：
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    # getter——这种机制可以有效避免修改初始值以及修改变量名的bug
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    # setter
    def set_age(self, newage):
        self.age= newage
    def set_name(self, newname=""):
        self.name = newname
    # defset_name(self, newname=""):    其中""中为初始化的默认值
    #     self.name = newname
    # 打印这种类型的object
    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)
###################################################################
# 父类
class Animal(object):
    def __init__(self, age):
        self.age= age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age= newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)
# 子类——继承关系，继承的是__init__和父类中的变量值
class Cat(Animal):    #父类是Class Animal
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)
# 子类
class Person(Animal):    #父类是Class Animal
    def __init__(self, name, age):
        Animal.__init__(self, age)    #调用Animal中的__init__
        self.set_name(name)    #调用Animal的方法
        self.friends = []    #创建新的数据类型
    # New Methods
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fnamenot in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        diff = self.age-other.age
        print(abs(diff), "year difference")
    # 覆盖Animal中__str__的方法
    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)

import random    #导入使用random的方法
# person的子类
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()    #生成的随机数为[0,1)
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")
    def __str__(self):
        return "student:" + str(self.name) + ":" + str(self.age) + ":" + str(self.major)
# 当子类中出现需要用到变量时：
class Rabbit(Animal):
    tag = 1   #class中的变量 
    def__init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag    #实例变量 = class变量
        Rabbit.tag += 1    #给每一只Rabbit赋id值
    # 从Animal中继承的get_name和get_age同样可用
    def get_rid(self):
        return str(self.rid).zfill(3)    #填充rid中的数字知道3位（001）
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
    # 加法 returning object of same type as this class
        return Rabbit(0, self, other)
        #recall Rabbit’s __init__(self, age, parent1=None, parent2=None)
        #                             0    ，    self    ，   other
    def __eq__(self, other):
        '''
        decide that two rabbits are equal if they have the same two parents
        '''
        parents_same= self.parent1.rid == other.parent1.rid \   
            and self.parent2.rid == other.parent2.rid
        parents_opposite= self.parent2.rid == other.parent1.rid \
            and self.parent1.rid == other.parent2.rid
        return parents_sameor parents_opposite
    # note you can’t compare objects directly
    # for ex. with self.parent1 == other.parent1
    # this calls the __eq__method over and over until call it on Noneand gives an AttributeErrorwhen it tries to do None.parent1