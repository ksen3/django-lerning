from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_review, name='post_review'),
    path('read/', views.read_review, name='read_review'),
]