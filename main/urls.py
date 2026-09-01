# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # مسیرهای استاتیک (بدون آرگومان)
    path('', views.home_view, name='home'),
    # path('blog/', views.blog_view, name='blog'), # کامنت شد تا اپلیکیشن جدید blog این مسیر را مدیریت کند
    path('series/', views.series_view, name='series'),
    path('cart/', views.cart_view, name='cart'),
    path('manager-dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('manager-dashboard/delete-post/<int:post_id>/', views.manager_delete_post, name='manager_delete_post'),
    path('tools/risk-management-calculator/', views.risk_calculator_view, name='risk_calculator'),
    path('tools/economic-calendar/', views.economic_calendar_view, name='economic_calendar'),

    # مسیرهای پروفایل و احراز هویت
    path('api/login/', views.login_api, name='login_api'),
    path('api/register/', views.register_api, name='register_api'),
    path('api/logout/', views.logout_api, name='logout_api'),
    path('api/newsletter/', views.newsletter_api, name='newsletter_api'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/courses/', views.profile_courses_view, name='profile_courses'),
    path('profile/financial/', views.profile_financial_view, name='profile_financial'),
    path('profile/comments/', views.profile_comments_view, name='profile_comments'),
    path('course/forex/', views.forex_course_view, name='forex_course'),
    path('course/smart-money/', views.smart_money_course_view, name='smart_money_course'),
    path('course/ict/', views.ict_course_view, name='ict_course'),
    path('course/private-mentorship/', views.private_mentorship_view, name='private_mentorship'),
    path('signals/gold/', views.gold_signal_view, name='gold_signal'),
    path('signals/crypto/', views.crypto_signal_view, name='crypto_signal'),
    path('broker/stb/', views.stb_broker_view, name='stb_broker'),

    # مسیرهای صفحات استاتیک (هاردکد شده)

    path('books/', views.books_view, name='books'),
    path('books/single/<int:item_id>/', views.books_single_view, name='books_single'),
    path('strategy/', views.strategy_view, name='strategy'),
    path('strategy/single/<int:item_id>/', views.strategy_single_view, name='strategy_single'),
    path('contact-us/', views.contact_us_view, name='contact_us'),
    path('employment/', views.employment_view, name='employment'),

    # === مسیرهای داینامیک (با آرگومان) ===
    path('course/<int:pk>/', views.course_detail_view, name='course_detail'),
    path('category/<slug:slug>/', views.course_category_view, name='course_category'),
    path('lecturer/<slug:username>/', views.lecturer_view, name='lecturer'),
    path('article/<slug:slug>/', views.article_detail_view, name='article_detail'),
    path('blog/category/<slug:slug>/', views.article_category_view, name='article_category'),
]