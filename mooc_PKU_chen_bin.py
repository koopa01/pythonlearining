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