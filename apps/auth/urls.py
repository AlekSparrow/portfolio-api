from django.urls import path
from rest_framework_simplejwt.views import (
    token_obtain_pair,
    token_refresh,
    token_verify,
)
from apps.auth.views import (
    LogoutView,
    RegisterView,
    ChangePasswordView,
    ProfileView,
)

urlpatterns = [
    path("login/", token_obtain_pair, name="token_obtain_pair"),
    path("login/refresh/", token_refresh, name="token_refresh"),
    path("login/verify/", token_verify, name="token_verify"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "profile/<str:username>/",
        ProfileView.as_view(),
        name="profile",
    ),
    path(
        "change_password/<str:username>/",
        ChangePasswordView.as_view(),
        name="change_password",
    ),
]
