# 多线程案例
import time
import _thread as thread
def loop1():
    # ctime 获取当前时间
    print('satart loop 1 at :', time.ctime())
    # 延迟时间
    time.sleep(4)
    print('end loop 1 at :', time.ctime())
def loop2():
    print('satart loop 2 at :', time.ctime())
    time.sleep(2)
    print('end loop 2 at :', time.ctime())
def main():
    print('STARTING at :', time.ctime())
    # 意义：用多个线程执行某个函数
    # 参数：需要运行的函数名       第二参数作为元祖使用，为空则使用空元祖
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())
    print('ALL done at :', time.ctime())
if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)