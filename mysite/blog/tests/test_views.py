from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login
from blog.models import Post
import json

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.list_posts_url = reverse('post_list')
		self.list_details_url = reverse('post_detail', args=['1'])
		self.post_new_url = reverse('post_new')

	def test_post_list_GET(self):
		response = self.client.get(self.list_posts_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/post_list.html')

	def test_post_detail_GET(self):
		user_instance = User.objects.create_user(
			username='testuser', password='root@1234'
		)
		Post.objects.create(
			author=user_instance,
			title="Hello world",
			text="Hey everyone, this is Dewansh Rawat writing a new blog post about the wonders of Django."
		)
		response = self.client.get(self.list_details_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/post_detail.html')

	def test_post_new_GET(self):
		response = self.client.get(self.post_new_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/post_edit.html')

	def test_post_new_POST(self):
		user_instance = User.objects.create(
			username='testuser'
		)
		user_instance.set_password('12345')
		user_instance.save()
		self.client.login(username='testuser', password='12345')
		response = self.client.post(self.post_new_url, {'title': 'Hello', 'text': 'testing this out'})
		pk = Post.objects.get(title="Hello")
		self.assertEquals(response.status_code, 302)
		self.assertRedirects(response, reverse('post_detail', kwargs={'pk': pk.id}))

	def test_post_new_POST_empty(self):
		user_instance = User.objects.create(
			username='testuser'
		)
		user_instance.set_password('12345')
		user_instance.save()
		self.client.login(username='testuser', password='12345')
		response = self.client.post(self.post_new_url, {'title': '', 'text': ''})
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/post_edit.html')
