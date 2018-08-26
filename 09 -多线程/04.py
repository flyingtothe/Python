import time
import threading
def loop1(in1):
    # ctime 获取当前时间
    print('satart loop 1 at :', time.ctime())
    print('我是参数', in1)
    # 延迟时间
    time.sleep(4)
    print('end loop 1 at :', time.ctime())
def loop2(in1, in2):
    # ctime 获取当前时间
    print('satart loop 2 at :', time.ctime())
    print('我是参数', in1, '和参数', in2)
    # 延迟时间
    time.sleep(2)
    print('end loop 2 at :', time.ctime())
def main():
    print('STARTING at :', time.ctime())
    # 意义：用多个线程执行某个函数
    # 参数：需要运行的函数名       第二参数作为元祖使用，为空则使用空元祖
    t1 = threading.Thread(target=loop1, args=('qqq',))
    t1.start()
    t2 = threading.Thread(target=loop2, args=('www', 'eee'))
    t2.start()
    print('ALL done at :', time.ctime())
if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)