from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """ User Model Definition """

    status_message = models.CharField(max_length=120, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField()
