'''
利用 parse 模块模拟 post 请求
分析百度词典
步骤
1.打开F12
2.尝试输入单词 girl，发现没输入一个字母后，都有请求
3.请求地址为 http;//fanyi.baidu.com/sug
4.利用 NetWork-All-Hearders 查看， 发现 FormData 的只是 kw:girl
5.检查返回内容格式，发现返回的是 json 格式的内容==>需要倒入 json 包
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

# 尝试发出请求
rsp = request.urlopen(baseurl, data=data)
json_data = rsp.read().decode()
print(json_data)

# 将 json 字符串转化为字典
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data['data']:
    print(item['k'], '---', item['v'])