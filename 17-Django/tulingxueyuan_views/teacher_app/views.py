from django.shortcuts import render_to_response, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

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
    return HttpResponse('Get value of Reauest is {0}'.format(rst))

def v9_get(request):
    # 渲染模板并返回
    return render_to_response('for_post.html')

def v9_post(request):
    rs = ''
    for k, v in request.POST.items():
        rs += k + '-->' + v
        rs += ", "
    return HttpResponse('Get value of Reauest is {0}'.format(rs))

def v10_1(request):
    return HttpResponseRedirect('/v11')

def v10_2(request):
    return HttpResponseRedirect(reverse('v11'))

def v11(request):
    return HttpResponseRedirect('v11')

def render_test(request):
    rsp = render(request, 'render.html')
    return rsp

def render2_test(request):
    # 环境变量
    c = dict()
    c['name'] = 'liuxueli'
    c['name'] = 'lxl'
    c['name'] = 'liu'
    rsp = render(request, 'render2.html', context=c)
    return rsp

def render3_test(request):
    # 得到模板
    t = loader.get_template('render2.html')
    print(type(t))
    r = t.render({'name':'liuxueli'})
    return HttpResponse(r)

def render4_test(request):
    # 反馈会模板 render2
    rsp = render_to_response('render2.html', context={'name':'lxl'})
    return rsp

def get404(request):
    from django.views import defaults
    return defaults.page_not_found(request, Exception)