# main/views.py
from django.shortcuts import render
from django.http import HttpResponse

# =========================================
# ویوهای اصلی و استاتیک
# =========================================

def home_view(request):
    """
    صفحه اصلی را رندر می‌کند.
    """
    # شما از قبل این ویو را داشتید و به 'home.html' متصل بود
    return render(request, 'home.html')

def blog_view(request):
    """
    صفحه لیست تمام مقالات (بلاگ) را نشان می‌دهد.
    """
    # بعداً باید یک قالب 'blog.html' بسازید
    return HttpResponse("اینجا صفحه لیست مقالات (بلاگ) است.")

def series_view(request):
    """
    صفحه لیست تمام دوره‌ها (سری‌های آموزشی) را نشان می‌دهد.
    """
    # بعداً باید یک قالب 'series.html' بسازید
    return HttpResponse("اینجا صفحه لیست همه دوره‌ها است.")

def cart_view(request):
    """
    صفحه سبد خرید کاربر را نشان می‌دهد.
    """
    # بعداً باید یک قالب 'cart.html' بسازید
    return HttpResponse("اینجا صفحه سبد خرید است.")

# =========================================
# ویوهای بخش پروفایل کاربر
# =========================================

def profile_view(request):
    """
    صفحه اصلی پروفایل کاربر.
    """
    # بعداً باید یک قالب 'profile.html' بسازید
    return HttpResponse("اینجا صفحه اصلی پروفایل کاربر است.")

def profile_courses_view(request):
    """
    صفحه "دوره‌های من" در پروفایل کاربر.
    """
    # بعداً باید یک قالب 'profile_courses.html' بسازید
    return HttpResponse("اینجا لیست دوره‌های کاربر است.")

def profile_financial_view(request):
    """
    صفحه "مالی" در پروفایل کاربر.
    """
    # بعداً باید یک قالب 'profile_financial.html' بسازید
    return HttpResponse("اینجا بخش مالی پروفایل کاربر است.")

def profile_comments_view(request):
    """
    صفحه "پرسش و دیدگاه‌ها" در پروفایل کاربر.
    """
    # بعداً باید یک قالب 'profile_comments.html' بسازید
    return HttpResponse("اینجا پرسش‌ها و دیدگاه‌های کاربر است.")

# =========================================
# ویوهای داینامیک (که آرگومان می‌گیرند)
# =========================================

def course_detail_view(request, pk):
    """
    جزئیات یک دوره خاص را بر اساس ID (pk) نشان می‌دهد.
    """
    # در قالب، {% url 'course_detail' 1 %} عدد 1 را به عنوان 'pk' به اینجا می‌فرستد
    return HttpResponse(f"اینجا جزئیات دوره با آیدی {pk} است.")

def course_category_view(request, slug):
    """
    لیست دوره‌های یک دسته‌بندی خاص را بر اساس slug نشان می‌دهد.
    """
    # در قالب، {% url 'course_category' 'frontend' %} رشته 'frontend' را به عنوان 'slug' به اینجا می‌فرستد
    return HttpResponse(f"اینجا لیست دوره‌های دسته‌بندی '{slug}' است.")

def lecturer_view(request, username):
    """
    صفحه پروفایل یک مدرس خاص را بر اساس نام کاربری (یا اسلاگ) نشان می‌دهد.
    """
    # در قالب، {% url 'lecturer' 'jalal-bahrami' %} رشته 'jalal-bahrami' را به عنوان 'username' به اینجا می‌فرستد
    return HttpResponse(f"اینجا صفحه پروفایل مدرس با نام کاربری '{username}' است.")

def article_detail_view(request, slug):
    """
    جزئیات یک مقاله خاص را بر اساس slug نشان می‌دهد.
    """
    # در قالب، {% url 'article_detail' 'react-next-course' %} رشته 'react-next-course' را به عنوان 'slug' به اینجا می‌فرستد
    return HttpResponse(f"اینجا جزئیات مقاله با اسلاگ '{slug}' است.")

def article_category_view(request, slug):
    """
    لیست مقالات یک دسته‌بندی خاص را بر اساس slug نشان می‌دهد.
    """
    # در قالب، {% url 'article_category' 'frontend' %} رشته 'frontend' را به عنوان 'slug' به اینجا می‌فرستد
    return HttpResponse(f"اینجا لیست مقالات دسته‌بندی '{slug}' است.")