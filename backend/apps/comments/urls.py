from django.urls import path

from apps.comments.views import List_Create_Comments

urlpatterns = [
    path('<int:id>/', List_Create_Comments.as_view())
]