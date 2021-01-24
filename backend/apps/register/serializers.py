from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.register.models import Registration
from apps.users.serializer import UserSerializer

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Registration
        fields = "__all__"

    # def save(self, validated_data):
    #     user = User.objects.get(email=validated_data.get("email"))
    #     user.username = validated_data.get("username")
    #     user.first_name = validated_data.get("first_name")
    #     user.last_name = validated_data.get("last_name")
    #     user.first_name = validated_data.get("first_name")
    #     user.is_active = True
    #     user.set_password(validated_data.get("password"))
    #     user.registration.code_used = True
    #     user.save()
    #     user.registration.save()
    #     return user

