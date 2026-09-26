from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django.http import HttpResponse
from .sitemaps import StaticViewSitemap, BlogSitemap

from blog import views as blog_views

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),

    # اندپوینت انتشار خودکار مقالات از n8n
    path('api/articles/create/', blog_views.create_article_api, name='api_create_article'),

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

    # تاییدیه اینماد
    path('18634421.txt', csrf_exempt(lambda request: HttpResponse("18634421", content_type="text/plain; charset=utf-8"))),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
