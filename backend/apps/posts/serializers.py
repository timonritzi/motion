from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.posts.models import Posts


User = get_user_model()


class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'followees', 'first_name', 'last_name', 'avatar']


class PostsGETUPDATESerializer(serializers.ModelSerializer):
    user = PostUserSerializer(read_only=True)

    class Meta:
        model = Posts
        fields = "__all__"

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        post = super().create(validated_data=validated_data)
        return post


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"