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