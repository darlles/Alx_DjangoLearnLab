# blog/tests/test_tags_search.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Tag

class TagSearchTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('alex', 'alex@example.com', 'StrongPass123!')
        self.p1 = Post.objects.create(title='Django Tips', content='Templates and views', author=self.user)
        self.p2 = Post.objects.create(title='Python Tricks', content='Generators and comprehensions', author=self.user)
        t_django = Tag.objects.create(name='django')
        t_python = Tag.objects.create(name='python')
        self.p1.tags.add(t_django)
        self.p2.tags.add(t_python)

    def test_tag_route(self):
        r = self.client.get(reverse('tag-posts', args=['django']))
        self.assertContains(r, 'Django Tips')
        self.assertNotContains(r, 'Python Tricks')

    def test_search_by_keyword_and_tag(self):
        r = self.client.get(reverse('search'), {'q': 'templates'})
        self.assertContains(r, 'Django Tips')
        r = self.client.get(reverse('search'), {'q': 'python'})
        self.assertContains(r, 'Python Tricks')