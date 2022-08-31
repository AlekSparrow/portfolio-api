from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.portfolio import views

router = DefaultRouter()
router.register(r"images", views.ImageViewSet)
router.register(r"portfolios", views.PortfolioViewSet, basename="portfolio")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "images/<int:image_pk>/comment",
        views.comment_create,
        name="image_comment_create",
    ),
]
