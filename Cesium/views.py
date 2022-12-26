from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! ")

def cesium(request):
    name ="cesium"
    return render(request,"index.html",{"name":name})