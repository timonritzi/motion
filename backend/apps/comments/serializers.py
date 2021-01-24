from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.comments.models import Comments
from apps.posts.serializers import PostsSerializer
from apps.users.serializer import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    post = PostsSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comments
        fields = "__all__"