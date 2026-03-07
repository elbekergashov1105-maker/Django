from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post 

def home(request):
    context = {
        'ism': '',
    }
    return render(request, 'api/home.html', context)

def about(request):
    return render(request, 'home/about.html')

def posts(request):
    query = request.GET.get('q', '')
    posts = Post.objects.all().order_by('-created_at')
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
    paginator = Paginator(posts, 3)
    page_nomer = request.GET.get('page')
    page_obj = paginator.get_page(page_nomer)
    context = {
        'page_obj': page_obj,
        'query': query
    }
    return render(request, 'api/posts.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'api/post_detail.html', context)

def post_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get("author")
        if title and content:
            Post.objects.create(title=title, content=content, author=author)
            return redirect('posts')
        return render(request, "api/post_create.html", {"error":"Barcha maydonlarni to'ldiring!!"})
    return render(request, "api/post_create.html")

def post_update(request, post_id):
    post = Post.objects.get( id=post_id)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.POST.get("author")
        if title and content and author:
            post.title=title
            post.content=content
            post.author=author
        post.save()
        return redirect("post_detail", post_id=post_id)
    return render(request, "api/post_edit.html", {"post": post})

def post_delete(request, post_id):
    post = Post.objects.get( id=post_id)
    if request.method == "POST":

        post.delete()
        return redirect("posts")
    return render(request, "api/post_delete.html", {"post": post})


