# 第七章 各个模块
# 1.datetime模块
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

# 2.calendar模块
import calendar

print(calendar.month(2020,7))   # 返回该月日历的多行字符串
calendar.prmonth(2020,7)        # 相当于print(calendar.month(2020,7))
print(calendar.calendar(2020))  # 返回一年日历
calendar.prcal(2020)
print(calendar.monthcalendar(2020,7))   # 返回某一年的某一个月份日历，是一个嵌套列表——最里层列表7个元素表示周一到周日，没有本月的日期为0
print(calendar.isleap(2020))    # 是否闰年，返回True/False
print(calendar.monthrange(2020,7))   # 返回元组(这个月从周几开始，这个月有多少天)，周几从0开始表示周一
print(calendar.weekday(2020,7,13))   # 返回这天是周几

# 3.time模块
import time

print(time.time())      # 精准机器时间(时间戳)，用作计时，t1 = time.time), t2 = time.time, print(t2 - t1)
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

# 4.算术模块
import math     # 浮点数运算

math.sin()
math.cos()
math.tan()
math.pi
math.log(x,a)   # 以a为底的x的对数
math.pow(x,y)   # x的y次方

import cmath    #复数运算

cmath.polar()   # 极坐标
cmath.rect()    # 笛卡尔坐标
cmath.exp(x)    # e的x次方
cmath.log(x,a)  # 以a为底的x的对数
cmath.log10(x)  # 以10为底的x的对数
cmath.sqrt(x)   # x的平方根

from decimal import Decimal     # 由于计算机内部把浮点数用10进制转化为2进制之后会有误差，可以用其生成小数-固定精度的浮点值

Decimal('0.1')
print(0.1 + 0.1 + 0.1 - 0.3)    # 输出一个极小的数但不为0
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))    # 输出为0.0

from fractions import Fraction    # 分数模块，实现有理数对象

Fraction(1,4) / Fraction('0.25')
Fraction.from_float(1.75)   # 浮点数转化为分数，会有精度损失，因为其最初的浮点形式就不精确，如1.3，二进制数为无理数，则转化为浮点数不精确

import random   # 伪随机数，按算法模拟产生，结果可预见

random.seed(a = None)   # 随机数种子，即随机序列
random.random()         # 生成[0.1)之间的随机实数
random.uniform()        # 生成指定范围内的随机浮点数
random.randint(m,n)     # 生成[m,n]内的整数
random.randrange(a,b,n) # 在[a,b)内按n递增的集合中随机选一个整数
random.getrandbits(k)   # 生成k位二进制随机整数
colors = ['red', 'green', 'blue', 'orange', 'black']
print(random.choice(colors))    # 在列表或元组中随机取一个元素
print(random.sample(colors,2))  # 随机取指定个数元素，无重复元素
random.shuffle(colors)          # 必须用在可变序列如列表，不可用在元组
print(colors)

# 5.持久化模块
# 类创建的对象不是真正的数据库记录，其存储在内存中，是临时性对象
import pickle   # 对象格式化、解格式化，保存到文件里

import dbm      # 通过key访问的文件系统，存储字节串

import shelve
# 按照key把pickle处理后的对象存储到一个外部存储文件（容器）中
# 构造一个简单的数据库，像操作字典一样按照key存储和获取本地python对象，使其持久化
# key必须是字符串，且唯一，value任意
# 必须先打开shelve，修改后需关闭
d = shelve.open(filename)   # open函数调用时返回shelf对象，可通过该对象存储内容
d[key] = data
data = d[key]
value = d[key]
del d[key]
d.close()

# 6.文本读写
# 1.纯文本文件txt
f = open(filename[,mode[,buffering]])
# mode为可选参数，打开模式和文件类型
# buffering为可选参数，文件的缓冲区，默认-1
# r 读，w 写，x 文件不存在情况下新创建并写文件，a 文件末尾追加写内容，+ 读写
# t 文本类型，b 二进制文件
f = open('my.txt','w')
f.writelines(['apple\n', 'pie\n'])  # 写入字符串列表/f.write(str)写入所有行
f.close()
f = open('my.txt','r')
f.readlines()   # 返回所有行、列表/f.readline()返回一行/f.read()读全部
f.close()
# 文件关闭的作用时终止对外部文件的链接，同时将缓冲区（内存中）的数据刷新到硬盘上

# 为确保退出后自动关闭文件，使用上下文管理器
with open('textfile','rt') as myfile:
    myfile.read()

# 2.结构化文本文件：CSV(comma,sperated,value) —— 以逗号分隔的纯文本文件(都是字符串)
import csv
# 文件读取
re = csv.reader()       # 返回生成器，通过迭代每行输出
re = csv.DictReader()   # 带表头的读取方式，返回的每一个单元格都放在一个元组的值内

w = csv.writer()        # 当文件不存在，自动生成，支持单行、多行写入
w.wirterow(rows)

w = csv.DictWriter()    # 字典数据写入
w.writeheader()         # 写表头
w.writerow(rows)        # 字典的key对应标题，value写入csv文件

from opendpyxl import workbook    # pip install openpyxl
# 用来读写拓展名为xlsx/xlsm/xltx/xltm的文件，
# workbook类时对工作簿的抽象，worksheet类是对表格的抽象，cell类是对单元格的抽象文件写操作
wb = Workbook()     # 创建一个workbook对象代表一个excel文档
ws = wb.active      # 引用当前唯一的worksheet

from opendpyxl import load_workbook
wb = load_workbook(filename)    # 加载进来变成wb对象
ws = wb.file.active             # 提取当前工作表

c = wb['sheet']['A1']           # 获取单元格信息(cell对象)，通过wb索引取到工作表sheet，再用A1坐标引用
c = wb['sheet'].cell(row = 1, cloumn = 1)   # 同上，写清坐标
c.coordinate    # 返回单元格坐标
c.value         # 返回单元格的值
c.rows          # 返回单元格所在行坐标
c.cloumn        # 返回单元格所在列坐标

# 3.结构化文本文件：PDF
import PyPDF2
# PdfFileReader/PdfFileWriter 读写，PdfFileMerger 合并/分割，PageObject 文件转换
# 只能提取文本返回字符串，无法提取图、表等
readFile = open('test.pdf','rb')    # 读取pdf文件。先打开对象，再用reader读取对象
pdfFileReader = PdfFileReader(readFile)
pdfFileReader.getNumPages()         # 计算PDF文件总页数
pdfFileReader.getPage(index)        # 检索指定编号的页面

writeFile = 'output.pdf'            # 写对象
pdfFileWriter = PdfFileWriter()
PdfFileWriter.addPage(pageObj)      # 根据每页返回的PageObject写入到文件
PdfFileWriter.addBlankPage()        # 在最后一页后面写入空白页，保存到新文件

pdf_merger = PdfFileMerger()        # 生成merger对象
pdf_merger.append('python2018.pdf') # 添加文档
pdf_merger.merge(20,'insert.pdf')   # 从索引开始，把另一个pdf文件添加进去
pdf_merger.write('merge.pdf')       # 最后把merger包含的所有pdf文件合在一起，输出新的pdf文件
pdf_merger.extractText()            # 按照顺序提取文本
pdf_merger.getContents()            # 访问页面内容，包括页面中每个文本分区
pdf_merger.rotateClockWise(angle)   # 顺时针旋转
pdf_merger.scale(sx,sy)             # 改变页面大小