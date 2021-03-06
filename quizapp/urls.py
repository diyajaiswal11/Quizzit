from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginpage,name='loginpage'),
    path('register/',views.register,name='register'),
    path('frontpage/',views.frontpage,name='frontpage'),
    path('logoutpage/',views.logoutpage,name='logoutpage'),
    path('question/<int:pk>/',views.question,name='question'),
    path('leaderboard/',views.leaderboard,name='leaderboard'),
    path('completed/',views.completed,name='completed'),
]
