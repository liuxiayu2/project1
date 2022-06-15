from django.shortcuts import render, redirect, reverse
from django.views.generic import View


class IndexView(View):
    def get(self, request):
        return render(request, 'base/test_base.html')
