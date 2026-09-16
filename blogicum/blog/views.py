from django.shortcuts import get_object_or_404, render

from .models import Category, Post


POSTS_PER_PAGE = 5


def index(request):
    posts = Post.objects.published()[:POSTS_PER_PAGE]

    return render(
        request,
        'blog/index.html',
        {'posts': posts},
    )


def post_detail(request, pk):
    post = get_object_or_404(
        Post.objects.published(),
        pk=pk,
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

    posts = category.posts.published()

    return render(
        request,
        'blog/category.html',
        {
            'category': category,
            'posts': posts,
        },
    )
