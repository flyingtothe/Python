'''
正则结果 Match 的使用案例
'''
import re

s = r'([a-z]+) ([a-z]+)'
pattern = re.compile(s, re.I)   # s.I 表示忽略大小写
m = pattern.match('Hello world wide web')

# group(0) 表示返回匹配成功的整个子串
s = m.group(0)
print(s)

a = m.span(0)   # 返回匹配成功的整个子串的跨度
print(a)

# group(1) 表示返回的第一个分组匹配成功的子串
s = m.group(1)
print(s)

a = m.span(1)   # 返回匹配成功的第一个个子串的跨度
print(a)

s = m.groups()  # 所有分组
print(s)