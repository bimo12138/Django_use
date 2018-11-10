from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .forms import Name


class IndexHandler(View):

    def get(self, request):

        ls = ['1', '2', '3']
        return render(request, 'index/Index.html', context={'ls': ls})

    def post(self, request):
        name = Name(request.POST)
        if name.is_valid():
            username = name.cleaned_data.get('name')
            return HttpResponse(username)
        return HttpResponse('信息输入有误！')