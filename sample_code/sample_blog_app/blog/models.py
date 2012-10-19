# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Haydi test yazalım!
    Önce hayali bir kullanıcı oluşturalım
    
    >>> u = User.objects.create(username='ali', password='veli')
    >>> u
    <User: ali>
    
    ali'yi verify edelim
    >>> u.id == u.pk
    True
    
    şimdi ali'ye ait blog post yapalım
    >>> p = Post(
    ...     owner=u,
    ...     title=u'Merhaba',
    ...     body=u'Posta ait uzun metin',
    ... )
    >>> p
    <Post: Merhaba>
    
    henüz 'save' etmedik... bakalım id'si ne? pk'i ne?
    save edilmediği için henüz id'si yok... yani
    >>> p.id
    
    >>> p.pk
    
    hatta
    >>> type(p.id)
    <type 'NoneType'>
    
    haydi şimdi save edelim:
    >>> p.save()
    >>> type(p.id)
    <type 'int'>
    >>> p.id == p.pk
    True
    
    sadece test amaçlıdır: *
    >>> users_posts = Post.objects.filter(owner=u).order_by('-updated_at')
    >>> users_posts
    [<Post: Merhaba>]
    
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    owner = models.ForeignKey(User, related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('blog.views.post_detail', (), {
            'post_id': self.id,
            }
        )

    @models.permalink
    def get_absolute_url_users_posts(self):
        return ('blog.views.posts_by_user', (), {
            'username': self.owner.username,
            }
        )

