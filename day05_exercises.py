import random
import math

# 水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，
# 例如：$1^3 + 5^3+ 3^3=153$。
l1 = []
for x in range(100,1000):
    a = (x % 10) ** 3
    b = ((x // 10) % 10) ** 3
    c = ((x // 10) // 10) ** 3
    if a + b + c == x:
        l1.append(x)
print(l1)

# 正整数反转，例如：将12345变成54321
# num = input("num =: ")
# num = list(num)
# l2 = []
# for x in range(len(num)):
#     l2.append(num.pop())
# print(l2)#结果是list类型的字符而不是int类型的整数
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

# 公鸡5元一只，母鸡3元一只，小鸡1元三只
# 用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

# CRAPS又称花旗骰，游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
# 玩家第一次摇骰子如果摇出了7点或11点，玩家胜
# 玩家第一次如果摇出2点、3点或12点，庄家胜
# 其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜
# 如果玩家摇出了第一次摇的点数，玩家胜
# 其他点数，玩家继续要骰子，直到分出胜负。
def gametwo():
    toss1 = random.randint(1,6)
    toss2 = random.randint(1,6)
    if toss1 + toss2 == 7:
        computer_win()
    elif toss1 + toss2 == a:
        player_win()
    else:
        gametwo()

def player_win():
    print("玩家胜")
def computer_win():
    print("庄家胜")

def gameone():
    toss1 = random.randint(1,6)
    toss2 = random.randint(1,6)
    a = toss1 + toss2
    if toss1 + toss2 == 7 or toss1 + toss2 == 11:
        player_win()
    elif toss1 + toss2 == 2 or toss1 + toss2 == 3 or toss1 + toss2 == 12:
        computer_win()
    else:
        gametwo()
gameone()

# 生成斐波那契数列的前20个数
l3 = [1,1]
def feb(a,b):
    a = a + b
    l3.append(a)
    b = a + b
    l3.append(b)
    while len(l3) <= 18:#第18次执行之后又进行循环加了两个数
        feb(a,b)
feb(1,1)#初始两个数为1，1 也可以先定义a=1,b=1，feb(a,b)
print(l3)
# print(len(l3))

# 输出100以内所有的素数。
# su = []
# for number in range(2,100):
#     facotr = number
#     for factor in range(2,facotr):
#         if number % factor == 0:
#             break
#     su.append(x)
# print(su)     
for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')

# 找出10000以内的完美数
# 完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
# 例如：6（6=1+2+3）和28（28=1+2+4+7+14）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。
# for perfect in range(1,10000):
#     is_factor = False
#     s = 0
#     for factor in range(1,int(math.sqrt(num)) + 1):
#         if perfect % factor == 0:
#             is_factor = True
#             if is_factor:
#                 s = s + factor
#     if perfect == s:
#         print(perfect)
for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)