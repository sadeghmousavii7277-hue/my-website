import os
import re

books_file = 'templates/books.html'
strategy_file = 'templates/strategy.html'

def update_books():
    with open(books_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_str = '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 w-full">'
    end_str = '        </div>\n    </div>\n</main>'
    
    start_idx = content.find(start_str)
    end_idx = content.rfind(end_str)
    
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx + len(start_str)] + """
            
            {% for book in books %}
            <div class="bg-secondary rounded-xl overflow-hidden shadow-md hover:shadow-xl transition-all duration-300 border border-border flex flex-col h-full">
                <a target="_blank" href="{% url 'books_single' book.id %}" class="block overflow-hidden relative group">
                    {% if book.image %}
                    <img src="{{ book.image.url }}" alt="{{ book.title }}" class="w-full h-56 object-cover rounded-t-xl transition-transform duration-500 group-hover:scale-110">
                    {% else %}
                    <div class="w-full h-56 bg-gray-200 flex items-center justify-center rounded-t-xl"><span class="text-gray-400">بدون تصویر</span></div>
                    {% endif %}
                </a>
                <div class="p-5 space-y-3 flex flex-col flex-grow justify-between">
                    <div>
                        <h3 class="font-bold text-lg text-foreground mb-2">
                            <a target="_blank" href="{% url 'books_single' book.id %}" class="transition-colors hover:text-primary">{{ book.title }}</a>
                        </h3>
                        <p class="text-sm text-muted leading-relaxed line-clamp-3">
                            {{ book.description }}
                        </p>
                    </div>
                    <div class="pt-4 border-t border-border mt-4">
                        <a target="_blank" href="{% url 'books_single' book.id %}" class="flex items-center justify-center w-full py-2 bg-primary text-primary-foreground rounded-lg font-bold transition-all hover:bg-primary/90 shadow-md shadow-primary/20 hover:shadow-primary/40">
                            مشاهده و دانلود
                        </a>
                    </div>
                </div>
            </div>
            {% empty %}
            <div class="col-span-full text-center text-muted py-10">
                هیچ کتاب یا جزوه‌ای یافت نشد.
            </div>
            {% endfor %}

""" + content[end_idx:]
        with open(books_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated books.html")

def update_strategy():
    with open(strategy_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_str = '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 w-full">'
    end_str = '        </div>\n    </div>\n</main>'
    
    start_idx = content.find(start_str)
    end_idx = content.rfind(end_str)
    
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx + len(start_str)] + """
            
            {% for strategy in strategies %}
            <div class="bg-secondary rounded-xl overflow-hidden shadow-md hover:shadow-xl transition-all duration-300 border border-border flex flex-col h-full">
                <a target="_blank" href="{% url 'strategy_single' strategy.id %}" class="block overflow-hidden relative group">
                    {% if strategy.image %}
                    <img src="{{ strategy.image.url }}" alt="{{ strategy.title }}" class="w-full h-56 object-cover rounded-t-xl transition-transform duration-500 group-hover:scale-110">
                    {% else %}
                    <div class="w-full h-56 bg-gray-200 flex items-center justify-center rounded-t-xl"><span class="text-gray-400">بدون تصویر</span></div>
                    {% endif %}
                </a>
                <div class="p-5 space-y-3 flex flex-col flex-grow justify-between">
                    <div>
                        <h3 class="font-bold text-lg text-foreground mb-2">
                            <a target="_blank" href="{% url 'strategy_single' strategy.id %}" class="transition-colors hover:text-primary">{{ strategy.title }}</a>
                        </h3>
                        <p class="text-sm text-muted leading-relaxed line-clamp-3">
                            {{ strategy.description }}
                        </p>
                    </div>
                    <div class="pt-4 border-t border-border mt-4">
                        <a target="_blank" href="{% url 'strategy_single' strategy.id %}" class="flex items-center justify-center w-full py-2 bg-primary text-primary-foreground rounded-lg font-bold transition-all hover:bg-primary/90 shadow-md shadow-primary/20 hover:shadow-primary/40">
                            مشاهده و دانلود
                        </a>
                    </div>
                </div>
            </div>
            {% empty %}
            <div class="col-span-full text-center text-muted py-10">
                هیچ استراتژی یافت نشد.
            </div>
            {% endfor %}

""" + content[end_idx:]
        with open(strategy_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated strategy.html")

update_books()
update_strategy()
