'''
爬取豆瓣数据
了解 ajax 的基本爬去方法
'''

from urllib import request
import json

url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=start=40&limit=20'

rsp = request.urlopen(url)
data = rsp.read().decode()

data = json.loads(data)

print(data)