from django.urls import path, re_path

from apps.posts.views import Create_Posts_View, Get_Update_Delete_Posts_View, List_Posts_Views, List_Posts_Single_User, ListAllUsers, ToggleLikedPost, GetLikedPosts, ListFollowedUsersPosts, Search_User



urlpatterns = [
    path('', Create_Posts_View.as_view()),
    path('get/', List_Posts_Views.as_view()),
    path('<int:id>/', Get_Update_Delete_Posts_View.as_view()),
    path('user/<int:user_id>/', List_Posts_Single_User.as_view()),
    path('users/', ListAllUsers.as_view()),
    path('toggle-like/<int:id>/', ToggleLikedPost.as_view()),
    path('likes/<int:user_id>/', GetLikedPosts.as_view()),
    path('following/', ListFollowedUsersPosts.as_view()),
    path('search/', Search_User.as_view())
]
