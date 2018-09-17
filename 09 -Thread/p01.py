# 利用 time 函数，生成两个函数，顺序调用，计算总运行时间
import time
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
    loop1()
    loop2()
    print('ALL done at :', time.ctime())
if __name__ == '__main__':
    main()