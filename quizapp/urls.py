from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginpage,name='loginpage'),
    path('register/',views.register,name='register'),
    path('frontpage/',views.frontpage,name='frontpage'),
    path('question/',views.question,name='question'),
]
