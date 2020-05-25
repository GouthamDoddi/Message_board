from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class HomePageView(ListView):
  """Inheriting from built in list view to display alll the post"""
  model = Post
  template_name = "posts/home.html"
  context_object_name = "posts"
  
