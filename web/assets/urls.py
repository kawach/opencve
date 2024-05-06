from django.urls import path

from assets.views import (AssetsListView, AssetCreateView)

urlpatterns = [
    path("assets/", AssetsListView.as_view(), name="list_assets"),
    path("assets/add", AssetCreateView.as_view(), name="create_asset"),
]