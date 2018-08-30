# coding=utf-8

# 变量作用域
# 范围： 全局（global）：在函数外部定义     局部（local)：函数内部
# LEGB原则：L（Local） 局部作用域    E（Enclosing function local） 外部嵌套函数作用域      G（Global modul） 函数定义所在模块作用域    B（buildin） python内置模块的作用域
# a1 = 100
# def fun():
#     print(a1)
#     print('i am in fun')
#     a2 = 99
#     print(a2)
# print(a1)
# fun()

# 提升局部变量为全局变量
# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
# x = 50
# func(x)
# print('x is still', x)
#
# def func():
#     global x
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
# x = 50
# func()
# print('Value of x is', x)

# globals,locals函数(内建函数)：显示全局变量/局部变量
# a = 1
# b = 2
# def fun(c,d):
#     e = 111
#     print('Locals={0}'.format(locals()))
#     print('Globals={0}'.format(globals()))
# fun(100,200)

# eval()函数：将字符串当表达式执行，返回表达式执行后的结果
# 语法：eval(string_code, globals=none, locals=none)
# x = 100
# y = 200
# z1 = x + y
# z2 = eval('x+y')
# print(z1)
# print(z2)

# exec()函数：将字符串当表达式执行，无返回值
# x = 100
# y = 200
# z1 = x + y
# z2 = exec("print('x+y:',x+y)")
# print(z1)
# print(z2)

# 递归函数：直接或间接调用自身    缺点：对递归深度有限制（自身限制最大12层），消耗资源大    需先确立结束条件，防止崩溃
# x = 0
# def fun():
#     global x
#     x += 1
#     print(x)
# #    if x == 98:
# #        return
#     fun()
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
# def fib(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)
# print(fib(3))
#
# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a+b

# 汉诺塔问题
# 规则：1.每次只能移动一个     2.任何一次移动必须是小的在上，大的在下
def hano(n, a, b, c):
    '''
    :param n: 代表有几个盘子
    :param a: 代表第一个塔
    :param b: 代表第二个塔
    :param c:代表第三个塔
    :return:
    '''
    if n == 1:
        print(a, '-->', c)
        return None
    # if n == 2:                # 可以没有
    #     print(a, '-->', b)
    #     print(a, '-->', c)
    #     print(b, '-->', c)
    #     return None
    hano(n-1, a, c, b)
    hano(n-1, b, a, c)
a = 'A'
b = 'B'
c = 'C'
n = 5
hano(n, a, b, c)