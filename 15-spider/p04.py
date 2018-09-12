from urllib import request, parse

'''
掌握对 url 进行参数编码的方法
需使用 parse 模块
'''

if __name__ == '__main__':
    url = 'http://www.baidu.com/s?'
    wd = input('input your keyword:')

    # 想要使用 data，需使用字典结构
    qs = {
        'wd': wd
    }

    # 转换 url 编码
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    rsp = request.urlopen(fullurl)

    html = rsp.read()

    # 使用get取值保证不会出错
    html = html.decode()
    print(html)