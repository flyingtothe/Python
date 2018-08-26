from multiprocessing import Process
import os
def info(title):
    print(title)
    print('module name:',__name__)
    # 获取父进程id
    print('parent process ', os.getppid())
    # 获取本身进程id
    print('process id ', os.getpid())
def f(name):
    info('function f')
    print('hello', name)
if __name__ == '__main__':
    info('main.line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()