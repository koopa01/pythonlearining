# 输入某年某月某日，判断这一天是这一年的第几天
import datetime

dtstr = input('Enther the datatime: (20170228):')
dt = datetime.datetime.strptime(dtstr, '%Y%m%d')
another_dtstr = dtstr[:4] + '0101'
another_dt = datetime.datetime.strptime(another_dtstr, '%Y%m%d')
print(int((dt - another_dt).days) + 1)

# 输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数
import string

s = input('input a string:')
letter = 0
space = 0
digit = 0
other = 0
for c in s:
    if c.isalpha():
        letter += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        other += 1
print('There are %d letters,%d spaces,%d digits and %d other\
    characters in your string' %(letter, space, digit, other))

# 归并排序
import random

def merge_sort(data_list):
    if len(data_list) <= 1:
        return data_list
    middle = int(len(data_list) / 2)
    left = merge_sort(data_list[:middle])
    right = merge_sort(data_list[middle:])
    merged = []
    while left and right:
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    merged.extend(right if right else left)
    return merged

data_list = [random.randint(1,100) for _ in range(50)]
print(merge_sort(data_list))

# 猜数字

# 第三章 作业
# 1.字符串循环左移
s=str(input())
n=int(input())
temp_list = list(s)
for _ in range(n):
    temp_str = temp_list.pop(0)
    temp_list.append(temp_str)

print(''.join(temp_list))

# 2.输入直角三角形两直角边a,b的值，输出斜边上的高
import math
a=int(input())
b=int(input())
print(math.sqrt(a**2 + b**2))

# 3.计算字符串最后一个单词的长度，单词以空格隔开。
s=str(input())
word_long = s.split(' ')[-1]
print(len(word_long))

# 4.接受一个由字母和数字组成的字符串，和一个字符，然后输出输入的字符串中含有该字符的个数。不区分大小写。
s=str(input())
s = s.split(' ')
target_strs = list(s[0])
target_str = s[1]
temp_add = 0
for _ in range(len(target_strs)):
    if target_str == target_strs[_]:
        temp_add += 1
print(temp_add)

# 5.给出两个整数，输出他们的和
n1=int(input())
n2=int(input())
print(n+n2)

# 6.给出一个圆的半径，求出圆的周长和面积
n=int(input())
print("%.4f,%.4f" % (2*n*3.14159, n**2*3.14159))

# 7.由三角形的三边长，求其面积。
a = int(input())
b = int(input())
c = int(input())
p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print('%.2f'%s)

# 8.给出一个等差数列的前两项a1，a2，求第n项是多少
a=int(input())
b=int(input())
n=int(input())
c = b - a
print(a+c*(n-1))

# 第四章 作业
# 1.输入两个列表alist和blist，要求列表中的每个元素都为正整数且不超过10；
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
print(sorted(list(set(alist+blist))))

# 2.输入一个列表，要求列表中的每个元素都为正整数且列表包含的元素个数为偶数；
#   将列表中前一半元素保存至字典的第一个键值1中，后一半元素保存至第二个键值2中。
alist=list(map(int,input().split()))
# front = []
# for _ in range(len(alist)/2):
#     front.append(alist.pop(0))
# d1 = {}
# d1[1] = front
# d1[2] = alist
# print(d1)
print({1:alist[:half_length:],2:alist[half_length::]})

# 3.输入一个列表，将其反转后输出新的列表。
alist=list(map(int,input().split()))
print(alist[::-1])

# 4.将列表中的所有元素按照它们的绝对值大小进行排序，绝对值相同的还保持原来的相对位置，
#   打印排序后的列表（绝对值大小仅作为排序依据，打印出的列表中元素仍为原列表中的元素）。
alist=list(map(int,input().split()))
# blist,clist = alist[::],[]
# for _ in range(len(alist)):
#     blist.append(abs(blist.pop(0)))
# blist.sort()
# for _ in range(len(alist)):
#     if blist[0] in alist:
#         clist.append(blist.pop(0))
#     else:
#         clist.append(0-blist.pop(0))
# # print(alist,blist,clist)
# print(clist)
print(sorted(alist, key=abs))


# 第五章 作业
# 1.输入一个正整数max，输出100到max之间的所有水仙花数（包括max）。水仙花数是指一个n位数 (n≥3)，它的每个位上的数字的n次幂之和等于它本身。
max_num = int(input())
for x in range(100,max_num+1):
    s = 0
    nums = list(str(x))
    n = len(nums)
    for _ in range(n):
        nums[_] = int(nums[_])
    for _ in range(n):
        s += nums[_]**n
    if s == x:
        print(s)

# 2.输入两个字符串，输出两个字符串集合的并集。
s1 = input()
s2 = input()
print(sorted(set(list(s1)+list(s2))))

# 3.给定一个正整数n（n<1000），求所有小于等于n的与7无关的正整数的平方和。
#   如果一个正整数，它能被7整除或者它的十进制表示法中某个位数上的数字为7，则称之为与7相关的数。
def isseven(n):
    m = str(n)
    if '7' in m:
        return 0
    elif n % 7 == 0:
        return 0
    else:
        return 1
n,s = int(input()),0
for _ in range(n + 1):
    if isseven(_):
        s += _**2
        # print(_)
print(s)

# 4.输入一个正整数n（n<1000），输出1到n之间的所有完数（包括n）。
def perfectnum(n):
    factor_sum = 0
    for _ in range(1,n//2+1):
        if n % _ == 0:
            factor_sum += _
    if factor_sum == n:
        return 1
    else:
        return 0
n = int(input())
for x in range(1,n):
    if perfectnum(x):
        print(x)

# 5.打印一个n层（1<n<20）金字塔，金字塔由“+”构成，塔尖是1个“+”，下一层是3个“+”，居中排列，以此类推。
level = int(input())
for x in range(1,level+1):
    print((level-x)*' ' + (2*x - 1)*'+' + (level-x)*' ')

# 6.给一个5位数，判断它是不是回文数，是则输出yes，不是则输出no。
n = int(input())
m = list(str(n))
if m[0] == m[4] and m[1] == m[3]:
    print('yes')
else:
    print('no')

# 7.将列表中的奇数变为它的平方，偶数除以2后打印新的列表（新的列表中所有元素仍都为整数）。
alist=list(map(int,input().split()))
for _ in range(len(alist)):
    if alist[_] & 1 == 1:
        alist[_] = alist[_] ** 2
    else:
        alist[_] = alist[_] // 2
print(sorted(alist))

# 8.给定一个大于2的正整数n，打印出小于n（不包括n且n不大于100）的所有素数。
n,result = int(input()),[]
def isprime(num):
    for _ in range(2, num // 2 + 1):
        if num % _ == 0:
            return 0
    return 1
for i in range(2, n):
    if isprime(i):
        result.append(i)
print(result)

# 9.猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
#   以后每天早上都吃了前一天剩下的一半零一个。到第n天（<1<n<11）早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
# def eat(num):
#     for day in range(9,0,-1):
#         num = (num + 1) * 2
#         print(num,"第%d天\n" % day)
#     return num
# print("第一天",eat(1))
n, r = int(input()), 1
for x in range(n - 1):
    r = (r + 1) * 2
print(r)

# 第六章 作业
# 1.已知斐波拉契数列的前两项都是1，我们定义求斐波拉契数列的第n项（n<=50）的函数为fbnq
def fbnq(n):
    l1 = [1,1]
    for x in range(n-2):
        l1.append(l1[x]+l1[x+1])
    return l1.pop()
n=int(input(""))
print(fbnq(n))

# 2.输入两个正整数num1和num2（不超过1000），求它们的最大公约数并输出。
def hcf(n1,n2):
    result = []
    for x in range(1,(n1+n2)//2+1):
        if n1%x==0 and n2%x==0:
            result.append(x)
    return sorted(result).pop()
num1=int(input(""))
num2=int(input(""))
print(hcf(num1,num2))

# 3.输入两个正整数num1和num2（不超过500），求它们的最小公倍数并输出。
def lcm(n1,n2):
    if n2 > n1:
        (n1,n2) = (n2,n1)
    for x in range(n2,n2*n1+1):
        if x%n2==0 and x%n1==0:
            return x
num1,num2=int(input("")),int(input(""))
print(lcm(num1,num2))

# 4.求n（n为正整数且n<=20）的阶乘的函数为fact
def fact(n):
    s = 1
    for x in range(1,n+1):
        s *= x
    return s
n=int(input(""))
print(fact(n))

# 5.已知输入为一个列表，列表中的元素都为整数，我们定义冒泡排序函数为bubbleSort，将列表中的元素按从小到大进行排序后得到一个新的列表并输出
def bubbleSort(alist):
    for x in range(len(alist)):
        for y in range(len(alist)):
            if alist[x] < alist[y]:
                temp = alist[x]
                alist[x] = alist[y]
                alist[y] = temp
    return alist
alist=list(map(int,input().split()))
print(bubbleSort(alist))

# 6.输入为一个列表，列表中的元素都为整数，我们定义元素筛选函数为foo，
# 功能是检查获取传入列表对象的所有奇数位索引（注意列表的索引是从0开始的）对应的元素，并将其作为新列表返回给调用者。
def foo(alist):
    return alist[1::2]
alist=list(map(int,input().split()))
print(foo(alist))

# 第七章 作业
# 1.给定年月日，如2019/1/8，打印输出这一天是该年的第几天。
import time

day = input()
f = time.strptime(day, '%Y/%m/%d')
print(f.tm_yday)

# from datetime import *

# d=input()
# d1=datetime.strptime(d[:4]+'/1/1','%Y/%m/%d')
# print(d1)
# d2=datetime.strptime(d,'%Y/%m/%d')
# print(d2)
# print((d2-d1).days+1)
# 要将输入的格式转换成计算机能识别的格式，time.strptime()。tm_yday可以直接得出是今年的第几天。
# strptime和strftime傻傻分不清楚，strftime是 str-format-time, 时间字符串格式化，即我们看到的格式；
# strptime是str-parse-time，时间字符串语法化，即计算机理解的格式

# 2.接受一个正整数输入x，打印上述公式的输出值。
from math import *

x=int(input())
y=sin(15/180*pi)+(e**x-5*x)/sqrt(x**2+1)-log(3*x)
print(round(y,10))

# 3.一个特殊的正整数，它加上150后是一个完全平方数，再加上136又是一个完全平方数，求符合条件的最小的一个数。
n=1
while True:
    if int((n+150)**0.5)**2 == (n+150) and int((n+150+136)**0.5)**2 == (n+150+136):
        print(n)
        break
    n=n+1