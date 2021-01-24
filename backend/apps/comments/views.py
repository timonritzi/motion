from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from apps.comments.models import Comments
from apps.comments.serializers import CommentSerializer
from apps.posts.models import Posts


class List_Create_Comments(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Posts.objects.all()
    lookup_url_kwarg = 'id'
    def create(self, request, *args, **kwargs):
        post = self.get_object()
        comment = Comments(user=request.user, post=post, content=request.data['content'])
        comment.save()
        return Response(self.get_serializer(instance=comment).data)
