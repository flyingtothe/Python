from urllib import request
from bs4 import BeautifulSoup
import re

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')


# 四大对象
# # bs 自动转码
# content = soup.prettify()
# print('==' * 20)
# print(soup.link)
# print(soup.link.name)
# print(soup.link.attrs)
# print(soup.link.attrs['type'])
# soup.link.attrs['type'] = 'jjjjj'
# print(soup.link)
# print('==' * 20)
# print(soup.title)
# print(soup.title.name)
# print(soup.title.attrs)
# print(soup.title.string)
# print('==' * 20)
# print(soup.name)
# print(soup.attrs)

# 遍利文档
# print(soup.name)
#
# for node in soup.head.contents:
#     if node.name == 'meta':
#         print(node)
#     if node.name == 'title':
#         print(node.string)


# 搜索文档
tags = soup.find_all(re.compile('^me'), content='always')
for tag in tags:
    print(tag)