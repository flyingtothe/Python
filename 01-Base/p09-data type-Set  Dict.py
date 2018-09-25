# coding=utf-8

# set(集合):无序的唯一数据

# # 集合定义
# s = set()
# print(type(s))
# print(s)
# s = {1, 2, 3, 4, 5}
# print(s)
# print(type(s))
# d = {}              # 只用大括号定义的是dict类型
# print(type(d))
# print(d)

# 集合特征：1、数据无序，无法使用索引雨与分片    2、集合内院宿具有唯一性，可用来处重      3，集合内只能放置可hash的数据

# 集合序列操作
# # 成员检测： in      not in
# s = {1, 2, '4', '4jj', 'sdjfsfj'}
# print(s)
# if '4jj' in s:
#     print('aaa')
# if 'jjj' not in s:
#     print('jfjfj')

# 集合遍历
#
# for i in s:
#     print(i,end=' ')
# # 带有元祖的结合遍历
# s = {(1, 2, 3) , ('4', '4jj', 'sdjfsfj')}
# for k,m,n in s:
#     print(k, '--', m, '--', n)
# for k in s:
#     print(k)

# 集合的内涵
# 普通集合内涵
# # 初始化后自动过滤重复元素
# s = {23, 223, 545, 3, 1, 2, 3, 4, 3, 2, 3, 1, 2, 4, 3}
# print(s)
# ss = {i for i in s}
# print(ss)
# # 带条件的集合内涵
# sss = {i for i in s if i % 2 ==0}
# print(sss)
# # 多循环的集合内涵
# s1 = {1, 2, 3, 4}
# s2 = {'i', 'love', 'money'}
# s = {m*n for m in s2 for n in s1}
# print(s)
# s = {m*n for m in s2 for n in s1 if n ==2}    # 生成两遍
# print(s)

# 结合函数/关于集合的函数

# # len, man, min：与其他函数一致
# s = {42, 23, 56, 223, 4, 2, 1222, 4, 323, 1}
# print(len(s))
# print(max(s))
# print(min(s))

# # set：生成一个集合
# l = [1, 2, 3, 4, 5]
# s = set(l)
# print(s)

# # add：向集合中添加元素
# s = {1}
# s.add(44)
# print(s)

# # clear：清空
# s = {1, 3, 5}
# print(id(s))
# s.clear()
# print(id(s))

# copy：拷贝
# remove：移除指定位置的值，直接改变原有值，如果该值不存在，报错
# dicard： 移除集合中指定的值，与上同，但不报错
# s = {23, 3, 4, 5, 1, 2, 4}
# s.remove(4)
# print(s)
# s.discard(1)
# print(s)
# print('*' * 20)
# s.discard(1100)
# print(s)
# s.remove(1100)
# print(s)

# pop: 随机移除一个元素,并返回该值
# s = {7, 6, '5', 4, 3, 2, 1}
# s = {23, 3, 4, 5, 1, 2, 4}
# s = {1, 2, '4', '4jj', 'sdjfsfj'}
# print(s.pop())
# print(s)

# Intersection:交集
# Difference:差集
# Union:并集
# Inssubset:检查一个集合是否为另一个的子集
# Issupereset:检查一个集合是否为另一个超集
# s1 = {1, 2, 3, 4, 5, 6}
# s2 = {5, 6, 7, 8, 9}
# s_1 = s1.intersection(s2)
# print(s_1)
# s_2 = s1.difference(s2)
# print(s_2)
# s_3 = s1.issubset(s2)
# print(s_3)

# 集合的数学操作
# s1 = {1, 2, 3, 4, 5, 6}
# s2 = {5, 6, 7, 8, 9}
# s_1 = s1 - s2
# print(s_1)
# s_2 = s1 + s2     # 无相加操作
# print(s2)

# frozen set(冰冻集合）：不可进行任何修改的集合
# s = frozenset()
# print(type(s))
# print(s)


# dict（字典）：没有顺序的组合数据

# 创建
# d = {}                                  # 空字符串
# print(d)
# d = dict()                              # 空字符串
# print(d)
# d = {'one':1, 'two':2, 'three':3}
# print(d)
# d = dict({ 'one':1, 'two':2, 'three':3 })   # 用dict创建有内容字典
# print(d)
# d = dict(one=1, two=2, three=3)             # 用dict创建有内容字典
# print(d)
# d = dict([("one",1), ("two",2), ("three",3)])
# print(d)

# 字典特征：是无序序列类型，没有分片和索引      由键值对组成

# 常见操作
# 访问
# d = {'one':1, 'two':2, 'three':2}
# print(d['one'])
# d['one'] = 'eins'
# print(d)

# 删除
# del d['one']
# print(d)

# 成员检测
# d = {'one':1, 'two':2, 'three':2}
# if 2 in d:
#     print('value')
# if 'two' in d:
#     print('key')
# if ('two',2) in d:
#     print('k v')

# 遍历
# Python2　与 python3　不同
# 按key来使用for循环
# d = {'one':1, 'two':2, 'three':3}
# for k in d:
#     print(k, d[k])
# for k in d.keys():
#     print(k, d[k])
# for v in d.values():        # 只访问字典的值
#     print(v)
# for k,v in d.items():       # 3 中想要同时遍历，需加 items()
#     print(k, '--', v)

# 字典生成式
# d = {'one':1, 'two':2, 'three':3}
# dd = {k:v for k,v in d.items()}                     # 常规
# print(dd)
# dd = {k:v for k,v in d.items() if v % 2 ==0}        # 加限制条件
# print(dd)

# 字典相关函数
# 通用函数：len, max, min, dict

# str(字典);返回字典的字符窜格式
# d = {'one':1, 'two':2, 'three':3}
# print(str(d))

# clear;清空字典

# items:返回字典的键值对组成的元组格式
# d = {'one':1, 'two':2, 'three':3}
# i = d.items()
# print(type(i))          # 2中返回可迭代标准类型
# print(i)

# keys:返回字典的键组成的一个结构
# k = d.keys()
# print(type(k))
# print(k)

# values:返回字典的值组成的一个结构
# v = d.values()
# print(type(v))
# print(v)

# get:根据制定的键返回相应的值
# d = {'one':1, 'two':2, 'three':3}
# print(d.get('on333'))
# # get默认值是 None,可以设置
# print(d.get('one',100))
# print(d.get('one333',100))
# # print(d['one333'])        两者区别

# formkeys:使用指定的序列作为键，使用一个值作为字典的所有的键的值
# l = ['eins', 'zwei', 'dree']
# # 注意formkeys两个参数的类型
# # 注意formkeys的调用主体
# d = dict.fromkeys(l, 'hahaha')
# print(d)