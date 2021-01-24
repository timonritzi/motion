from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()


class Posts(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    post_content = models.CharField(max_length=150)
    user = models.ForeignKey(to=User, related_name="posts", on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(to=User, verbose_name="liked by", related_name="liked_posts", blank=True)
