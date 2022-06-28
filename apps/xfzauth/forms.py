from django import forms
from .models import User
from django.contrib import messages
from django.shortcuts import redirect, reverse
import re  # 引入re模块实现正则匹配


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=2, required=True, error_messages={
        'required': '用户名不能为空',
        'max_length': '用户名长度应小于20',
        'min_length': '用户名长度应大于2',
    })
    telephone = forms.CharField(error_messages={
        'required': '电话不能为空',
    })
    password = forms.CharField(min_length=2, max_length=20, required=True, error_messages={
        'required': '密码不能为空',
        'max_length': '密码长度应小于20',
        'min_length': '密码长度应大于2',
    })

    def validate_date(self, request):
        data = self.cleaned_data
        telephone = data.get('telephone')
        password = data.get('password')
        tel_exists = User.objects.filter(telephone=telephone).exists()
        tel = re.match(r"^1[35678]\d{9}$", telephone)
        passwd = re.match(r'[a-zA-z0-9]', password)
        print(passwd)
        if tel_exists:
            # messages.info(request, '手机号已存在')
            # print('form手机号已存在')
            return redirect(reverse('xfzauth:login'))
        elif tel is None:
            # messages.info(request, '手机号格式不正确')
            # print('wwwwwwwwwww')
            return 1
        elif passwd is None:
            return 2
        else:
            return True
