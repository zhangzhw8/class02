"""wechat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from moments.views import home, show_user, show_status, submit_post, like, comment, \
    delete_comment, report, stats, friends
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_status),
    path('user', show_user),
    path('status', show_status),
    path('friends', friends),
    path('post', submit_post),
    path('exit', LogoutView.as_view(next_page="/")),

    path('like', like),
    path('comment', comment),
    path('comment/delete', delete_comment),
    path('report', report),
    path('stats', stats)
]
