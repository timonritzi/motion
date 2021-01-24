from django.urls import path
from django.contrib.auth import get_user_model

from apps.users.views import List_All_User, List_Single_User, Follow, ListFolloweesUsers, ListFollwing, ViewPatchUserData

User = get_user_model()

urlpatterns = [
    path('', List_All_User.as_view()),
    path('<int:id>/', List_Single_User.as_view()),
    path('toggle-follow/<int:id>/', Follow.as_view()),
    path('followers/', ListFolloweesUsers.as_view()),
    path('following/', ListFollwing.as_view()),
    path('me/', ViewPatchUserData.as_view())
]