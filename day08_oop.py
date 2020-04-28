class student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name,age):
        # super(student, self).__init__()
        self.name = name
        self.age = age
    def study(self,course_name):
        print("%s正在学习%s" % (self.name,course_name))
    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print("%s不能看" % self.name)
        else:
            print("%s来康康" % self.name)
def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = student("koopa",26)
    stu2 = student("廖雪峰",42)
    # 给对象发study消息
    stu1.study("python")
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2.study("教python")
    stu2.watch_movie()

# if __name__ == '__main__':
#     main()

# 在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的
# 如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头

# Python并没有从语法上严格保证私有属性或方法的私密性，
# 它只是给私有的属性和方法换了一个名字来妨碍对它们的访问,
# 事实上如果你知道更换名字的规则仍然可以访问到它们

# 定义一个类描述数字时钟
from time import sleep

class Clock(object):
    """docstring for Clock"""
    def __init__(self,hour=0,minute=0,second=0):
        # super(Clock, self).__init__()
        self.hour = hour
        self.minute = minute
        self.second = second
    def run(self):
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
            if self.minute == 60:
                self.hour += 1
                self.minute = 0
                if self.hour == 24:
                    self.hour = 0
                    self.minute = 0
                    self.second = 0
    def show(self):
        return "%02d : %02d : %02d" % (self.hour,self.minute,self.second)

def main():
    clock = Clock(11,59,59)
    while True:
        sleep(1)
        print(clock.show())
        clock.run()

# if __name__ == '__main__':
#     main()

# 定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法
from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        """初始化方法
        
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """移动到指定位置
        
        :param x: 新的横坐标
        "param y: 新的纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """移动指定的增量
        
        :param dx: 横坐标的增量
        "param dy: 纵坐标的增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """计算与另一个点的距离
        
        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()