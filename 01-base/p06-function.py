# coding=utf-8

# 只定义不会执行
# 一种组织形式    一个函数只完成一项特定的功能（类似于JAVA的方法）
# 命名规则：不能使用大驼峰
# def func():
#     print('一个函数')
#     print('要完成一定功能')
#     print('结束了')
# 调用：直接函数名
# func()

# 函数的参数
# def hello(person):
#     print('{0},你怎么了'.format(person))
#     print('sir,我走了')
# a = 'shu'
# hello(a)
# # 函数的返回值    如果没有return，默认返回none
# def hello(person):
#     print('{0},你怎么了'.format(person))
#     print('sir,我走了')
#     return "我已经跟{0}打招呼了，{1}不理我".format(person,person)
# b = 'shu'
# rst = hello(b)
# print(rst)

# 九九乘法表
for row in range(1,10):
    for col in range(1,row+1):
        # print函数默认任务打印完成后换行
        print( row * col, end=' ')
    print()

# https://www.cnblogs.com/bingabcd/p/6671368.html
# 资料:hesdfirst    零基础入门学python    腾讯公开课
# 普通参数：直接定义变量名  用时将变量或值传入   多参调用时，按位置对应
# 默认参数：形参有默认值，调用时没队形参赋值，使用默认值
def reg(name, age, gender='male'):
    if gender == 'male':
        print('{0} is {1},and he is a good student'.format(name,age))
    else:
        print('{0} is {1},and she is a goos student'.format(name,age))
reg('wang', 15, 'fenale')
# 关键字参数:变量=值
# def func(p1=v1,p2=v2....):    func body
# 调用:func(p1=value1,p2=value2..)    不容易混淆   可以不考虑参数位置
def stu( name='no name', age=0, addr='addr'):
    print('i am a student')
    print('我叫{0},今年{1}岁，我住{2}'.format(name, age, addr))
n = 'jingjing'
a = 19
addr = '你猜'
stu(name=n, age=a, addr=addr)
# 收集参数:把没有位置，不能和定义时的参数位置相对应的参数，放入一个特定的数据结构中     可以与其他参数共存   可没有参数
# def func(*args):    func body
# 调用:func(p1,p2,p3....)
def stu(*args):
    print(type(args))
    for i in args:          # 遍历
        print(i)
stu('lll',19,'sssss','sjjfkd','ffjfjjf')
stu('sssss')
# 如果使用关键字参数格式调用，会出错
# stu(name='liyang')
# 收集参数之关键字收集参数：将关键字参数按字典格式（只有）存入收集参数        参数可为空
# kwargs:一般约定俗成     调用时把多余的关键字参数放入kwargs    访问kwargs需按字典格式
# def func(**kwargs):   func_body   func(pq=va,p2=v2,p3=v3...)
def stu( **kwargs):
    # 在函数体内对于kwargs的使用不用带星号
    print('hello')
    print(type(kwargs))
    # 对字典的访问，py2 与 py3 有区别
    for k,v in kwargs.items():
        print(k,'...',v)
stu(name='qqq', age=10, addr='wwww', lover='rrrr', work='tttt')
print('***********')
print('*' * 20)     # 将 * 重复 20 遍输出
stu(name='yyyy')
# 收集参数混合调用问题：收集、关键字、普通可混合使用     规则：普通与关键字优先     定义：普通，关键字，收集tuple，收集dict
# 模拟学生自我介绍
def stu(name, age, *args, hobby='没有', **kwargs):
    print('hello,大家好')
    print('我叫 {0} ，我今年{1}打了。'.format(name, age))
    if hobby == '没有':
        print('我没有爱好')
    else:
        print('我爱好 {0}'.format(hobby))
    print('*' * 20)
    for i in args:
        print(i)
    print('#' * 30)
    for k,v in kwargs.items():
        print(k,"----",v)
name = '12222'
age = 11
stu(name, age)
stu(name, age, hobby='wan')
stu(name, age, 'wang', 'liushitou', hobby='xxx', hobby2='iiii', hobby3='5555')
# 收集参数解包问题：将参数放入list/dictionary中，直接将ist/dict中的值放入手机参数中
def stu(*args):
    print('aaaa')
    for i in args:
        print(i)
stu('liu', 'liji', 19, 200)
l = list()
l.append('lliu')
l.append(20)
l.append(230)
stu(l)
stu(*l)     # * 解包符号

# 返回值：有无返回值都用return结束
def func_1():
    print('有返回值')
    return 1
def func_2():
    print('没有返回值')
f1 = func_1()
print(f1)
f2 = func_2()
print(f2)

# 函数文档：对当前行数提供参考信息      函数内部开始的第遗憾用三引号字符串定义符      一般有特定格式
# 查看文档：help(函数名)        函数名.__doc__
def stu(name, age, *args):
    '''
    这是文档内容
    :param name: 参数：学生姓名
    :param age: 参数：学生年龄
    :param args:
    :return:     返回值
    '''
    print('zhe shi yi ge wen dang')
print(help(stu))
print(stu.__doc__)