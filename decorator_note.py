# 闭包:通过函数的嵌套，把值保留起来，以后方便的时候调用(封装值 + 内层函数需要使用)
# django缓存 -- 用装饰器实现数据存活多久(多少秒) / 被装饰的函数要执行多少次
# 需要补充的内容： 元数据、多个装饰器

def func(arg):
    def inner():
        print("before")
        v = arg()
        print("after")
        return v
    return inner

def index():
    print(123)
    return 666

# 这两步可以转化为装饰器
# 意义:在不改变index函数内部代码的前提下，可在index函数之前或之后加自定义功能/操作，即为装饰。
index = func(index)
index() # func(index)() --> 执行before，index函数，after，返回index函数的返回值666
# 现在的index函数变成了func(index)函数，但是func(index)中的inner函数依然执行的是最开始的index()函数

# 第一步：执行func函数并将下面的函数作为参数传递，相当于func(index)
# 第二部：将fucn的返回值重新赋值给下面的函数名。index = func(index)
@func 
def index():
    print(123)
    return 666

##################################################
# 例子：用装饰器输出函数所执行时间
import time

def wrapper(func):
    def inner2():
        start_time = time.time()
        v = func()
        end_time = time.time()
        print(end_time - start_time)
        return v
    return inner2
    
@wrapper
def func1():
    time.sleep(1)
    print("11111111111111")

@wrapper
def func2():
    time.sleep(2)
    print("22222222222222")

@wrapper
def func3():
    time.sleep(3)
    print("33333333333333")

func1()
func2()
# 现在调用func1()相当于调用的是inner2函数，在inner2函数中继续调用func1函数，即先inner2.后func1

# 装饰器就是通过变化全局变量和装饰器函数功能来实现在目标函数前后添加自定义功能的函数。
# 应用场景：想为函数拓展功能，又不能改变所有工程文件时，选用装饰器。

'''
装饰器标准格式：
def 外层函数(参数):
    def 内层函数(*args,**kwargs):
        return 参数(*args,**kwargs)
    return 内层函数

装饰器应用格式：
@外层函数
def index():
    pass
index()
'''

# 需要提前考虑被装饰的函数的参数，即为 *args,**kwargs
# *args 用来将参数打包成tuple给函数体调用
# **kwargs 打包关键字参数成dict给函数体调用

# 带参数的装饰器 -- 相当于在原装饰器外又套了另一个带有参数的外部函数，而且该参数为整个装饰器中的全局变量。
# 第一步：执行 x(9),拿到返回值
# 第二步：@x --> inner = x(9)(index)
# 第三步：index = x(9)(index)
def x(counter):
    print('x函数')
    def wrapper2(func):
        print('wrapper函数')
        def inner3(*args,**kwargs):
            print('inner')
            v = []
            for i in range(counter):
                data = func(*args,**kwargs)
                v.append(data)
            return data

        return inner3
    return wrapper2

@x(9)
def index():
    print("装饰器输出参数次")
    return 1 # return的是1，inner里list就有装饰器参数个1

index()


# 生成器的坑
p = [99 if i >5 else 66 for i in range(10)]
print(p)
a = [lambda x:x*i for i in range(10)]
# 如果生成的是函数列表，由于生成后没有执行这些函数，所以i的值全是9
print(a[0](2),type(a[0]))
print(a[0](2),a[1](2),a[2](2))

# python最大可迭代次数
sys.getrecursionlimit() # 1000
# 可以改最大可迭代次数，别改
sys.setrecursionlimit()
