import os

base_dir = r'c:\Users\RV\Desktop\New folder (4)\mosavi\templates'
categories = ['tools_tradingview', 'tools_mt4', 'tools_mt5', 'books', 'strategy']
titles_map = {
    'tools_tradingview': 'اندیکاتور تریدینگ ویو',
    'tools_mt4': 'اندیکاتور متاتریدر 4',
    'tools_mt5': 'اندیکاتور متاتریدر 5',
    'books': 'کتاب و جزوه',
    'strategy': 'استراتژی'
}

html_template = """{{% extends 'base.html' %}}
{{% load static %}}

{{% block title %}}مشاهده جزئیات - {title_type}{{% endblock %}}

{{% block content %}}
<main class="flex-auto py-10">
    <div class="max-w-5xl px-4 mx-auto space-y-10">
        
        <!-- هدر مطلب -->
        <div class="bg-secondary rounded-2xl p-6 md:p-10 shadow-lg border border-border grid grid-cols-1 md:grid-cols-12 gap-8 items-start">
            
            <!-- تصویر شاخص -->
            <div class="md:col-span-5 lg:col-span-4">
                <img src="{{% static 'assets/images/IMG_6637.JPEG' %}}" alt="تصویر شاخص" class="w-full h-auto object-cover rounded-xl shadow-md border border-border">
            </div>
            
            <!-- اطلاعات و دانلود -->
            <div class="md:col-span-7 lg:col-span-8 space-y-6">
                <div class="space-y-3">
                    <span class="inline-flex items-center justify-center px-3 py-1 bg-primary/10 text-primary text-xs font-bold rounded-full">
                        {title_type}
                    </span>
                    <h1 class="font-black text-2xl md:text-3xl lg:text-4xl text-foreground leading-tight">
                        نام آیتم شماره {{{{ item_id|default:"1" }}}}
                    </h1>
                </div>
                
                <p class="text-muted leading-relaxed text-sm md:text-base text-justify">
                    توضیحات کوتاه و مفید در مورد این مورد. در این بخش شما می‌توانید یک مرور کلی بر عملکرد این ابزار داشته باشید و متوجه شوید که چگونه در تحلیل‌های شما کمک خواهد کرد. این متن به گونه‌ای تنظیم شده که در نمایشگرهای مختلف به خوبی خوانده شود و فضای مناسبی را اشغال کند.
                </p>
                
                <div class="pt-6 border-t border-border flex flex-col sm:flex-row gap-4">
                    <a href="#" class="inline-flex items-center justify-center gap-2 px-8 py-3.5 bg-primary text-primary-foreground rounded-xl font-bold transition-all hover:bg-primary/90 shadow-lg shadow-primary/30 hover:shadow-primary/50">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-5 h-5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3" />
                        </svg>
                        دانلود فایل 
                    </a>
                </div>
            </div>
        </div>

        <!-- محتوای کامل -->
        <div class="bg-secondary rounded-2xl p-6 md:p-10 shadow-lg border border-border space-y-8 text-foreground leading-relaxed">
            <div class="flex items-center gap-3 mb-6">
                <span class="flex items-center justify-center w-10 h-10 bg-primary/10 text-primary rounded-lg">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z" />
                    </svg>
                </span>
                <h2 class="font-bold text-xl md:text-2xl">توضیحات تکمیلی و آموزش استفاده</h2>
            </div>
            
            <p class="text-justify">
                در این قسمت می‌توانید محتوای کامل، نحوه نصب، تنظیمات پیشنهادی و تصاویر تکمیلی را قرار دهید. این بخش به صورت کاملاً استاتیک طراحی شده تا هر محتوایی که نیاز دارید به راحتی در اینجا جایگذاری کنید. 
            </p>
            
            <div class="bg-background/50 p-6 rounded-xl border border-border">
                <h3 class="font-bold text-lg mb-4 text-primary">ویژگی‌های کلیدی:</h3>
                <ul class="list-disc list-inside space-y-3 text-muted marker:text-primary">
                    <li>شناسایی دقیق نقاط ورود و خروج</li>
                    <li>محیط کاربری ساده و قابل فهم برای افراد مبتدی</li>
                    <li>قابل استفاده در تمامی تایم فریم‌های معاملاتی</li>
                    <li>تست شده و بدون خطای محاسباتی (No Repaint)</li>
                </ul>
            </div>

            <div class="my-10 rounded-xl overflow-hidden border border-border shadow-md">
                <img src="{{% static 'assets/images/IMG_6643.JPEG' %}}" alt="تصویر محیط افزونه" class="w-full h-auto object-cover">
            </div>
            
            <p class="text-justify">
                برای استفاده بهینه‌تر، حتماً ویدیوهای آموزشی مرتبط با نحوه راه‌اندازی را در کانال آکادمی مشاهده کنید تا بالاترین بازدهی را دریافت نمایید.
            </p>
        </div>

    </div>
</main>
{{% endblock content %}}
"""

for cat in categories:
    filepath = os.path.join(base_dir, f'{cat}_single.html')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_template.format(title_type=titles_map[cat]))
print('Rewritten all single pages with grid layout.')
