from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('api/articles/create/', views.create_article_api, name='api_create_article'),
    path('', views.post_list, name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]

