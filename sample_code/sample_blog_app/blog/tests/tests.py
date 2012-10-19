# -*- coding: utf-8 -*-

# APP = blog
import os
from operator import attrgetter

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import Http404

from blog.models import Post

## TEST = PostTestCaseFixtured
class PostTestCaseFixtured(TestCase):
    fixtures = ['unittest_Post.json', 'unittest_User.json']
    
    def test_all_users_and_posts(self):
        # id'si 1 olan user
        self.assertQuerysetEqual(
            User.objects.filter(pk=1),
            [u'ali'],
            attrgetter("username")
        )
        
        # toplam 4 user...
        self.assertEqual(len(User.objects.all()), 4)
        
        # toplam 16 post
        self.assertEqual(len(Post.objects.all()), 16)
        [
            (
                self.assertIsInstance(post, Post),
                self.assertEqual(post.get_absolute_url(), reverse("post_detail", args=[post.pk]))
            )
            for post in Post.objects.all()
        ]
        

class PostTestCase(TestCase):
    def setUp(self):
        self.post_counter = 0
        # 4 adet kullanıcı oluşturalım
        self.users = [
            self.create_user(username)
            for username in ['ali', 'veli', 'selami', 'nuri']
        ]
    
    def create_fixture(self, model):
        from django.core import serializers
        fixture_dir = "%s/fixtures" % os.path.dirname(os.getcwd())
        fixture_file = "%s/unittest_%s.json" % (fixture_dir, str(model.__name__))
        if not os.path.exists(fixture_dir):
            os.mkdir(fixture_dir)
        out = open(fixture_file, 'w')
        serializers.serialize("json", model.objects.all(), indent=4, stream=out)
        out.close()
        
    def create_user(self, username):
        return User.objects.create(username=username, password='1234')

    def create_post(self, owner):
        self.post_counter += 1
        return Post.objects.create(
            owner=owner,
            title=u"Merhaba Dünya %d" % self.post_counter,
            body=u"Post için body %d" % self.post_counter,
        )

    def create_post_for_each_user(self):
        return [
            self.create_post(user)
            for user in self.users
        ]

    def test_users(self):
        [
            (
                # user gerçekten User'ın instance'ımı?
                self.assertIsInstance(user, User),
                
                # user.id ile user.pk aynı olmalı!
                self.assertEqual(user.id, user.pk),
                
                # user'a ailt hiç post olmamalı
                self.assertQuerysetEqual(Post.objects.filter(owner=user), []),
            )
            for user in self.users
        ]

    def test_create_post(self):
        # önce ali için post oluşturalım
        user = [user for user in self.users if user.username == 'ali'][0]
        post = self.create_post(user)
        
        # post gerçekten Post'un instance'ımı?
        self.assertIsInstance(post, Post)
        self.assertEqual(post.id, post.pk)
        self.assertEqual(post.id, Post.objects.get(pk=post.pk).pk)
        self.assertQuerysetEqual(Post.objects.filter(pk=post.pk), [
            '<Post: Merhaba Dünya 1>'
        ])
        self.assertQuerysetEqual(Post.objects.filter(pk=post.pk), [
            u'ali',
        ], attrgetter("owner.username"))

    def test_create_post_for_each_user(self):
        # her user için post oluştur
        posts = self.create_post_for_each_user()
        
        # postları kontrol et oluşmuşmu?
        self.assertQuerysetEqual(Post.objects.all(), [
            '<Post: Merhaba D\xc3\xbcnya 1>',
            '<Post: Merhaba D\xc3\xbcnya 2>',
            '<Post: Merhaba D\xc3\xbcnya 3>',
            '<Post: Merhaba D\xc3\xbcnya 4>',
        ])
        
        # oluşturduğun post'larla database'deki Post'ları karşılaştır
        self.assertListEqual(
            [post for post in Post.objects.all()],
            [post for post in posts])
        
        # user bazında Post'u çek karşılaştır...
        [
            (
                self.assertQuerysetEqual(
                    Post.objects.filter(owner=user),[user.username], attrgetter("owner.username")
                ),
                
            )
            for user in self.users
        ]
    
    ## TEST = PostTestCase.test_home_view
    def test_home_view(self):
        # yeni test, bu bakımdan post oluşturmak gerekiyor
        
        # önce url'i kontrol et
        self.assertEqual('/blog/', reverse("home"))
        
        # home view'u bize ne oluşturdu
        response = self.client.get(reverse("home"))
        
        # http status 200 olmalı...
        self.assertEqual(response.status_code, 200)
        
        # aynı zamanda debug ediyoruz...
        print response.content
        print "**************************************************************"
        
        # acaba render edilen template'a POSTS gelmişmi?
        self.assertTrue('POSTS' in response.context)
        
        # hiç kayıt olmadığı için boş olmalı
        self.assertEqual(len(response.context['POSTS']), 0)
        
        # doğru template render edilmişmi?
        self.assertTemplateUsed(response, "home.html")
        
        # şimdi dummy data oluşturalım...
        posts = self.create_post_for_each_user()
        
        # sayfayı tekrar çağıralım
        response = self.client.get(reverse("home"))
        print response.content
        print "**************************************************************"
        
        # acaba render edilen template'a POSTS gelmişmi?
        self.assertTrue('POSTS' in response.context)
        
        # toplam 4 kullanıcı olduğu için 4 kayıt olmalı
        self.assertEqual(len(response.context['POSTS']), 4)
        
        # oluşan html içinde 4 adet <li><a href="..." olmalı...
        self.assertContains(response, '<li><a href="/blog/post/', count=4)
    
    ## TEST = PostTestCase.test_post_detail_view
    def test_post_detail_view(self):
        # önce url'i kontrol et
        self.assertEqual('/blog/post/1/', reverse("post_detail", args=[1]))
        # kayıt olmadığı için hata mesajı gelmeli
        response = self.client.get(reverse("post_detail", args=[1]))
        self.assertEqual(response.status_code, 404)
        
        # postları oluşturalım
        posts = self.create_post_for_each_user()
        response = self.client.get(reverse("post_detail", args=[1]))
        
        # http status 200 olmalı...
        self.assertEqual(response.status_code, 200)
        
        # acaba render edilen template'a POST gelmişmi?
        self.assertTrue('POST' in response.context)
        
        # doğru template render edilmişmi?
        self.assertTemplateUsed(response, "detail.html")
        
        print response.content
        print "**************************************************************"
        
        # render edilen html'i kontrol edelim
        self.assertContains(response, '<a href="/blog/post/1/">Permalink</a>')
        self.assertContains(response, '<a href="/blog/posts/ali/">ali</a>')
    
    # TEST = PostTestCase.test_posts_by_user
    def test_posts_by_user(self):
        # önce url'i kontrol et
        self.assertEqual('/blog/posts/ali/', reverse("posts_by_user", args=[u'ali']))
        
        # kayıt olmadığı için hata mesajı gelmeli
        response = self.client.get(reverse("post_detail", args=[1]))
        self.assertEqual(response.status_code, 404)
        
        posts = []
        # 16 tane kayıt oluşturuyoruz
        [
            posts.append(self.create_post_for_each_user())
            for i in range(4)
        ]
        posts = sum(posts, [])

        self.create_fixture(User)
        self.create_fixture(Post)
        
        response = self.client.get(reverse("posts_by_user", args=[u'ali']))
        # print response.content
        # print "**************************************************************"

        # html içinde kontrol
        self.assertContains(response, "ali Tarafından Post Edilenler")

        # url'leri kontrol edelim
        [
            self.assertEqual(post.get_absolute_url(), reverse("post_detail", args=[post.pk]))
            
            for post in response.context['POSTS']
        ]
