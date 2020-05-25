from django.db import models


class Post(models.Model):
  text = models.TextField()

  def __str__(self):
    """this methods helps us represent the model in the admin"""
    return self.text[:50]
