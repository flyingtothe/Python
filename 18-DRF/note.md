# Django REST Framework
- 中文文档：https://q1mi.github.io/Django-REST-framework-documentation/
- REST
    - 前后端分离
    - API-ApplicationProgrammingInterface:应用程序编程接口
        - 为了应对前端的需求多样性
    - REST-RepresentationalStateTransfe:表述性状态传递,一种规范
        - RESTful:遵守 REST 规范的设计的软件称为 RESTful
    - REST 规范
        - URL定位资源，用HTTP动词（GET,POST,DELETE,PUT）描述操作
        - URL 代表一个资源，一个资源应该是名词
        - 动作由 HTTP 的 methode 方法提供
        - URL 应包含版本信息，也可放在 HTTP 中
        - 使用 URL 参数代表过滤信息
        - 返回值：每一个返回代码都有特定含义
        - 返回格式：推荐固定具体格式
    - Django REST Framework
        - 中文文档：https://q1mi.github.io/Django-REST-framework-documentation/
        - 安装：pip install djangorestframework
        - 版本问题：version3.7 基于 1.xx 版本django，之后 2.xx 版本
        - django_filter 依赖 djangorestframework3.7
    - DRF 主要任务
    - 案例TlxyDRF
        - django-admin startproject TlxyDRF
        - python manage.py startapp case01
        - 配置 settings
        - 配置 urls
        - 创建模型
        - 创建序列化器
        - 创建视图集合

- 序列化
    - 序列化 (Serialization):将对象的状态信息转换为可以存储或传输的形式的过程
    - 反序列化：序列化的逆过程

- 序列化/反序列化-DRF

- 实验步骤
    - 创建项目
    - 创建app
    - 修改settings

- serializer 的类型参数
    - read_only:仅用于序列化输出
    - write_only:仅用于反序列化输入
    - required:反序列化是必须输入，默认 True
    - allow_null:允许传入 None
    - validators:使用验证器

- 创建 serializer 对象
    - 构造方法

        Serializer(instance=None, data=empty, **kwarg)

    - 反序列化
        - 验证
            - 外来数据必须验证
            - is_valid:
                - 数据是否合法，返回boolean
                - 在使用从哇哦不传入的数据之前，必须使用此函数进行验证
                - 验证失败，返回数据错误异常
            - validataed_data:
                - 经过验证后的数据，存入此结构
    - 视图
        - DRF 的视图从处理任务，处理流程等跟 Django 基本一致
        - 此视图基本是 django 试图的扩展
        - Request
            - 将请求解析成一个 request 实例
            - 属于 DRF，与 django 有一定的区别
            - 在得到 request 前，有一个 Parse 对传入数据请求进行解析
            - data 属性(区别)
                - 请求数据体，类似与 django 的 request.POST,request.FILES
                - 在 DRF 中主要指 Json
            - query_params
                - 所有传入的关键字参数

                        api.rulingxueyuan.com/student/?naem='liu'
                        # 使用案例
                        name = self.request.query_params.get('name', None)
                        
            - user
                - 登陆后的用户信息存储在 user 中
                - 如果没有登陆，则是 anoymous
                - 可用来判断用户是否登陆
        - Response
            - rest_framework.response.Response
            - 在 settis 中设置
            - 用 Renderer 渲染器对返回内容进行渲染

                        REST_FRAMEWORK = {
                            'DEFAAULT_RENDERER_CLASSES':(   # 默认响应渲染类
                                'rest_framework.renderers.JSONRenderer', # JSON 渲染器
                                'rest_framework.renderers.BrowsableAPIRenderer', # 浏览 API 渲染器
                        }
                        
            - 返回的构造方式
                - return Response(data, status=None, template_name=None, headers=None, content_type=None)
                - 主要使用 data
                - data:返回的数据    *
                - status:返回的状态码（http 状态码）
                    - 1xx:信息告知
                    - 2xx:成功
                    - 3xx:重定向
                    - 4xx:请求错误
                    - 5xx:服务器错误
                - headers:http 中的协议头
                - content_type:返回的数据类型
        - 视图类
            - APIview
                - rest_framework.views.APIView
                - 是 django 中 view 的子类
                - 与 view 区别
                    - 传入传出数据用的是 drf 的请求和反馈类
                    - 会引发并处理 APIExceprion（由 drf 处理）
                    - 在 dispatch 之前，会进行身份验证，权限检查，流量控制
                - 支持的属性
                    - authentication_classes:列表或者元组，身份验证类
                    - permisson_classes:进行权限验证
                    - throttle_classes:流量控制类
                - 对 API 的访问提供了一些方便
                    - HTTP-Method + 名词
                    - 默认对 HttpMethod 常用方法提供支持
                - 案例 views - StudentAPIView
- API 调试工具
    - chorm - postman
    - firefox - RESTClient
    
    - GenericAPIView
        - APIView 的子类
        - 支持的属性
            - quersset:查询结果集
            - serializer_class:试图使用的序列化器
            - panination_class:分页控制器
            - filter_backends:过滤器后端
            - look_field:查询条件字段，默认pk
        - get_queryset:返回查询结果集集合，经常需要重写
        - get_serializer_class:得到序列化器类
        - get_serializer:得到序列化器

- LisetModelMixin(无任何参数，将结果以列表形式返回)
    - list(request, *arg, **kwargs)
- CreateModelMixim(增加)
    - create(request, *args, **kwargs)
- RetrieveModelMixin(准确查询一个)
    - retrieve(request, *args, **kwargs)
- UpdateModelMixin(修改)
    - update(request, *args, **kwargs)
- DestoryModelMixin(删除)
    - destory(request, *args, **kwargs)

- ViewSet
    - 将一系列操作打包，放入一个类中
    - list:GET
    - retrieve:GET+id
    - destory:DELETE
    - update:UPDATE
    - create:POST