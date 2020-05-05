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
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()

# Python中的多线程
# Unix和Linux操作系统上提供了fork()系统调用来创建进程，调用fork()函数的是父进程，
# 创建出的是子进程，子进程是父进程的一个拷贝，但是子进程拥有自己的PID。
# fork()函数非常特殊它会返回两次，父进程中可以通过fork()函数的返回值得到子进程的PID，
# 而子进程中的返回值永远都是0。Python的os模块提供了fork()函数。由于Windows系统没有fork()调用，
# 因此要实现跨平台的多进程编程，可以使用multiprocessing模块的Process类来创建子进程，
# 而且该模块还提供了更高级的封装，例如批量启动进程的进程池（Pool）、用于进程间通信的队列（Queue）和管道（Pipe）等。

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

