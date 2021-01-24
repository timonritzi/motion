from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=10)

    last_name = models.CharField(max_length=10)

    location = models.CharField(max_length=20, blank=True)

    about = models.CharField(max_length=250, blank=True)

    phone = models.IntegerField(null=True, blank=True)

    avatar = models.ImageField(null=True, blank=True)

    followees = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name="followers", blank=True)

    def __str__(self):
        return self.username
