from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def teacher(r):
    return HttpResponse("teacher 的视图")