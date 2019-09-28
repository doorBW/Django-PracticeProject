from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signupView, name='signup_signupView'),
    path('email/', views.email, name='signup_email'),
    path('verifyView/', views.verifyView, name='signup_verifyView'),
    path('verify/', views.verify, name='signup_verify')
]
