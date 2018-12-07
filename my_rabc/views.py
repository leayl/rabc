from django.http import HttpResponse
from django.shortcuts import render, redirect

from my_rabc.models import User
from my_rabc.service.init_permission import init_permission


def login(request):
    if request.method == "GET":
        return render(request, "my_rabc/login.html")
    else:
        username = request.POST.get('username')
        password = request.POST .get('password')
        user = User.objects.filter(username=username, password=password)
        if not user:
            return render(request, "my_rabc/login.html", {"error": "用户名或密码错误"})
        else:
            init_permission(request,user)
            return redirect('/index/')


def index(request):
    return HttpResponse("首页啦......")