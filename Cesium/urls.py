"""Cesium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cesium import apps
from cesium import views


# 绑定URL与管理员视图函数
urlpatterns = [
    path('admin/', admin.site.urls), # 管理员视图函数
    path('hello/', views.hello), # hello视图函数
    path('index/', views.index), # index视图函数
    path('cesium/', views.login), # cesium视图函数
]

# 绑定 URL 与hello视图函数



