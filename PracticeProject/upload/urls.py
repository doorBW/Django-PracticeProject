from django.urls import path, include
from . import views

urlpatterns = [
    path('fileView/', views.fileView, name='upload_fileView'),
    path('file/', views.uploadFile, name='upload_file')
]
