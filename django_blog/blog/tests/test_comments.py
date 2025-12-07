# blog/tests/test_comments.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment

class CommentTests(TestCase):
    def setUp(self):
        self.author = User.objects.create_user('alex', 'alex@example.com', 'StrongPass123!')
        self.other = User.objects.create_user('sam', 'sam@example.com', 'StrongPass123!')
        self.post = Post.objects.create(title='Hello', content='World', author=self.author)

    def test_list_comments_on_post_detail(self):
        Comment.objects.create(post=self.post, author=self.author, content='Nice read!')
        r = self.client.get(reverse('post-detail', args=[self.post.pk]))
        self.assertContains(r, 'Nice read!')

    def test_create_comment_requires_login(self):
        r = self.client.post(reverse('post-detail', args=[self.post.pk]), {'content': 'Anonymous comment'})
        self.assertEqual(Comment.objects.count(), 0)
        self.client.login(username='sam', password='StrongPass123!')
        r = self.client.post(reverse('post-detail', args=[self.post.pk]), {'content': 'Logged in comment'})
        self.assertEqual(Comment.objects.count(), 1)

    def test_edit_comment_author_only(self):
        c = Comment.objects.create(post=self.post, author=self.other, content='Original')
        self.client.login(username='alex', password='StrongPass123!')
        r = self.client.get(reverse('comment-update', args=[c.pk]))
        self.assertIn(r.status_code, (302, 403))
        self.client.login(username='sam', password='StrongPass123!')
        r = self.client.post(reverse('comment-update', args=[c.pk]), {'content': 'Edited'})
        c.refresh_from_db()
        self.assertEqual(c.content, 'Edited')

    def test_delete_comment_author_only(self):
        c = Comment.objects.create(post=self.post, author=self.other, content='Delete me')
        self.client.login(username='alex', password='StrongPass123!')
        r = self.client.post(reverse('comment-delete', args=[c.pk]))
        self.assertTrue(Comment.objects.filter(pk=c.pk).exists())
        self.client.login(username='sam', password='StrongPass123!')
        r = self.client.post(reverse('comment-delete', args=[c.pk]))
        self.assertFalse(Comment.objects.filter(pk=c.pk).exists())