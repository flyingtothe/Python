# Django系统
- 环境
    - python3.6
    - django1.18
- 参考资料
    - [django中文教程](http://python.usyiyi.cn/)
    - django 架站的 16 堂课

# 环境搭建
- anaconda+pycharm
- anaconda使用
    - conda list: 显示当前环境安装的包
    - conda env list:显示安装的虚拟环境列表
    - conda create -n env_name python=3.6
    - 激活conda的虚拟环境
        - (Linux)source activate env_name
        - (win) activate env_name
    - pip install django=1.8
 
 
# 后台需要的流程

# 创建第一个django 程序
- 命令行启动

        django-admin startproject tulingxueyuan
        cd tulingxueyuan
        python manage.py runserver
        
- pycharm 启动
    - 需要配置
    
# 路由系统-urls
- 创建 app
    - app：负责一个具体业务或者一类具体业务的模块
    - python manage.py startapp teacher
    
- 路由
    - 按照具体的请求url，导入到相应的业务处理模块的一个功能模块
    - django 的信息控制中枢
    - 本质上是接收的URL和相应的处理模块的一个映射
    - 在接受URL请求的匹配上使用了 RE
    - URL 的具体格式如 urls.py 中所示

- 需关注两点
    1. 接收的 url 是什么，及如何用 RE 对传入 url 匹配
    2. 已知 url 匹配到哪个处理模块

- url 匹配规则

    path('articles/<int:year>/<int:month>)/', views.month_archive),

    - 从上向下，一个个比对
    - url 格式是分级格式，则按照级别向下对比，主要对应 url 包含子 url 的情况
    - 子 url 一旦被调用，则不会反回到主 url
        - '/one/two/three/'
    - 正则，命名格式（?P<name>pattern），name是组的命名，pattern是需要匹配的表达式
            
            urlpatterns = [
                path('articles/2003/', views.special_case_2003),
                re_path('articles/(?P<year>[0-9]{4})/', views.year_archive),
                re_path('articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.month_archive),
                re_path('articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[^/]+)/', views.article_detail),
            ]

    - 如果从上向下都没有找到合适的匹配内容，则报错

# 正常映射
- 将某一个符合 RE 的 URL 映射到事务处理函数中去
    - 例
        from showeast import views as sv
        
        urlpattens = [
            path('^admin/', admin.site.urls),
            path('^normalmap/', sv.normalmap),
        ]

# url 带参数映射
- 在事件处理代码中须由 url 传入参数，形如 /myurl/param 中的 param
- 参数都是字符串形式，如需其他类型，需自行转换
- 通常的形式
    '''
    /search/page/432 中的 432 需要经常更换
    '''
s
# url 在 app 中处理
- 如果所有应用的 url 都集中在 tulingxueyuan/urls/py 中，可能导致文件臃肿
- 可将 urls 具体功能逐渐拆分至各个 app 中
    - 从 django.conf.urls 导入 include
    - 注意 RE 写法
    - 添加 include 导入

- 使用方法
    - 导入 include
    - 写主路由的开头 url
    - 写子路由
    - 编写视图

- 可以使用参数

# url 中嵌套的参数（级联参数）
- 捕获某个参数的一部分
    - 例如 URL/index/page-3, 需要捕获数字 3 作为参数
        
        '''
        re_path(r'^blog/(page-(\d+)/)?$', blog_articles),                  # bad
        
        会得到两个参数，但 ?: 表示忽略此参数
        re_path(r'^comments/(?:page-(?P<page_number>\d+)/)?$', comments),  # good
        '''

# 传递额外参数
- 参数不仅仅来自 url，还可能是自己定义的内容
    
    re_path('blog/<extrem>/', views.extremParam, {'name': 'bar'}),

- 附加参数同样适用与 include 语句，此时对 include 内所有都添加

# 反向解析
- 防止硬编码
- 本质上是对每一个 url 进行命名
- 以后在变大代码中使用 url 的值，原则上都应该使用反向解析

# 视图
## 概述
- 视图即视图函数，接手 web 请求并返回 web 相应的事务处理函数
- 响应值符合 http 协议要求的任何内容，包括 json string html 等
- 本次忽略事务处理，重点在如何返回处理结果上

## 其他简单视图
