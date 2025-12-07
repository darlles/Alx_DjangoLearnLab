# blog/tests/test_posts.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post

class PostCRUDTests(TestCase):
    def setUp(self):
        self.author = User.objects.create_user('alex', 'alex@example.com', 'StrongPass123!')
        self.other = User.objects.create_user('sam', 'sam@example.com', 'StrongPass123!')

    def test_list_and_detail_public(self):
        post = Post.objects.create(title='Hello', content='World', author=self.author)
        r = self.client.get(reverse('post-list'))
        self.assertContains(r, 'Hello')
        r = self.client.get(reverse('post-detail', args=[post.pk]))
        self.assertContains(r, 'World')

    def test_create_requires_login(self):
        r = self.client.get(reverse('post-create'))
        self.assertEqual(r.status_code, 302)  # redirect to login
        self.client.login(username='alex', password='StrongPass123!')
        r = self.client.post(reverse('post-create'), {'title': 'New', 'content': 'Text'})
        self.assertEqual(Post.objects.count(), 1)

    def test_edit_author_only(self):
        post = Post.objects.create(title='Edit me', content='Body', author=self.author)
        self.client.login(username='sam', password='StrongPass123!')
        r = self.client.get(reverse('post-edit', args=[post.pk]))
        self.assertIn(r.status_code, (302, 403))
        self.client.login(username='alex', password='StrongPass123!')
        r = self.client.post(reverse('post-edit', args=[post.pk]), {'title': 'Edited', 'content': 'Updated'})
        post.refresh_from_db()
        self.assertEqual(post.title, 'Edited')

    def test_delete_author_only(self):
        post = Post.objects.create(title='Delete me', content='Body', author=self.author)
        self.client.login(username='sam', password='StrongPass123!')
        r = self.client.post(reverse('post-delete', args=[post.pk]))
        self.assertTrue(Post.objects.filter(pk=post.pk).exists())
        self.client.login(username='alex', password='StrongPass123!')
        r = self.client.post(reverse('post-delete', args=[post.pk]))
        self.assertFalse(Post.objects.filter(pk=post.pk).exists())