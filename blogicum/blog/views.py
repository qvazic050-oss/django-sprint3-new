from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


def index(request):
    posts = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    ).order_by('-pub_date')[:5]

    return render(
        request,
        'blog/index.html',
        {'posts': posts},
    )


def post_detail(request, pk):
    post = get_object_or_404(
        Post,
        pk=pk,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    )

    return render(
        request,
        'blog/detail.html',
        {'post': post},
    )


def category_posts(request, slug):
    category = get_object_or_404(
        Category,
        slug=slug,
        is_published=True,
    )

    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now(),
    ).order_by('-pub_date')

    return render(
        request,
        'blog/category.html',
        {
            'category': category,
            'posts': posts,
        },
    )
