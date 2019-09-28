from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='main_index'),
    path('', views.loginView, name='main_loginView'),
]
