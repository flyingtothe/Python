from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

'''
视图函数需要一个参数，类型应该是 HttpRequest
'''
def do_normalmap(request):
    return HttpResponse('this is normalmap')

def withparam(request, year, month):
    return HttpResponse('this is with param {0}, {1}'.format(year, month))