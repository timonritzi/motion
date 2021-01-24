from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from apps.posts.models import Posts


class Comments(models.Model):
    content = models.CharField(max_length=150)

    created = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(to=Posts, related_name="comments", on_delete=models.CASCADE)

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name="comments", on_delete=models.CASCADE)