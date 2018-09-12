import requests
from urllib import parse
# 负责处理 json 格式的模块
import json

'''
1.利用 data 够着内容，用urlopen打开
2.返回一个json'格式的结果
3.结果就应该是girl的释义
'''

baseurl = 'https://fanyi.baidu.com/sug'

# 存放用来提取 form 的数据一定是 dict 格式
data = {
    # kw 时翻译输入的英文内容，由用户输入
    'kw': 'girl'
}

# 构造请求头，请求头至少应包括传入数据的长度
# request 要求传入的请求头是一个 dict 格式

headers = {
    # 因使用 post，至少应包含 content-length 字段
    'Content-Length': str(len(data))
}

# 尝试发出请求
rsp = requests.post(baseurl, data=data, headers=headers)

print(rsp.text)
print(rsp.json())

