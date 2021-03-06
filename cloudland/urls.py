"""cloudland URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from homeapp import views

urlpatterns = [
    path('', views.home_view, name="home"),
    # path('area/', views.area_view, name="area"),
    path('secret/', admin.site.urls),
    path('.well-known/pki-validation/7C41CA9043FD281856B204018F1837A9.txt',  views.ssl_view, name="ssl")
]
