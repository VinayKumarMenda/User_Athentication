from django.shortcuts import render,redirect
from django.urls import path
from .views import home,Register,Login_user,Logout_user

urlpatterns = [
    path('',home,name='home'),
    path('register/',Register,name='register'),
    path('login/',Login_user,name='login'),
    path('logout/',Logout_user,name='logout'),
]
