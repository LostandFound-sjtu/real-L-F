from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def get_login(request):
    if request.user.is_authenticated:   # 用户已经登陆
        return redirect('index')        # home页面
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)  # 返回经过身份验证的用户或None。
            if auth is not None:
                login(request, auth)
                messages.add_message(request, messages.INFO, 'Login successfully complete')
                # 在处理表单或其他类型的用户输入后向用户显示一次性通知消息，需要手动x掉
                return redirect('index')
            # 这里没有写else，所以不输入或输错只是刷新当前界面
    return render(request, "login.html")
# render必需的参数¶
# request
# 用于生成此响应的请求对象。
# template_name
# 要使用的模板的全名或模板名称的顺序。
# 如果给出了序列，将使用存在的第一个模板。有关如何找到模板的更多信息，请参见 模板加载文档。


"""
This Function Work
"""


def get_logout(request):
    logout(request)
    return redirect('index')


# 大概是因为分到的app比较简单（login），在官方文档里把函数一个个查完后感觉良好
# 但是前端还是看不懂，估计得专门学一下
