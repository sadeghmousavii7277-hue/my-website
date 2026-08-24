from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def price_box(request):
    prices = {"currency": [], "gold": []}
    UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    try:
        url = "https://www.tgju.org/"
        res = requests.get(url, headers=UA, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        # === 📊 نرخ ارز آزاد ===
        currency_ids = {
            "price_dollar": "دلار",
            "price_eur": "یورو",
            "price_gbp": "پوند انگلیس",
            "price_aed": "درهم امارات",
            "price_try": "لیر ترکیه",
        }

        for cid, name in currency_ids.items():
            el = soup.find("tr", id=cid)
            if el:
                val_el = el.find("td", class_="nf")
                if val_el:
                    value = val_el.text.strip()
                    prices["currency"].append({"name": name, "price": value})

        # === 🪙 نرخ طلا و سکه ===
        gold_ids = {
            "sekee": "سکه امامی",
            "sekeb": "سکه بهار آزادی",
            "nim": "نیم سکه",
            "rob": "ربع سکه",
            "gerami": "سکه گرمی",
            "geram18": "هر گرم طلای ۱۸ عیار",
        }

        for gid, name in gold_ids.items():
            el = soup.find("tr", id=gid)
            if el:
                val_el = el.find("td", class_="nf")
                if val_el:
                    value = val_el.text.strip()
                    prices["gold"].append({"name": name, "price": value})

    except Exception as e:
        print("⚠️ TGJU fetch error:", e)

    # در صورت خالی بودن
    if not prices["currency"]:
        prices["currency"] = [{"name": n, "price": "—"} for n in currency_ids.values()]
    if not prices["gold"]:
        prices["gold"] = [{"name": n, "price": "—"} for n in gold_ids.values()]

    return render(request, "box.html", {"prices": prices})
