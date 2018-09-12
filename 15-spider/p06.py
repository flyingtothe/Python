'''
需求与 05 相同
本案例使用 Request 实现 05 内容
'''

from urllib import request, parse
# 负责处理 json 格式的模块
import json

'''
1.利用 data 够着内容，用urlopen打开
2.返回一个json'格式的结果
3.结果就应该是girl的释义
'''

baseurl = 'https://fanyi.baidu.com/sug'

kw = input('input:')

# 存放用来提取 form 的数据一定是 dict 格式
data = {
    # kw 时翻译输入的英文内容，由用户输入
    'kw': kw
}

# 需要用 parse 模块对 data 编码
data = parse.urlencode(data).encode('utf-8')

# 构造请求头，请求头至少应包括传入数据的长度
# request 要求传入的请求头是一个 dict 格式
headers = {
    # 因使用 post，至少应包含 content-length 字段
    'Content-Length': len(data)
}

# 构造 Request 实例
req = request.Request(url=baseurl, data=data, headers=headers)

# 因为已经够造了一个 Request 的请求实例，则所有的请求信息都可以封装在 Request 实例中
rsp = request.urlopen(req)
json_data = rsp.read().decode()
print(json_data)

# 将 json 字符串转化为字典
json_data = json.loads(json_data)

for item in json_data['data']:
    print(item['k'], '---', item['v'])