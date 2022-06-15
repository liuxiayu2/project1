from django.shortcuts import render, redirect, reverse
from django.views.generic import View


class LoginView(View):
    def get(self,request):
        return render(request, 'auth/test_login.html')

class ResignView(View):
    def get(self,request):
        return render(request, 'auth/test_resign.html')

    def post(self,request):
        return
