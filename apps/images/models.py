from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from utils.model_mixins import AuthorizedTimestampedModelMixin
from apps.comments.models import Comment


def image_path(instance, filename):
    return "user_{0}/{1}/{2}".format(
        instance.created_by.id, instance.created_at, filename
    )


class Image(AuthorizedTimestampedModelMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2048)
    image = models.ImageField(upload_to=image_path)
    comments = GenericRelation(Comment)

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"
        ordering = ("created_at",)

    def __str__(self):
        return "%s: %s" % (self.name, self.description)
