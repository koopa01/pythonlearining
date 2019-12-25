##############################################################
#  # 10个数中显示奇偶
# print("1-10所有数的奇偶")
# def even(i):
# 	return i % 2 == 0

# for i in range(1,11):
# 	if even(i):
# 		print(i, "偶数")
# 	else:
# 		print(i, "基数")

##############################################################

# #返回值的作用
# def func_a():
#     print("aaa")

# def func_b(y):
#     print("bbb")
#     return y

# def func_c(z):
#     print("ccc")
#     return z()

# print(func_a())             #调用func_a，打印aaa，无返回值，打印none
# print(5+func_b(2))			#调用func_b，打印bbb，返回2，打印7
# print(func_c(func_a))		#调用func_c，打印ccc，调用func_a，打印aaa，无返回值，z=none，打印none

##############################################################

# #函数可以嵌套
# def f():
#     def x(a, b):
#         return a+b
#     return x
    
# # the first part, f(), returns a function object
# # then apply that function with parameters 3 and 4
# val = f()(3,4)
# print(val)

##############################################################

#写一个100以内猜数字的游戏 —— 人生成，机器猜

# x = input(print("what's your name"))
# print("welcome to play number guess",x)

# def higher(i):
# 	i = i + i/2
# 	return i

# def lower(i):
# 	i = i - i/2
# 	return i

# i = 50
# p = ["higher","lower","bingo"]
# print("think of a number in 1 to 100")
# j = input(print("Is this number higher or lower?", i))

# if j == "bingo":
# 	print("thank you for playing!")

# if j == "higher":
# 	i = higher(i)
# elif j == "lower":
# 	i = lower(i)

# else:
# 	print("please insert higher or lower or bingo")
# print("Is this number higher or lower?", i)

# print("")

##############################################################
# #猜数字 —— 机器生成，人猜
# import random						# 导入 random(随机数) 模块
# i = random.randint(0,100)			#使用了 random 模块的 randint() 函数生成随机数
# name_user = input("What's your name")
# print("Welcome to play number guess", name_user)

# for x in range(7):
# 	j = int(input("please guess what number it is"))
# 	if j == i:
# 		print("bingo")
# 		break
# 	elif j > i:
# 		print("higher")
# 	else :
# 		print("lower")

##############################################################
# #猜数字 —— 机器生成，人猜V2
import random						# 导入 random(随机数) 模块
i = random.randint(0,10)			#使用了 random 模块的 randint() 函数生成随机数
name_user = input("Welcome to play number guess, what's your name: ")
print(name_user ,"please guess a number in 0-100: ")

for x in range(7):
	j = int(input())
	if j>100 or j<0:								#嵌套判定输入范围
		print("please insert a number in 0 - 100")
	else:
		if j == i:
			print("bingo, you win")
			break
		elif j > i:
			print("higher")
		else :
			print("lower")
 # 以后版本其他功能：结束重启，奖励界面
 # if i == j:
 # 	t = input("play again? press "y" end press anyother key)
 # 		if t == "y":
 # 			pass
