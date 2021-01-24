from django.shortcuts import render
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, \
    ListAPIView, RetrieveAPIView
from apps.posts.permissons import isCreatorOrReadOnly
# Create your views here.
from apps.posts.models import Posts
from apps.posts.serializers import PostsSerializer, PostsGETUPDATESerializer, PostUserSerializer
from apps.users.serializer import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response

User = get_user_model()


# Create a post View
class Create_Posts_View(CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsGETUPDATESerializer


# List Post View
class List_Posts_Views(ListAPIView):
    queryset = Posts.objects.all().order_by("-created")
    serializer_class = PostsGETUPDATESerializer


# List all Posts of ONE user
class List_Posts_Single_User(ListAPIView):
    serializer_class = PostsGETUPDATESerializer

    def get_queryset(self):
        return Posts.objects.filter(user=self.kwargs['user_id'])


# Get single posts update/delete single posts
class Get_Update_Delete_Posts_View(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsGETUPDATESerializer
    lookup_field = "id"
    permission_classes = [isCreatorOrReadOnly]


class ListAllUsers(ListAPIView):
    queryset = User.objects.all()
    serializer_class = PostUserSerializer


class ToggleLikedPost(GenericAPIView):
    queryset = Posts
    serializer_class = PostsGETUPDATESerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        posts = self.get_object()
        user = self.request.user
        user_liked_post = user in posts.liked_by.all()
        if user_liked_post:
            posts.liked_by.remove(user)
        else:
            posts.liked_by.add(user)
        return Response(self.get_serializer(posts).data)

class GetLikedPosts(ListAPIView):
    serializer_class = PostsGETUPDATESerializer

    def get_queryset(self):
        return Posts.objects.filter(liked_by=self.kwargs['user_id'])

class ListFollowedUsersPosts(ListAPIView):
    serializer_class = PostsGETUPDATESerializer

    def get_queryset(self):
        followed_user_ids = self.request.user.followees.all().values_list("id", flat=True)
        posts = Posts.objects.filter(user__in=followed_user_ids)
        return posts


class Search_User(ListAPIView):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['post_content', 'user__username']




