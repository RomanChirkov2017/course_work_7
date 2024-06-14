from django.contrib.auth.views import LogoutView
from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig
from users.views import (MyTokenObtainPairView, UserCreateAPIView,
                         UserDestroyAPIView, UserListAPIView,
                         UserUpdateAPIView, user_verification)

app_name = UsersConfig.name

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_list"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path(
        "login/",
        MyTokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/confirm/<str:token>/", user_verification, name="user_verification"),
    path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
    path("<int:pk>/delete/", UserDestroyAPIView.as_view(), name="user_delete"),
]
