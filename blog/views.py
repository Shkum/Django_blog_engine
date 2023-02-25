from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Tag


def posts_list(request):
    # return HttpResponse('<h1>Blog Page</h1>')
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)


def tags_list(request):
    tags = Tag.objects.all()
    context={
        'tags': tags
    }
    return render(request, 'blog/tags_list.html', context)


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    context={
        'tag': tag
    }
    return render(request, 'blog/tag_detail.html', context)

