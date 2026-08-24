from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from .sitemaps import StaticViewSitemap, BlogSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),

    # مسیر صفحه اصلی سایت (اپ main)
    path('', include('main.urls')),

    # مسیر اپ قیمت‌های لحظه‌ای
    path('market/', include('prices.urls')),

    # مسیر اپ وبلاگ
    path('blog/', include('blog.urls')),

    # مسیر ادیتور متن پیشرفته
    path('tinymce/', include('tinymce.urls')),

    # Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # Robots.txt
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
