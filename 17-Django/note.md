# Django系统
- 环境
    - python3.6
    - django1.18
- 参考资料
    - [django中文教程](http://python.usyiyi.cn/)
    - django 架站的 16 堂课

- django 简化版是 Flask

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
- django.http 提供了很多类似 HttpResponse 的简单视图
- 此类视图实用的方法基本类似，可通过 return 语句直接反馈给浏览器
- Http404 是 Exception 子类，需要 raise 使用

## HttpResponse 详解
- 方法
    - init:使用页面内容实例化 HttpResponse 对象
    - write(content):以文件方式写
    - flush():以文件的方式输出缓存区
    - set_cookie(key, value='', max_age=None, expisres=None):设置 Cookie
        - key, value 都是字符串类型
        - max_age 是一个证书，表示在指定秒数后过期
        - expires 是一个 datetime 或 timedelta 对象，会话将在这个指定的日期/时间过期
        - max_age/expires 二选一使用
        - 如果不指定过期时间，则两个星期后过期
    - delete_cookie(key):删除指定的 key 的 cookie，如果 key 不存在则什么也不发生

## HttpRsponesRedirect
- 重定向，服务器端跳转
- 构造函数的第一个参数用来指定重定向的地址
- 案例
        '''
        # 在 easr/urls 中添加以下内容
        path('v10_1/', views.v10_1),
        path('v10_2/', views.v10_2),
        path('v11/',views.v11, name='v11'),
        '''
        '''
        def v10_1(request):
            return HttpRespinesRedirect('/v11)
        def v10_2(request):
            return HttpResponesRedirect(reverse('v11))
        def v11(request):
            return HttpResponesRedirect('v11')
        '''

## Request详解
- 介绍
    - 服务器收到 http 请求后，会根报文创建 HttpRequest 对象
    - 视图函数的第一个参数是 HttpRequest 对象
    - 在 django.http 模块中定义了 HttpRequest 对象的 API

- 属性
    - 下面除非特殊说明，属性都是只读的c
    - path:一个字符串，表示请求页面的完整路径，不包含域名
    - method:一个字符串，表示请求使用的 Http 方法，常用值包含 GET POST
    - enoding:一个字符串，表示提交数据的编码方式
        - 为 none 表示浏览器默认设置，一般为 utf-8
        - 这个属性是可写的，可通过设置 encoding 更改表单数据使用的编码方式
    - GET:类似于字典的对象，包含 get 请求方式的所有参数
    - POST:类似于字典的对象，包含 post 请求方式的所有参数
    - Files:类似于字典的对象，包含所有的上传文件
    - COOKIES:标准的 python 字典，包含所有的 cookie，键和值为字符串
    - session:一个可读写的类似于字典的对象，表示当前会话
        - 只有当 django 启用会话的支持时才可用
        - 详细内容建“状态保持”

- 方法
    - is_ajax():入股请求是通过 XMLHttpRequest 发起的，则返回 True

- QueryDict 对象
    - 定义在 django.http.Querydict
    - request 对象的属性 GET POST 都是 QueryDict 类型对象
    - 与 python 字典不同，QueryDice 类型的对象用来处理弄一键多值的情况
    - 方法 get() 根据键获取值
        - 只能获取键的一个值
        - 一键多值时，获取最后一个
    - 方法 getlist()  
        - 将键的值以列表返回，可以获取一键的多个值

- GET 属性
    - QueryDict 类型对象
    - 包含 get 请求方式的所有参数
    - 与 url 请求地址中的参数对应，位于 ？ 后
    - 参数的格式是键值对
    - 多个参数间使用 & 链接
    - 键是开发人员定下来的，值是可变的
    - 案例 tulingxueyuan_views/views/v8_get

- POST 属性
    - QueryDict 类型对象
    - 包含 post 请求方式的所有参数
    - 与 form 表单中的控件对应
    - 表单中控件必须有 name 属性，name 为键，value 为值
        - checkbox 存在一键多值的问题
    - 键是开发人员定下来的，值是可变的
    - 案例 tulingxueyuan_views/views/v9_post
        - settings 中设置模板位置
        - 设置 get 页面的 urls 和函数
        '''
        east/urls.py
        需要在路由文件中添加两个路由
        path('v9_get/', views.v9_get),
        path('v9_post/', views.v9_post),
        '''
        '''
        tulingxueyuan_views/views.py
        在文件中添加两个处理函数
        def v9_get(request):
            return render_to_response('for_post.html')
        def v9_post(request):
            rst = ''
            for k, v in request.POST.items():
                rst += k + '-->' + v
                rst += ", "
            return HttpResponse('Get value of Reauest is {0}'.format(rst))
        '''
        - 添加文件 /easr/templates/for_post.html
        - 有拦截，需在 settings 中注掉 crsf 设置
        '''
            MIDDLEWARE = [
                'django.middleware.security.SecurityMiddleware',
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.middleware.common.CommonMiddleware',
                # 安全中间件
                # 'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
                'django.middleware.clickjacking.XFrameOptionsMiddleware',
            ]    
        '''

## 手动编写视图
- 目的
    - 利用 django 快捷函数手动编写视图处理函数
    - 编写过程中理解视图运行原理

- 分析
    - django 将所与请求信息封装入 request
    - django 公国 urls 模块将相应请求跟时间处理函数链接，并将 request 作为参数传入
    - 在相应的处理函数中，需要完成两部分
        - 处理业务
        - 将结果封装并返回
    - 本案例不介绍业务处理，将目光集中在如何渲染结果并返回

- render(request, template_name[,context][,context_instance][,content_type])
    - 使用模板和一个给定的上下文环境，返回一个渲染过的HttpResponse
    - request：django 的传入请求
    - template_name：模板名称
    - content_instance：上下文环境
    - 案例 teacher_app/views/render_test

- render_to_response
    - 功能与上同
    - 根据给定的上下文字典渲染指定模板，返回渲染后的 HttpResponse
## 系统内建视图
- 系统内见视图，可直接使用
- 404
    - default.page_not_found(request, template_name='404.html')
    - 系统引发 Http404 时触发
    - 默认传递 request_path 变量给模板，既导致错误的 url
    - DEBUG=True 则不会调用 404，取而代之的时调试信息
    - 404 视图会被传递一个 RequestContext 对象并且可以访问模板上下文处理器提供的变量
- 500(server error)
    - default.server_error(request, template_name='500.html')
    - DEBUG=False,否则不可调用
- 403(HTTP Forbidden) 视图
    - default.permission_denied(request, template_name='403.html')
    - 通过 PermissionDenied 触发
- 400(bad request) 视图
    - default.bad_request(request, template_name='400.html')
    - DEBUG=True

## 基于类的视图
- 与基于函数的视图的优势与区别
    - HTTP 方法的 methode 可以有各自的方法，不需要使用条件分支来解决
    -可以使用 oop 技术（例如 mixin）
- 概述
    - 核心是允许使用不同的势力方法来响应不同的 HTTP 请求，避开条件分支实现
    - as_view 函数作为类的可调入库，该方法穿件一个示例并调用 dispath 方法，按照请求方法
    方法没有定义，则引发HttpResponseNotAllowed
- 类属性使用
    - 定义是直接覆盖
    - 调用 as_view 时直接作为参数使用，例
        '''
        urlpatterns = [
            path('about/', GreetingView.as_view(greeting="G'day")),
        ]
        '''
- 对于基于类的视图的扩充大致有三种方法：Mixin,装饰as_ciew,装饰dispatch
- 使用 Mixin
    - 所继承的一种形式，来自父类的行为和属性组合在一起
    - 解决多继承问题
    - view 的子类只能单继承，多继承会导致不可期问题
    - 多继承带来的问题
        - 结构复杂
        - 优先顺序模糊
        - 功能冲突
    - 解决方法
        - 规格继承 - java interface
        - 实现继承 - python ruby
- 在 URLconf 中装饰
    '''
    from django.contrib.auth.decotators import login_required, permission_required
    from django.views.generic import TemplateView
    from .views import VoteView
    
    urlpatterns = [
        path('about/', login_required(TemplateView.as_view(template_name))),
        path('vote/', permission_required('polls.can_vote')(Voteview))
    ]
    
    '''
- 装饰类 
    -类的方法和独立方法不同，不能直接运用装饰器，需要用methode_decorator
        '''
        rom django.contrib.auth.decotators import login_required
        from django.utils.decorators import method_decorator
        from django.voews.generic import TemplateView
        class protectedview(TemplateView):
            template_name = 'scret.html'
            
            @method_decorator(login_reqired)
            def dispatch(self, *args, **kwargs):
                return super(Protectedview, self).dispatch
        '''

## models 模型
- ORM
    - ObjectRelationMap:将面向对象思想转换成关系数据库
    - 类对应表格
    - 类中的属性对应表中的字段
    - 在应用中的 models.py 文件中定义 class
    - 所有需要使用 orm 的 class 都必须是 models.Model 的子类
    - class 中的所有属性都对应表格中的字段
    - 字段的类型都必须使用 models.xxx 不能使用 python 中的类型
    - 在 django 中，Models 负责跟数据库交互
- django连接数据库
    - 自带默认数据库 sqlite3
        - 关系型数据库
        - 轻量级
    - 建议开发用 sqlite3，部署用 mysql 之类的数据库
        - 切换数据库在 settings 中设置
            '''
            链接 mysql
            DATABASES = [
                'default' = {
                    'ENGINE':'django.db.backends.mysql',
                    'NAME':'数据库名称',
                    'PASSWORD':'数据库密码',
                    'HOST':'127.0.0.1',
                    'PORT':'3306',
                }
           ]
            '''
        
        - 需要在项目文件下的 __init__ 文件中导入 pymsql 包
            '''
            在项目 __init__ 文件中
            import pymysql
            pymysql.install_as_MySQLdb()
            '''

## models类的使用
- 定义和数据库表映射的类
    - 在应用中的 models.py 文件中定义 class
    - 所有需要使用 orm 的 class 都必须是 models.Model 的子类
    - class 中的所有属性对应表格的字段
    - 字段的类型都必须使用 modles.xxx 不能使用 python 中的类型

- 字段常用参数
    - max_length:规定数值的最大长度
    - blank:是否允许字段为空，默认不允许
    - null:在 DB 中冬至是否保存为null，默认为 false
    - defaule:默认值
    - unique:唯一
    - verbose_name:假名

- 数据库的迁移
    '''
    1.在命令行中，生成数据迁移的语句（生成 sql 语句）
    python3 manange.py makemigrrations
    
    2.在命令行中，输入数据迁移指令
    python3 manage.py migrate
    
    ps:如果迁移中出现没有过变化或者报错，可以尝试强制迁移
    
    强制迁移指令
    python manage.py makemigrations 应用名
    python magage.py migrate 应用名
    
    3.对于默认数据库，为了避免出现胡乱，如果数据库中没有数据，每次迁移前可将自带的 sqlite3 数据库删除
    '''