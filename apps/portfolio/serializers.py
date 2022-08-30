from rest_framework.serializers import ModelSerializer, ReadOnlyField
from apps.portfolio.models import Portfolio
from apps.images.serializers import ImageSerializer
from utils.serializer_mixins import CreateMixin


class PortfolioSerializer(CreateMixin, ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = ["name", "description", "images"]


class PortfolioListSerializer(ModelSerializer):
    created_by = ReadOnlyField(source="created_by.username")

    class Meta:
        model = Portfolio
        fields = ["id", "name", "description", "created_at", "created_by"]

    read_only_fields = ["created_at", "created_by"]
