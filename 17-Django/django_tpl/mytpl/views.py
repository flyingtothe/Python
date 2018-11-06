from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def one(request):
    return render(request, 'one.html')

def two(request):
    # 用来存放向模板中传递的数据
    ct = dict()
    ct['name'] = input()
    ct['name2'] = 'write'
    ct['name3'] = 'read'

    return render(request, 'two.html', context=ct)

def three(request):
    ct = dict()
    ct['score'] = [99, 98, 22, 44, 24, 78]
    return render(request, 'three.html', context=ct)

def four(request):
    ct = dict()
    ct['name'] = '爱'
    return render(request, 'four.html', context=ct)

def five_get(request):
    return render(request, 'five_get.html')

def five_post(request):
    print(request.POST)
    return render(request, 'one.html')