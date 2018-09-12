from urllib import request
# 使用 urllib.request 请求一个网页内容，并将内容打印出来

if __name__ == '__main__':
    url = 'http://jobs.zhaopin.com/195435110251173.htm?ssidkey=y&ss=409&ff=03&sg=2644e782b8b143419956320b22910c91&so=1'
    # 打开响应url并将相应页面作为返回
    rsp = request.urlopen(url)

    # 将返回结果读取出来
    # 读取出来的内容类型为bytes
    html = rsp.read()
    print(type(html))

    # 将 bytes 内容转换为字符串，需要解码
    html = html.decode('utf-8')

    print(html)