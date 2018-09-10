from urllib import request, parse
from http import cookiejar

# 创建 cookiejar 实例
cookie = cookiejar.CookieJar()

# 生成 cookie 管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 生成 http 管理器
http_handler = request.HTTPHandler()

# 生成 https 管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    '''
    负责初次登陆
    需要输入用户名密码，用来获取登录 cookie 凭证
    '''

    # 此 url 需要从登陆 form 的 action 属性中获得
    url = 'http://www.renren.com/PLogin.do'

    # 此键值徐聪登陆 form 的 input 中获取 name 属性
    data = {
        'email': '13119144223',
        'password': '123456'
    }

    # 将数据编码
    data = parse.urlencode(data)
    # 创建请求对象
    req = request.Request(url, data=data.encode())
    # 使用 opener 发起请求
    rsp = opener.open(req)

def getHomePage():
    url = 'http://www.renren.com/965187997/profile'
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open('rsp.html', 'w') as f:
        f.write(html)
if __name__ == '__main__':
    login()
    getHomePage()