# 爬虫框架
- 框架
    - scrapy
    - pyspider
    - crawley
- scrapy 框架介绍
    - https://doc.scrapy.org/en/latest/
    - http://scrapy-chs.readthedocs.io/zh_CN/latest/index.html

- 安装
    - 使用 pip

- scrapy 概述
    - 包含部件
        - ScrapyEngine: 神经中枢，大脑，核心
        - Scheduler 调度器: 引擎飞来的 request 请求，调度器需要处理，然后交换引擎
        - Downloader下载器: 将引擎发来的 requests 下载，得到 response
        - Spider爬虫: 将下载器得到的网也/结果进行分解，分解成 数据加链接
        - ItemPipeline管道: 详细处理 item
        - DownloadMiddleware下载中间件: 自定义下载功能扩展组件
        - SpiderMiddleware爬虫中间件：对spider进行功能扩展
        
- 爬虫项目大概流程
    - 新建项目：scrapy startproject xxx
    - 明确需要目标/产出:  编写item.py
    - 制作爬虫 ： 地址 spider/xxspider.py
    - 存储内容： pipelines.py,   
    
- ItemPipeline
    - 对应的是 pipelines 文件
    - 爬虫提取出数据存入 item 后，item 中保存的数据需要进一步处理，比如清洗，去重，存储等
    - process_item:
        - spider提取出来的 item 作为参数传入，同时传入的还有 spider
        - 此方法必须实现
        - 必须返回一个 Item 对象，被丢弃的 item 不会被之后的 pipeline 处理
    - __init__:构造函数
        - 进行一些必要的参数初始化     
    - open_spider(spider):
        - spider对象被开启的时候调用
    - close_spider(spider):
        - 当spider对象被关闭的时候调用 

- Spider
    - 对应的是文件夹 spiders 下的文件
    - __init__: 初始化爬虫名称，start_urls 列表
    - start_requests:生成 Requests 对象交给 Scrapy 下载并返回 response
    - parse： 根据返回的 response 解析出相应的 item，item 自动进入 pipeline； 如果需要，解析出 url，url 自动交给
            requests 模块，一直循环下去
    - start_request: 此方法仅能被调用一次，读取 start_urls 内容并启动循环过程
    - name:设置爬虫名称
    - start_urls:  设置开始第一批爬取的 url
    - allow_domains:spider 允许爬去的域名列表
    - start_request(self)： 只被调用一次
    - parse
    - log:日志记录

- 中间件(DownloaderMiddlewares)
    - 中间件是处于引擎和下载器中间的一层组件
    - 可以有很多个，被按顺序加载执行
    - 作用是对发出的请求和返回的结果进行预处理
    - 在 middlewares 文件中
    - 需要在 settings 中设置以便生效
    - 一般一个中间件完成一项功能
    - 必须实现以下一个或者多个方法
        - process_request(self, request, spider)
            - 在 request 通过的时候被调用
            - 必须返回 None 或 Response 或 Request 或 raise IgnoreRequest
            - None: scrapy 将继续处理该 request
            - Request： scrapy 会停止调用 process_request 并冲洗调度返回的 reqeust
            - Response： scrapy 不会调用其他的 process_request 或者 process_exception，直接讲该 response 作为结果返回
                        同时会调用 process_response 函数
        
        - process_response(self, request, response,  spider)
            - 跟 process_request 同小异
            - 每次返回结果的时候会自动调用
            - 可以有多个，按顺序调用
        
        - 案例代码
        
                import random
                import base64
                
                # 从 settings 设置文件中导入值
                from settings import USER_AGENTS
                from settings import PROXIES
                
                #  随机的 User-Agent
                class RandomUserAgent(object):
                    def process_request(self, request, spider):
                        useragent = random.choice(USER_AGENTS)
                        request.headers.setdefault("User-Agent", useragent)
                        
                class RandomProxy(object):
                    def process_request(self, request, spider):
                        proxy = random.choice(PROXIES)
                        if proxy['user_passwd'] is None:
                            #  没有代理账户验证的代理使用方式
                            request.meta['proxy'] = "http://" + proxy['ip_port']
                        else:
                            #  对账户密码进行 base64 编码转换
                            base64_userpasswd = base64.b64encode(proxy['user_passwd'])
                            #  对应到代理服务器的信令格式里
                            request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd
                            request.meta['proxy'] = "http://" + proxy['ip_port']
        
        - 设置 settings 的相关代码
        
                USER_AGENTS = [
                            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR
                            3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
                            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0;
                            SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET
                            CLR 1.1.4322)",
                            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR
                            2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko,
                            Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
                            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3)
                            Arora/0.6",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-
                            Ninja/2.1.1",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0
                            Kapiko/3.0",
                            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
                            ]           
   
                PROXIES = [
                        {'ip_port': '111.8.60.9:8123', 'user_passwd': 'user1:pass1'},
                        {'ip_port': '101.71.27.120:80', 'user_passwd': 'user2:pass2'},
                        {'ip_port': '122.96.59.104:80', 'user_passwd': 'user3:pass3'},
                        {'ip_port': '122.224.249.122:8088', 'user_passwd': 'user4:pass4'},
                        ]

- 去重
    - 为了放置爬虫陷入死循环，需要去重
    - 即在 spider 的 parse 函数中，返回 Request 的时候加上 dont_filter=False 参数
    
            myspider(scrapy.Spider):
                def parse(.....):
                
                    ......
                    
                    yield  scrapy.Request(url=url, callback=self.parse, dont_filter=False)                
       
- 如何在 scrapy 使用 selenium
    - 可以放入中间件中的 process_request 函数中
    - 在函数中调用 selenium，完成爬取后返回 Response
    
            calss MyMiddleWare(object):
                def process_request(.....):
                    
                    driver = webdriver.Chrome()
                    html = driver.page_source
                    driver.quit()
                    
                    return HtmlResponse(url=request.url, encoding='utf-8', body=html, request=request)
            
# scrapy-shell
- https://segmentfault.com/a/1190000013199636?utm_source=tag-newest
- shell 
- 启动
	- Linux： ctr+T,打开终端，然后输入 scrapy shell "url:xxxx"
	- windows: scrapy shell "url:xxx"
	- 启动后自动下载指定 ur l的网页
	- 下载完成后，url 的内容保存在 respons e的变量中，如果需要，我们需要调用 response
- response
	- 爬取到的内容保存在 response 中
	- response.body 是网页的代码
	- resposne.headers 是返回的 http 的头信息,可用 for 遍历
	- response.xpath() 允许使用 xpath 语法选择内容
	- response.css() 允许使用 css 语法选区内容
- selector
	- 选择器，允许用户使用选择器来选择自己想要的内容
	- response.selector.xpath: response.xpath 是 selector.xpath 的快捷方式
	- response.selector.css: response.css 是他的快捷方式
	- selector.extract:把节点的内容用 unicode 形式返回
	- selector.re:允许用户通过正则选取内容

# 分布式爬虫
- 单机爬虫的问题：
    - 单机效率
    - IO 吞吐量
- 多爬虫问题
    - 数据共享
    - 在空间上不同的多台机器，可以成为分布式
- 需要做：
    - 共享队列
    - 去重
- Redis
    - 内存数据库
    - 同时可以落地保存到硬盘
    - 可以去重
    - 可以把他理解成一个 dict，set，list 的集合体  
    - 可以对保存的内容进行生命周期控制 

- 需更改设置，将队列设置为远程的

- 内容保存数据库
    - MongoDB
    - Mysql 等传统关系数据库
  
- 安装 scrapy_redis
    - pip install scrapy_reids
    - github.com/rolando/scrapy-redis
    - scrapy-redis.readthedocs.org

# 推荐书籍
- Python 爬虫开发与项目实战， 范传辉， 机械工业出版社
- 精通 python 爬虫框架 scrapy, 李斌 翻译， 人民邮电出版社
- 崔庆才， 

- 案例e16-qq招聘
    - 创建项目
    - 编写item
    - 编写spider
    - 编写pipeline
    - 设置pipeline
     
- 案例 e14-scrapy-baidu
    - 利用最简单的爬虫
    - 爬去百度页面
    - 关闭配置机器人协议
    - scrapy startproject baidu
    - scrapy crawl baidu
    
- 案例e15-meiju
    - 创建新项目
    - 分析网页，定义item
    - 编写pipeline， 确定如何处理item
    - 编写spider， 确定如何提取item
    - 可以通过增加一个单独命令文件的方式在pycharm中启动爬虫
    
- 案例e17-校花网
    - 创建项目
    - 编写item
    - spider
    - pipeline
    - 设置pipeline
    - 中间件， 会使用selenium