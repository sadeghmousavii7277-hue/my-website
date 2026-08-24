from django.db import models

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان کتاب")
    description = models.TextField(verbose_name="توضیحات کوتاه")
    content = models.TextField(verbose_name="محتوای کامل", blank=True, null=True)
    link = models.URLField(max_length=500, verbose_name="لینک دانلود/مشاهده", blank=True, null=True)
    image = models.ImageField(upload_to='books/', verbose_name="تصویر کتاب", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    views = models.PositiveIntegerField(default=0, verbose_name="تعداد بازدید")

    class Meta:
        verbose_name = "کتاب و جزوه"
        verbose_name_plural = "کتاب‌ها و جزوه‌ها"

    def __str__(self):
        return self.title

class Strategy(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان استراتژی")
    description = models.TextField(verbose_name="توضیحات کوتاه")
    content = models.TextField(verbose_name="محتوای کامل", blank=True, null=True)
    link = models.URLField(max_length=500, verbose_name="لینک ویدیو/مشاهده", blank=True, null=True)
    image = models.ImageField(upload_to='strategies/', verbose_name="تصویر استراتژی", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    views = models.PositiveIntegerField(default=0, verbose_name="تعداد بازدید")

    class Meta:
        verbose_name = "استراتژی"
        verbose_name_plural = "استراتژی‌ها"

    def __str__(self):
        return self.title

from django.utils import timezone

class SiteVisit(models.Model):
    date = models.DateField(default=timezone.now, unique=True, verbose_name="تاریخ")
    count = models.PositiveIntegerField(default=0, verbose_name="تعداد بازدید")

    class Meta:
        verbose_name = "بازدید سایت"
        verbose_name_plural = "بازدیدهای سایت"

    def __str__(self):
        return f"{self.date} - {self.count}"
