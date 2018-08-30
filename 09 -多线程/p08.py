import time
import threading
def loop1():
    # ctime 获取当前时间
    print('satart loop 1 at :', time.ctime())
    # 延迟时间
    time.sleep(6)
    print('end loop 1 at :', time.ctime())
def loop2():
    # ctime 获取当前时间
    print('satart loop 2 at :', time.ctime())
    # 延迟时间
    time.sleep(1)
    print('end loop 2 at :', time.ctime())
def loop3():
    # ctime 获取当前时间
    print('satart loop 1 at :', time.ctime())
    # 延迟时间
    time.sleep(5)
    print('end loop 1 at :', time.ctime())
def main():
    print('start at', time.ctime())
    t1 = threading.Thread(target=loop1, args=())
    t1.setName('THR_1')
    t1.start()
    t2 = threading.Thread(target=loop2, args=())
    t2.setName('THR_2')
    t2.start()
    t3 = threading.Thread(target=loop3, args=())
    t3.setName('THR_3')
    t3.start()
    time.sleep(3)
    for thr in threading.enumerate():
        print('运行的是 {0}'.format(thr.getName()))
    print('数量 {0}'.format(threading.activeCount()))
    print('all done at:', time.ctime())
if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)