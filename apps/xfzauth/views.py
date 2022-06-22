from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .forms import RegisterForm
from .models import User
from django.contrib.auth import authenticate, login, logout


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
        if form.is_valid():
            username = form.cleaned_data.get('username')
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            # print('sss%s' % username)
            # print('sss%s' % telephone)
            # print('sss%s' % password)
            user = User.objects.create_user(username, telephone, password)
            login(request,user)
            return redirect(reverse("news:index"))

        else:
            print('ddddd')
            return redirect(reverse('xfzauth:login'))
