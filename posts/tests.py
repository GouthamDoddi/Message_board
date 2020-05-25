from django.test import TestCase
from django.urls import reverse

from .models import Post


class TestingPosts(TestCase):

  def setUp(self):
    """Setting up common variables in this method"""
    Post.objects.create(text='This is a test post')

  def test_post_name(self):
    """Test that the post name is correct"""
    post_object = Post.objects.get(id=1)
    expected_text = f"{post_object.text}"
    self.assertEqual(expected_text, "This is a test post")

  def test_if_the_page_loads(self):
    """Twst if the response is 200 when the page is requested"""
    res = self.client.get('')
    
    self.assertEqual(res.status_code, 200)

  def test_that_the_page_loads_using_urls_name(self):
    """Test that HomePageView is called when request the right url"""
    res = self.client.get(reverse('home'))
    
    self.assertEqual(res.status_code, 200)

  def test_that_the_right_template_is_used(self):
    """Test that the righttemplate is called by the view"""
    res = self.client.get(reverse('home'))
    
    self.assertEqual(res.status_code, 200)
    self.assertTemplateUsed(res, 'posts/home.html')
