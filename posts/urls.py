from django.urls import path, URLPattern

from .views import HomePageView


urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  ]
