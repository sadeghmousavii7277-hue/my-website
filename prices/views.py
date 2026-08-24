# main/views.py
from django.http import JsonResponse
from bs4 import BeautifulSoup
import requests

# -------------------------------
# Helper functions
# -------------------------------
def fetch_crypto_prices():
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        # دریافت قیمت‌های کریپتو و تتر به تومان از صرافی ایرانی والکس
        wallex = requests.get("https://api.wallex.ir/v1/markets", headers=headers, timeout=5).json()
        btc = float(wallex['result']['symbols']['BTCUSDT']['stats']['lastPrice'])
        eth = float(wallex['result']['symbols']['ETHUSDT']['stats']['lastPrice'])
        usdt_tmn = float(wallex['result']['symbols']['USDTTMN']['stats']['lastPrice'])
        return [
            {"name": "بیت‌کوین", "price": f"{btc:,.0f} دلار"},
            {"name": "اتریوم", "price": f"{eth:,.0f} دلار"},
            {"name": "تتر", "price": f"{usdt_tmn:,.0f} تومان"},
        ]
    except:
        return [
            {"name": "بیت‌کوین", "price": "—"},
            {"name": "اتریوم", "price": "—"},
            {"name": "تتر", "price": "—"},
        ]

def fetch_tgju_prices():
    prices = {"gold": []}
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        url = "https://www.tgju.org/"
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        # طلا 18 عیار (قیمت در TGJU به ریال است، پس تقسیم بر 10 می‌شود)
        el = soup.find("tr", attrs={"data-market-row": "geram18"})
        if el:
            value_str = el.find("td", class_="nf").text.strip()
            if value_str != "—":
                value_int = int(value_str.replace(",", ""))
                toman = value_int // 10
                prices["gold"].append({"name": "طلای ۱۸ عیار", "price": f"{toman:,.0f} تومان"})
            else:
                prices["gold"].append({"name": "طلای ۱۸ عیار", "price": "—"})
    except:
        prices["gold"] = [{"name": "طلای ۱۸ عیار", "price": "—"}]

    return prices

# -------------------------------
# API اصلی
# -------------------------------
from django.core.cache import cache

def prices_api(request):
    data = cache.get('market_prices_data')
    if not data:
        data = {
            "crypto": fetch_crypto_prices(),
            **fetch_tgju_prices()  # currency + gold
        }
        # ذخیره اطلاعات به مدت یک ساعت (۳۶۰۰ ثانیه)
        cache.set('market_prices_data', data, 3600)
        
    return JsonResponse(data)
