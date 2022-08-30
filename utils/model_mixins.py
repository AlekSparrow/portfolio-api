from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthorizedTimestampedModelMixin(models.Model):
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="+"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
