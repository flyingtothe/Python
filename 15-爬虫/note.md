# 参考资料
- python 网络数据采集
- 精通Python爬虫框架Scrapy
- 网络爬虫：http://blog.csdn.net/c406495762/article/details/72858983
- Scrapy：http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html

# 定义：
- 网络爬虫（Web Spider），又被称为网页蜘蛛，是一种按照一定的规则，自动地抓取网站信息的程序或者脚本。

# 简介
- 网络蜘蛛是一个很形象的名字。如果把互联网比喻成一个蜘蛛网，那么Spider就是在网上爬来爬去的蜘蛛。网络蜘蛛是通过网页的链接地址来寻找网页，从网站某一个页面开始，读取网页的内容，找到在网页中的其它链接地址，然后通过这些链接地址寻找下一个网页，这样一直循环下去，直到把这个网站所有的网页都抓取完为止。

- 两大特征
    - 能按作者要求下载数据或者内容
    - 能自动在网络上流窜

- 三大步骤
    - 下载信息
    - 提取正确的信息
    - 根据一定规则自动跳转到另外的网页，执行上两步内容

- 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）

- Python网络报简介
    - python2.x:urllib, urllib2, urllib3, bttplib, httplib2, reqests
    - python3.x:urllib, urllib3, httplib2, requests
    - python2:urllib 与 urllib2配合使用，或者requests
    - python3:urllib,requests

# urllib
- 包含模块
    - urllib.request:打开和读取 url
    - urllib.error:包含 urllib.request 产生常见的错误，使用 try 捕捉
    - urllib.parse:包含解析 URL 的方法
    - urllib.robotparse:解析 robots.txt 文件
    - 案例 01

- 禁止频繁对同一网站进行爬取

- 网页编码问题解决
    - chardet:可以自动检测页面文件的编码格式，但可能有误
    - 需要安装 conda install chardet
    - 案例 02

- urlopen 的返回对象
    - 案例 03
    - geturl:返回请求对象的 url
    - info:请求反馈对象的 meta 信息
    - getcode:返回的 http code

- request.data 的使用
    - 访问网络的两种方式
        - get
            - 利用参数给服务器传递信息
            - 参数 dict，用 parse 编码
            - 案例 04
        - post
            - 一般向服务器传递参数使用
            - post 是将信息自动加密
            - 如想使用 post 信息，需要用到 data 参数
            - 使用 post，意味着 http 的请求头可能需要更改
                - Content-Type;application/x-www.form-urlencode
                - Content-Length:数据长度
                - 注意，一旦更改，其他请求头信息相对应
            - urllib.parse.urlencode 可以将字符串自动转换成上面内容
            - 案例 05
            - 为更多设置请求信息，urlopen 无法满足需要
            - 需要利用 resquest.Request 类
            - 案例 06

- utllib.error
    - URLError 产生原因
        - 没网
        - 服务器连接失败
        - 找不到指定服务器
        - 是 OSError 子类
        - 案例 07
    
    - HTTPError, 是urlerror的子类
        - 案例 08

    - 两者区别
        - HTTPError 是对应 HTTP 请求的返回码错误，返回错误码 400 以上，引发 HTTPError
        - URLError 对应的一般是网络出现问题，包括 url 问题
        - 关系：OSError - URLError - HTTPError
    
    - UserAgent
        - 用户代理，简称UA，属于heads的一部分，服务器通过UA来判断访问者的身份
        - 常见UA值，使用时可直接复制粘贴，也可以用浏览器访问的时候抓包