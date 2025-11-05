# main/urls.py
from django.urls import path
from . import views  # ایمپورت کردن فایل views.py از همین پوشه

urlpatterns = [
    # مسیرهای استاتیک (بدون آرگومان)
    path('', views.home_view, name='home'),
    path('blog/', views.blog_view, name='blog'),
    path('series/', views.series_view, name='series'),
    path('cart/', views.cart_view, name='cart'),

    # مسیرهای پروفایل
    path('profile/', views.profile_view, name='profile'),
    path('profile/courses/', views.profile_courses_view, name='profile_courses'),
    path('profile/financial/', views.profile_financial_view, name='profile_financial'),
    path('profile/comments/', views.profile_comments_view, name='profile_comments'),

    # === مسیرهای داینامیک (با آرگومان) ===

    # این مسیر آدرسی مثل /course/1/ را مدیریت می‌کند
    # <int:pk> یعنی یک عدد صحیح بگیر و آن را با نام 'pk' به ویو بفرست
    path('course/<int:pk>/', views.course_detail_view, name='course_detail'),

    # این مسیر آدرسی مثل /category/frontend/ را مدیریت می‌کند
    # <slug:slug> یعنی یک رشته (اسلاگ) بگیر و آن را با نام 'slug' به ویو بفرست
    path('category/<slug:slug>/', views.course_category_view, name='course_category'),

    # این مسیر آدرسی مثل /lecturer/jalal-bahrami/ را مدیریت می‌کند
    path('lecturer/<slug:username>/', views.lecturer_view, name='lecturer'),

    # این مسیر آدرسی مثل /article/react-next-course/ را مدیریت می‌کند
    path('article/<slug:slug>/', views.article_detail_view, name='article_detail'),

    # این مسیر آدرسی مثل /blog/category/frontend/ را مدیریت می‌کند
    path('blog/category/<slug:slug>/', views.article_category_view, name='article_category'),
]