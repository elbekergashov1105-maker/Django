from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
=======

def index(request):
    return render(request, 'api/index.html')
>>>>>>> 7c627db (first commit)

def home(request):
    context = {
        'ism': '',
    }
    return render(request, 'api/home.html', context)


<<<<<<< HEAD
=======

>>>>>>> 7c627db (first commit)
def about(request):
    return render(request, 'home/about.html')

@login_required
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

@login_required
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'api/post_detail.html', context)

@login_required
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

@login_required
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

@login_required
def post_delete(request, post_id):
    post = Post.objects.get( id=post_id)
    if request.method == "POST":

        post.delete()
        return redirect("posts")
    return render(request, "api/post_delete.html", {"post": post})


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            User.objects.create_user(username=username, password=password)
            return redirect("posts")
        return render(request, "api/register.html", {"error": "Barcha maydonlarni to'ldiring!"})
    return render(request, "api/register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("posts")
        return render(request, "api/login.html", {"error": "Login yoki parol xato!"})
    return render(request, "api/login.html")

def user_logout(request):
    logout(request)
<<<<<<< HEAD
    return redirect("home")
=======
    return redirect("login")

def mahsulotlar(request):
    return render(request, 'api/mahsulotlar.html')
>>>>>>> 7c627db (first commit)
