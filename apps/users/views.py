import re

from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def register(request):
    return render(request, 'register.html')


def do_register(request):
    # 获取post请求数据
    username = request.POST.get('username')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    email = request.POST.get('email')
    allow = request.POST.get('allow')
    # 判断参数不为空
    if not all([username, password, password2, email]):
        return render(request, 'register.html', {'error': '参数不能为空'})
    # 判断密码是否一致
    if password != password2:
        return render(request, 'register.html', {'error': '密码不一致'})
    # 判断邮箱是否合法
    if not re.match('^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, 'register.html', {'error': '邮箱不合法'})
    # 判断勾选：on
    if allow != 'on':
        return render(request, 'register.html', {'error': '没有勾选协议'})
    return HttpResponse('注册成功')


def login(request):
    return render(request, 'login.html')


def user_center_info(request):
    return render(request, 'user_center_info.html')


def user_center_order(request):
    return render(request, 'user_center_order.html')


def user_center_site(request):
    return render(request, 'user_center_site.html')


def order_comment(request):
    return render(request, 'order_comment.html')
