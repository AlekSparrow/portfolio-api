import shutil
import tempfile
from unittest import mock
from django.contrib.auth import get_user_model
from django.test import override_settings, TestCase
from rest_framework.reverse import reverse, reverse_lazy
from PIL import Image
from apps.portfolio.models import Image
from apps.portfolio.views import ImageViewSet

User = get_user_model()

MEDIA_ROOT = tempfile.mkdtemp()


class UserMixin(object):
    @staticmethod
    def _create_user(user_number: int):
        user = User.objects.create(
            username=f"test{user_number}",
            first_name=f"Name{user_number}",
            last_name=f"Lname{user_number}",
            email=f"test{user_number}@example.com",
        )
        user.set_password(f"testPassword")
        user.save()
        return user


class ImageTestCase(TestCase, UserMixin):
    def setUp(self) -> None:
        self.user_1 = self._create_user(user_number=1)
        self.user_2 = self._create_user(user_number=2)
        self.user_3 = self._create_user(user_number=3)

        self.login_url = reverse("accounts:login")
        self.image_list_url = reverse("portfolio:image-list")
        self.image_detail_url = reverse("dialogs:image-detail", kwargs={"pk": 1})

        self.image = Image.objects.create()

    def _get_user_token(self, username="test", password="testPassword"):
        response = self.client.post(
            self.login_url,
            {"username": username, "password": password},
            format="json",
        )
        response_data = response.json()
        return "JWT {}".format(response_data.get("token", ""))
