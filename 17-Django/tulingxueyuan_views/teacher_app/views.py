from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def teacher(r):
    return HttpResponse("teacher 的视图")

def v2_exception(r):
    raise Http404
    return HttpResponse('ok')

def v8_get(request):
    rst = ''
    for k,v in request.GET.items():
        rst += k + '-->' + v
        rst += ", "
    return HttpResponse('Get value of Reauest is {0}'.format())

def v10_1(request):
    return HttpResponseRedirect('/v11')

def v10_2(request):
    return HttpResponseRedirect(reverse('v11'))

def v11(request):
    return HttpResponseRedirect('v11')