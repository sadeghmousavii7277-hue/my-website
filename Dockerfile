# 1️⃣ پایه پایتون
FROM python:3.11-slim

# 2️⃣ مسیر کاری
WORKDIR /app

# 3️⃣ نصب dependencies موردنیاز
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 4️⃣ کپی requirements و نصب پکیج‌ها
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ کپی کل پروژه
COPY . /app/

# 6️⃣ تنظیم متغیرهای محیطی
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 7️⃣ باز کردن پورت Gunicorn
EXPOSE 8000

# 8️⃣ جمع‌آوری فایل‌های استاتیک
RUN python manage.py collectstatic --noinput

# 9️⃣ اجرای Gunicorn
CMD ["gunicorn", "mousavi.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]

