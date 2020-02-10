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