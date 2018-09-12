from urllib import request, parse
from http import cookiejar

# 创建 cookiejar 实例
cookie = cookiejar.MozillaCookieJar()
cookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)
# 生成 cookie 管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 生成 http 管理器
http_handler = request.HTTPHandler()

# 生成 https 管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def getHomePage():
    url = 'http://www.renren.com/965187997/profile'
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open('rsp.html', 'w') as f:
        f.write(html)
if __name__ == '__main__':
    getHomePage()