'''
python生成式、推导式
运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。

格式
[x for x in 内容]
[x for x in 内容 if 条件]
[expression for item in iterable if condition]

{key_expression : value_expression for expression in iterable}

{expression for expression in iterable}


1：要把生成的元素x放到前面，执行的时候，先执行后面的for循环
2：后面跟上for循环 可以有多个for循环，也可以在for循环后面加个if条件
3：for循环后面可以是任何方式的迭代器(元组，列表，生成器。。)只要可以迭代的对象中有一个值。

'''

# 一、列表推导式

# 字符串生成列表
print([x for x in 'abcd'])#['a', 'b', 'c', 'd']
# 列表生成列表
print([x for x in range(10)] )#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 列表生成列表 if条件
print([x for x in range(10) if x > 5] )#[6, 7, 8, 9]
# 双循环列表生成式
print( [m + n for m in 'ABC' for n in 'XYZ'])#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
# 两个元组中各取一个元素生成的元组的列表
a=(1,2);b=(3,4)
a_b=[(na,nb) for na in a for nb in b]# [(1, 3), (1, 4), (2, 3), (2, 4)]

# 二、字典推导式

# 字符串中字符为键，出现次数为值
s='letters'
d={letter : s.count(letter) for letter in set(s)}# {'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}

# 三、集合推导式
# 1-20 能被3整除的数的集合
m_set={x for x in range(1,21) if x%3==0}#{3, 6, 9, 12, 15, 18}

# 四、生成器推导式
# 将列表推导式中的方括号换成圆括号就是生成器推导式，不是元组推导式，元组是没有推导式的。生成器推导式返回的是一个生成器对象。
number_thing=(number for number in range(1,11))
number_thing # <generator object <genexpr> at 0x00000287D48DFFC0>
type(number_thing) # <class 'generator'>
number_list = list(number_thing) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
try_again = list(number_thing) # [] 注意：生成器推导式只能迭代一次，再次迭代时会发现已经被擦除

