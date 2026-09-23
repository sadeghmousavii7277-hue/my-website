import os
import json
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.text import slugify
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from .models import Post, Category, Tag

DEFAULT_API_KEY = 'your-very-secure-secret-token-12345'


def post_list(request):
    posts_list = Post.objects.filter(status='published').order_by('-published_date')
    
    # Pagination - 9 posts per page
    paginator = Paginator(posts_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    
    post.views += 1
    post.save(update_fields=['views'])
    
    # Related posts (by category or tags)
    related_posts = Post.objects.filter(
        status='published',
        categories__in=post.categories.all()
    ).exclude(id=post.id).distinct()[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)


import uuid
import time

def _get_unique_slug(model, text, max_len=150):
    base_slug = slugify(text, allow_unicode=True) or 'item'
    base_slug = base_slug[:max_len - 10]
    slug = base_slug
    counter = 1
    while model.objects.filter(slug=slug).exists():
        slug = f"{base_slug[:max_len - 10]}-{counter}"
        counter += 1
    return slug


def _get_unique_post_slug(raw_slug, title):
    base_slug = ''
    if raw_slug and raw_slug.strip():
        # First try ascii slugify for English slug as specified
        base_slug = slugify(raw_slug.strip(), allow_unicode=False)
        if not base_slug:
            base_slug = slugify(raw_slug.strip(), allow_unicode=True)

    if not base_slug:
        base_slug = slugify(title, allow_unicode=False)

    if not base_slug:
        # If title is in Persian and no english slug was provided
        base_slug = f"post-{int(time.time())}"

    base_slug = base_slug[:230]
    slug = base_slug
    counter = 1
    while Post.objects.filter(slug=slug).exists():
        slug = f"{base_slug[:220]}-{counter}"
        counter += 1
    return slug



@csrf_exempt
def create_article_api(request):
    if request.method != 'POST':
        return JsonResponse({
            'status': 'error',
            'message': 'Method not allowed. Only POST is accepted.'
        }, status=405)

    # 1. API Key check
    expected_api_key = getattr(settings, 'BLOG_API_KEY', os.environ.get('BLOG_API_KEY', DEFAULT_API_KEY))
    provided_api_key = request.headers.get('X-API-KEY') or request.META.get('HTTP_X_API_KEY')

    if not provided_api_key or provided_api_key != expected_api_key:
        return JsonResponse({
            'status': 'error',
            'message': 'Unauthorized: Invalid or missing X-API-KEY header.'
        }, status=401)

    # Support JSON payload if body is JSON, otherwise request.POST
    data = {}
    if request.content_type and 'application/json' in request.content_type:
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            data = {}
    else:
        data = request.POST

    # 2. Extract and validate required fields
    title = data.get('title', '').strip()
    if not title:
        return JsonResponse({
            'status': 'error',
            'message': "Field 'title' is required."
        }, status=400)

    content = data.get('content', '').strip()
    if not content:
        return JsonResponse({
            'status': 'error',
            'message': "Field 'content' is required."
        }, status=400)

    raw_slug = data.get('slug', '').strip()
    slug = _get_unique_post_slug(raw_slug, title)

    excerpt = data.get('excerpt', '').strip()
    if not excerpt:
        plain_text = strip_tags(content)
        excerpt = plain_text[:300].strip()
    excerpt = excerpt[:500]

    alt_text = data.get('alt_text', '').strip()
    meta_title = (data.get('meta_title', '').strip() or title)[:250]
    meta_description = data.get('meta_description', '').strip() or excerpt

    status_val = data.get('status', 'published').strip().lower()
    if status_val not in ['published', 'draft']:
        status_val = 'published'

    # 3. Find Author (sadeqmou -> sadeghmou -> first active superuser -> first active user)
    author = (
        User.objects.filter(username='sadeqmou').first()
        or User.objects.filter(username='sadeghmou').first()
        or User.objects.filter(is_superuser=True, is_active=True).first()
        or User.objects.filter(is_staff=True, is_active=True).first()
        or User.objects.filter(is_active=True).first()
    )
    if not author:
        author = User.objects.create_user(username='sadeqmou', is_staff=True, is_superuser=True)

    # 4. Create Post object
    post = Post(
        title=title,
        slug=slug,
        author=author,
        excerpt=excerpt,
        content=content,
        thumbnail_alt=alt_text,
        status=status_val,
        meta_title=meta_title,
        meta_description=meta_description,
    )

    featured_image = request.FILES.get('featured_image') or request.FILES.get('thumbnail')
    if featured_image:
        post.thumbnail = featured_image

    post.save()

    # 5. Handle Categories (ManyToMany)
    categories_str = data.get('categories', '')
    if categories_str:
        cat_names = [c.strip() for c in categories_str.split(',') if c.strip()]
        for name in cat_names:
            category = Category.objects.filter(title__iexact=name).first()
            if not category:
                cat_slug = _get_unique_slug(Category, name, max_len=150)
                category = Category.objects.create(title=name, slug=cat_slug)
            post.categories.add(category)

    # 6. Handle Tags (ManyToMany)
    tags_str = data.get('tags', '')
    if tags_str:
        tag_names = [t.strip() for t in tags_str.split(',') if t.strip()]
        for name in tag_names:
            tag = Tag.objects.filter(title__iexact=name).first()
            if not tag:
                tag_slug = _get_unique_slug(Tag, name, max_len=150)
                tag = Tag.objects.create(title=name, slug=tag_slug)
            post.tags.add(tag)

    # 7. Generate absolute URL
    try:
        article_path = post.get_absolute_url()
    except Exception:
        article_path = f"/blog/{post.slug}/"

    host = request.get_host()
    if 'moosavi-academy.ir' in host:
        full_url = f"https://{host}{article_path}"
    else:
        full_url = request.build_absolute_uri(article_path)


    return JsonResponse({
        'status': 'success',
        'message': 'Article published successfully',
        'url': full_url,
        'post_id': post.id,
        'slug': post.slug
    }, status=201)

