from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from apps.portfolio.models import Portfolio
from apps.auth.permissions import IsOwnerOrReadOnly
from apps.portfolio.serializers import PortfolioSerializer, PortfolioListSerializer


class PortfolioViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Portfolio.objects.filter(created_by=self.request.user).order_by(
            "created_at"
        )

    def get_serializer_class(self):
        return PortfolioListSerializer if self.action == "list" else PortfolioSerializer
