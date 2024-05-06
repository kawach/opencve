from rest_framework import viewsets

from assets.models import Asset
from assets.serializers import AssetSerializer


class AssetViewSet(viewsets.ModelViewSet):
    serializer_class = AssetSerializer
    lookup_field = "name"
    lookup_url_kwarg = "name"
    serializer_classes = {
        "list": AssetSerializer,
        "retrieve": AssetSerializer,
    }

    def get_queryset(self):
        return (
            Asset.objects.filter(members=self.request.user)
            .order_by("name")
            .all()
        )

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)
