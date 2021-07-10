"""soilapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from soilapp import settings
from django.contrib import admin
from django.urls import path
from . import views
from .views import SoilList,SoilDetails
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='Home'),
    path('home',views.index,name='Home'),
    path('showtable',views.showtable,name='Database Table'),
    path('api/soil',SoilList.as_view()),
    path('api/soil/<int:pk>',SoilDetails.as_view()),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
