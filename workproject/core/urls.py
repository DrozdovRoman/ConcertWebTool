"""workproject URL Configuration

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
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('concert', views.ConcertCreateView.as_view(), name='concert'),
    path('update-page/<int:pk>',views.ConcertUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>',views.delete_page, name='delete_page'),
    path('sell', views.sell, name='sell'),
    path('target', views.target, name='target'),
]