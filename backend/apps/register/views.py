from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView, UpdateAPIView
from django.core.mail import send_mail
from apps.register.models import Registration
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from apps.register.serializers import RegisterSerializer
from apps.users.serializer import UserSerializer

User = get_user_model()


# Sending Email with confirmation code


# Create your views here.
# Posting email to receive code
class RegisterSendCode(GenericAPIView):
    serializer = UserSerializer

    def post(self, request, *args, **kwargs):
        user = User(email=request.data['email'], is_active=False, username=request.data['email'])
        user.save()
        registration = Registration(user=user)
        registration.save()

        send_mail(
            'Verify Account',
            f'Welcome to Motion : {registration.code}',
            'motionpropulsionaccess@gmail.com',
            [f'{user.email}'],
            fail_silently=False,
        )

        return Response(status=status.HTTP_200_OK)


# Confirm code which was sent by email
class ValidateUser(GenericAPIView):
    serializer_class = UserSerializer

    def patch(self, request, *args, **kwargs):

        if Registration.objects.filter(code=request.data['code'], user__email=request.data['email']):
            # serializer = self.get_serializer(data=request.data)
            # serializer.is_valid(raise_exception=True)
            # serializer.save(serializer.validated_data)
            user = User.objects.get(email=request.data['email'])
            user.is_active=True
            user.first_name=request.data['first_name']
            user.last_name=request.data['last_name']
            user.username=request.data['username']
            user.set_password(request.data['password'])
            user.save()
        return Response(self.get_serializer(user).data)