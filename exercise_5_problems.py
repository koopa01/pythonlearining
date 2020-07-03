# 1、用户从终端输入一个分数，程序输出这个分数所属的考评等级，90到100分是A，60到89是B，60分以下是C。（15分）
def number():
    while True:
        try:
            point = int(input("请输入一个分数："))
            if point < 0 and point > 100:
                print("请输入0-100的数字\n")
            elif point < 60:
                print("C")
            elif point < 90:
                print("B")
            elif point <= 100:
                print("A")
        except ValueError as ve:
            print('请输入一个数字!')
            print(ve,"\n")
            break
    ###################可选项########################
        else:#如果没有异常（输入正确）就打印本句话
            print('谢谢参与\n')
        # finally:#不管是否发生异常，都执行
        #     print('谢谢参与')
if __name__ == '__main__':
    number()

# 2、有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和（15分）
def feb():
    l1 = [2,3]
    l2 = [1,2]
    for i in range(0,18):
        num3 = l1[i] + l1[i+1]
        l1.append(num3)
    # print(l1)
    # print(len(l1))
    for j in range(0,18):
        num4 = l2[j] + l2[j+1]
        l2.append(num4)
    # print(l2)
    # print(len(l2))
    l3 = []
    for j in range(20):
        l3.append(l1[j]/l2[j])
    print(l3)
    return sum(l3)
print(feb())

# 3、猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。（20分）
def eat(num):
    for day in range(9,0,-1):
        num = (num + 1) * 2
        print(num,"第%d天\n" % day)
    return num
print("第一天",eat(1))


# 4、请用面对对象的思想编写一个小游戏，人狗大站，2个角色，人和狗，游戏开始后，生成2个人，3条狗，互相混战，人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。（25分）
class People():
    agressivity = 10
    life_value = 100

    def __init__(self,name):
        self.name = name

    def attack(self,dog):
        dog.life_value -= 10

    def __str__(self):
        return '人%s剩余生命值:%s，状态值%s'%(self.name,self.life_value,self.agressivity)


class Dogs():
    agressivity = 15
    life_value = 80

    def __init__(self,name):
        self.name = name

    def attack(self,people):
        people.life_value -= 10

    def __str__(self):
        return '狗%s剩余生命值:%s，状态值%s'%(self.name,self.life_value,self.agressivity)

p1 = People('Tom')
p2 = People('Jack')
d1 = Dogs('niker')
d2 = Dogs('geeker')
d3 = Dogs('chaox')

print(p1)
print(p2)

p1.attack(d1)

print(d1)

# 5、一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？（25分）
high = 100
total = 0 - high
for x in range(1,11):
    total += high*2
    high /= 2
    print(total,high)
print("第10次落地时共经过%f米" % total,"第10次反弹%f米" % high)
