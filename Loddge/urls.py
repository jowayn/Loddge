"""Loddge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.landing, name='landing'),
    path('home/', app.views.home, name='home'),
    path(r'home_user/<str:id>', app.views.home_user, name='home_user'),
    path('home_user/marketplace_user/', app.views.marketplace_user, name='marketplace_user'),
    path('home_user/marketplace_user/add_user/', app.views.add_user, name='add_user'),
    path('home_user/marketplace_user/view/<str:id>', app.views.view, name='view'),
    path('home_user/marketplace_user/addreservation/', app.views.addreservation, name='addreservation'),
    path('home_user/marketplace_user/view_reservations/<str:id>', app.views.view_reservations, name='view_reservations'),
    path('admin_page/', app.views.admin_page, name='admin_page'),
    path('admin_page/marketplace/', app.views.marketplace, name='marketplace'),
    path('admin_page/marketplace/add/', app.views.add, name='add'),
    path('admin_page/marketplace/view/<str:id>', app.views.view, name='view'),
    path('admin_page/marketplace/edit/<str:id>', app.views.edit, name='edit'),
    path('admin_page/reservations/', app.views.reservations, name='reservations'),
    path('admin_page/reservations/addreservation/', app.views.addreservation, name='addreservation'),
    path('admin_page/reservations/editR/<str:id>', app.views.editR, name='editR'),
    path('admin_page/dashboard/', app.views.dashboard, name='dashboard'),
    path('register/', app.views.register, name='register'),
    path('login/', app.views.login, name='login'),
    path('login/register', app.views.register, name='register')
] 
