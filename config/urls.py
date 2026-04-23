"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
import main.views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', main.views.index, name='index'),
    path('home/', main.views.home, name='home'),
    path('about', main.views.about, name='about'),
    path('posts/', main.views.posts, name='posts'),
    path('posts/<int:post_id>/', main.views.post_detail, name='post_detail'),
    path('posts/create/', main.views.post_create, name="post_create"),
<<<<<<< HEAD
    path('posts/<int:post_id>/edit/', main.views.post_update, name="post_update"),
    path('posts/<int:post_id>/delete/', main.views.post_delete, name="post_delete"),
    path('accounts/register/', main.views.register, name='register'),
    path('accounts/login/', main.views.user_login, name='login'),
    path('accounts/logout/', main.views.user_logout, name='logout'),
    



]
=======
    path('posts/<int:post_id>/edit/', main.views.post_update, name='post_update'),
    path('posts/<int:post_id>/delete/', main.views.post_delete, name='post_delete'),
    path('accounts/register/', main.views.register, name='register'),
    path('accounts/login/', main.views.user_login, name='login'),
    path('accounts/logout/', main.views.user_logout, name='logout'),
    path('mahsulotlar/', main.views.mahsulotlar, name='mahsulotlar'),
)
>>>>>>> 7c627db (first commit)
