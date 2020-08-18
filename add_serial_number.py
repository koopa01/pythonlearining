obj = open('day4.py', mode='r', encoding='utf-8')
data = obj.readlines()  # 1个字符
obj.close()
print(data)

file = open('day04.py', mode='a', encoding='utf-8')
counter = 1
for i in data:
    if '\u4e00' <= i[0] <= '\u9fff':
        file.write('# '+str(counter)+'.'+i)
        counter += 1
    else:
        file.write(i)
file.close()
