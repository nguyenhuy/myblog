"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime
from django.contrib.auth.models import User

from django.test import TestCase, Client
from MyBlog import settings
from MyBlogApp.models import Blog


class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.blog = Blog.objects.create(title='Blog post',
                                        content='A new blog post.',
                                        time_stamp=datetime.now())
        self.user = User.objects.create_user("huy",
                                             "huy.x.nguyen@abo.fi",
                                             "abcxyz")


    def test_edit_blog(self):
        url = '/editblog/' + str(self.blog.id)

        # Try to edit blog post without logging in
        response = self.client.get(url)
        # Expect a redirect
        redirectedUrl = settings.LOGIN_URL + '?next=' + url
        self.assertRedirects(response, redirectedUrl)

        # Login and edit blog post again
        self.client.login(username="huy",
                          password="abcxyz")
        response = self.client.get(url)
        # Expect a 200 status code now
        self.assertEqual(response.status_code, 200)