# 可迭代
# l = [i for i in range(10)]
# # l 时可迭代的，但不是迭代器
# for idx in l:
#     print(idx)
# # range是迭代器
# for i in range(5):
#     print(i)

# isinstance案例
# 判断某个变量是否为一个实例
# 判断是否可迭代对象
# from collections import Iterable
# l1 = [1, 2, 3, 4, 5]
# print(isinstance(l1, Iterable))
# # 判断是否为迭代器
# from collections import Iterator
# print(isinstance(l1, Iterator))

# iter函数
# s = 'i love money'
# print(isinstance(s, Iterable))
# print(isinstance(s, Iterator))
# # 通过 iter 函数转变
# s_iter = iter(s)
# print(isinstance(s_iter, Iterator))
# print(isinstance(s_iter, Iterable))

# 直接使用生成器
# L = [x*x for x in range(5)]     # 放在中括号中是列表生成器
# g = (x*x for x in range(5))     # 放在小括号中式生成器
# print(type(L))
# print(type(g))

# 函数案例
# def odd():
#     print('step 1')
#     print('step 2')
#     print('step 3')
#     return None
# odd()

# 生成器案例
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield 2
#     print('stop 3')
#     yield 3
# # odd() 是调用生成器
# g = odd()
# one = next(g)
# print(one)
# two = next(g)
# print(two)

# for 循环调用生成器
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a+b
#         n += 1
#     return 'done'
# print(fib(5))

# 斐波那契数列的生成器写法
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield  b
#         a, b = b, a+b
#         n += 1
#     # 注意：出现的异常返回值为 return 的返回值
#     return 'done'
# g = fib(5)
# for i in range(6):
#     rst = next(g)
#     print(rst)

# ge = fib(10)
# 生成器典型用法：在for中使用，比较常用的典型生成器是 range()
# for i in ge:
#     print(i)

# 协程案例
def simple_coroutine():
    print('-> start')
    x = yield
    print('->recived', x)
# 主线程
sc = simple_coroutine()
print(111)
# 可以使用 sc.send(None)，效果一致
next(sc)    # 预激
print(2222)
sc.send('zhexiao')