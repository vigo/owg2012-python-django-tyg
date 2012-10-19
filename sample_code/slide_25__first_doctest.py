# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    """
    A blog belonging to a user.
    Blogs have multiple posts and one user can have many blogs.
    
    >>> b = Blog()
    >>> b.name = 'Foo Blog'
    >>> b.user = User.objects.create(username='foo', password='test')
    >>> b.save()
    >>> print b
    Foo Blog
    >>> print b.user.username
    foo
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, related_name='blogs')
    
    def __unicode__(self):
        return self.name