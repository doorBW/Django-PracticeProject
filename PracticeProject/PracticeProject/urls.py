from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', include('signup.urls'), name='signup'),
    path('upload/', include('upload.urls'), name='upload'),
    path('', include('main.urls'), name='main'),
]
