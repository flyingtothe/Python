"""tulingxueyuan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from teacher import views, teacher_url

urlpatterns = [
    path('admin/', admin.site.urls),

    # 视图函数只有名称，无括号、参数
    path('normalmap/', views.do_normalmap),

    # 使用尖括号 <> 从 url 中捕获值
    # 圆括号表示的是一个参数，里面的内容作为参数传递个被调用的函数
    # 参数名称以 ?P 开头，尖括号内是参数的名字
    # 尖括号后表示正则
    # 大括号表示出现的次数
    re_path('withparam/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.withparam),

    # 约定，凡是有 teacher 模块处理的视图的 url 都已 teacher 开头
    path('teacher/', include(teacher_url)),

    re_path(r'^book/(?:page-(?P<pn>\d+)/)$', views.do_param2),

    # re_path('yourname/', views.extremParam, {'name': 'bar'}),

    path('yourname/', views.revParse, name='askname'),
]