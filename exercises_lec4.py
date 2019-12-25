# def even_num(i):
# 	"""
# 	input: i, a positive int
# 	returns true if i is even
# 	"""
# 	print("this number is ")
# 	remainder == i % 2
# 	return remainder == 0
# even_num(input)

#10个数中显示奇偶
def even(i):
	return i % 2 == 0

for i in range(1,11):
	if even(i):
		print("偶数", i)
	else:
		print("基数", i)


