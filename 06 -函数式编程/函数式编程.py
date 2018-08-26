# lambda函数案例
# def printA():
#     print('AAAAA')
# printA()

# lambda表达式案例
# stm = lambda x: 100 * x
# print(stm(89))
# stm2 = lambda x, y, z: x+ y*10 +z*100
# print(stm2(4, 5, 6))

# 高阶函数案例
# 函数名称就是一个变量
# def funA():
#     print('In funA')
# funB = funA
# funB()
# 结论：1.函数名称是变量  2.funB和funA只是名称不一样  3.既然韩式名称是变量，则应该可以被当做参数参入另一个参数

# funA是普通函数，返回一个传入数字的100倍数字
# def funA(n):
#     return n * 100
# # 在写一个函数，把传入参数乘以300倍，利用高阶函数
# def funB(n ):
#     # 最终想返回 300n
#     return funA(n) * 3
# print(funB(9))
# # 写一个高阶函数
# def funC(n, f):
#     # 假定函数是将 n 扩大 100 倍
#     return f(n) * 3
# print(funC(9, funA))

# map案例
# 将列表中的每个元素乘以10生成新列表
# l1 = [i for i in range(10)]
# print(l1)
# l2 = []
# for i in l1:
#     l2.append(i * 10)
# print(l2)
# # 利用map实现
# def mulTen(n):
#     return n * 10
# # python2中用映射对列表进行操作，返回的还是列表
# # python3中用映射队列表进行操作，反回的是map类型
# l3 = map(mulTen, l1)
# # map是可迭代结构，可用for遍历
# for i in l3:
#     print(i)

# reduce案例
# from functools import reduce
# # 定义一个操作函数
# # 加入操作函数只是想加
# def myAdd(x, y):
#     return x + y
# # 对于列表[1,2,3,4,5,6]执行myAdd的reduce操作
# rst = reduce(myAdd, [1,2,3,4,5,6])
# print(rst)

# filter案例
# 定义过滤函数
# def isEven(a):
#     return a % 2 == 0
# l = [1, 3, 45, 6, 64, 3, 65, 3, 5, 633, 453, 3, 3, 4, 3]
# rst = filter(isEven, l)
# print(type(rst))
# print(rst)
# print([i for i in rst])

# 排序案例
# a = [1, 2, 3, 6, 767, 345, 4345, 55]
# al = sorted(a, reverse=True)
# print(al)
# 按照绝对值排序
# a = [-334, 34, -43, 33, -3, 5864, 45]
# # abs是求绝对值的
# # 按绝对值的倒序排列
# al = sorted(a, key=abs, reverse=True)
# print(al)
# astr = ['dana', 'Dana', 'wangxiaojing', 'jingjing', 'haha']
# str1 = sorted(astr)
# print(str1)
# str2 = sorted(astr , key=str.lower)
# print(str2)

# 返回函数案例
# def myF(a):
#     print('In myF')
#     return None
# a = myF(8)
# print(a)
# 函数作为返回值返回，被返回的函数在函数体内定义
# def myF2():
#     def myF3():
#         print('In myF3')
#         return '5'
#     return myF3
# f3 = myF2()
# print(type(f3))
# print(f3)
# print(f3())
# myF4定义函数，返回内部定义的函数myF5    myF5使用了外部变量，这个变量是myF4的参数
# def myF4( *args ):
#     def myF5():
#         rst = 0
#         for n in args:
#             rst += n
#         return rst
#     return myF5
# f5 = myF4(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# # f5的调用参数
# print(f5())
# f6 = myF4(10, 20, 30, 40, 50)
# print(f6())

# 闭包常见问题
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#         fs.append(f)
#     return fs
# f1, f2, f3 = count()
# 出现原因：返回函数引用了变量 i，i 并非立即执行，而是等到三个函数都返回的时候才同意使用，此时 i 已经变为 3，最终调用时，都返回的是 3*3
# 注意：返回比保湿，返回函数不能引用任何循环变量
# print(f1())
# print(f2())
# print(f3())
# 解决方案：创建一个新函数，用该函数的参数绑定循环变量的当前值，无论该循环变量如何改变，已绑定的函数参数值不在改变
# def count2():
#     def f(j):
#         def g():
#             return j * j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))
#     return fs
# f1, f2, f3 = count2()
# print(f1())
# print(f2())
# print(f3())

# 装饰器
# def hello():
#     print('Hello World')
# hello()
# f = hello
# f()
# print(id(f))
# print(id(hello))
# print(f.__name__)
# print(hello.__name__)
# # 不改变现有代码的情况下进行功能扩展，每次打印 hello 之前打印系统时间
# # 使用装饰器
# import time
# def printTime(f):
#     def wrapper(*args, **kwargs):
#         print('Time:', time.ctime())
#         return f(*args, *kwargs)
#     return wrapper
# @printTime
# def hello():
#     print('Hello World')
# hello()
# # 装饰器一旦定义可装饰任意函数
# # 一旦被装饰，则将装饰器功能直接添加到定义函数的功能上
# @printTime
# def hello2():
#     print('今天很高兴，被老板揪着讲课了')
#     print('还可以有很多选择')
# hello2()
# # 上面对函数装饰使用了系统定义的语法塘
# # 手动执行装饰器
# def hello3():
#     print('我是手动执行的')
# hello3()
# hello3 = printTime(hello3)
# hello3()
# f = printTime(hello3)
# f()

# 偏函数案例
# 将字符串转化为十进制数字
# print(int('12345'))
# # 将八进制字符串12345，表示成十进制数字
# print(int('12345', base=8))
# # 新建一个函数，此函数默认输入的字符串时十六进制数字
# # 用时仅只返回此字符串
# def int16(x, base=16):
#     return int(x, base)
# print(int16('12345'))

# import functools
# # 实现 int16 的功能
# int16 = functools.partial(int, base=16)
# print(int16('12345'))

# zip案例
# l1 = [1, 2, 3, 4, 5]
# l2 = [i*11 for i in l1]
# z = zip(l1, l2)
# print(type(z))
# print(z)
# for i in z:
#     print(i)
# l1 = ['xiaodong', 'xiaoxi ', 'xiaonan']
# l2 = [33, 54, 65]
# z = zip(l1, l2)
# for i in z:
#     print(i)
# l3 = [i for i in z]
# print(l3)

# enumerate案例
# enumerate(列表[，start=下标开始位置])
# l1 = [11,33,44,66,33]
# em = enumerate(l1)
# l2 = [i for i in em]
# print(l2)


# collection案例
import collections

# nametuple案例
# Point = collections.namedtuple('Point', ['x', 'y'])
# p = Point(33,44)
# print(p.x)
# print(p[0])

# Circle = collections.namedtuple('Circle', ['x', 'y', 'z'])
# c = Circle(100, 150, 200)
# print(c)
# print(type(c))

# deque案例
# from collections import deque
# q = deque(['a', 'b', 'c'])
# print(q)
# q.append('d')
# print(q)
# q.append('x')
# print(q)

# defaultdict案例
# d1 = {'one':1, 'two':2, 'three':3}
# print(d1['one'])
# # print(d1['four'])
#
# from collections import defaultdict
# func = lambda:'111'
# d2 = defaultdict(func)
# d2['one'] = 1
# d2['two'] = 3
# print(d2['one'])
# print(d2['four'])

# counter案例
# from collections import Counter
# # 需要内容可迭代   将字符串拆分为单个字符
# c = Counter('abcdefgabcdefabcdeabcdabcaba')
# print(c)
# s = ['liudana', 'love', 'love', 'love', 'love', 'wangxiaojing']
# c = Counter(s)
# print(c)

