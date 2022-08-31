from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from apps.accounts.permissions import IsOwnerOrReadOnly
from .serializers import (
    RegisterSerializer,
    ChangePasswordSerializer,
    UpdateUserSerializer,
)

User = get_user_model()


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordView(APIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOwnerOrReadOnly,
    )
    serializer_class = UpdateUserSerializer


class DeleteProfileView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOwnerOrReadOnly,
    )


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


register_view = RegisterView.as_view()
change_password = ChangePasswordView.as_view()
update_profile = UpdateProfileView.as_view()
delete_profile = DeleteProfileView.as_view()
logout_view = LogoutView.as_view()
