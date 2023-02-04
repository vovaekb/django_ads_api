from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Ad(models.Model):
    title = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=350)
    category = models.CharField(max_length=40)
    status = models.CharField(max_length=15)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)