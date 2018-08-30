# coding=utf-8


# 内置数据结构（变量类型）
# list（列表）：顺序数据的组合      //结构上类似Array
# l1 = []             # 空列表
# print(type(l1))

# 常用操作
# 访问：下标访问 从0开始
# 分片操作：对列表进行截取      [:]     生成了一个新的list
# l = [3,5,1,5,49,8]
# print(l[3])
# print(l[2:5])
# print(l[::2])       # 可控制截取间隔，默认为1连续截取
# print(l[2:10])      # 下标可超出范围，超出范围不考虑下标的内容
# print(l[-4:-2])     # 下标可为负数,顺序从右向左，最后一位下标为-1，冒号右侧必须大于冒号左侧
# print(l[-2:-4:-1])  # 左边大于右边，不产参数用复数，但截取后顺序颠倒
# 内置函数 ID：显示一个变量或函数的唯一编号
# a = 100
# b = 200
# c = a               # 将 a 的引用赋值给 c
# d = 100             # 新变量与原变量指向同一个值
# a =101              # 重新赋值是将变量的引用指向新值，不会影响其他变量
# print(a)
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
# ll = l[:]
# lll = ll
# 如果两个 ID 值一样，表明分片产生的列表使用的是同一地址同一数据
# 否则，则表明分片是新生成了一份数据、新列表，将之拷贝至列表中
# print(id(l))
# print(id(ll))
# print(id(lll))
# # 通过 ID 知道，ll和lll是同一份数据，验证
# l[1] = 100
# print(l)
# print(ll)
# ll[1] = 100
# print(ll)
# print(lll)

# 删除命令: 删除后ID只和删除的不一样，呢说明生成了一个新的list
# a = [1, 2, 3, 4, 5, 6]
# print(id(a))
# del a[2]
# print(id(a))
# print(a)
# # del a         # 删除一个变量后不能再继续使用此变量
# # print(a)

# 使用加号连接两个列表
# a = [1, 2, 3, 4, 5, 6]
# b = [3, 4, 5, 6, ]
# c = ['a', 'b', 'c']
# d = a + b + c
# print(d)

# 使用乘号操作：列表直接跟一个整数相乘    相当于将整数个列表连接在一起
# a = [1, 2, 3, 4]
# b = a * 3
# print(b)

# 成员资格运算：判断一个元素是否在list中
# a = [1, 2, 3, 4]
# b = 8
# c = b in a  # c 为布尔值
# print(c)
# a = [1, 2, 3, 4]
# b = 8
# c = b not in a  # c 为布尔值
# print(c)

# 遍历
# a = [1, 2, 3, 4]
# # for in list         in 后的变量许世可迭代的
# for i in a:
#     print(i)
# # while 遍历
# length = len(a)
# index = 0
# while index < length:
#     print(a[index])
#     index += 1

# 双层列表循环
# a = [['one', 1], ['two', 2], ['three', 3]]
# for k,v in a:
#     print(k, '-->', v)
# 变异:遍历返回值与与解包出来变量个数一致
# a = [['one', 1, 'a'], ['two', 2, 'e'], ['three', 3, 't']]
# for k,v,w in a:
#     print(k, v, w)

# 列表内涵：list content(简单创建列表)
# for 创建
# a = ['a', 'b', 'c']
# b = [i for i in a]      # 将 a 中所有元素，逐个放入新列表 b 中
# print(b)
# 对 a 中所有元素乘 10，生成一个新list
# a = ['a', 2, 3, 4, 5]
# b = [i*10 for i in a]
# print(b)
# 过滤元列表中内容，放入新列表
# a = [x for x in range(1,35)]
# b = [m for m in a if m % 2 == 0]        # 将 a 所有偶数生成一个新列表
# print(b)
# 列表生成式可以嵌套：两个 for 循环嵌套
# a = [i for i in range(1,4)]
# # print(a)
# # b = [i for i in range(100,400) if i % 100 == 0]
# # print(b)
# # c = [m+n for m in a for n in b if m+n < 250]
# # print(c)

# list 函数

# len:求列表长度
# a = [x for x in range(1,100)]
# print(len(a))
# # max:求最大值
# b = ['man', 'film', 'python']
# print(max(b))

# list;将其他格式转换为list     可迭代的可以转换
# a = [1, 2, 3]
# print(list(a))
# s = 'i love money'
# print(list(s))

# 列表的函数
# l = ['a', 'h', 22, 44, 4+2j]

# # qppend:追加内容
# a = [i for i in range(1,5)]
# print(a)
# a.append(100)
# print(a)

# # insert:指定位置插入
# print(a)
# a.insert(3,66)
# print(a)

# 删除:del
# pop:从列表中取出一个元素，删除最后一个元素
# last_ele = a.pop()
# print(last_ele)
# print(a)

# # remove:删除列表中指定值的元素
# print(a)
# print(id(a))
# a.remove(66)
# print(a)
# print(id(a))

# # clear:清空
# print(a)
# print(id(a))
# a.clear()
# print(a)
# print(id(a))

# # reverse:翻转
# a = [1, 2, 3, 4, 5]
# print(a)
# print(id(a))
# a.reverse()
# print(a)
# print(id(a))

# # extend:，扩展列表，讲一个列表拼接到后一个上
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9]
# print(a)
# print(id(a))
# a.extend(b)
# print(a)
# print(id(a))

# # count:查找列表元素个数
# print(a)
# a.append(8)
# a.insert(5, 8)
# print(a)
# a_len = a.count(8)
# print(a_len)

# # copy:拷贝   浅拷贝
# a = [1, 2, 3, 4, 5, 666]
# print(a)
# # 简单赋值，传递地址
# b = a
# b[3] = 777
# print(a)
# print(id(a))
# print(b)
# print(id(b))
# print('*', 20)
# # 为解决传址影响，list赋值需要拷贝操作
# b = a.copy()
# print(a)
# print(id(a))
# print(b)
# print(id(b))
# print('*', 20)
# b[3] = 4444
# print(a)
# print(b)
# 深拷贝与浅拷贝区别
# copy函数是浅拷贝函数，只拷贝一层内容
# 深拷贝需用特定工具
# a = [1, 2, 3,[10, 20, 30]]
# b = a.copy()
# print(id(a))
# print(id(b))
# print(id(a[3]))
# print(id(b[3]))
# a[3][2] = 4
# print(a)
# print(b)


# tuple（元组）：一个不可更改的list

# 创建空元组
# t = ()
# print(type(t))
# 创建一个只有一个值得元组
# t = (1)
# t1 = (1,)
# t2 = 1,
# print(type(t))
# print(t)
# print(type(t1))
# print(t1)
# print(type(t2))
# print(t2)
# 创建多个值的元组
# t = (1, 3, 5, 6)
# print(type(t))
# print(t)
# t = 1, 2, 3, 4,5
# print(type(t))
# print(t)
# l = [1, 2, 3, 4, 5]
# t = tuple(l)
# print(type(t))
# print(t)

# 元组特性
# 1、是序列表，有序     2、元组数据只可以访问，元组中的元素值不能修改    3、元组数据可以是任意类型   总结：list有的特性元组都有，除了可修改

# # 索引操作
# t = (1, 3, 5, 7)
# print(t[3])
# # # 超标错误
# print(t[12])
# t = (1, 2, 3, 4, 5, 6, 7)
# t1 = t[1::2]
# print(id(t))
# print(id(t1))
# print(t1)
# # 切片可超标
# t2 = t[2:100]
# print(t2)

# # 序列相加
# t1 = (1, 2, 3)
# t2 = (5, 6, 7)
# print(t1)
# print(id(t1))
# t1 = t1 + t2
# print(t1)
# print(id(t1))
# # t1[1] = 100

# # 元祖相乘
# t = (1, 3, 5)
# t = t * 3
# print(t)

# # 成员检测
# t = (1, 3, 5)
# if 2 in t:
#     print('yes')
# else:
#     print('no')

# 元祖遍历
# # 单层遍历
# t = (1, 2, 3, 'www', 'u', 'jjij')
# for i in t:
#     print(i, end=' ')
# 双层遍历
# t = ((1, 2, 3), (2, 3, 4), ('www', 'u', 'jjij'))
# for i in t:
#     print(i)
# for k,v,n in t:
#     print(k, '-->', v, '-->', n)

# 关于元祖函数

# # len：获取长度
# t = (1, 2, 3, 4, 5)
# print(len(t))

# # max,min；最大/小值     如有多个最值，实际打印出哪个？
# print(max(t))
# print(min(t))

# # tuple：转化或创建元组
# l = [1, 2, 3, 4, 5]
# t = tuple(l)
# print(t)
# t = tuple()
# print(t)

# 元祖函数

# # count：机选指定数据出现的次数
# t = (2, 1, 2, 3, 45, 1, 1, 2,)
# print(t.count(2))
#
# # index：求指定元素在元祖中的索引位置
# print(t.index(45))
# print(t.index(1))       # 如果需要查找的数字是多个，则返回第一个

# 元组变量交换法： 两个变量交换值
a = 1
b = 3
a,b = b,a
print(a)
print(b)