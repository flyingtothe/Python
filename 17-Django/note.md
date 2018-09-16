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
    - 从上向下，一个个比对
    - url 格式是分级格式，则按照级别向下对比，主要对应 url 包含子 url 的情况
    - 子 url 一旦被调用，则不会反回到主 url
        - '/one/two/three/'
    - 正则已 r 开头，表示不需要转义，注意 ^ 和 $
        - '/one/two/three'     配对 r'^one/'
        - '/oo/one/two/three'  不配对 r'^one/'
        - '/one/two/three/'    配对 r'three/$'
        - '/oo/one/two/three/oo/' 不配对 r'three/$'
        - 开头反斜杠会被路由忽略
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