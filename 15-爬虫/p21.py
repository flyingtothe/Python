import requests

url = 'http://www.baidu.com'

# 使用 get 请求
rsp = requests.get(url)
print(rsp.text)

# 使用 request 请求
rsp = requests.request('get', url)
print(rsp.text)