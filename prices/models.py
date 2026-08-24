from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام ارز")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="قیمت")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    class Meta:
        verbose_name = "ارز"
        verbose_name_plural = "ارزها"

    def __str__(self):
        return f"{self.name} - {self.price}"

class Coin(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام سکه")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="قیمت")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    class Meta:
        verbose_name = "سکه"
        verbose_name_plural = "سکه ها"

    def __str__(self):
        return f"{self.name} - {self.price}"