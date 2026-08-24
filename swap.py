import os

with open('templates/home.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '<div class="space-y-8">' in line and start_idx == -1:
        start_idx = i
    if '</script>' in line and start_idx != -1 and i > start_idx + 10:
        end_idx = i + 2
        break

if start_idx != -1 and end_idx != -1:
    calc_block = lines[start_idx:end_idx]
    del lines[start_idx:end_idx]

    main_idx = -1
    for i, line in enumerate(lines):
        if '</main>' in line:
            main_idx = i
            break
            
    if main_idx != -1:
        wrapper = ['\n', '        <div class="max-w-7xl space-y-14 px-4 mx-auto">\n']
        end_wrapper = ['        </div>\n']
        lines = lines[:main_idx] + wrapper + calc_block + end_wrapper + lines[main_idx:]
        
    with open('templates/home.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print('Success')
else:
    print('Could not find calculator block')
