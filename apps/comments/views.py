from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    permission_classes = [
        AllowAny,
    ]
    serializer_class = CommentSerializer

    def get_queryset(self):
        object_id = self.request.GET.get("id")
        return Comment.objects.filter(object_id=object_id)
