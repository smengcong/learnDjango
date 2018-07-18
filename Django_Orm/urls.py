"""Django_Orm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url,include
from app01 import views
from app02 import views as views2

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/', views.index.as_view()),
    url(r'^addbook/',views.addbook),
    url(r'^updatebook/',views.updatebook),
    url(r'^deletebook/',views.deletebook),
    url(r'^getbook/',views.showbook),
    url(r'^login',views.login),
    url(r'^homepage',views.homepage),
    url(r'^loout',views.loout),
    url(r'^form',views2.form),
    url(r'^showData',views2.showData),
    url(r'^mdindex/',views2.mdindex),
    url(r'^mdlogin/',views2.mdlogin),
    path('app03/',include('app03.urls')),
    path('video/',include('video.url')),
]
