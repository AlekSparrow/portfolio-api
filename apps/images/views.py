from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from apps.accounts.permissions import IsOwnerOrReadOnly
from apps.images.models import Image
from apps.images.serializers import ImageListSerializer, ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by("created_at")
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "description", "portfolio__name"]

    def get_serializer_class(self):
        return ImageListSerializer if self.action == "list" else ImageSerializer
