import random

from django.conf import settings
from django.db import models


# Create your models here.
from django.dispatch import receiver


def code_generator(length=6):
    numbers = '0123456789'
    return ''.join(random.choice(numbers) for _ in range(length))


class Registration(models.Model):

    code = models.CharField(default=code_generator, max_length=6)

    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name="registration", on_delete=models.CASCADE)

    code_used = models.BooleanField(default=False)
