from django.test import SimpleTestCase
from blog.forms import PostForm

class TestForms(SimpleTestCase):
	
	def test_post_form_valid_data(self):
		form = PostForm(
			data={
				'title': "Hey world",
				'text': "Peeps there are working on it"
			}
		)
		self.assertTrue(form.is_valid())

	def test_post_form_empty(self):
		form = PostForm(data={})
		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 2)