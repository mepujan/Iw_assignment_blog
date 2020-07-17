from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Blog


def index(request):
    return render(request, 'post/index.html')


def blog(request):
    data = Blog.objects.all().order_by('-updated_date')
    paginator = Paginator(data, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'post/blog.html', {'data': post})


def selected_post(request, post_slug):
    post = get_object_or_404(Blog, slug=post_slug)
    posts = Blog.objects.order_by('-updated_date')
    context = {
        'post': post,
        'posts': posts
    }
    return render(request, 'post/selected_blog.html', context)
