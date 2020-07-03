'''
进程和线程

1.进程概念：

    进程就是操作系统中执行的一个程序，操作系统以进程为单位分配存储空间，
每个进程都有自己的地址空间、数据栈以及其他用于跟踪进程执行的辅助数据，
操作系统管理所有进程的执行，为它们合理的分配资源。

2.线程概念：

    一个进程还可以拥有多个并发的执行线索，简单的说就是拥有多个可以获得CPU调度的执行单元，
这就是所谓的线程。由于线程在同一个进程下，它们可以共享相同的上下文，因此相对于进程而言，
线程间的信息共享和通信更加容易。当然在单核CPU系统中，真正的并发是不可能的，
因为在某个时刻能够获得CPU的只有唯一的一个线程，多个线程共享了CPU的执行时间。


'''
# Python中的多进程
# Unix和Linux操作系统上提供了fork()系统调用来创建进程，调用fork()函数的是父进程，
# 创建出的是子进程，子进程是父进程的一个拷贝，但是子进程拥有自己的PID。
# fork()函数非常特殊它会返回两次，父进程中可以通过fork()函数的返回值得到子进程的PID，
# 而子进程中的返回值永远都是0。Python的os模块提供了fork()函数。由于Windows系统没有fork()调用，
# 因此要实现跨平台的多进程编程，可以使用multiprocessing模块的Process类来创建子进程，
# 而且该模块还提供了更高级的封装，例如批量启动进程的进程池（Pool）、用于进程间通信的队列（Queue）和管道（Pipe）等。
#在上面的代码中，我们通过Process类创建了进程对象，通过target参数我们传入一个函数来表示进程启动后要执行的代码，
# 后面的args是一个元组，它代表了传递给函数的参数。Process对象的start方法用来启动进程，而join方法表示等待进程执行结束。
# 运行下面的代码可以明显发现两个下载任务“同时”启动了，而且程序的执行时间将大大缩短，不再是两个任务的时间总和。下面是程序的一次执行结果。

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
    p1.start()
    p1.join()
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
 
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()

# Python中的多线程
# 我们可以直接使用threading模块的Thread类来创建线程，但是我们之前讲过一个非常重要的概念叫“继承”，
# 我们可以从已有的类创建新类，因此也可以通过继承Thread类的方式来创建自定义的线程类，然后再创建线程对象并启动线程。

from threading import Thread
# from random import randint
# from time import time, sleep


class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))


def main():
    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()

# 因为多个线程可以共享进程的内存空间，因此要实现多个线程间的通信相对简单，
# 大家能想到的最直接的办法就是设置一个全局变量，多个线程共享这个全局变量即可。
# 但是当多个线程共享同一个变量（我们通常称之为“资源”）的时候，很有可能产生不可控的结果从而导致程序失效甚至崩溃。
# 如果一个资源被多个线程竞争使用，那么我们通常称之为“临界资源”，对“临界资源”的访问需要加上保护，否则资源会处于“混乱”的状态。

# from time import sleep
# from threading import Thread

class Account(object):

    def __init__(self):
        self._balance = 0
        # self._lock = Lock()

    def deposit(self, money):
        # 计算存款后的余额
        new_balance = self._balance + money
        # 模拟受理存款业务需要0.01秒的时间
        sleep(0.01)
        # 修改账户余额
        self._balance = new_balance

        # # 先获取锁才能执行后续的代码
        # self._lock.acquire()
        # try:
        #     new_balance = self._balance + money
        #     sleep(0.01)
        #     self._balance = new_balance
        # finally:
        #     # 在finally中执行释放锁的操作保证正常异常锁都能释放
        #     self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()

# 运行上面的程序，结果让人大跌眼镜，100个线程分别向账户中转入1元钱，结果居然远远小于100元。
# 之所以出现这种情况是因为我们没有对银行账户这个“临界资源”加以保护，多个线程同时向账户中存钱时，
# 会一起执行到new_balance = self._balance + money这行代码，多个线程得到的账户余额都是初始状态下的0，
# 所以都是0上面做了+1的操作，因此得到了错误的结果。在这种情况下，“锁”就可以派上用场了。
# 我们可以通过“锁”来保护“临界资源”，只有获得“锁”的线程才能访问“临界资源”，
# 而其他没有得到“锁”的线程只能被阻塞起来，直到获得“锁”的线程释放了“锁”，
# 其他线程才有机会获得“锁”，进而访问被保护的“临界资源”。
# 上面被注释的代码演示了如何使用“锁”来保护对银行账户的操作，从而获得正确的结果。

'''
比较遗憾的一件事情是Python的多线程并不能发挥CPU的多核特性，这一点只要启动几个执行死循环的线程就可以得到证实了。
之所以如此，是因为Python的解释器有一个“全局解释器锁”（GIL）的东西，任何线程执行前必须先获得GIL锁，
然后每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行，这是一个历史遗留问题，
但是即便如此，就如我们之前举的例子，使用多线程在提升执行效率和改善用户体验方面仍然是有积极意义的。

多进程还是多线程:
无论是多进程还是多线程，只要数量一多，效率肯定上不去。
操作系统在切换进程或者线程时也是一样的，它需要先保存当前执行的现场环境（CPU寄存器状态、内存页等），
然后，把新任务的执行环境准备好（恢复上次的寄存器状态，切换内存页等），才能开始执行。这个切换过程虽然很快，
但是也需要耗费时间。如果有几千个任务同时进行，操作系统可能就主要忙着切换任务，根本没有多少时间去执行任务了，
这种情况最常见的就是硬盘狂响，点窗口无反应，系统处于假死状态。所以，多任务一旦多到一个限度，
反而会使得系统性能急剧下降，最终导致所有任务都做不好。

是否采用多任务的第二个考虑是任务的类型，可以把任务分为计算密集型和I/O密集型。
计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如对视频进行编码解码或者格式转换等等，
这种任务全靠CPU的运算能力，虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，
CPU执行任务的效率就越低。计算密集型任务由于主要消耗CPU资源，这类任务用Python这样的脚本语言去执行效率通常很低，
最能胜任这类任务的是C语言，我们之前提到了Python中有嵌入C/C++代码的机制。

除了计算密集型任务，其他的涉及到网络、存储介质I/O的任务都可以视为I/O密集型任务，这类任务的特点是CPU消耗很少，
任务的大部分时间都在等待I/O操作完成（因为I/O的速度远远低于CPU和内存的速度）。
对于I/O密集型任务，如果启动多任务，就可以减少I/O等待时间从而让CPU高效率的运转。
有一大类的任务都属于I/O密集型任务，这其中包括了我们很快会涉及到的网络应用和Web应用。
'''

'''
单线程+异步I/O（协程）:

现代操作系统对I/O操作的改进中最为重要的就是支持异步I/O。如果充分利用操作系统提供的异步I/O支持，
就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型。
Nginx就是支持异步I/O的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务。
在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。用Node.js开发的服务器端程序也使用了这种工作模式，
这也是当下实现多任务编程的一种趋势。

在Python语言中，单线程+异步I/O的编程模型称为协程，有了协程的支持，
就可以基于事件驱动编写高效的多任务程序。协程最大的优势就是极高的执行效率，
因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销。
协程的第二个优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，
在协程中控制共享资源不用加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
如果想要充分利用CPU的多核特性，最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，
可获得极高的性能。关于这方面的内容，我稍后会做一个专题来进行讲解。

'''

# 关于super().__init__()：
# 如果不加super().__init__()，继承自父类，覆盖初始化化def init，增加属性age，不能调用name属性
# 增加super().__init__()，继承自父类，覆盖初始化化def init，并继承初始化属性name，可以调用

class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename