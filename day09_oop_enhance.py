# 访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作
# 使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


# if __name__ == '__main__':
#     main()

# 如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义__slots__变量来进行限定
# __slots__的限定只对当前类的对象生效，对子类并不起任何作用
class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age,gender):
        self._name = name
        self._age = age
        self._gender = gender

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋%s.' % (self.name,self._gender))
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 16,'男')
    person.play()
    person._gender = '女'
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True
    person.play()
if __name__ == '__main__':
    main()

# 静态方法和类方法
from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod#静态方法
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')


# if __name__ == '__main__':
#     main()


# 子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）
# 当我们调用这个经过子类重写的方法时，不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）
# 所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。


# 装饰器的引入纯粹是一个“语法糖”，即让代码看起来更加易懂。装饰器引入前Python中已经存在了“class method”, "static method"等包裹函数，
# 不使用装饰器的结果是如果一个方法要被声明为class method，那么在他的“def”语句结束后需要立即使用"classmethod"将其注册成类方法。
# 这样有一些弊端：当代码的读者开始读这个函数的时候，他一般看不到末尾的"classmethod"语句，所以可能直到看完整个函数的定义才知道这是一个类方法，
# 也即是最初没有装饰器时在定义的结尾对方法进行装饰的设定比较反人类；另外采用 method = classmethod(method) 方式写出来的代码，
# 设计Python的大神们觉得 method 竟然重复出现了两次太多了，写这两次 method 的时间已经够他们喝一壶的了，所以引入了更为简洁的decorator。

# 装饰器以“@”标识，实质上是一层包裹函数，即函数的函数。写在函数定义（ def 语句）的前面，表示 def 语句后定义的函数受到装饰器的装饰，
# 也就是说这个新定义的函数刚刚出生，立刻在函数定义结束的下一行代码运行装饰器给她穿点衣服遮羞。


# abc.ABCMeta 这是用来生成抽象基础类的元类。由它生成的类可以被直接继承。
# abc.ABC辅助类，让你可以不用关心元类概念，直接继承它，就有了ABCMeta元类。使用时注意元类冲突
# @abc.abstractmethod 定义抽象方法，除了这个装饰器，其余装饰器都被deprecated了。