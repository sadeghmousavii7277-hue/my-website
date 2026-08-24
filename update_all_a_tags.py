import os
import re

base_dir = r'c:\Users\RV\Desktop\New folder (4)\mosavi\templates'

def replace_a_tag(match):
    tag = match.group(0)
    # Check if target already exists
    if re.search(r'\btarget\s*=', tag, re.IGNORECASE):
        return tag
    # Check if href is '#' or javascript
    href_match = re.search(r'href\s*=\s*["\']([^"\']*)["\']', tag, re.IGNORECASE)
    if href_match:
        href = href_match.group(1).strip()
        if href.startswith('#') or href.startswith('javascript:'):
            return tag
    # Insert target="_blank" after '<a '
    return re.sub(r'^<\s*a\b', '<a target="_blank"', tag, flags=re.IGNORECASE)

modified_files = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Match <a ... > tags
            new_content = re.sub(r'<\s*a\b[^>]*>', replace_a_tag, content, flags=re.IGNORECASE)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                modified_files += 1

print(f"Updated links in {modified_files} HTML files.")
