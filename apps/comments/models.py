from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth import get_user_model

from django.db import models

User = get_user_model()


class Comment(models.Model):
    text = models.TextField(max_length=255)
    object_id = models.PositiveSmallIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey("content_type", "object_id")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="+"
    )

    def __str__(self):
        return self.text
