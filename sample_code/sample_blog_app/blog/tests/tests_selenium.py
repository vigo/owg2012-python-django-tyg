# -*- coding: utf-8 -*-
# APP = blog
import os
from time import sleep

from django.test import LiveServerTestCase
from django.utils.encoding import smart_str, smart_unicode
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from django.core.urlresolvers import reverse


class MySeleniumTests(LiveServerTestCase):
    fixtures = ['unittest_Post.json', 'unittest_User.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(MySeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        # sleep(2)
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_browse(self):
        # print [m for m in dir(WebDriver) if not m.startswith('_')]
        # help()
        
        # home'u çağır...
        self.selenium.get('%s%s' % (self.live_server_url, reverse("home")))
        self.assertEqual(self.selenium.title, "Blog Sitesi")
        # ekran görüntüsü al...
        WebDriver.get_screenshot_as_file(self.selenium, "%s/Desktop/stest_home.png" % os.environ['HOME'])
        # self.selenium.implicitly_wait(20)
        # sleep(2)
        
        # <ul id="posts"> var mı?
        ul_posts = self.selenium.find_element_by_id("posts")
        self.assertGreater(len(ul_posts.text), 0)
        
        # <a href="/blog/post/15/">Merhaba Dünya 15</a> linki bul
        first_link = self.selenium.find_element_by_xpath('//a[@href="/blog/post/15/"]')
        first_link_text = first_link.text.encode('utf-8')
        
        # Texti "Merhaba Dünya 15"?
        self.assertEqual(first_link_text, "Merhaba D\xc3\xbcnya 15")
        
        # Linke tıkla...
        first_link.click()
        self.assertEqual(self.selenium.title.encode('utf-8'), "Blog Sitesi | Merhaba D\xc3\xbcnya 15")
        WebDriver.get_screenshot_as_file(self.selenium, "%s/Desktop/stest_detial.png" % os.environ['HOME'])
        # sleep(2)
        
        # gelen sayfadaki <h1> i bul, texti "Detay" mı?
        self.assertEqual(self.selenium.find_element_by_tag_name('h1').text, "Detay")
        
        
        # username_input = self.selenium.find_element_by_name("username")
        # username_input.send_keys('myuser')
        # password_input = self.selenium.find_element_by_name("password")
        # password_input.send_keys('secret')
        # self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()