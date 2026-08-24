from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True, verbose_name="نامک (Slug)")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان برچسب")
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True, verbose_name="نامک (Slug)")

    class Meta:
        verbose_name = "برچسب"
        verbose_name_plural = "برچسب‌ها"

    def __str__(self):
        return self.title

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'پیش‌نویس'),
        ('published', 'منتشر شده'),
    )

    title = models.CharField(max_length=250, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=250, unique=True, allow_unicode=True, verbose_name="نامک (Slug)")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name="نویسنده")
    
    excerpt = models.TextField(max_length=500, verbose_name="توضیح کوتاه (Excerpt)")
    content = HTMLField(verbose_name="محتوای مقاله")
    
    thumbnail = models.ImageField(upload_to='blog/thumbnails/', verbose_name="تصویر شاخص")
    thumbnail_alt = models.CharField(max_length=200, blank=True, verbose_name="متن جایگزین تصویر (Alt Text)")
    views = models.PositiveIntegerField(default=0, verbose_name="تعداد بازدید")
    
    categories = models.ManyToManyField(Category, related_name='posts', verbose_name="دسته‌بندی‌ها")
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True, verbose_name="برچسب‌ها")
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="وضعیت")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="تاریخ آخرین بروزرسانی")
    
    meta_title = models.CharField(max_length=250, blank=True, verbose_name="عنوان سئو (Meta Title)")
    meta_description = models.TextField(blank=True, verbose_name="توضیحات سئو (Meta Description)")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
