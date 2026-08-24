# main/views.py
import requests
import json
import threading
import logging
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

logger = logging.getLogger(__name__)


def send_signup_webhook_async(name, phone, registered_at=None):
    """
    ارسال غیرهمگام (Async / Background) اطلاعات ثبت‌نام کاربر به آدرس وبهوک.
    عملیات در یک Thread پس‌زمینه اجرا شده و خطاها در بلوک try/except مدیریت می‌شوند
    تا مانع یا تأخیری در فرآیند ثبت‌نام و لاگین کاربر ایجاد نشود.
    """
    if registered_at is None:
        registered_at = timezone.now().isoformat()

    webhook_url = getattr(
        settings,
        'USER_SIGNUP_WEBHOOK_URL',
        'https://carry-doctor-gentleman-lance.trycloudflare.com/webhook/user-signup'
    )

    def _post():
        try:
            payload = {
                "name": name,
                "phone": phone,
                "registered_at": registered_at
            }
            headers = {
                "Content-Type": "application/json"
            }
            requests.post(webhook_url, json=payload, headers=headers, timeout=10)
        except Exception as e:
            logger.warning(f"Failed to send signup webhook: {e}")

    threading.Thread(target=_post, daemon=True).start()



# =========================================
# ویوهای اصلی و استاتیک
# =========================================

def home_view(request):
    """
    صفحه اصلی + قیمت لحظه‌ای رمزارزها (دلار) از CoinGecko
    """
    crypto_ids = {
        "bitcoin": "بیت‌کوین",
        "ethereum": "اتریوم",
        "binancecoin": "بایننس‌کوین",
        "dogecoin": "دوج‌کوین",
        "ripple": "ریپل",
    }

    crypto_rows = []
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": ",".join(crypto_ids.keys()),
            "vs_currencies": "usd",
            "include_24hr_change": "true",
        }
        res = requests.get(url, params=params, timeout=10)
        data = res.json()

        for key, name in crypto_ids.items():
            if key in data:
                crypto_rows.append({
                    "symbol": key.upper()[:3],
                    "name": name,
                    "price_usd": f"{data[key]['usd']:,.2f}",
                    "change": data[key].get("usd_24h_change", 0),
                })
    except Exception as e:
        print("⚠️ خطا در دریافت داده از CoinGecko:", e)

    return render(request, "home.html", {"crypto_rows": crypto_rows})


def blog_view(request):
    """
    صفحه لیست تمام مقالات (بلاگ) را نشان می‌دهد.
    """
    return HttpResponse("اینجا صفحه لیست مقالات (بلاگ) است.")


def series_view(request):
    """
    صفحه لیست تمام دوره‌ها (سری‌های آموزشی) را نشان می‌دهد.
    """
    return HttpResponse("اینجا صفحه لیست همه دوره‌ها است.")


def cart_view(request):
    """
    صفحه سبد خرید کاربر و خریدهای پیشین را نشان می‌دهد.
    """
    return render(request, "cart.html")


def forex_course_view(request):
    """
    صفحه دوره جامع صفر تا صد فارکس
    """
    return render(request, 'partials/forex_course.html')


def smart_money_course_view(request):
    """
    صفحه دوره اسمارت مانی
    """
    return render(request, 'partials/smart_money_course.html')


def ict_course_view(request):
    """
    صفحه دوره جامع صفر تا صد ICT
    """
    return render(request, 'partials/ict_course.html')


def private_mentorship_view(request):
    """
    صفحه منتورشیپ خصوصی
    """
    return render(request, 'partials/private_mentorship.html')


def gold_signal_view(request):
    """
    صفحه سیگنال طلا (فارکس)
    """
    return render(request, 'partials/gold_signal.html')


def crypto_signal_view(request):
    """
    صفحه سیگنال فیوچرز کریپتو
    """
    return render(request, 'partials/crypto_signal.html')

def stb_broker_view(request):
    return render(request, 'partials/stb_broker.html')

from django.template.exceptions import TemplateDoesNotExist

# =========================================
# ویوهای صفحات استاتیک (هاردکد شده)
# =========================================


from django.shortcuts import render, get_object_or_404
from .models import Book, Strategy

def books_view(request):
    books = Book.objects.all().order_by('-created_at')
    return render(request, 'books.html', {'books': books})

def books_single_view(request, item_id):
    book_data = get_object_or_404(Book, id=item_id)
    book_data.views += 1
    book_data.save(update_fields=['views'])
    return render(request, 'books_single.html', {'book': book_data})

def strategy_view(request):
    strategies = Strategy.objects.all().order_by('-created_at')
    return render(request, 'strategy.html', {'strategies': strategies})

def strategy_single_view(request, item_id):
    strategy_data = get_object_or_404(Strategy, id=item_id)
    strategy_data.views += 1
    strategy_data.save(update_fields=['views'])
    return render(request, 'strategy_single.html', {'strategy': strategy_data})

def contact_us_view(request):
    return render(request, 'contact_us.html')

def employment_view(request):
    return render(request, 'employment.html')

# =========================================
# ویوهای بخش پروفایل کاربر
# =========================================

@login_required(login_url='/')
def profile_view(request):
    return render(request, 'dashboard/profile.html')


@login_required(login_url='/')
def profile_courses_view(request):
    return render(request, 'dashboard/courses.html')


@login_required(login_url='/')
def profile_financial_view(request):
    return render(request, 'dashboard/financial.html')


@login_required(login_url='/')
def profile_comments_view(request):
    return render(request, 'dashboard/comments.html')

# =========================================
# ویوهای احراز هویت (AJAX)
# =========================================

@csrf_exempt
def login_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            phone = data.get('phone')
            password = data.get('password')
            
            # Since phone is stored in username
            user = authenticate(request, username=phone, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'success', 'message': 'با موفقیت وارد شدید'})
            else:
                return JsonResponse({'status': 'error', 'message': 'شماره موبایل یا رمز عبور اشتباه است'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'})


@csrf_exempt
def register_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            phone = data.get('phone')
            name = data.get('name')
            password = data.get('password')
            
            if User.objects.filter(username=phone).exists():
                return JsonResponse({'status': 'error', 'message': 'این شماره موبایل قبلا ثبت نام کرده است'})
                
            user = User.objects.create_user(username=phone, password=password, first_name=name)
            user.save()
            
            # ارسال اطلاعات ثبت‌نام به وب‌هوک به صورت پس‌زمینه و غیرهمگام
            send_signup_webhook_async(name=name, phone=phone)

            # Log the user in immediately after registration
            user = authenticate(request, username=phone, password=password)
            if user is not None:
                login(request, user)
            
            return JsonResponse({'status': 'success', 'message': 'ثبت نام با موفقیت انجام شد'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'})

@csrf_exempt
def logout_api(request):
    logout(request)
    return JsonResponse({'status': 'success', 'message': 'خروج موفقیت آمیز'})

@csrf_exempt
def newsletter_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            
            if not email or '@' not in email:
                return JsonResponse({'status': 'error', 'message': 'لطفاً ایمیل معتبری وارد کنید'})
                
            from .models import Newsletter
            if Newsletter.objects.filter(email=email).exists():
                return JsonResponse({'status': 'error', 'message': 'این ایمیل قبلاً ثبت شده است'})
                
            Newsletter.objects.create(email=email)
            return JsonResponse({'status': 'success', 'message': 'ایمیل شما با موفقیت ثبت شد'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'})


# =========================================
# ویوهای داینامیک (که آرگومان می‌گیرند)
# =========================================

def course_detail_view(request, pk):
    return HttpResponse(f"اینجا جزئیات دوره با آیدی {pk} است.")


def course_category_view(request, slug):
    return HttpResponse(f"اینجا لیست دوره‌های دسته‌بندی '{slug}' است.")


def lecturer_view(request, username):
    return HttpResponse(f"اینجا صفحه پروفایل مدرس با نام کاربری '{username}' است.")


def article_detail_view(request, slug):
    return HttpResponse(f"اینجا جزئیات مقاله با اسلاگ '{slug}' است.")


def article_category_view(request, slug):
    return HttpResponse(f"اینجا لیست مقالات دسته‌بندی '{slug}' است.")

# =========================================
# Manager Dashboard
# =========================================
from django.contrib.auth.decorators import user_passes_test
from django.utils import timezone
from django.db.models import Sum
from .models import SiteVisit, Newsletter, Book, Strategy
from blog.models import Post

def manager_check(user):
    return user.is_active and (user.is_superuser or user.groups.filter(name='Manager').exists())

@user_passes_test(manager_check, login_url='/admin/login/')
def manager_dashboard(request):
    total_users = User.objects.count()
    total_newsletters = Newsletter.objects.count()
    
    today = timezone.now().date()
    daily_visit_obj = SiteVisit.objects.filter(date=today).first()
    daily_visits = daily_visit_obj.count if daily_visit_obj else 0
    
    current_month = today.month
    current_year = today.year
    monthly_visits = SiteVisit.objects.filter(date__year=current_year, date__month=current_month).aggregate(Sum('count'))['count__sum'] or 0

    users_list = User.objects.all().order_by('-date_joined')
    
    top_posts = Post.objects.all().order_by('-views')[:5]
    top_strategies = Strategy.objects.all().order_by('-views')[:5]
    top_books = Book.objects.all().order_by('-views')[:5]
    
    context = {
        'total_users': total_users,
        'total_newsletters': total_newsletters,
        'daily_visits': daily_visits,
        'monthly_visits': monthly_visits,
        'users_list': users_list,
        'top_posts': top_posts,
        'top_strategies': top_strategies,
        'top_books': top_books,
    }
    return render(request, 'manager_dashboard.html', context)


def risk_calculator_view(request):
    """
    نمایش ماشین حساب مدیریت ریسک برای بهینه‌سازی سئو
    """
    return render(request, 'risk_calculator.html')


def economic_calendar_view(request):
    """
    نمایش تقویم اقتصادی اختصاصی
    """
    return render(request, 'economic_calendar.html')