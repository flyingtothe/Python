from django.urls import path
from . import views

urlpatterns = [

    # 视图函数只有名称，无括号、参数
    path('liudana/', views.do_app),
]