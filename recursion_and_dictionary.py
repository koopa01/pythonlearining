# 乘法：
def mult(a , b):
	if b == 1:
		return a
	else:
		return a + mult(a , b-1)
a = int(input())
b = int(input())
print(mult(a , b))

# 阶乘：
def factorial(a):
	if a == 1:
		return 1
	else:
		return a * factorial(a-1)
# a = int(input())
# print(factorial(a))
print(factorial(int(input())))

# TOWERS OF HANOI:
def printMove(fr, to): 
	print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare): 
	if n == 1:
		printMove(fr, to) 
	else:
		Towers(n-1, fr, spare, to)
		Towers(1, fr, to, spare)
		Towers(n-1, spare, to, fr)

# 斐波那契数列
