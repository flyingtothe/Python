import re

# 查找数字
# p = re.compile(r'\d+')
# m = p.match('342o34i3i2j3k423kkj45k3kjjk5k3')
# print(m)

# p = re.compile(r'\d+')
# # 参数　3， 6 表示查找范围
# m = p.match('one12two33456four78', 3, 22)
# print(m)
# print(m[0])
# print(m.start(0))
# print(m.end(0))

# 表示忽略大小写
# p = re.compile(r'([a-z]+) ([a-z]+)', re.I)
# m = p.match("I am really love money")
# print(m)
#
# print(m.group(0))
# print(m.group(1))
# print(m.groups())


# 查找案例
# p = re.compile(r'\d+')
# m = p.search('one12two33456four')
# print(m.group())
# rst = p.findall('one12two33456four')
# print(type(rst))
# print(rst)


# 替换
# p = re.compile(r'(\w+) (\w+)')
# s = 'hello 123 wang 456 xiaojing, i love you'
# rst = p.sub(r'Hello World', s)
# print(rst)

# 匹配中文
# title = u'世界 你好, hello moto'
# p = re.compile(r'[\u4e00-\u9fa5]+')
# rst = p.findall(title)
# print(rst)


# 贪婪和非贪婪案例
title = u'<div>name</div><div>age</div>'
p1 = re.compile(r'<div>.*</div>')
p2 = re.compile(r'<div>.*?</div>')
m1 = p1.search(title)
print(m1.group())
m2 = p2.search(title)
print(m2.group())