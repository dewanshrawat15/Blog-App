from django.test import TestCase
from blog.models import Post

from django.contrib.auth.models import User

class TestModels(TestCase):

	def setUp(self):
		self.user_instance = User.objects.create(
			username='testuser'
		)
		self.user_instance.set_password('12345')
		self.user_instance.save()
	
	def test_adding_a_new_post(self):
		post = Post.objects.create(
			title="Some dummy content title",
			text="Some dummy content text that can be used to check things out",
			author=self.user_instance
		)
		self.assertEquals(post.id, 1)
		self.assertEquals(len(Post.objects.all()), 1)
		self.assertEquals(post.author.username, 'testuser')
		self.assertEquals(post.title, 'Some dummy content title')