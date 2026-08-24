import requests
from bs4 import BeautifulSoup
from celery import shared_task
from decimal import Decimal
from .models import Currency, Coin  # ایمپورت مدل‌ها از اپلیکیشن فعلی

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def clean_price(price_str):
    """ '۵۵,۴۰۰' را تمیز و به Decimal تبدیل می‌کند """
    if not price_str or price_str.strip() in ['—', '']:
        return None
    # تبدیل اعداد فارسی/عربی به انگلیسی
    persian_to_english = str.maketrans('۰۱۲۳۴۵۶۷۸۹', '0123456789')
    price_str = price_str.translate(persian_to_english)
    # حذف کاما
    price_str = price_str.replace(',', '')
    try:
        return Decimal(price_str)
    except Exception:
        return None


@shared_task
def update_prices_from_tgju():
    """ وظیفه Celery: واکشی قیمت‌ها و ذخیره در دیتابیس """
    url = "https://www.tgju.org/"

    try:
        res = requests.get(url, headers=UA, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        # === واکشی ارزها ===
        currency_ids = {
            "price_dollar": "دلار",
            "price_eur": "یورو",
            "price_gbp": "پوند انگلیس",
            "price_aed": "درهم امارات",
            "price_try": "لیر ترکیه",
        }
        for cid, name in currency_ids.items():
            row = soup.find("tr", id=cid)
            if not row: continue
            cell = row.find("td", class_="nf")
            if cell:
                price_val = clean_price(cell.get_text(strip=True))
                if price_val is not None:
                    # قیمت را پیدا و آپدیت می‌کند، یا یک رکورد جدید می‌سازد
                    Currency.objects.update_or_create(
                        name=name,
                        defaults={'price': price_val}
                    )

        # === واکشی طلا و سکه ===
        gold_ids = {
            "sekee": "سکه امامی",
            "sekeb": "سکه بهار آزادی",
            "nim": "نیم سکه",
            "rob": "ربع سکه",
            "gerami": "سکه گرمی",
            "geram18": "هر گرم طلای ۱۸ عیار",
        }
        for gid, name in gold_ids.items():
            row = soup.find("tr", id=gid)
            if not row: continue
            cell = row.find("td", class_="nf")
            if cell:
                price_val = clean_price(cell.get_text(strip=True))
                if price_val is not None:
                    Coin.objects.update_or_create(
                        name=name,
                        defaults={'price': price_val}
                    )

        return "Price update successful"

    except Exception as e:
        # در صورت خطا، تسک شکست می‌خورد و ما می‌توانیم آن را در Celery مانیتور کنیم
        print(f"⚠️ خطای Celery در واکشی قیمت: {e}")
        raise