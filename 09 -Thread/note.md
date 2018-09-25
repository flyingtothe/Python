# 环境
- xubuntu 16.04
- anaconda
- pycharm
- python 3.6
- 多线程资料(全局解释器锁)
    - https://www.cnblogs.com/jokerbj/p/7460260.html
    - http://www.dabeaz.com/python/UnderstandingGIL.pdf

# 多线程 && 多进程
- 程序：将代码以文本形式存入文档
- 进程：程序运行的状态
    - 包含地址空间，内存，数据线
    - 每个进程由自己完全独立的运行环境
- 线程
    - 一个进程可有多个线程
    - 轻量化进程
    - 一个进程的多个线程键共享数据和上下文环境
    - 共享互斥空间
- 全局解释器锁(GIL)
    - Python代码的执行由python虚拟机进行控制
    - 在主循环中只能由一个控制线程在执行
- Python包
    - thread:有问题，不好用，python3改为 _thread
        - 案例01：顺序执行，耗时比较长
        - 案例02：该用所县城，缩短总时长，使用_thread
        - 案例03：多线程，传参数
    - threading:通行的包
        - 直接利用threading.Thread(target=函数名， args=(参数一，))
            1.t = threading.Thread(target= , args= )
            2.t.start():启动线程
            3.t.join():等待多线程完成
            - 案例04
            - 案例05：比较加入 join 后区别
        - 守护线程（daemon）
            - 守护线程的实现与环境相关
            - 案例06非守护线程
            - 案例07守护线程
        - 线程常用属性
            - threading.currentThread:返回当前线程变量
            - threading.enumerate:返回一个包含正在运行的线程的list
            - threading.activeCount:返回正在运行的线程数量
            - thr.setName:设置线程名称v 
            - thr.getName:获取线程名称
            - 案例08
    - 直接继承threading.Thread
        - 直接继承
        - 重写 run 函数
        - 类实例可直接运行
        - 案例09
        - 案例10
- 共享变量
    - 多个线程访问同一变量时，会导致变量问题
    - 案例11
    - 解决：加锁
        - 是一个标志，表示一个线程在占用一些资源
        - 使用方法：
            - 上锁
            - 使用资源
            
            - 开锁，释放资源
            - 案例12
- 线程安全问题
    - 一个变量/资源，对于多线程来说，不用加锁也不会引起，任何文，则称为线程安全
    - 不安全：list，set， dict
    - 安全：queue
- 生产者消费者问题
    -  一个模型，可用来搭建消息队列
    - 使用 queue 存放变量
    - 案例13
- 死锁问题：案例14
- 锁的等待时间问题：案例15
- semphore 
    - 允许一个资源最多有几个线程同时使用
    - 案例16
- threading.Timer
    - 案例17
    - 利用多线程，在指定时间启动一个功能
- 可重入锁
    - 一个锁，可被一个线程多次申请
    - 主要解决递归调用的时候，需要申请锁
    - 案例18

# 线程替代方案
- subprocess
    - 完全跳过线程，使用进程
    - 是派生进程的主要替代方案
    - 2.4 后引入
- multiprocessiong
    - 使用 threading 接口派生，使用子进程
    - 允许为多喝或多cpu派生进程，接口更threading非常相似
    - 2.6 引入
- concurrent.futures
    - 新的异步执行模块
    - 任务基本的操作
    - 3.2 后引入

# 多进程
 - 进程间通讯(InterprocessCommnication, IPC)
 - 进程间无任何共享状态
 - 进程创建
    - 直接生成 Process 实例对象  案例19
    - 派生子类  案例20
- 在 os 中查看 pid ppid 以及他们的关系
    - 案例21
- 生产者消费者模型
    - JoinableQueue
    - 案例22
    - 队列中哨兵的使用 案例23