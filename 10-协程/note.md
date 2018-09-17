# 协程
- 参考资料
    - http://python.jobbole.com/86481/
    - http://python.jobole.com/87310/
    - http://segmentfault.com/a/1190000009781688
    
# 迭代器
- 可迭代（Iterable）：直接作用与 for 循环的变量
- 迭代器（Iterator）：不但可作用 for 循环，还可被 next 调用
- list是典型的可迭代对象，但不是迭代器
- 通过 isinstance 判断
- iterable 和 iterator 可以转换
    - 通过 iter 函数转换

# 生成器
- generator:一边循环以便计算下一个元素的机制/算法
- 需满足三个条件
    - 煤气调用都产生出 for 循环需要的下一个元素
    - 达到最后一个元素，爆出 Stopiteration 异常
    - 可以被 next 函数调用
- 如何生成生成器
    - 直接使用
    - 如函数中包含 yield， 则指个函数叫生成器
    - next 调用函数，遇到 yield 返回
    - 将一段程序分段执行，返回值为 yield 后得值，再次调用会从上次结束后的下一行代码开始执行

# 协程
- 历史
    - 3.4 引入，用 yield 实现
    - 3.5 引入协程语法
    - 实现协程比较好的包：asyncio, tronado, gevent
- 定义
    - 协程是一种程序组件，是由子例程（过程、函数、例程、方法、子程序）的概念泛化而来的，子例程只有一个入口点且只返回一次，而协程允许多个入口点，可以在指定位置挂起和恢复执行
- 携程的实现
    - yield返回
    - send调用
- 携程的四个状态
    - inspect.getgeneratorstate(…) 函数确定，该函数会返回下述字符串中的一个：
    - GEN_CREATED：等待开始执行
    - GEN_RUNNING：解释器正在执行
    - GEN_SUSPENED：在yield表达式处暂停
    - GEN_CLOSED：执行结束
    - next预激（prime)
    - 案例02
- 协程终止
    - 协程中未处理的异常会向上冒泡，传给 next 函数或 send 方法的调用方（即触发协程的对象）。
    - 终止协程的一种方式：发送某个哨符值，让协程退出。内置的 None 和Ellipsis 等常量经常用作哨符值。 
- yield from
    - 为了得到返回值，协程必须正常终止；
    - 然后生成器对象会抛出StopIteration 异常，异常对象的 value 属性保存着返回的值。from
    - yield from 从内部捕获StopIteration异常
    - 并且把StopIteration异常value属性子作为yield from表达式的返回值
    - 案例03
    - 委派生成器
        - 包含 yield from 表达式的生成器函数
        - 委派生成器在 yield from 表达式处暂停时，调用方可以直接把数据发给子生成器。
        - 子生成器再把产出的值发给调用方。
        - 子生成器返回之后，解释器会抛出 StopIteration 异常，并把返回值附加到异常对象上，
        此时委派生成器会恢复。
        - 案例04

# asyncio
    - 3.4 开始引入标准克重，内置对异步 io 的支持
    - asynico本身是消息循环
    - 步骤：
        - 创建消息循环
        - 将协程导入
        - 关闭

# async & await
- 为了更好的表示异步 io
- 3.5 引入
- 让协程代码更简单
- 使用上，可简单地进行替换
    - 用 async 替换 @asyncio.coroutine
    - await 替换 yield from
    - 案例06

# aiohttp
- asyncio 实现单线程得病发 io，在客户端用处不大
- 在服务器端可以 asyncio + coroutine 配合，因为 http 时 io 操作
- asyncio 实现了 tcp, udp, ssl 等协议
- aiohttp 是给予 asyncio 实现的 http 框架
- pip install aiohttp 进行安装
- 案例07

# concurrent.futures
- python3 新增的库
- 类似其他语言的线程池概念
- 利用 mulltiprocessiong 实现真正的并行计算
- 核心原理是：concurrent.futures会以子进程的形式，平行的运行多个python解释器，从而令python程序可以利用多核CPU来提升执行速度。
由于子进程与主解释器相分离，所以他们的全局解释器锁也是相互独立的。每个子进程都能够完整的使用一个CPU内核。
- concurrent.futures.Executor 
    - ThreadPoolExecutor
    - ProcessPoolExecutor
- submit(fn, args, kwargs)
    - fn:异步执行的函数
    - args,kwargs:参数
    - 案例08
- map 函数(fn, \*iterables, timeout=None)
    - 跟 map 函数类似
    - 函数需要异步执行
    - timeout：超过时间
    - map 与 submit 选择一个使用
    - 案例09
- future