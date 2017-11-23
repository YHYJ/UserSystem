from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import RegisterForm

# Create your views here.


def register(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        '''进行注册处理'''
        form = RegisterForm(request.POST)

        if form.is_valid():
            '''验证数据合法性'''
            new_user = form.save()

            if redirect_to:
                # 注册成功自动登录并重定向到首页
                authenticated_user = authenticate(username=new_user.username,
                                                  password=request.POST['password1'])
                login(request, authenticated_user)
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        # GET请求则显示空注册表单
        form = RegisterForm()
    # 渲染模板：如果数据合法则为绑定了数据的表单，否则是带有错误信息的表单；GET请求则返回一个空表单
    return render(request, 'users/register.html', context={'form': form, 'next': redirect_to})


def index(request):
    return render(request, 'index.html')
