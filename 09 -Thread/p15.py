import time
import threading

lock_1 = threading.Lock()
lock_2 = threading.Lock()
def func_1():
    print('func_1 starting')
    lock_1.acquire(timeout=4)
    print('func_1申请了lock_1')
    time.sleep(2)
    print('func_1 等待lock_2')
    rst = lock_2.acquire(timeout=2)
    if rst:
        print('func_1 已经得到锁 lock_2')
        lock_2.release()
        print('func_1 释放了 lock_2')
    else:
        print('func_1 没申请到 lock_2')
    lock_1.release()
    print('func_1释放了lock_1')
    print('func_1 done')
def func_2():
    print('func_2 starting')
    lock_2.acquire()
    print('func_2申请 lock_2')
    time.sleep(4)
    print('func_2 等待 lock_1')
    lock_1.acquire()
    print('func_2 没申请到 lock_1')
    lock_1.release()
    print('func_2 释放了lock_1')
    lock_2.release()
    print('func_2 释放了lock_2')
    print('func_1 done')
if __name__ == '__main__':
    print('start')
    t1 = threading.Thread(target=func_1, args=())
    t2 = threading.Thread(target=func_2, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('done')