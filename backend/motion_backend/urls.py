"""motion_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework_simplejwt import views as jwt_views
from django.urls import path, include

from motion_backend import settings
from django.conf.urls.static import static

urlpatterns = [
    path('backend/admin/', admin.site.urls),

    # TOKEN
    path('backend/api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('backend/api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('backend/api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_refresh'),

    # Posts
    path('backend/api/social/posts/', include('apps.posts.urls')),

    #Users
    path('backend/api/users/', include('apps.users.urls')),
    path('backend/api/social/followers/', include('apps.users.urls')),

    path('backend/api/auth/registration/', include('apps.register.urls')),

    path('backend/api/social/comments/', include('apps.comments.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

