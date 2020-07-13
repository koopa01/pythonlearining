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

# 第七章 各个模块
import datetime,time

print(datetime.date.today())    # 获取今天日期
print(datetime.date.today().strftime('%Y-%m-%d %H:%M:%S'))    # 格式化字符串输出
print(datetime.datetime.now())    # 获取今天日期
d = datetime.datetime.now()
print(d.isoformat())    # 标准格式，固定宽度
print(d.timetuple())    # 将日期转化为时间戳，struct_time格式，用元组表示时间的各个数值
print(time.mktime(d.timetuple()))    # 返回用秒数表示时间的浮点数
print(datetime.date.fromtimestamp(time.mktime(d.timetuple())))    # 将时间戳转换为日期

yesterday = d - datetime.timedelta(days = 1)    # 时间运算（相减）
print(yesterday)
hours = d - datetime.timedelta(hours = -1)
print(hours)

import calendar

print(calendar.month(2020,7))   # 返回该月日历的多行字符串
calendar.prmonth(2020,7)    # 相当于print(calendar.month(2020,7))
print(calendar.calendar(2020))    # 返回一年日历
calendar.prcal(2020)
print(calendar.monthcalendar(2020,7))   # 返回某一年的某一个月份日历，是一个嵌套列表——最里层列表7个元素表示周一到周日，没有本月的日期为0
print(calendar.isleap(2020))    # 是否闰年，返回True/False
print(calendar.monthrange(2020,7))  # 返回元组(这个月从周几开始，这个月有多少天)，周几从0开始表示周一
print(calendar.weekday(2020,7,13))   # 返回这天是周几

import time

print(time.time())  # 精准机器时间(时间戳)，用作计时，t1 = time.time), t2 = time.time, print(t2 - t1)
print(time.ctime())     # 字符串表示的当前时间

t = (2020,7,13,10,49,12,0,0,0)
print(time.asctime(t))     # 将元组转化为日期，不加参数为返回当前时间
# struct_time类，继承自c语言中的struct类
print(time.localtime())
# 输出：time.struct_time(tm_year=2020, tm_mon=7, tm_mday=13, tm_hour=10, tm_min=52, tm_sec=19, tm_wday=0, tm_yday=195, tm_isdst=0)
t = time.localtime()
year = t[0]
print(year)
# 用例
for x in range(3):
    print(x)
    t1 = time.time()
    time.sleep(1)
    t2 = time.time()
    print(t2 - t1)