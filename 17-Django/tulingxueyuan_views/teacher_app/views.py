from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def teacher(r):
    return HttpResponse("teacher 的视图")

def v2_exception(r):
    raise Http404
    return HttpResponse('ok')

def v10_1(request):
    return HttpResponseRedirect('/v11')

def v10_2(request):
    return HttpResponseRedirect(reverse('v11'))

def v11(request):
    return HttpResponseRedirect('v11')