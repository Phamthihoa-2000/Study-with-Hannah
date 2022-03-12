import email
from email.policy import default
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    bio = models.TextField(null=True)
    username = models.CharField(unique=True, max_length=200, null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
