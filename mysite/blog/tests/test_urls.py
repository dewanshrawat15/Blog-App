from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import post_list, post_new, post_detail, post_edit

class TestUrls(SimpleTestCase):

	def test_blog_views_url(self):
		url = reverse('post_list')
		self.assertEquals(post_list, resolve(url).func)

	def test_blog_add_blog_post_url(self):
		url = reverse('post_new')
		self.assertEquals(post_new, resolve(url).func)

	def test_blog_blog_detail_url(self):
		url = reverse('post_detail', args=['2'])
		self.assertEquals(post_detail, resolve(url).func)

	def test_blog_blog_edit_url(self):
		url = reverse('post_edit', args=['1'])
		self.assertEquals(post_edit, resolve(url).func)