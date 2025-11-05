from django.contrib import admin
from django.urls import path, include  # دکمه include را اضافه کنید

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]