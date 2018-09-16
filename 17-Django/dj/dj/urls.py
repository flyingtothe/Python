"""dj URL Configuration

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
from django.urls import path
from teacher import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 视图函数只有名称，无括号、参数

    # 尖括号表示以后面内容开头的表达式
    # 圆括号表示的是一个参数，里面的内容作为参数传递个被调用的函数
    # 参数名称以问号加大写P开头，尖括号内是参数的名字
    # 尖括号后表示正则，[0-9]表示内容仅能是由0-9的数字构成
    # 大括号表示出现的次数
    path('withpatam/<int:year>', tv.year_archive),
]