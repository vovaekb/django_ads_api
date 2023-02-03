from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Ad(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=350)
    status = models.CharField(max_length=15)