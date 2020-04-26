# 从现在开始我们可以将Python代码按照下面的格式进行书写
# def main():
#     # Todo: Add your code here
#     pass


# if __name__ == '__main__':
#     main()
# 减少全局变量的使用就意味着我们应该尽量让变量的作用域在函数的内部
# 在实际开发中，我们应该尽量减少对全局变量的使用，
# 因为全局变量的作用域和影响过于广泛，可能会发生意料之外的修改和使用，
# 除此之外全局变量比局部变量拥有更长的生命周期，可能导致对象占用的内存长时间无法被垃圾回收。
# 事实上，减少对全局变量的使用，也是降低代码之间耦合度的一个重要举措，
# 同时也是对迪米特法则的践行。

# 实现计算求最大公约数和最小公倍数的函数。
def main():
    one = int(input())
    two = int(input())
    print("最大公约数 =:", zdgys(one,two))
    print("最小公倍数 =:", zxgbs(one,two))
    print(is_palindrome(int(input("判断回文数"))))
    print(is_prime(int(input("判断素数"))))
    print(is_prime_and_palindrome(int(input("判断回文素数"))))

def zdgys(one,two):
    # target1 = []
    # for x in range(2,one+1):
    #     if one % x == 0:
    #         if two % x == 0:
    #             target1.append(x)
    #     return target1.pop()
    if one < two:
        (one,two) = (two,one)
    for x in range(one,0,-1):
        if one % x == 0 and two % x == 0:
            return x

def zxgbs(one,two):
    return one * two // zdgys(one,two)#如果用/则返回的是float类型的小数

# 实现判断一个数是不是回文数的函数
def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    if total == num:
        return "is palindrome"
    else:
        return "not palindrome"

# 实现判断一个数是不是素数的函数。
def is_prime(num):
    for x in range(2,num):
        if num % x == 0:
            return "not prime"
    return "is prime"

# 写一个程序判断输入的正整数是不是回文素数。
def is_prime_and_palindrome(num):
    if is_prime(num) == "is prime" and is_palindrome(num) == "is palindrome":
        return "is prime and palindrome"
    return "not prime and palindrome"

if __name__ == '__main__':
    main()
