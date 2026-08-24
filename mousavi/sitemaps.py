from django.contrib import sitemaps
from django.urls import reverse
from blog.models import Post  # Assuming there's a Post model in blog

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return ['home', 'contact_us', 'strategy', 'books', 'risk_calculator', 'economic_calendar', 'employment', 'forex_course', 'smart_money_course', 'ict_course', 'private_mentorship', 'gold_signal', 'crypto_signal', 'stb_broker']

    def location(self, item):
        try:
            return reverse(item)
        except Exception:
            # اگر مسیری یافت نشد، از خطا جلوگیری می‌کنیم
            return '/'

class BlogSitemap(sitemaps.Sitemap):
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        try:
            return Post.objects.filter(status='published') # Adjust filter as per actual model
        except:
            return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at if hasattr(obj, 'updated_at') else obj.created_at if hasattr(obj, 'created_at') else None

    def location(self, obj):
        if hasattr(obj, 'get_absolute_url'):
            return obj.get_absolute_url()
        return f'/blog/post/{obj.slug}/' if hasattr(obj, 'slug') else f'/blog/post/{obj.id}/'
