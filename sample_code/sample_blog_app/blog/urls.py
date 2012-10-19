# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
urlpatterns = patterns('blog.views',

    # blog/
    url(r'^$', 'home', name='home'),
    
    # blog/post/1/
    url(r'post/(?P<post_id>\d+)/', 'post_detail', name='post_detail'),
    
    # blog/posts/veli/
    url(r'posts/(?P<username>\w+)/', 'posts_by_user', name='posts_by_user'),
)

