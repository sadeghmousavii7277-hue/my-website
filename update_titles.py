import os
import re

base_dir = r'c:\Users\RV\Desktop\New folder (4)\mosavi\templates'
categories = ['tools_tradingview', 'tools_mt4', 'tools_mt5', 'books', 'strategy']

for cat in categories:
    filepath = os.path.join(base_dir, f'{cat}_single.html')
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace <h1 class="font-black text-2xl md:text-3xl text-foreground">نام اندیکاتور شماره ۱</h1>
    # with <h1 class="font-black text-2xl md:text-3xl text-foreground">نام آیتم شماره {{ item_id|default:"1" }}</h1>
    
    # Or just replace 'شماره ۱' with 'شماره {{ item_id|default:"1" }}'
    content = content.replace('شماره ۱', 'شماره {{ item_id|default:"1" }}')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
print('Updated titles in single pages.')
