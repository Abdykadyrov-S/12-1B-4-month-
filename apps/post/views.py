from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello Geeks")

def goodbye(request):
    return HttpResponse("Goood Bye")

def index(request):
    return HttpResponse("Это главная страница")
