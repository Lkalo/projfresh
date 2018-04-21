from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def detail(request):
    return render(request, 'detail.html')


def detail2(request):
    return render(request, 'detail2.html')


def list(request):
    return render(request, 'list.html')
