# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404, get_list_or_404

from blog.models import Post

def home(request):
    template_params = {}
    posts = Post.objects.all().order_by('-updated_at')
    template_params['POSTS'] = posts
    return render_to_response(
        'home.html',
        template_params,
        context_instance=RequestContext(request)
    )
    # return HttpResponse('<strong>Hello world</strong>')

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    template_params = {}
    template_params['POST'] = post
    return render_to_response(
        'detail.html',
        template_params,
        context_instance=RequestContext(request)
    )
    # return HttpResponse(post.pk)

def posts_by_user(request, username):
    users_posts = get_list_or_404(Post, owner__username = username)
    template_params = {}
    template_params['POSTS'] = users_posts
    return render_to_response(
        'posts_by_user.html',
        template_params,
        context_instance=RequestContext(request)
    )
    # return HttpResponse('username: %s' % username)