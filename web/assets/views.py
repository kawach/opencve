from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, FormView, ListView,
                                  UpdateView, View)

from assets.models import Asset
from assets.forms import AssetForm


class AssetsListView(LoginRequiredMixin, ListView):
    template_name = "list_assets"

    def get_queryset(self):
        return Asset.objects.all()


class AssetCreateView(LoginRequiredMixin, CreateView):
    model = Asset
    form_class = AssetForm
    template_name = "assets/asset_add.html"


    def get_success_url(self):
        return reverse("list_assets")