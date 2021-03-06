# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^account/', include('blueapps.account.urls')),
    # 如果你习惯使用 Django 模板，请在 home_application 里开发你的应用，
    # 这里的 home_application 可以改成你想要的名字
    url(r'^', include('moments.urls')),
    # 如果你习惯使用 mako 模板，请在 mako_application 里开发你的应用，
    # 这里的 mako_application 可以改成你想要的名字
    url(r'^mako/', include('mako_application.urls')),
    url(r'^weixin/login/', include('weixin.core.urls')),
    url(r'^weixin/', include('weixin.urls')),

]
