from django.urls import path

from apps.register.views import RegisterSendCode, ValidateUser

urlpatterns = [
    path("", RegisterSendCode.as_view()),
    path("validation/", ValidateUser.as_view())
]