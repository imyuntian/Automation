from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect


# Create your views here.
def index(request):
    # return HttpResponse("Hello Django!")
    return render(request, "index.html")

# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')  # 第二个参数是给content的默认值，避免content没值报错
        password = request.POST.get('password', '')
        # if username == 'admin' and password == 'admin123':
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            # return HttpResponsePermanentRedirect('/event_manage/')  # 账号密码正确，登录成功
            response = HttpResponsePermanentRedirect('/event_manage/')
            # response.set_cookie('user', username, 3600)  # 添加浏览器 cookie  说白了，就是用key=user，把用户名存在cookie中
            request.session['user'] = username  # 将session信息记录到浏览器
            return response
        else:
            return render(request,'index.html',{'error':'username or password error !'})  # 账号密码错误，登录失败，返回登录页

# 发布会管理
@login_required
def event_manage(request):
    # username = request.COOKIES.get('user', '')  # 读取浏览器 cookie
    username = request.session.get('user', '')  # 读取浏览器session
    return render(request,"event_manage.html", {"user":username})