from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

"""
class Users(models.Model):
    user_name = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    vote_count = models.IntegerField(default=0)
"""

class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=50, default="null")
    body = models.TextField(max_length=5000)
    vote_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=5000)
    vote_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Posts', on_delete=models.DO_NOTHING)
