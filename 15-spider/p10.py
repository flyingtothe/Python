'''
使用代理访问百度
'''

from urllib import request, error
if __name__ == '__main__':
    url = 'http://www.baidu.com'
    # 1.设置代理地址
    proxy = {'http': '120.76.77.152:9999'}
    # 2.常见 ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3.创建  Opener
    opener = request.build_opener(proxy_handler)
    # 4.安装 Opener
    request.install_opener(opener)

    # 现在访问 url，使用的是代理服务器
    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)