"""TlxyDRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

# 导入路由
from rest_framework import routers

from case01 import views
router = routers.SimpleRouter()
# 视图注册
router.register('student', views.StudentVS)

urlpatterns = [
    path('admin/', admin.site.urls),
    # 需要将 drf 路由当作子路由，配置好
    path('api/', include(router.urls)),
]
