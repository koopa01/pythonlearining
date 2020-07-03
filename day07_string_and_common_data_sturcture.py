s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')
print("\n########################################\n")

# 用八进制或者十六进制数来表示字符，用Unicode字符编码来表示字符
s1 = '\u004b\u006f\u006f\x70\x61'
s2 = '\n\u7f57\u6631'
print(s1, s2)
print("\n########################################\n")

# 不希望\表转义--前面加r
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')
print("\n########################################\n")

s1 = 'hello ' * 3
print(s1) # hello hello hello 
s2 = 'world'
s1 += s2
print(s1) # hello hello hello world
print('ll' in s1) # True
print('good' in s1) # False
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2]) # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246
print(str2[::-1]) # 654321cba
print(str2[-3:-1]) # 45
print("\n########################################\n")

# 对字符串的处理
str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1)) # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or')) # 8
print(str1.find('shit')) # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())
print("\n########################################\n")

# 格式化输出字符串
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))
a, b = 5, 10
print(f'{a} * {b} = {a * b}')
print("\n########################################\n")

# 如何向列表中添加元素以及如何从列表中移除元素
list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)
list1.insert(1, 400)
# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1) # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(len(list1)) # 9
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1) # [1, 400, 5, 7, 100, 200, 1000, 2000]
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1) # [400, 5, 7, 100, 200, 1000]
# 清空列表元素
list1.clear()
print(list1) # []
print("\n########################################\n")

# 对列表的排序
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)
print("\n########################################\n")

# 生成式和生成器
f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
# import sys
# f = [x ** 2 for x in range(1, 1000)]
# print(sys.getsizeof(f))  # 查看对象占用内存的字节数
# print(f)
# # 请注意下面的代码创建的不是一个列表而是一个生成器对象
# # 通过生成器可以获取到数据但它不占用额外的空间存储数据
# # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
# f = (x ** 2 for x in range(1, 1000))
# print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
# print(f)
# for val in f:
#     print(val)

# 就是通过yield关键字将一个普通函数改造成生成器函数
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

def main():
    for val in fib(20):
        print(val)
main()
print("\n########################################\n")

# 创建和使用集合
# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 50) if num % 3 == 0 or num % 5 == 0}
print(set4)

# 向集合添加元素和从集合删除元素
set1.add(4)#set1 = 1，2，3
set1.add(5)
set2.update([11, 12])#set2 = 1-9
set2.discard(5) #删除set中的5，若没有5也不会报错
if 4 in set2:
    set2.remove(4) #删除set中的4，若没有4会报错，所以要用if
print(set1, set2)
print(set3.pop())
print(set3)
set5 = set('abc')
print(set5)#结果为随机位置的{'c', 'b', 'a'}
print("\n########################################\n")
# 集合的交集、并集、差集、对称差（反交集）运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2) #反交集
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))
print("\n########################################\n")

# 字典
# 创建字典的字面量语法
scores = {'罗昱': 95, '廖雪峰': 78, '吴恩达': 82}
print(scores)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)
# 通过键可以获取字典中对应的值
print(scores['罗昱'])
print(scores['廖雪峰'])
# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')
# 更新字典中的元素
scores['白元芳'] = 65
scores['诸葛王朗'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60))
# 删除字典中的元素
print(scores.popitem()) #随机删除列表中的一条数据，括号中无参数
print(scores.popitem())
print(scores.pop('罗昱', 100))
# 清空字典
scores.clear()
print(scores)
print("\n########################################\n")

# 在屏幕上显示跑马灯文字
import os
import time


# def paomadeng():
#     content = '北京欢迎你为你开天辟地…………'
#     while True:
#         # 清理屏幕上的输出
#         0 os.system('clear')
#         print(content)
#         # 休眠200毫秒
#         time.sleep(0.5)
#         content = content[1:] + content[0]
# paomadeng()
print("\n########################################\n")

# 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
import random
from random import randint
def Verification_Code(changdu):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars = ""
    for x in range(1,changdu+1):
        random_number = random.randint(0,61)
        chars += all_chars[random_number]
        # chars += all_chars[random.randint(0,61)]
    return chars

print(Verification_Code(int(input())))
print("\n########################################\n")

# 设计一个函数返回传入的列表中最大和第二大的元素的值。
op = [3, 8, 7, 8, 3, 9, 1, 9, 0, 2, 5, 8, 0, 9, 1, 1, 2, 1, 6, 0]
po = []
def fanhui():
    for i in range(len(op)):
        for j in range(len(op)):
            if op[i] - op[j] < 0:
                (op[i] , op[j]) = (op[j] , op[i])
    print(op)
    return op.pop(),op.pop()
print(fanhui())
print("\n########################################\n")

# 计算指定的年月日是这一年的第几天
year = int(input("请输入年: "))
month = int(input("请输入月: "))
day = int(input("请输入日: "))
calendar = [31,28,31,30,31,30,31,30,31,30,31,30]
calendar2 = [31,29,31,30,31,30,31,30,31,30,31,30]
def dijitian():
    allday = day
    # if month == 1:
    #     return day
    if year % 4 == 0:#闰年   
        for x in range(month-1):
            allday += calendar2[x]
    else:
        for x in range(month-1):
            allday += calendar[x]
    return allday
print(dijitian())
print("\n########################################\n")

# 约瑟夫环问题
allpeople = [True] * 30
def josephus():
    died,position,count = 0,0,0
    while died < 15:
        if allpeople[position]:
            count += 1
            if count == 9:
                allpeople[position] = False
                died += 1
                count = 0
        position += 1
        position %= 30
    # print(allpeople)
    for x in allpeople:
        print("基" if x else "非",end = " ")
josephus()