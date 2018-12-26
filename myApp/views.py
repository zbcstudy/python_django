from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('第一个视图')


def detail(request,num):
    return HttpResponse('detail-%s' % num)

