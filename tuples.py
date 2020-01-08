# tuple核心意义在于函数中可以返回多个不同类型的对象
t_1 = ()
t = (5.1,10,"koopa")
print(t[2])
t += (2,4)
print(t)
print(len(t))


# slice切片
print(t[1:2])
# 输出为“10，”其中“，”代表这是一个元组中的对象
# 其本质是输出部分类别是元组,而不是字符串


# swap交换赋值,在c语言中
# temp = a
# b = a
# b = temp
# 在python中
a = 2
b = 3
(a , b) = (b , a)
# print((a,b))


# 计算x除以y的时候的商和余数
def quotient_and_remainder(x,y):
	q = x // y
	r = x % y
	return (q , r)
# print(int(input(quotient_and_remainder(x , y)))
x = int(input())
y = int(input())
print(quotient_and_remainder(x , y))

############################################################
# list列表: 其中元素可变的元组
a_list = []
L = [1 , 'v' , 2 , [3,4] , (5,6)]

print(L[-2]+["7","8"])
L[2] = 9
print(L , L[0] + 1)
L.append(10) #.append只能用在列表对象中
print(L)
# 注意attention:append有副作用
warm = ['hot','cold','good']
chill = warm
chill.append('cool')
print(warm)
print(chill)
# warm和chill中的元素一样，是因为warmlist在内存中，chill只是warm的别名（alias）
# 若需要原list不变的同时改变复制后的list
chill = warm[0:0]
chill = warm[:] #创建新list，并clone素有元素

############################################################
# 对于list的增删改查
L.extend([11,12]) #在本list中增加元素
del(L[0])   #删除特定元素
print(L.pop())     #删除list中最后一个元素,并return它
L.remove(9) #查找list中特定的元素,并删除查找到的第一个特定元素,没找到会报error
print(L)

############################################################
# 将string转化为list
s = "koopa-L niu bi! 233" #s是字符串

list(s) #s转化为list,每个字母包括空格为list中的一个元素
print(list(s))
s.split(' ') #以"空格"为界限分离元素
print(s.split(' '))

############################################################
# 将list转化为spring
s_0 = ["k","o","o","p","a"]

"".join(s_0)  #加入list中的每个元素,并在list中的每个元素之间添加""
print("".join(s_0))
"_".join(s_0) #在list中的每个元素之间添加"_"
print("_".join(s_0))
print(s_0)

############################################################
# 将list排序(sort,reverse)
L_0 = [8 , 3 , 7 , 5 , 6 , 4]

sorted(L_0)   #return排序后的list，不改变L_0本身
L_0.sort()    #将L_0转变成排序后的list，升序
L_0.reverse() #将L_0转变成排序后的list，降序
# .sort和sorted()区别
biaoge = [3,1,2]
sortedbiaoge = biaoge.sort()
print(biaoge)
print(sortedbiaoge)
# 输出被改变了的biaoge，原list在内存中被改变了
# .sort return的是none
gebiao = [6,4,5]
sortedgebiao = sorted(gebiao)
print(gebiao)
print(sortedgebiao)
# 输出没有改变gebiao，原list爱内存中还在
# sorted()必须赋值才能用，return的是被排序后的list
