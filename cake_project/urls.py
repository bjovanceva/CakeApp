"""
URL configuration for cake_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from cake_app import views as CakeViews

urlpatterns = ([
    path("admin/", admin.site.urls),
    path("index/", CakeViews.index, name='index'),
    path("add_cake/", CakeViews.add_cake, name='add_cake'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
