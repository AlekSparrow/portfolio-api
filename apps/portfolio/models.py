from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from apps.comments.models import Comment

User = get_user_model()


def image_path(instance, filename):
    return "user_{0}/{1}/{2}".format(
        instance.created_by.id, instance.created_at, filename
    )


class BaseModel(models.Model):
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="+"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Portfolio(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1024)
    images = GenericRelation(Comment)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name


class Image(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2048)
    image = models.ImageField(upload_to=image_path)
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="images"
    )

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"
        ordering = ("created_at",)

    def __str__(self):
        return "%s: %s" % (self.name, self.description)


class Comment(BaseModel):
    text = models.TextField(max_length=255)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.text
