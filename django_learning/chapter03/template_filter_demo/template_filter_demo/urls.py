"""template_filter_demo URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add_view),
    path('cut/', views.cut_view),
    path('date/', views.date_view),
    path('default/', views.dafault_view),
    path('first/', views.first_view),
    path('floatformat/', views.floatformat_view),
    path('join/', views.join_view),
    path('length/', views.length_view),
    path('lower/', views.lower_view),
    path('random/', views.random_view),
    path('safe/', views.safe_view),
    path('slice/', views.slice_view),
    path('striptags/', views.stringtags_view),
    path('truncatechars/', views.truncatechars_view),
]
