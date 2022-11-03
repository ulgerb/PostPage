"""odevboot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from myApp.views import *
from django.conf import settings
from django.conf.urls.static import static
from odevboot.settings import MEDIA_URL, MEDIA_ROOT
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('<id>/detail/', detail, name='detail'),
    path('create/post/', postCreate, name='postCreate'),
    path('delete/<id>/', postDelete, name='delete'),
    path('upgrade/<id>', postUpgrade, name='upgrade'),
    
] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
