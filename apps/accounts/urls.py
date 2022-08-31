from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh
from apps.accounts.views import (
    register_view,
    change_password,
    update_profile,
    logout_view,
    delete_profile,
)


namespace = "accounts"

urlpatterns = [
    path("login/", token_obtain_pair, name="token_obtain_pair"),
    path("login/refresh/", token_refresh, name="token_refresh"),
    path("register/", register_view, name="accounts_register"),
    path(
        "change_password/<int:pk>/",
        change_password,
        name="accounts_change_password",
    ),
    path(
        "update_profile/<int:pk>/",
        update_profile,
        name="accounts_update_profile",
    ),
    path(
        "delete_profile/<int:pk>/",
        delete_profile,
        name="accounts_delete_profile",
    ),
    path("logout/", logout_view, name="accounts_logout"),
]
