from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from utils.model_mixins import AuthorizedTimestampedModelMixin
from apps.comments.models import Comment


class Portfolio(AuthorizedTimestampedModelMixin):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1024)
    images = GenericRelation(Comment)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name
