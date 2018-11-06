from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView

# Create your views here.

"""
# 基于类视图
class SrudentListView(ListView):
    '''
    需要设置两个主要内容
    1.queryset:数据来源集合
    2.template_name:模板名称
    '''
    queryset = Srudent.object.all().filter(gender='nan')
    template_name = 'student_list.html'
"""


"""
# session
def mySess(request):
    print(request.session)
    print(type(request.session))

    # 如果 session 中没有 teacher_name 的值，则返回NoName
    print(request.session.get('teacher_name', 'NoName'))
    # 清空 session
    request.session.clear()

    print('in mySess')
    return None
"""


"""
# 分页器
def student(request):
    # 大约有1万名学生
    # 请求所有学生的详情列表
    stus = Student.objects.all()

    '''两个参数：
    1.数据来源，也即从数据库中查询出的结果
    2.但也返回数据量
    '''
    p = Paginator(stus, 50)
    # 对 Paginator 惊醒设置或者对变量属性使用
    print(p.count)          # p 里面有多少数据
    print(p.num_pages)      # 页面总数
    print(p.page_range)     # 野马列表，从 1 开始

    # 获取第三页内容,不存在，报异常 InvalidPage
    p.page(3)

    return stus
"""
