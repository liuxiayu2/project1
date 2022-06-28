from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .forms import RegisterForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.html import strip_tags  # strip_tags去掉HTML文本的全部HTML标签


class LoginView(View):
    def get(self, request):
        return render(request, 'auth/test_login.html')


# 注册
class ResignView(View):
    def get(self, request):
        print('getgetget')
        return render(request, 'auth/test_resign.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid() and form.validate_date(request) is True:
            username = form.cleaned_data.get('username')
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username, telephone, password)
            login(request, user)
            return redirect(reverse("news:index"))

        elif form.errors:
            desc = strip_tags(list(form.errors.values())[0])  # 去掉返回值中所有html标签
            messages.info(request, desc)
            return redirect(reverse('xfzauth:resign'))
        elif form.validate_date(request) is 1:
            messages.info(request, "请输入正确的手机号")
            return redirect(reverse('xfzauth:resign'))
        elif form.validate_date(request) is 2:
            messages.info(request, "密码应为大小写字母和数字的组合")
            return redirect(reverse('xfzauth:resign'))
        else:
            messages.info(request, "手机号已存在")
            return redirect(reverse('xfzauth:resign'))
