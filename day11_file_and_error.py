'''
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise OSError upon failure.

    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)

    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:

    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists

需要在使用open函数时指定好带路径的文件名（可以使用相对路径或绝对路径）并将文件模式设置为'r'（如果不指定，默认值也是'r'）
然后通过encoding参数指定编码（如果不指定，默认值是None，那么在读取文件时使用的是操作系统默认的编码）
'''

# Python的异常机制

def main():
    f = None
    try:
        f = open('C:\\Users\\Koopa\\Desktop\\tuples_and_list.py', 'r', encoding='utf-8')#路径上的'\'需要转义成'\\'
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()

# 可以将那些在运行时可能会出现状况的代码放在try代码块中，在try代码块的后面可以跟上一个或多个except来捕获可能出现的异常状况
# 我们通常把finally块称为“总是执行代码块”，用来做释放外部资源的操作
#多次输入直到输入正确为止
while True:
    try:
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        print(num1/num2)
        break#跳出while循环
    except ValueError as ve:
        print('Please insert a digit!')
        print(ve)
    except ZeroDivisionError as ze:
        print('The second number cannot be zero')
        print(ze)
###################可选项########################
    else:#如果没有异常（输入正确）就打印本句话
        print('Aja,everything is OK')
    finally:#不管是否发生异常，都执行
        print('It is a finally clause.')

# 如果不愿意在finally代码块中关闭文件对象释放资源，也可以使用上下文语法，
# 通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源

import time
# 上下文管理器————实现异常处理和关闭
# try:
#     f = open('data.txt')
#     for line in f:
#         print(line,end = '')
# except IOError:
#     print('Cannot open the file')
# finally:
#     f.close()#关闭文件
with open('C:\\Users\\Koopa\\Desktop\\tuples_and_list.py',encoding='utf-8') as f:#打开当前目录下的data文件，并把文件变量赋给f
    for line in f:#将文件内容逐行输出
        print(line,end = '')
        # time.sleep(0.5)
#文件操作最好用with语句

# 将1-9999之间的素数分别写入三个文件中（1-99之间的素数保存在a.txt中，100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）
from math import sqrt

def is_prime(num):
    for factor in range(2,int(sqrt(num))+1):
        if num % factor == 0:
            return False
    return True if num != 1 else False


def main():
    filenames = ['a.txt','b.txt','c.txt']
    fs_list = []
    try:
        for filenames in filenames:
            fs_list.append(open(filenames,'w',encoding='utf-8'))
        for x in range(1,10000):
            if is_prime(x):
                if x<100:
                    fs_list[0].write(str(x)+'\n')
                elif 100<=x<1000:
                    fs_list[1].write(str(x)+'\n')
                else :
                    fs_list[2].write(str(x)+'\n')
    except IOError as IO:
        print('io错误',IO)
    finally:
        for x in fs_list:
            x.close()
        print('完事')



if __name__ == '__main__':
    main()

# 读写二进制文件可以实现复制图片文件的功能
def main():
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('吉多.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')


if __name__ == '__main__':
    main()

# 读写JSON文件，JSON是“JavaScript Object Notation”的缩写