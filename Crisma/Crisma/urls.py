"""Crisma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from login import urls as login_url
from encontro import urls as encontro_url
from crismando import urls as crismando_url
from .views import bemVindo

urlpatterns = [
    path('encontro/', include(encontro_url), name='urlEncontro'),
    path('crismando/', include(crismando_url), name='urlCrismando'),
    path('login/', include(login_url)),
    path('admin/', admin.site.urls),
    path('',bemVindo,name='bemvindo')
]
