from django.urls import path
from . import views

urlpatterns = [
    path('api/prices/', views.prices_api, name='prices_api'),
]
