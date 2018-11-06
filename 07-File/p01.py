# coding=utf-8

# 用写的方式打开文件
# f 称为文件句柄
# f = open(r'test.txt', 'w')
# 关闭文件
# f.close()
# 以写方式打开文件，默认没有文件，则创建

# with语句案例
# with open(r'test.txt', 'r') as f:
#     pass
    # 下面语句块开始对文件 f 进行操作
    # 在本模块中不需要在使用close关闭 f

# with案例
# with open(r'test.txt', 'r', encoding='utf-8')) as f:
#     # 按行读取内容
#     strline = f.readline()
#     # 此结构保证能够完整读取文件直到文件结束
#     while strline:
#         print(strline)
#         strline = f.readline()

# list能用打开的文件作为参数，把文件内每一行内容作为一个元素
# with open(r'test.txt', 'r', encoding='utf-8')) as f:
#     l = list(f)
#     for line in l:
#         print(line)

# read是按字符苏区文件内容
# 允许输入参数决定读取几个字符，如果没有指定，从当前位置读取到结尾
# 否则，从当前位置读取指定个数字符
# with open(r'test.txt', 'r', encoding='utf-8') as f:
#     strChar = f.read()
#     print(len(strChar))
#     print(strChar)

# seek案例
# 打开文件后，从第五个字节处开始读取
# 打开后读写指针在 0 处，寄文件的开头
# with open(r'test.txt', 'r', encoding='utf-8') as f:
#     f.seek(6, 0)
#     strChar = f.read()
#     print(strChar)

# 练习
# 打开文件，三个字符一组读取出内容，并显示
# 每读取一次,休息一秒钟
# 使用time模块下 sleep 函数，使程序暂停
# import time
# with open(r'test.txt', 'r', encoding='utf-8') as f:
#     # read参数单位使字符
#     strChar = f.read(3)
#     while strChar:
#         print(strChar)
#         # sleep 参数单位使秒
#         time.sleep(1)
#         strChar = f.read(3)
# ??? 为什么不是每行三个字符

# tell案例
# with open(r'test.txt', 'r', encoding='utf-8') as f:
#     strChar = f.read(3)
#     pos = f.tell()
#     while strChar:
#         print(pos)
#         print(strChar)
#         strChar = f.read(3)
#         pos = f.tell()
# tell 返回的数字单位是byte
# read 以字符单位

# write案例
# 想问件追加一句话
# with open(r'test.txt', 'a', encoding='utf-8') as f:
#     f.write('qqqqq,\n iiiii')

# 直接写入行
# with open(r'test.txt', 'a', encoding='utf-8') as f:
#     f.writelines('qqqqq,\n iiiii')
#     f.writelines('qqqqq,\n iiiii')

# l = ['i', 'love', 'money']
# with open(r'test.txt', 'w', encoding='utf-8') as f:
#     f.writelines(l)


# 序列化案例
# import pickle
# age = 19
# with open(r'test.txt', 'wb') as f:
#     pickle.dump(age, f)

# 反序列化案例
# import pickle
# with open(r'test.txt', 'rb') as f:
#     age = pickle.load(f)
#     print(age)

# import pickle
# a = [19, '我', '爱钱', [122, 34]]
# with open(r'test.txt', 'wb') as f:
#     pickle.dump(a, f)
# with open(r'test.txt', 'rb') as f:
#     a = pickle.load(f)
#     print(a)

# shelve案例
# 一般用于数据库
import shelve
# shv = shelve.open(r'shv.db')
# shv['one'] = 1
# shv['two'] = 2
# shv['three'] = 3
# shv.close()
# shelve 自动创建的不仅是一个 shv.db 文件，还包括其他文件

# 读取案例
# shv = shelve.open(r'shv.db')
# try:
#     print(shv['one'])
#     print(shv['threee'])
# except:
#     print('aaa')
# finally:
#     shv.close()

# shelve只读打开
# import shelve
# shv = shelve.open(r'shv.db', flag='r')
# try:
#     k1 = shv['one']
#     print(k1)
# finally:
#     shv.close()

import shelve
# shv = shelve.open(r'shv.db', flag='r')
# try:
#     k1 = shv['one']
#     print(k1)
# finally:
#     shv.close()
# 将 one 对应的值改为字典
# shv = shelve.open(r'shv.db')
# try:
#     shv['one'] = {'enis':1, 'zwei':2, 'drei':3}
# finally:
#     shv.close()
# shv = shelve.open(r'shv.db')
# try:
#     one = shv['one']
#     print(one)
# finally:
#     shv.close()
# shelve 忘记协会，需使用强制写回
# shv = shelve.open(r'shv.db', writeback=True)
# try:
#     k1 = shv['one']
#     print(k1)
#     # 此时，内容仍储存在内存中，没有写回数据库，关闭 shelve，数据库中内容不会改变
#     k1['enis'] = 100
# finally:
#     shv.close()
# shv = shelve.open(r'shv.db')
# try:
#     k1 = shv['one']
#     print(k1)
# finally:
#     shv.close()
# shelve 使用 with 管理上下文环境
with shelve.open(r'shv.db', writeback=True) as shv:
    k1 = shv['one']
    print(k1)
    k1['enis'] = 1000
with shelve.open(r'shv.db') as shv:
    print(shv['one'])