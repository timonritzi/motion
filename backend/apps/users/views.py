from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView, RetrieveUpdateAPIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
# Create your views here.
from apps.users.serializer import UserSerializer

User = get_user_model()


class List_All_User(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class List_Single_User(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"


class Follow(GenericAPIView):
    queryset = User
    serializer_class = UserSerializer
    lookup_field = "id"

    def patch(self, request, *args, **kwargs):
        follow = self.get_object()
        user = self.request.user
        user_followed = user in follow.followees.all()
        if user_followed:
            follow.followees.remove(user)
        else:
            follow.followees.add(user)
        return Response(self.get_serializer(user).data)


class ListFolloweesUsers(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(followers=user)


class ListFollwing(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(followees=user)

class ViewPatchUserData(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        # serializer = UserSerializer(request.user)
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)