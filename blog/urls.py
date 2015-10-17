"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.dates import ArchiveIndexView
from blogentry.views import BlogYearArchiveView

urlpatterns = [
	url(r'^register/$',"signup.views.register", name='register'),
	url(r'^register/registration_complete/$',"signup.views.registration_complete", name='registration_complete'),
    url(r'^$', "blogentry.views.home", name="home"),
	#url(r'^(?P<year>[0-9]{4})/$', 'BlogYearArchiveView.as_view(),', name="archive"),
	url(r'^blog/(?P<slug>[\w-]+)/$', 'blogentry.views.blog_detail', name='blog_detail'),
	url(r'^post/$', "blogentry.views.blog_post", name="blog_post"),
	url(r'^login/$', "signup.views.auth_login", name='login'),
    url(r'^logout/$', "signup.views.auth_logout", name='logout'),
	url(r'^comments/(?P<id>\d+)/$', "comments.views.comment_thread", name='comment_thread'),
    url(r'^comments/create/$', "comments.views.comment_create_view", name='comment_create_view'),
    url(r'^admin/', include(admin.site.urls)),
]
