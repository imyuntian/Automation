"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from sign import views

urlpatterns = [
    url(r'^$', views.index),  # 127.0.0.1:8000/
    url(r'^admin/', admin.site.urls),  # 使用自带的管理后台， > python manage.py createsuperuser   自动生成该行代码
	url(r'^index/$', views.index),  #127.0.0.1:8000/index/
    url(r'^login_action/$', views.login_action),
    url(r'^event_manage/$', views.event_manage),
    url(r'^accounts/login/$', views.index),  #127.0.0.1:8000/index/accounts/login/
]
