import os
import re

base_dir = r'c:\Users\RV\Desktop\New folder (4)\mosavi\templates'
categories = ['tools_tradingview', 'tools_mt4', 'tools_mt5', 'books', 'strategy']

for cat in categories:
    filepath = os.path.join(base_dir, f'{cat}.html')
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    target = f"{{% url '{cat}_single' %}}"
    
    parts = content.split('<!-- آیتم ۲ -->')
    if len(parts) == 2:
        part1 = parts[0]
        part2_3 = parts[1].split('<!-- آیتم ۳ -->')
        part2 = part2_3[0]
        part3 = part2_3[1]
        
        part1 = part1.replace(target, f"{{% url '{cat}_single' 1 %}}")
        part2 = part2.replace(target, f"{{% url '{cat}_single' 2 %}}")
        part3 = part3.replace(target, f"{{% url '{cat}_single' 3 %}}")
        
        content = part1 + '<!-- آیتم ۲ -->' + part2 + '<!-- آیتم ۳ -->' + part3
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
print('Updated links in categories.')
