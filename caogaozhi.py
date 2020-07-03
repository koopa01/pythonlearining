import random
import turtle
import pygame



# def main():
#     persons = [True] * 30
#     counter, index, number = 0, 0, 0
#     while counter < 15:
#         if persons[index]:
#             number += 1
#             if number == 9:
#                 persons[index] = False
#                 counter += 1
#                 number = 0
#         index += 1
#         index %= 30
#     for person in persons:
#         print('基' if person else '非', end='')

# def main():
#     persons = [True] * 30
#     counter, index, number = 0, 0, 0
#     while counter < 15:
#         if persons[index]:
#             number += 1
#             if number == 9:
#                 persons[index] = False
#                 counter += 1
#                 number = 0
#         index += 1
#         index %= 30
#     for person in persons:
#         print('基' if person else '非', end=',')


# if __name__ == '__main__':
#     main()

# def countBits(n):
#     l = bin(n)
#     l = list(l)
#     print(l)
#     s = 0
#     for i in range(len(l)):
#         if l.pop() == '1':
#             s += 1
#     return s
# 
# def countBits(n):
#     return bin(n).count("1")
# 
# x = int(input())
# print(countBits(x))

# walk = ['n','n','n','s','n','s','n','s','n','s']
# def is_valid_walk(walk):
#     b = walk.count('n')
#     n = walk.count('s')
#     d = walk.count('e')
#     x = walk.count('w')
#     if b == n and d == x and len(walk) <= 10:
#         print('Ture')
#         return 'Ture'
#     else:
#         print('False')
#         return 'False'
# print(is_valid_walk(walk))

# names = ['Ana', 'John', 'Denise', 'Katy']
# grade = ['B', 'A+', 'A', 'A']
# course = [2.00, 6.0001, 20.002, 9.01]
# def get_grade(student, name_list, grade_list, course_list):
# 	i = name_list.index(student) 
# 	grade = grade_list[i]
# 	course = course_list[i]
# 	return (course, grade)
# print(get_grade(names , grade , course))

# grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}
# print(grades['John'])
# grades['Sylvan'] = 'A'  #添加项（标签label+值）
# 'John' in grades     #查询：返回True 
# 'Daniel' in grades   #查询：返回False
# del(grades['Ana'])   #删除项

# grades.keys() # returns ['Denise','Katy','John','Ana']，返回一组类似list的keys
# grades.values() # returns ['A', 'A', 'A+', 'B']。返回一组类似list的values

# # 检索歌词
# def lyrics_to_frequencies(lyrics):
# 	myDict = {}
# 	for word in lyrics:
# 		if word in myDict:
# 			myDict[word] += 1
# 		else:
# 			myDict[word] = 1
# 	return myDict
# def most_common_words(freqs):
# 	values = freqs.values()
# 	best = max(values)
# 	words = []
# 	for k in freqs:
# 		if freqs[k] == best:
# 			words.append(k)
# 	return (words, best)
# def words_often(freqs, minTimes):
# 	result = []
# 	done = False
# 	while not done:
# 		temp = most_common_words(freqs)
# 		if temp[1] >= minTimes:
# 			result.append(temp)
# 			for w in temp[0]:
# 				del(freqs[w])
# 			else:
# 				done = True
# 	return result
# print(words_often(beatles, 5))
# print(5+6*3/2)
# a=[1,3,5,6,7]                # 将序列a中的元素顺序打乱
# b = random.shuffle(a)
# print(b)
# a = [1,2]
# def b():
#     a.pop(0)
# b()
# print(a)
# turtle.pensize(10)
# turtle.pencolor('green')
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.mainloop()
