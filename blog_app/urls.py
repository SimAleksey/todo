from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_title/', views.crate_title, name='create_title'),
    path('create_tasks/<int:pk>', views.create_tasks, name='create_tasks'),
    path('delete_tasks/<int:pk>', views.delete_tasks, name='delete_tasks'),
    path('delete_title/<int:pk>', views.delete_title, name='delete_title'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_, name='login'),
    path('logout/', views.user_logout, name='logout')
]
