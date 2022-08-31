from rest_framework.serializers import (
    ModelSerializer,
    ReadOnlyField,
    PrimaryKeyRelatedField,
    CharField,
)
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from apps.portfolio.models import Portfolio, Image, Comment


class CreateMixin:
    @property
    def request(self):
        return self._context["request"]

    def create(self, validated_data):
        validated_data.update(
            {
                "created_by": self.request.user,
            }
        )
        return super().create(validated_data)


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "text", "image"]


class CommentListSerializer(ModelSerializer):
    created_by = ReadOnlyField(source="created_by.username")

    class Meta:
        model = Comment
        fields = ["id", "name", "text", "image", "created_at", "created_by"]
        read_only_fields = ["created_at", "created_by"]


class ImageSerializer(CreateMixin, ModelSerializer):
    comments = PrimaryKeyRelatedField(many=True, read_only=True)
    created_by = ReadOnlyField(source="created_by.username")
    name = CharField(
        max_length=100, validators=[UniqueValidator(queryset=Image.objects.all())]
    )

    class Meta:
        model = Image
        fields = [
            "id",
            "name",
            "description",
            "portfolio",
            "comments",
            "created_by",
            "created_at",
            "image",
        ]
        read_only_fields = ["created_by", "created_at"]

    def validate_image(self, upload_image):
        if not upload_image.name.lower().endswith((".png", ".jpg", ".jpeg")):
            raise ValidationError("Invalid file type.")
        return upload_image


class ImageListSerializer(ModelSerializer):
    created_by = ReadOnlyField(source="created_by.username")

    class Meta:
        model = Image
        fields = [
            "id",
            "name",
            "description",
            "portfolio",
            "created_at",
            "created_by",
        ]
        read_only_fields = ["created_at", "created_by"]


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
