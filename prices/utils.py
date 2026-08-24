# prices/utils.py
import requests
from bs4 import BeautifulSoup

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def fetch_tgju_prices():
    prices = {"currency": [], "gold": []}

    url = "https://www.tgju.org/"
    res = requests.get(url, headers=UA, timeout=10)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    # ارز آزاد (ستون «قیمت زنده»)
    currency_ids = {
        "price_dollar": "دلار",
        "price_eur": "یورو",
        "price_gbp": "پوند انگلیس",
        "price_aed": "درهم امارات",
        "price_try": "لیر ترکیه",
    }
    for cid, name in currency_ids.items():
        row = soup.find("tr", id=cid)
        if not row:
            continue
        # اولین سلول عددیِ ردیف همان «قیمت زنده» است
        cell = row.find("td", class_="nf")
        if cell:
            prices["currency"].append({"name": name, "price": cell.get_text(strip=True)})

    # طلا و سکه
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
        if not row:
            continue
        cell = row.find("td", class_="nf")
        if cell:
            prices["gold"].append({"name": name, "price": cell.get_text(strip=True)})

    return prices
