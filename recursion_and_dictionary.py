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

# 斐波那契数列求和
def fib(x):
	"""
	assumes x an int >= 0
	returns Fibonacci of x
	"""
	if x == 0 or x == 1:
		return 1 
	else:
		return fib(x-1) + fib(x-2)

print(fib(int(input())))

# 回文
def isPalindrome(s): 
	def toChars(s):
		s = s.lower()
		ans = ''
		for c in s:
			if c in 'abcdefghijklmnopqrstuvwxyz':
				ans = ans + c
				return ans 
		def isPal(s):
			if len(s) <= 1:
				return True
			else:
				return s[0] == s[-1] and isPal(s[1:-1]) 
	return isPal(toChars(s))
# def isPalindrome():
# 	pal = "blewasiereisawleb"
# 	pal = list(pal.lower())
# 	i = 0
# 	if len(pal) <= 1 and True:
# 		return True
# 	elif pal[i] == pal[-i-1]:
# 		isPalindrome(i+1)
# 	else:
# 		return False
# print(isPalindrome())

# 字典 dicrionaries
# names = ['Ana', 'John', 'Denise', 'Katy']
# grade = ['B', 'A+', 'A', 'A']
# course = [2.00, 6.0001, 20.002, 9.01]
# def get_grade(student, name_list, grade_list, course_list):
# 	i = name_list.index(student) 
# 	grade = grade_list[i]
# 	course = course_list[i]
# 	return (course, grade)
grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}
print(grades['John'])
grades['Sylvan'] = 'A'  #添加项（标签label+值）
'John' in grades     #查询：返回True 
'Daniel' in grades   #查询：返回False
del(grades['Ana'])   #删除项

grades.keys() # returns ['Denise','Katy','John','Ana']，返回一组类似list的keys
grades.values() # returns ['A', 'A', 'A+', 'B']。返回一组类似list的values

# 检索歌词
def lyrics_to_frequencies(lyrics):
	myDict = {}
	for word in lyrics:
		if word in myDict:
			myDict[word] += 1
		else:
			myDict[word] = 1
	return myDict
def most_common_words(freqs):
	values = freqs.values()
	best = max(values)
	words = []
	for k in freqs:
		if freqs[k] == best:
			words.append(k)
	return (words, best)
def words_often(freqs, minTimes):
	result = []
	done = False
	while not done:
		temp = most_common_words(freqs)
		if temp[1] >= minTimes:
			result.append(temp)
			for w in temp[0]:
				del(freqs[w])
			else:
				done = True
	return result
print(words_often(beatles, 5))