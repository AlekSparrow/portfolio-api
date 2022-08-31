from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.portfolio.views import PortfolioViewSet, ImageViewSet, CommentView

router = DefaultRouter()
router.register(r"images", ImageViewSet)
router.register(r"portfolios", PortfolioViewSet, basename="portfolio")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "images/<int:image_pk>/comment",
        CommentView.as_view(),
        name="image_comment_create",
    ),
]