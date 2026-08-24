from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

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
